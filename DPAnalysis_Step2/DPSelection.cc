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



vector<TLorentzVector> CombineJets_R_no_seed(vector<TLorentzVector> ,TLorentzVector, TLorentzVector);
double CalcMTR(TLorentzVector , TLorentzVector , TVector3 );
double CalcGammaMRstar(TLorentzVector , TLorentzVector);



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


double smallest(double w, double x, double y, double z) {

  double smallest = 99999.;

  if (w < smallest)
    smallest=w;
  if (x < smallest)
    smallest=x;
  if (y < smallest)
    smallest=y;
  if(z < smallest)
    smallest=z;

  return smallest;
}


 double deltaPhi(double a, double b){

    double deltaphi = fabs(a - b);
    if (deltaphi > TMath::Pi())
      deltaphi = TMath::TwoPi() - deltaphi;
    return deltaphi;
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
bool comp_pair2(const TLorentzVector &a, const TLorentzVector &b){ return a.Pt() > b.Pt(); }

//================================================
double weightCrossSection(const char* outname) {
  //================================================
  
  double weight;
  
 
  if (string(outname).find("GMSB_Lambda-120") != std::string::npos) weight = 0.133;  
  if (string(outname).find("GMSB_Lambda-140") != std::string::npos) weight = 0.0574;
  if (string(outname).find("GMSB_Lambda-160") != std::string::npos) weight = 0.0277;
  if (string(outname).find("GMSB_Lambda-180") != std::string::npos) weight = 0.0145;

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
 
  return weight;
}




int getsumcounterzero(const char* outname){
// int getsumcounterzero(TString infile){



//   TString dir = "/afs/cern.ch/work/w/wvandrie/public/EXO/CMSSW_7_1_8/src/EXO/DPAnalysis/test/v24/";
//   TFile f(dir+infile+".root");


//   TTree* ftree= (TTree*)f.Get("CutFlow");
      
//   TH1D* hist = new TH1D("hist","",150000,0,150000);

//   ftree->Draw("counter[0]>>hist");

//   int nbins = hist->GetNbinsX();
//   double hmin = hist->GetXaxis()->GetBinLowEdge(1);
//   double hmax = hist->GetXaxis()->GetBinUpEdge(nbins);

//   int entries = 0;
//   for(int b=1; b<=nbins; ++b){

//     if (hist->GetBinContent(b) > 0 ) {
//       entries += (hist->GetBinContent(b)) * hist->GetXaxis()->GetBinLowEdge(b);
//     }


//   }


  int entries; 

  // if (TString(outname) == "GMSB_Lambda-120_CTau-10") entries = ???;
  // if (TString(outname) == "GMSB_Lambda-120_CTau-100") entries = ???;
  // if (TString(outname) == "GMSB_Lambda-120_CTau-250") entries = ???;
  // if (TString(outname) == "GMSB_Lambda-120_CTau-1000") entries = ???;
  // if (TString(outname) == "GMSB_Lambda-120_CTau-2000") entries = ???;
  if (TString(outname) == "GMSB_Lambda-140_CTau-1") entries = 50112 ;
  if (TString(outname) == "GMSB_Lambda-140_CTau-10") entries = 50112;
  if (TString(outname) == "GMSB_Lambda-140_CTau-50") entries = 50112 ;
  if (TString(outname) == "GMSB_Lambda-140_CTau-100") entries = 50112 ;
  if (TString(outname) == "GMSB_Lambda-140_CTau-500") entries = 50112;
  if (TString(outname) == "GMSB_Lambda-140_CTau-1000") entries = 50112 ;
  if (TString(outname) == "GMSB_Lambda-140_CTau-2000") entries = 50112 ;
  if (TString(outname) == "GMSB_Lambda-160_CTau-1") entries = 50112 ;
  if (TString(outname) == "GMSB_Lambda-160_CTau-10") entries = 998272 ;
  if (TString(outname) == "GMSB_Lambda-160_CTau-50") entries = 993664 ;
  if (TString(outname) == "GMSB_Lambda-160_CTau-100") entries = 969984 ;
  if (TString(outname) == "GMSB_Lambda-160_CTau-500") entries = 988576 ;
  if (TString(outname) == "GMSB_Lambda-160_CTau-1000") entries = 50112 ;
  if (TString(outname) == "GMSB_Lambda-160_CTau-2000") entries = 50112 ;
  if (TString(outname) == "GMSB_Lambda-180_CTau-1") entries = 50112 ;
  if (TString(outname) == "GMSB_Lambda-180_CTau-10") entries = 993376;
  if (TString(outname) == "GMSB_Lambda-180_CTau-50") entries = 995392 ;
  if (TString(outname) == "GMSB_Lambda-180_CTau-250") entries = 997120 ;
  if (TString(outname) == "GMSB_Lambda-180_CTau-500") entries = 993000 ;
  if (TString(outname) == "GMSB_Lambda-180_CTau-2000") entries = 50112 ;

  if (TString(outname) == "TTJets") entries = 3.74644e+06;
  
  if (TString(outname) == "G_Pt-50to80") entries = 1.99506e+06;
  if (TString(outname) == "G_Pt-80to120") entries = 1.99263e+06;
  if (TString(outname) == "G_Pt-120to170") entries = 2.00004e+06;
  if (TString(outname) == "G_Pt-170to300") entries = 2.00007e+06;
  if (TString(outname) == "G_Pt-300to470") entries = 1.90665e+06;
  if (TString(outname) == "G_Pt-470to800") entries = 1.67523e+06;

  if (TString(outname) == "QCD_Pt-80to120") entries = 5.89486e+06;
  if (TString(outname) == "QCD_Pt-120to170") entries = 5.93573e+06;
  if (TString(outname) == "QCD_Pt-170to300") entries = 5.8144e+06;
  if (TString(outname) == "QCD_Pt-300to470") entries = 1.5535e+06;
  if (TString(outname) == "QCD_Pt-470to600") entries = 550000;
  if (TString(outname) == "QCD_Pt-600to800") entries = 761448;
  if (TString(outname) == "QCD_Pt-800to1000") entries = 2.4532e+06;
  if (TString(outname) == "QCD_Pt-1000to1400") entries = 1.96409e+06;
  
  if (TString(outname) == "Run2012A") entries = 1.423650e+06;
  if (TString(outname) == "Run2012B_1") entries = 1.746522e+06;
  if (TString(outname) == "Run2012B_2") entries = 1.783702e+06;
  if (TString(outname) == "Run2012B_3") entries = 1.6859e+06;
  if (TString(outname) == "Run2012B_4") entries = 1.56462e+06;
  if (TString(outname) == "Run2012C_1") entries = 1.780056e+06;
  if (TString(outname) == "Run2012C_2") entries = 1.868314e+06;
  if (TString(outname) == "Run2012C_3") entries = 1.900796e+06;
  if (TString(outname) == "Run2012C_4") entries = 1.933735e+06;
  if (TString(outname) == "Run2012C_5") entries = 1.594005e+06;
  if (TString(outname) == "Run2012D_1") entries = 1.934311e+06;
  if (TString(outname) == "Run2012D_2") entries = 1.9866e+06;
  if (TString(outname) == "Run2012D_3") entries = 1.915217e+06;
  if (TString(outname) == "Run2012D_4") entries = 1.938768e+06;
  if (TString(outname) == "Run2012D_5") entries = 1.365449e+06;

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
  h000->GetXaxis()->SetBinLabel(4,"MET>60");
  h000->GetXaxis()->SetBinLabel(5,"nJet2");
  h000->GetXaxis()->SetBinLabel(6,"nPhot2");
  
  
  h000->Fill(0.,entries);
   
  Int_t nPhot;
  Int_t nMuon;
  Int_t nEle;
  Int_t nJet;
  Int_t nGoodVtx;
 
  Int_t isMC; 
  Int_t triggeredvariable;

  Float_t MET;
  Float_t METUP;
  Float_t METDOWN;
  Float_t phiMET;
  Float_t minDPhi; 
  Float_t CrossSectionWeight;
  Float_t EfficiencyScaleFactors;
  Float_t PUScaleFactors;
  Float_t Rsqrd;

  TTree *anaTree     = new TTree("anaTree","Tree of variables"); 
  anaTree->Branch("nPhot", &nPhot, "nPhot/I");
  anaTree->Branch("nMuon", &nMuon, "nMuon/I");
  anaTree->Branch("nEle", &nEle, "nEle/I");
  anaTree->Branch("nJet", &nJet, "nJet/I");
  anaTree->Branch("nGoodVtx", &nGoodVtx, "nGoodVtx/I");
  anaTree->Branch("isMC", &isMC, "isMC/I");
  anaTree->Branch("Rsqrd", &Rsqrd);
  anaTree->Branch("PhotEn", &PhotEn);
  anaTree->Branch("ptPhot", &ptPhot);
  anaTree->Branch("ptPhotUp", &ptPhotUp);
  anaTree->Branch("ptPhotDown", &ptPhotDown);
  anaTree->Branch("etaPhot", &etaPhot);
  anaTree->Branch("phiPhot", &phiPhot);
  anaTree->Branch("dxyConv", &dxyConv);
  anaTree->Branch("dzConv", &dzConv);
  anaTree->Branch("conversionR", &conversionR);
  anaTree->Branch("etaConv", &etaConv);
  anaTree->Branch("phiConv", &phiConv);
  anaTree->Branch("deltaRward", &deltaRward);
  anaTree->Branch("ConvChi2", &ConvChi2);
  anaTree->Branch("sMinPhot", &sMinPhot);
  anaTree->Branch("sMajPhot", &sMajPhot);
  anaTree->Branch("sigmaIetaPhot", &sigmaIetaPhot);
  anaTree->Branch("aveTimePhot", &aveTimePhot);
  anaTree->Branch("ptJet", &ptJet);
  anaTree->Branch("ptJetUp", &ptJetUp);
  anaTree->Branch("ptJetDown", &ptJetDown);
  anaTree->Branch("phiJet", &phiJet);
  anaTree->Branch("MET", &MET, "MET/F");
  anaTree->Branch("METUP", &METUP, "METUP/F");
  anaTree->Branch("METDOWN", &METDOWN, "METDOWN/F");
  anaTree->Branch("phiMET", &phiMET, "phiMET/F");
  anaTree->Branch("minDPhi", &minDPhi, "minDPhi/F");
  anaTree->Branch("CrossSectionWeight", &CrossSectionWeight, "CrossSectionWeight/F");
  anaTree->Branch("EfficiencyScaleFactors", &EfficiencyScaleFactors, "EfficiencyScaleFactors/F");
  anaTree->Branch("PUScaleFactors", &PUScaleFactors, "PUScaleFactors/F");
  anaTree->Branch("convMatched", &convMatched, "convMatched/F");
  anaTree->Branch("phoMatched", &phoMatched, "phoMatched/F");
  anaTree->Branch("phohovere", &phohovere);
  anaTree->Branch("chadiso", &chadiso);
  anaTree->Branch("nhadiso", &nhadiso);
  anaTree->Branch("photiso", &photiso);
  anaTree->Branch("triggeredvariable", &triggeredvariable, "triggeredvariable/I");
  anaTree->Branch("rnine", &rnine);
  anaTree->Branch("EoverP",&EoverP);
  anaTree->Branch("EoverP2",&EoverP2);
  anaTree->Branch("EThreeByThree", &EThreeByThree);
  
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

    //Triggeredvariable!!!
    if (MC == 0 && !(triggered == 1 || triggered == 3)) continue;
    if (MC == 1 && triggered != 1) continue;


    int entries = getsumcounterzero(outname); 


    if ( MC == 0 ) {CrossSectionWeight  = 1.;}
    else CrossSectionWeight = weightCrossSection(outname) * 1. / double(entries);   

    double puweight = 1.;


    if( MC == 1 ){

      puweight = pile->GetBinContent( (PU_NumInter + 1) );
      PUScaleFactors = puweight;
    }


    double phiPhot1 = 0.;
    double phiPhot2 = 0.;
    double phiJet1 = 0.;
    double phiJet2 = 0.;

    PhotEn.clear();
    ptPhot.clear();
    ptPhotUp.clear();
    ptPhotDown.clear();
    ptJet.clear();
    ptJetUp.clear();
    ptJetDown.clear();
    etaPhot.clear();
    phiPhot.clear();
    phiJet.clear();
    dxyConv.clear();
    dzConv.clear();
    conversionR.clear();
    phiConv.clear();
    etaConv.clear();
    deltaRward.clear();
    ConvChi2.clear();
    sMinPhot.clear();
    sMajPhot.clear();
    sigmaIetaPhot.clear(); 
    aveTimePhot.clear();
    photiso.clear();
    nhadiso.clear();
    chadiso.clear();
    phohovere.clear();
    rnine.clear();
    EoverP.clear();
    EoverP2.clear();
    EThreeByThree.clear();

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
       
      if (convMatchedEle[i] > 0) continue;
       
      bool matching = false;
      double tempdeltar = 10000.;
      double deltar = 0.;
      double eoverp = 10000.;
      double eoverp2 = 10000.;

      for (int k=0; k < nPhotons; k++){
	TLorentzVector phoP4( phoPx[k], phoPy[k], phoPz[k], phoE[k] );
	double photonEta = phoP4.Eta();
	double photonPhi = phoP4.Phi();
	if (photonPhi > pi){
	  photonPhi -= 2.*pi;
	}
	if (photonPhi < -pi){
	  photonPhi += 2.*pi;
	}

	deltar = sqrt((photonEta-convEta[i])*(photonEta-convEta[i]) + (photonPhi-convPhi[i])*(photonPhi-convPhi[i]));

	deltaRward.push_back(deltar);

	//if (deltar < tempdeltar and deltar < 0.3){ 
	//  tempdeltar = deltar;
	//  eoverp = phoP4.E() / convMomentum[i];
	//  eoverp2 = phoP4.E() / convMomentum2[i];
	//}
    
	//if (deltar < 0.25) {matching = true;}

      }

    //if (eoverp < 1000) EoverP.push_back(eoverp);
    //  if (eoverp2 < 1000) EoverP2.push_back(eoverp2);
      
      //if (!matching) continue;
       
      dzConv.push_back(convDz[i]);
      dxyConv.push_back(convDxy[i]);
      conversionR.push_back(convR[i]);
      phiConv.push_back(convPhi[i]);
      etaConv.push_back(convEta[i]);
      ConvChi2.push_back(convChi2[i]);
    }


    // For R^2 calculation
    vector<TLorentzVector> jets;
    vector<TLorentzVector> photons;


    for (int i=0; i <nPhotons; i++) {
       
      TLorentzVector phoP4( phoPx[i], phoPy[i], phoPz[i], phoE[i] ) ;
      TLorentzVector phoP4up( phoPx[i], phoPy[i], phoPz[i], phoE[i] ) ;
      TLorentzVector phoP4down( phoPx[i], phoPy[i], phoPz[i], phoE[i] ) ;

      double egScaleup = 1.;
      double egScaledown  = 1.;

      bool photpt = true;
      bool photptup = true;
      bool photptdown = true;


      if (phoMatchedEle[i] > 0) continue;

       
      egScaleup = ( fabs(phoP4up.Eta()) < 1.479 ) ? 1.006 : 1.015 ;
      egScaledown = ( fabs(phoP4down.Eta()) < 1.479 ) ? 0.994 : 0.985 ;

      phoP4up = phoP4up * egScaleup;
      phoP4down = phoP4down * egScaledown;
       
      if ( fabs(fSpike[i]) > 0.001 ) continue ;
      if ( phoP4.Pt() < 50. )  continue ; //N-1!!!!!!!!!!!!!!!!!!!!!!!
      if ( fabs(phoP4.Eta()) > 1.47 )  continue ; //N-1!!!!!!!!!!!!!!!!!!!
      if ( phoHoverE[i] > 0.05 ) continue ; //PHOTONISOLATION
      if ( sigmaIeta[i] >  0.012 ) continue ; //N-1!!!!!!!!!!!!!!!!!1  
      if ( phoP4.Eta() > -0.75 && phoP4.Eta() < -0.6 && phoP4.Phi() > -1. && phoP4.Phi() < -0.8 ) continue ;

      if ( phoP4.Eta() > 0.80 && phoP4.Eta() < 0.95 && phoP4.Phi() > -1.95 && phoP4.Phi() < -1.8 ) continue ; 

      bool fakephotons = false;

      if (string(outname).find("fake") != std::string::npos) fakephotons = true;

      if (!fakephotons){

	/***********************************************************************/
	//                   Cut for isolated photons  
	/***********************************************************************/
       
	
	if ( cHadIso[i] >= 2.6 ) continue ;  // chargedHadron PHOTONISOLATION
	if ( nHadIso[i] >= 3.5 + ( 0.04*phoP4.Pt()   ) ) continue ;   // neutralHadron PHOTONISOLATION
	if ( photIso[i] >= 1.3 + ( 0.005*phoP4.Pt() ) ) continue ;  // photon PHOTONISOLATION

      }	
      
      if (fakephotons){
	/***********************************************************************/
	//                   Cut for fake photons                                                            
	/***********************************************************************/
	
	      
	if (!( cHadIso[i] >= 2.6 )  && (!( nHadIso[i] >= 3.5 + ( 0.04*phoP4.Pt()   ) )) && (!( photIso[i] >= 1.3 + ( 0.005*phoP4.Pt() ) ))  ) continue ;
      
      }
      
      if (phoMatchedEle[i] > 0) continue;
      if (conversionVeto[i] > 0) continue;

      //cout <<"phoMatchedEle: " << phoMatchedEle[i] << endl; 
      //cout <<"conversionVeto: " << conversionVeto[i] << endl; 

      PhotEn.push_back(phoE[i]);
      ptPhot.push_back(phoP4.Pt());
      sort(ptPhot.begin(),ptPhot.end(),comp_pair);
      sort(ptPhotUp.begin(),ptPhotUp.end(),comp_pair);
      sort(ptPhotDown.begin(),ptPhotDown.end(),comp_pair);
      etaPhot.push_back(phoP4.Eta());
      phiPhot.push_back(phoP4.Phi());
      sMinPhot.push_back(sMinPho[i]);
      sMajPhot.push_back(sMajPho[i]);
      sigmaIetaPhot.push_back(sigmaIeta[i]);
      aveTimePhot.push_back(aveTime[i]);
      phohovere.push_back(phoHoverE[i]);
      chadiso.push_back(cHadIso[i]);
      nhadiso.push_back(nHadIso[i]);
      photiso.push_back(photIso[i]);
      //rnine.push_back(r9[i]);
      EThreeByThree.push_back(E3x3[i]);

      weight = pow(0.99887, ptPhot.size());

      photons.push_back(phoP4);
      sort(photons.begin(),photons.end(),comp_pair2);

      phiPhot1 = photons[0].Phi(); 
      phiPhot2 = photons[1].Phi(); 

    }


    // Data MC efficiency scale factors for photons
     
    if ( MC == 0 ) {EfficiencyScaleFactors  = 1.;}
    else EfficiencyScaleFactors = weight; 
     


    for ( int j=0 ; j< nJets; j++ ) {

       
      TLorentzVector jp4( jetPx[j], jetPy[j], jetPz[j], jetE[j] ) ;
      TLorentzVector jp4up( jetPx[j], jetPy[j], jetPz[j], jetE[j] ) ;
      TLorentzVector jp4down( jetPx[j], jetPy[j], jetPz[j], jetE[j] ) ;

      double jCorr;

      jCorr = ( 1. + jecUnc[j] ) ;
      jp4up = jp4up*jCorr;
       
      jCorr = ( 1. - jecUnc[j] ) ;
      jp4down = jp4down*jCorr;

      if ( jp4.Pt() < 30) continue;  //N-1!!!!!!!!!!!!!!!!!11
      
      if ( fabs(jp4.Eta()) > 2.4 ) continue ; //N-1!!!!!!!!!!!!!!!!!!!!!
       
      if ( jetNDau[j] < (double)   2 )  continue ;
      if ( jetCEF[j] >= (double)0.99 )  continue ;
      if ( jetNEF[j] >= (double)0.99 )  continue ;
      if ( jetNHF[j] >= (double)0.99 )  continue ;
      if ( fabs( jp4.Eta() ) < 2.4 && jetCM[j]  <= 0 ) continue ;
      
      ptJet.push_back(jp4.Pt());
      sort(ptJet.begin(),ptJet.end(),comp_pair);
      sort(ptJetUp.begin(), ptJetUp.end(),comp_pair);
      sort(ptJetDown.begin(), ptJetDown.end(), comp_pair);

      phiJet.push_back(jp4.Phi());

      jets.push_back(jp4);

      phiJet1 = jets[0].Phi();
      phiJet2 = jets[1].Phi();

    }


    nPhot = ptPhot.size(); 
    nJet = ptJet.size();
    nMuon = nMuons; 
    nEle = nElectrons; 
    isMC = MC;
    nGoodVtx = nVtx; 
    MET = met;
    METUP = met*1.01;
    METDOWN = met*0.99;

    bool inverted = false;

    if (string(outname).find("low") != std::string::npos) inverted = true;


    //Normal    
                                               h000->Fill(1.);
    if (nGoodVtx < 1) continue;                h000->Fill(2.);
    if (!inverted && MET < 60) continue;       h000->Fill(3.);
    if (inverted && MET > 30) continue;        h000->Fill(3.);
    if (nJet < 2) continue;                    h000->Fill(4.);
    if (nPhot < 2) continue;                   h000->Fill(5.);

    
    //E3x3
    //                                            h000->Fill(1.);
    // if (nGoodVtx < 1) continue;                h000->Fill(2.);
    //                                            h000->Fill(3.);
    // if (nJet < 2) continue;                    h000->Fill(4.);
    // if (nPhot < 1) continue;                   h000->Fill(5.);

    //Test
    //                                              h000->Fill(1.);
    // if (nGoodVtx < 1) continue;                  h000->Fill(2.);
    // if (!inverted && MET < 60) continue;         h000->Fill(3.);
    // if (nJet < 2 or ptJet[0] < 35) continue;     h000->Fill(4.);
    // if (nPhot < 2 or ptPhot[0] < 85) continue;   h000->Fill(5.);
    
    //N-1
    //                                            h000->Fill(1.);
    // if (nGoodVtx < 1) continue;                h000->Fill(2.);
    // if (!inverted && MET < 0) continue;        h000->Fill(3.);
    // if (inverted && MET > 30) continue;        h000->Fill(3.);
    // if (nJet < 1) continue;                    h000->Fill(4.);
    // if (nPhot < 1) continue;                   h000->Fill(5.);

    //Triggeredvariable
    //                                            h000->Fill(1.);
    // if (nGoodVtx < 1) continue;                h000->Fill(2.);
    //                                            h000->Fill(3.);
    // if (nJet < 2) continue;                    h000->Fill(4.);
    // if (nPhot < 2) continue;                   h000->Fill(5.);



    TVector3 MET( metPx, metPy, 0);  

    phiMET = MET.Phi();

    double dPhi1 = deltaPhi(phiMET,phiPhot1);
    double dPhi2 = deltaPhi(phiMET,phiPhot2);
    double dPhi3 = deltaPhi(phiMET,phiJet1);
    double dPhi4 = deltaPhi(phiMET,phiJet2);

   
    double mindPhi = smallest(dPhi1,dPhi2,dPhi3, dPhi4);
    minDPhi = mindPhi;
    

    // R^2 calculation
    vector<TLorentzVector> HEMIS = CombineJets_R_no_seed(jets, photons[0], photons[1]);
    double MTR = CalcMTR(HEMIS[0], HEMIS[1], MET);
    double MRSTAR = CalcGammaMRstar(HEMIS[0], HEMIS[1]);
    Rsqrd = pow(MTR/MRSTAR,2); 

    triggeredvariable = triggered;

    anaTree->Fill();



  }
   
  fout->cd();
  h000->Write();
  anaTree->Write();
  fout->Write();
  fout->Close();

}



