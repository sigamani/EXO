#include <iostream>   
#include <algorithm>  
#include <iomanip>
#include <string>
#include <fstream>
#include <map>
#include <sstream>
#include "TColor.h"
#include "TStyle.h"
#include "TMath.h"
#include "TFile.h"
#include "TH1F.h"
#include "TH2F.h"
#include "TTree.h"
#include "TGraph.h"
#include "TMultiGraph.h"
#include "TCanvas.h"
#include "TLegend.h"
#include "TStyle.h"
#include "TLatex.h"
#include "TPolyLine.h"
#include "TROOT.h"
#include <stdio.h>
#include <stdlib.h>



using namespace std;



TH1D* bkgShapeErrUp(const TH1D* hin, int bin){

  char histname[100];
  

	sprintf(histname,"background_shape_b%dUp", bin-1);


      TH1D* hout = (TH1D*) hin->Clone(histname);
   
      double area = hout->GetBinWidth(bin);
  
      double bincontent = hout->GetBinContent(bin);     
      double binerror   = hout->GetBinError(bin);   
	  double newbincontent = bincontent + binerror;

      hout->SetBinContent(bin, newbincontent); 
  
  return hout;  
}



TH1D* bkgShapeErrDown(const TH1D* hin, int bin){

  char histname[100];
  

	sprintf(histname,"background_shape_b%dDown", bin-1);


      TH1D* hout = (TH1D*) hin->Clone(histname);
   
      double area = hout->GetBinWidth(bin);
  
      double bincontent = hout->GetBinContent(bin);     
      double binerror   = hout->GetBinError(bin);   
	  double newbincontent = bincontent + binerror;

      hout->SetBinContent(bin, newbincontent); 
  
  return hout;  
}


TH1D* statUp(const TH1D* hin, int bin){

  char histname[100];
  

	if (  string(hin->GetName()).find("signal") != std::string::npos ){  
	sprintf(histname,"signal_statA_b%dUp", bin-1);
	} else

	sprintf(histname,"background_statB_b%dUp", bin-1);


      TH1D* hout = (TH1D*) hin->Clone(histname);
   
      double area = hout->GetBinWidth(bin);
  
      double bincontent = hout->GetBinContent(bin);     
      double binerror   = hout->GetBinError(bin);   
	  double newbincontent = bincontent + binerror;

      hout->SetBinContent(bin, newbincontent); 
  
  return hout;  
}



TH1D* statDown(const TH1D* hin, int bin){

  char histname[100];
  

	if (  string(hin->GetName()).find("signal") != std::string::npos ){  
	sprintf(histname,"signal_statA_b%dDown", bin-1);
	} else

	sprintf(histname,"background_statB_b%dDown", bin-1);


      TH1D* hout = (TH1D*) hin->Clone(histname);
   
      double area = hout->GetBinWidth(bin);
  
      double bincontent = hout->GetBinContent(bin);     
      double binerror   = hout->GetBinError(bin);   
	  double newbincontent = bincontent - binerror;

      hout->SetBinContent(bin, newbincontent); 
  
  return hout;  

}




