#include <cmath> 
#include <math.h>
#include <vector>
#include <stdlib.h>
#include <iostream>
#include <fstream>
#include <string>

#include <TTree.h>
#include <TChain.h>
#include <TROOT.h>
#include <TChain.h>
#include <TFile.h>
#include <TH2.h>
#include <TH1F.h>
#include <TStyle.h>
#include <TCanvas.h>
#include <TVector2.h>
#include <TVector3.h>
#include <TAxis.h>
#include <TLorentzVector.h>
#include "TRegexp.h"

#define pi 3.141592653589793
#include "DPSelection.h"


using namespace std;
using std::vector;
using std::cout; using std::endl;




//===== constructor  ====
DPSelection::DPSelection(TTree *tree): GMSBTree_V3(tree) { 
//=======================
   cout << "Building DPSelection..." << endl;

}


//================================================
void DPSelection::SetFilename(const char* outname) {
//================================================

   sprintf(file,"%s",outname);

}


double deltaR(double eta1, double phi1, double eta2, double phi2){
    double deltaeta = fabs(eta1 - eta2);
    double deltaphi = fabs(phi1 - phi2);
    if (deltaphi > TMath::Pi())
      deltaphi = TMath::TwoPi() - deltaphi;
    double deltaR = sqrt(pow(deltaeta,2) + pow(deltaphi,2));
    return deltaR;
  
}


double deltaR(TLorentzVector a, TLorentzVector b) {

    return deltaR(a.Eta(), a.Phi(), b.Eta(), b.Phi());
  
}
 

bool comp_pair (double i,double j) { return (i>j); }



//================================================
double weightCrossSection(const char* outname) {
//================================================
  
 double weight;
  
 
   if (string(outname).find("GMSB_L160") != std::string::npos) weight = 0.0277;
   if (string(outname).find("GMSB_L180") != std::string::npos) weight = 0.0145;

   if (TString(outname) == "TTJets") weight = 13.43;
 
   if (TString(outname) == "G_Pt-50to80") weight = 3322.309;
   if (TString(outname) == "G_Pt-80to120") weight = 558.2865;
   if (TString(outname) == "G_Pt-120to170") weight = 108.0068;
   if (TString(outname) == "G_Pt-170to300") weight = 30.12207;
   if (TString(outname) == "G_Pt-300to470") weight = 2.138632;
   if (TString(outname) == "G_Pt-470to800") weight = 0.2119244;

   if (TString(outname) == "QCD_Pt-80to120") weight = 1033680.0;
   if (TString(outname) == "QCD_Pt-120to170") weight = 156293.3;
   if (TString(outname) == "QCD_Pt-170to300") weight = 34138.15;
   if (TString(outname) == "QCD_Pt-300to470") weight = 1759.549;
   if (TString(outname) == "QCD_Pt-470to600") weight = 113.8791;
   if (TString(outname) == "QCD_Pt-600to800") weight = 26.9921;
   if (TString(outname) == "QCD_Pt-800to1000") weight = 3.550036;
   if (TString(outname) == "QCD_Pt-1000to1400") weight = 0.737844;

//   cout << weight << endl;

 
 return weight;
}




int getsumcounterzero(TString infile){

	  //TString dir = "/localgrid/wvandrie/CMSSW_5_3_11_DP/src/EXO/DPAnalysis/test/v21/";
          //TFile f(dir+infile+".root");

	  TString dir = "root://eoscms//eos/cms/store/caf/user/sigamani/DPAnalysis/v21/"; 
          TFile *f = TFile::Open(dir+infile+".root");

          TTree* ftree= (TTree*)f->Get("CutFlow");
      
          TH1D* hist = new TH1D("hist","",150000,0,150000);

          ftree->Draw("counter[0]>>hist");

          int nbins = hist->GetNbinsX();
          double hmin = hist->GetXaxis()->GetBinLowEdge(1);
          double hmax = hist->GetXaxis()->GetBinUpEdge(nbins);

                        int entries = 0;
                        for(int b=1; b<=nbins; ++b){

                                if (hist->GetBinContent(b) > 0 ) {
                                entries += (hist->GetBinContent(b)) * hist->GetXaxis()->GetBinLowEdge(b);
                                }


                        }
 return entries;
}