vector<TLorentzVector> CombineJets_R_no_seed(vector<TLorentzVector> myjets,TLorentzVector ph1, TLorentzVector ph2){
  vector<TLorentzVector> mynewjets;
  TLorentzVector j1, j2;

  myjets.push_back(ph1);
  myjets.push_back(ph2);

  int N_comb = 1;
  for(int i = 0; i < myjets.size(); i++){
    N_comb *= 2;
  }

  double M_min = 9999999999.0;
  int j_count;
  for(int i = 1; i < N_comb-1; i++){
    TLorentzVector j_temp1, j_temp2;
    int itemp = i;
    j_count = N_comb/2;
    int count = 0;
    while(j_count > 0){
      if(itemp/j_count == 1){
        j_temp1 += myjets[count];
      } else {
        j_temp2 += myjets[count];
      }
      itemp -= j_count*(itemp/j_count);
      j_count /= 2;
      count++;
    }
    double M_temp = j_temp1.M2()+j_temp2.M2();
    // smallest mass
    if(M_temp < M_min){
      // R selection
      M_min = M_temp;
      j1 = j_temp1;
      j2 = j_temp2;
    }
  }


  // set masses to 0
  j1.SetPtEtaPhiM(j1.Pt(),j1.Eta(),j1.Phi(),0.0);
  j2.SetPtEtaPhiM(j2.Pt(),j2.Eta(),j2.Phi(),0.0);

  if(j2.Pt() > j1.Pt()){
    TLorentzVector temp = j1;
    j1 = j2;
    j2 = temp;
  }

  mynewjets.push_back(j1);
  mynewjets.push_back(j2);
  return mynewjets;
}