void makeAllFiles(int Lambda, int ctau) { 


    char histname[100];
    char histname2[100];
    sprintf(histname,"histofile_L%dCT%d.root", Lambda, ctau);
    sprintf(histname2,"simple-shapes-TH1L%dCT%d.root", Lambda, ctau);


      TFile histofile(histname); 
      TFile *fout = new TFile(histname2,"recreate");


      TH1D* datahist= (TH1D*)histofile.Get("data_obs"); 
      TH1D* signalhist= (TH1D*)histofile.Get("signal"); 
      TH1D* bkg1hist= (TH1D*)histofile.Get("background"); 
      TH1D* bkg1shapehist= (TH1D*)histofile.Get("background_alphaUp"); 

		 // signal stat
         TH1D* GMSB_stat_b1_Up = statUp(signalhist, 1);
         TH1D* GMSB_stat_b2_Up = statUp(signalhist, 2);
         TH1D* GMSB_stat_b3_Up = statUp(signalhist, 3);
         TH1D* GMSB_stat_b4_Up = statUp(signalhist, 4);

         TH1D* GMSB_stat_b1_Down = statDown(signalhist, 1);
         TH1D* GMSB_stat_b2_Down = statDown(signalhist, 2);
         TH1D* GMSB_stat_b3_Down = statDown(signalhist, 3);
         TH1D* GMSB_stat_b4_Down = statDown(signalhist, 4);

		 //bkg stat
         TH1D* bkg_stat_b1_Up = statUp(bkg1hist, 1);
         TH1D* bkg_stat_b2_Up = statUp(bkg1hist, 2);
         TH1D* bkg_stat_b3_Up = statUp(bkg1hist, 3);
         TH1D* bkg_stat_b4_Up = statUp(bkg1hist, 4);

         TH1D* bkg_stat_b1_Down = statDown(bkg1hist, 1);
         TH1D* bkg_stat_b2_Down = statDown(bkg1hist, 2);
         TH1D* bkg_stat_b3_Down = statDown(bkg1hist, 3);
         TH1D* bkg_stat_b4_Down = statDown(bkg1hist, 4);

         TH1D* bkg_shape_b1Up = bkgShapeErrUp(bkg1shapehist, 1);
         TH1D* bkg_shape_b2Up = bkgShapeErrUp(bkg1shapehist, 2);
         TH1D* bkg_shape_b3Up = bkgShapeErrUp(bkg1shapehist, 3);
         TH1D* bkg_shape_b4Up = bkgShapeErrUp(bkg1shapehist, 4);

         TH1D* bkg_shape_b1Down = bkgShapeErrDown(bkg1shapehist, 1);
         TH1D* bkg_shape_b2Down = bkgShapeErrDown(bkg1shapehist, 2);
         TH1D* bkg_shape_b3Down = bkgShapeErrDown(bkg1shapehist, 3);
         TH1D* bkg_shape_b4Down = bkgShapeErrDown(bkg1shapehist, 4);



      int nbins = signalhist->GetNbinsX();

      double nsignal = signalhist->Integral();
      double nbkg = bkg1hist->Integral();
      double ndata = datahist->Integral();


	  // put the signal uncertainty (without stat) here instead of 0.25	  
	  double sig_err_percentage = 0.25 + 1.;


      makeCards(Lambda, ctau, ndata, nsignal, sig_err_percentage, nbkg);

      fout->cd();
	  datahist->Write();
	  signalhist->Write();
	  bkg1hist->Write();
      fout->Write();
      fout->Close();
	  
}










void makeCards(int Lambda, int ctau, double ndata, double nsignal, double sig_err_percentage, double nbkg) { 

  
  char datacardname[100];
  sprintf(datacardname,"datacard-S%d-N%d.txt", Lambda, ctau);  

  ofstream  tablesFile(datacardname);
  tablesFile.setf(ios::fixed);
  tablesFile.precision(3);
 
  tablesFile << "imax 1  number of channels" << endl
             << "jmax 1  number of backgrounds" << endl
             << "kmax *  "<< endl 
             << "------------"<<endl
             << "shapes * * simple-shapes-TH1L"<<Lambda<<"CT"<<ctau<<".root $PROCESS $PROCESS_$SYSTEMATIC" << endl
             << "------------"<<endl
             << "bin 1" <<endl    
             << "observation \t " << ndata << endl
             << "bin            	\t\t 1              \t 1          	" << endl
             << "process        	\t\t signal         \t background   " << endl
             << "process        	\t\t 0              \t 1          	" << endl
             << "rate           	\t\t " << nsignal << "  \t \t "<< nbkg << endl
             << "------------" << endl
             << "signal_syst \t lnN 	\t   " << sig_err_percentage << "          \t\t -      \t   Total uncertainty on the signal " << endl
             << "statA_b0 \t shapeN2 	\t   1          \t\t -      \t   Stat. unc signal" << endl
             << "statA_b1 \t shapeN2 	\t   1          \t\t -      \t   Stat. unc signal" << endl
             << "statA_b2 \t shapeN2 	\t   1          \t\t -      \t   Stat. unc signal" << endl
             << "statA_b3 \t shapeN2 	\t   1          \t\t -      \t   Stat. unc signal" << endl
             << "statB_b0 \t shapeN2 	\t   -          \t\t 1      \t   Stat. unc background" << endl
             << "statB_b1 \t shapeN2 	\t   -          \t\t 1      \t   Stat. unc background" << endl
             << "statB_b2 \t shapeN2 	\t   -          \t\t 1      \t   Stat. unc background" << endl
             << "statB_b3 \t shapeN2 	\t   -          \t\t 1      \t   Stat. unc background" << endl
             << "shape_b0 \t shapeN2 	\t   -          \t\t 1      \t   Shape unc background" << endl
             << "shape_b1 \t shapeN2 	\t   -          \t\t 1      \t   Shape unc background" << endl
             << "shape_b2 \t shapeN2 	\t   -          \t\t 1      \t   Shape unc background" << endl
             << "shape_b3 \t shapeN2 	\t   -          \t\t 1      \t   Shape unc background" << endl;

 
   
  tablesFile.close();


  //TString savedir = "/afs/cern.ch/work/s/sigamani/public/CMSSW_6_1_1/src/HiggsAnalysis/CombinedLimit/";
  //TString savedir = "."; 
  //gSystem->Exec("mv "+TString(datacardname)+" "+savedir); 


}