//----------------------------
void DPSelection::Loop(int nMaxEvents, const char* outname)
//----------------------------
{
   if (fChain == 0) return;

   char line[300];
   sprintf(line,"%s.root",file);
   
   TFile *fout = new TFile(line,"RECREATE");
   
   int a = getsumcounterzero(outname);

   double entries = (double) a;

   TH1D* h000 = new TH1D("Entries","",9,0,9);
   h000->GetXaxis()->SetBinLabel(1,"All");
   h000->GetXaxis()->SetBinLabel(2,"Preselection");
   h000->GetXaxis()->SetBinLabel(3,"OneGoodVtx");
   h000->GetXaxis()->SetBinLabel(4,"MET>0");
   h000->GetXaxis()->SetBinLabel(5,"nPhot1");
   h000->GetXaxis()->SetBinLabel(6,"nJet2");

   h000->Fill(0.,entries);
   
   Int_t nPhot;
   Int_t nMuon;
   Int_t nEle;
   Int_t nJet;
   Int_t nGoodVtx;
 
   Int_t isMC; 

   Float_t MET;
   Float_t CrossSectionWeight;
   Float_t EfficiencyScaleFactors;
   Float_t PUScaleFactors;


   TTree *anaTree     = new TTree("anaTree","Tree of variables"); 
   anaTree->Branch("nPhot", &nPhot, "nPhot/I");
   anaTree->Branch("nMuon", &nMuon, "nMuon/I");
   anaTree->Branch("nEle", &nEle, "nEle/I");
   anaTree->Branch("nJet", &nJet, "nJet/I");
   anaTree->Branch("nGoodVtx", &nGoodVtx, "nGoodVtx/I");
   anaTree->Branch("isMC", &isMC, "isMC/I");
   anaTree->Branch("ptPhot", &ptPhot);
   anaTree->Branch("etaPhot", &etaPhot);
   anaTree->Branch("phiPhot", &phiPhot);
   anaTree->Branch("dxyConv", &dxyConv);
   anaTree->Branch("dzConv", &dzConv);
   anaTree->Branch("etaConv", &etaConv);
   anaTree->Branch("phiConv", &phiConv);
   anaTree->Branch("deltaR", &deltaR);
   anaTree->Branch("sMinPhot", &sMinPhot);
   anaTree->Branch("sMajPhot", &sMajPhot);
   anaTree->Branch("sigmaIetaPhot", &sigmaIetaPhot);
   anaTree->Branch("aveTimePhot", &aveTimePhot);
   anaTree->Branch("ptJet", &ptJet);
   anaTree->Branch("MET", &MET, "MET/F");
   anaTree->Branch("CrossSectionWeight", &CrossSectionWeight, "CrossSectionWeight/F");
   anaTree->Branch("EfficiencyScaleFactors", &EfficiencyScaleFactors, "EfficiencyScaleFactors/F");
   anaTree->Branch("PUScaleFactors", &PUScaleFactors, "PUScaleFactors/F");
   anaTree->Branch("convMatched", &convMatched, "convMatched/F");
   anaTree->Branch("phoMatched", &phoMatched, "phoMatched/F");


   Long64_t nentries = fChain->GetEntriesFast();
   Float_t N_events_w = (Float_t) fChain->GetEntries();

   Long64_t nbytes = 0, nb = 0;
   selectedEvents_ = 0;
  
   Long64_t jentry;
  


   TFile *pileup = TFile::Open("PUweights.root");
   TH1D *pile = (TH1D*)pileup->FindObjectAny("pileup");



   for (jentry=0; jentry<nentries && jentry<nMaxEvents;jentry++) {
     Long64_t ientry = LoadTree(jentry);
     if (ientry < 0) break;
     nb = fChain->GetEntry(jentry);   nbytes += nb;

     if( (jentry+1)%10000==0) cout << "Processing event " << jentry+1 << endl;

     

     /***********************************************************************/
     //                   LOOP OVER EVENTS AND PERFORM CUTS
     /***********************************************************************/

     bool MC = 0;
  
     if (string(outname).find("Run2012") != std::string::npos)  { MC=0;} 
     else MC = 1;
	
     if (triggered != 1) continue;

     int entries = getsumcounterzero(outname); 

     if ( MC == 0 ) {CrossSectionWeight  = 1.;}
     else CrossSectionWeight = weightCrossSection(outname) * 1. / double(entries);	   

     double puweight = 1.;


     if( MC == 1 ){

       puweight = pile->GetBinContent( (PU_NumInter + 1) );
       PUScaleFactors = puweight;
       
       //cout << "weight: "<< puweight << endl;
     }




     ptPhot.clear();
     ptJet.clear();
     etaPhot.clear();
     phiPhot.clear();
     dxyConv.clear();
     dzConv.clear();
     phiConv.clear();
     etaConv.clear();
     deltaR.clear();
     sMinPhot.clear();
     sMajPhot.clear();
     sigmaIetaPhot.clear(); 
     aveTimePhot.clear();

     int nVtx = 0 ;
	
     for ( int j=0 ; j< nVertices; j++ ) {
       
       if ( nVertices < 1 )   continue ;
       if ( vtxNdof[j]     < 0 )  continue ;
       if ( fabs(vtxZ[j]) >= 24. )  continue ;
       if ( vtxRho[j]        >= 2. )  continue ;
       
       nVtx++ ;
     }


     double weight = -99.;
     int largest = 0;
     double largestvalue = 0.;
     double largesttempdxy = 0.;
     double largesttempeta = 0.;
     double largesttempphi = 0.;
     
     for (int i=0; i < nConversions; i++) {

       /*
       if (convMatchedEle[i] > 0) continue;
       
       bool matching = false;
       double deltar = 0.;
       
       for (int k=0; k < nPhotons; k++){
         TLorentzVector phoP4( phoPx[k], phoPy[k], phoPz[k], phoE[k] );
         double photonEta = phoP4.Eta();
         double photonPhi = phoP4.Phi();

         deltar = sqrt((photonEta-convEta[i])*(photonEta-convEta[i]) + (photonPhi-convPhi[i])*(photonPhi-convPhi[i]));

         deltaR.push_back(deltar);

         if (deltar < 0.25) {matching = true;}

       }

       if (!matching) continue;
       */

       dzConv.push_back(convDz[i]);
       dxyConv.push_back(convDxy[i]);
       phiConv.push_back(convPhi[i]);
       etaConv.push_back(convEta[i]);

       /*
       if (abs(convDxy[i]) > abs(largestvalue)){
         largest = i;
	 largestvalue = convDxy[i];
       }
       */       
     }

     /*
     //sorting the largest Dxy in the first place
     if(dxyConv.size() > 0 && largest != 0){

       largesttempdxy = dxyConv.at(0);
       largesttempeta = etaConv.at(0);
       largesttempphi = phiConv.at(0);
       
       dxyConv.at(0) = dxyConv.at(largest);
       phiConv.at(0) = phiConv.at(largest);
       etaConv.at(0) = etaConv.at(largest);
       
       //dxyConv.at(largest) = largesttempdxy;
       //phiConv.at(largest) = largesttempphi;
       //etaConv.at(largest) = largesttempeta;
     }
     */

     for (int i=0; i <nPhotons; i++) {
			 

       TLorentzVector phoP4( phoPx[i], phoPy[i], phoPz[i], phoE[i] ) ;

       
       if ( fabs(fSpike[i]) > 0.001 ) continue ;
       if ( phoP4.Pt() < 50. )  continue ;
       if ( fabs(phoP4.Eta()) > 1.47 )  continue ;
       if ( phoHoverE[i] > 0.05 ) continue ;
       //if ( sMinPho[i] < 0.15 || sMinPho[i] > 0.3 )  continue ; WAS WEG
       //if ( sMinPho[i] < 0.12 || sMinPho[i] > 0.38 )                continue ; WAS WEG
       if ( sigmaIeta[i] >  0.012 ) continue ;
       //if ( dR_TrkPho[i] < 0.6 ) continue; WAS WEG
       if ( phoP4.Eta() > -0.75 && phoP4.Eta() < -0.6 && phoP4.Phi() > -1. && phoP4.Phi() < -0.8 ) continue ;
       if ( phoP4.Eta() > 0.80 && phoP4.Eta() < 0.95 && phoP4.Phi() > -1.95 && phoP4.Phi() < -1.8 ) continue ;
       
       
       /***********************************************************************/
       //                   Cut for isolated photons  
       /***********************************************************************/
      
       if ( cHadIso[i] >= 2.6 ) continue ;  // chargedHadron
       if ( nHadIso[i] >= 3.5 + ( 0.04*phoP4.Pt()   ) ) continue ;  // neutralHadron
       if ( photIso[i] >= 1.3 + ( 0.005*phoP4.Pt() ) ) continue ;  // photon
       
       /***********************************************************************/
       //                   Cut for fake photons                                                                                                                                                          
       /***********************************************************************/
       
       /*       	   	   
       if (!( cHadIso[i] >= 2.6 )  && (!( nHadIso[i] >= 3.5 + ( 0.04*phoP4.Pt()   ) )) && (!( photIso[i] >= 1.3 + ( 0.005*phoP4.Pt() ) ))  ) continue ;
       */

       //if (phoMatchedEle[i] > 0) continue;
       
       ptPhot.push_back(phoP4.Pt());
       sort(ptPhot.begin(),ptPhot.end(),comp_pair);
       etaPhot.push_back(fabs(phoP4.Eta()));
       phiPhot.push_back(fabs(phoP4.Phi()));
       sMinPhot.push_back(sMinPho[i]);
       sMajPhot.push_back(sMajPho[i]);
       sigmaIetaPhot.push_back(sigmaIeta[i]);
       aveTimePhot.push_back(aveTime[i]);

       weight = pow(0.99887, ptPhot.size());

     }	


     // Data MC efficiency scale factors for photons
     
     if ( MC == 0 ) {EfficiencyScaleFactors  = 1.;}
     else EfficiencyScaleFactors = weight; 
     


     for ( int j=0 ; j< nJets; j++ ) {

       
       TLorentzVector jp4( jetPx[j], jetPy[j], jetPz[j], jetE[j] ) ;

       if ( jp4.Pt()        < 35 ) continue ;
       if ( fabs(jp4.Eta()) > 2.4 ) continue ;
       
       if ( jetNDau[j] < (double)   2 )  continue ;
       if ( jetCEF[j] >= (double)0.99 )  continue ;
       if ( jetNEF[j] >= (double)0.99 )  continue ;
       if ( jetNHF[j] >= (double)0.99 )  continue ;
       if ( fabs( jp4.Eta() ) < 2.4 && jetCM[j]  <= 0 ) continue ;
       
       double dR_gj = 999. ;
       
       for ( int k=0 ; k< nPhotons; k++ ) {
	 TLorentzVector phoP4( phoPx[k], phoPy[k], phoPz[k], phoE[k] ) ;
	 
	 if ( phoP4.Pt() < 50. )   continue ;
	 if ( phoHoverE[j] > 0.05 ) continue ;
	 
	 /***********************************************************************/
	 //                   Cut for isolated photons
	 /***********************************************************************/
	 
	 if ( cHadIso[j] >= 2.6 ) continue ;  // chargedHadron
	 if ( nHadIso[j] >= 3.5 + ( 0.04*phoP4.Pt()   ) ) continue ;  // neutralHadron
	 if ( photIso[j] >= 1.3 + ( 0.005*phoP4.Pt() ) ) continue ;  // photon      
	 

	 /***********************************************************************/
         //                   Cut for fake photons
	 /***********************************************************************/

         /*  
         if (!( cHadIso[j] >= 2.6 )  && (!( nHadIso[j] >= 3.5 + ( 0.04*phoP4.Pt()   ) )) && (!( photIso[j] >= 1.3 + ( 0.005*phoP4.Pt() ) ))  ) continue ;
	 */
	 
	 //if ( phoP4.DeltaR( jp4 ) < dR_gj )  dR_gj  = phoP4.DeltaR( jp4 ) ; 
       }	     
       
       //if ( dR_gj < 0.3 ) continue ;
       
       ptJet.push_back(jp4.Pt());
       sort(ptJet.begin(),ptJet.end(),comp_pair);
       
     }

     nPhot = ptPhot.size(); 
     nJet = ptJet.size();
     nMuon = nMuons; 
     nEle = nElectrons; 
     isMC = MC;
     nGoodVtx = nVtx; 
     MET = met; 
     
                                        h000->Fill(1.);
     if (nGoodVtx < 0) continue; 	h000->Fill(2.);
     if (MET < 30) continue; 	        h000->Fill(3.);
     if (nPhot < 1) continue;  	        h000->Fill(4.);
     if (nJet < 2) continue; 	        h000->Fill(5.);
	  
     anaTree->Fill();



   }
   
   fout->cd();
   h000->Write();
   anaTree->Write();
   fout->Write();
   fout->Close();

}