double CalcMTR(TLorentzVector ja, TLorentzVector jb, TVector3 met){

  double temp = met.Mag()*(ja.Pt()+jb.Pt()) - met.Dot(ja.Vect()+jb.Vect());
  temp /= 2.;

  temp = sqrt(temp);

  return temp;
}


double CalcGammaMRstar(TLorentzVector ja, TLorentzVector jb){
  double A = ja.P();
  double B = jb.P();
  double az = ja.Pz();
  double bz = jb.Pz();
  TVector3 jaT, jbT;
  jaT.SetXYZ(ja.Px(),ja.Py(),0.0);
  jbT.SetXYZ(jb.Px(),jb.Py(),0.0);
  double ATBT = (jaT+jbT).Mag2();

  double temp = sqrt((A+B)*(A+B)-(az+bz)*(az+bz)-
                     (jbT.Dot(jbT)-jaT.Dot(jaT))*(jbT.Dot(jbT)-jaT.Dot(jaT))/(jaT+jbT).Mag2());

  double mybeta = (jbT.Dot(jbT)-jaT.Dot(jaT))/
    sqrt(ATBT*((A+B)*(A+B)-(az+bz)*(az+bz)));

  double mygamma = 1./sqrt(1.-mybeta*mybeta);

  //gamma times MRstar                                                                                                                                                                              
  temp *= mygamma;

  return temp;
}
