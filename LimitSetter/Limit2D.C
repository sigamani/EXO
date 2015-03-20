#include <vector>
#include <stdio.h>
#include <stdlib.h>
#include <TFile.h>
#include <TMath.h>
#include <iostream>
#include <TGraphErrors.h>
#include <TGraphAsymmErrors.h>


// define the generator's information across different ctau models
void Limit2D() {

   gROOT->LoadMacro("CMS_lumi.C");

   string hfolder  = "~/www/home/" ;

   //TString legTitle = "#tilde{#chi}^{0}_{1} #rightarrow #gamma #tilde{G}, c#tau ="+ ctau + " mm" ;
   string limitPlotName = "limit2D" ;

   // For the frame:
   gStyle->SetFrameBorderMode(0);
   gStyle->SetFrameBorderSize(1);
   gStyle->SetFrameFillColor(0);
   gStyle->SetFrameFillStyle(0);
   gStyle->SetFrameLineColor(1);
   gStyle->SetFrameLineStyle(1);
   gStyle->SetFrameLineWidth(1);
   gStyle->SetOptTitle(0);

//   gStyle->SetLabelOffset(0.007, "XYZ");
//   gStyle->SetLabelSize(0.04, "XYZ");

   TCanvas *c1a = new TCanvas("c1a","c1a" ,800,800);

   c1a->cd() ;
   //c1a->SetGridy() ;
   c1a->SetTopMargin(0.1);
   c1a->SetBottomMargin(0.22);
   c1a->SetLeftMargin(0.15);
   c1a->SetRightMargin(0.05);

   c1a->SetLogy() ;


   

   //************** Observed 8 TeV Limits ********************************//
   // Mass  = 1.45*Lambda - 5
   // fitted tip: (321.08, 141.84)
   Double_t obs_cms_8TeV[13] = {  140,   169,   198,  227,   256,    314,    314, 285,    256,     227,     198,     169,     140 }; 
   Double_t obs_ct_8TeV[13]  = {92.39, 56.98, 51.43, 48.6, 70.59, 138.78, 212.92, 290, 702.16, 1063.61, 1298.93, 1243.29, 1349.28 }; 

   TGraph* obs_cms_gr = new TGraph(13, obs_cms_8TeV, obs_ct_8TeV );
   obs_cms_gr->GetXaxis()->SetLimits( 100, 460 ) ;
   obs_cms_gr->SetMaximum(1000000 ) ;
   obs_cms_gr->SetMinimum(0.5 ) ;
   obs_cms_gr->GetYaxis()->SetTitle( "#tilde{#chi}^{0}_{1} Mean Proper Decay Length (cm)"  ) ;
   obs_cms_gr->GetXaxis()->SetTitle( "#tilde{#chi}^{0}_{1} Mass (GeV)") ;
   obs_cms_gr->GetYaxis()->SetTitleSize(0.047);
   obs_cms_gr->GetXaxis()->SetTitleSize(0.047);
   obs_cms_gr->GetXaxis()->SetTitleOffset(1.45);
   obs_cms_gr->GetYaxis()->SetTitleOffset(1.45);
   obs_cms_gr->SetLineColor(2);
   obs_cms_gr->SetLineWidth(4);
   obs_cms_gr->SetLineStyle(7);
   obs_cms_gr->Draw("AL");
   c1a->Update() ;

   //**************************observed cms 7 TeV *******************************//
   Double_t obs_cms_7TeV[16]={100., 145., 157., 179., 192., 216., 221., 218., 218., 221., 216., 192., 179., 157., 145., 100.}; 
   Double_t obs_ct_7TeV[16] ={0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 10., 25.0, 50.0, 100.0, 200.0, 400.0, 600.0, 600.0}; 

   TGraph* obs_cms7_gr;
   obs_cms7_gr = new TGraph(16, obs_cms_7TeV, obs_ct_7TeV );
   obs_cms7_gr->SetFillColor(5);
   obs_cms7_gr->SetLineColor(1);
   obs_cms7_gr->SetFillStyle(3001) ;
   obs_cms7_gr->Draw("FLsames");
   c1a->Update() ;

   //**************************observed cdf*******************************//
   Double_t obs_cdf[6]={100., 146., 149.5, 149.5, 146., 100.};
   Double_t ct_cdf[6] ={0.0, 0.0, 0.0, 30.0, 60.0, 60.0};

   TGraph* obs_cdf_gr;
   obs_cdf_gr = new TGraph(6, obs_cdf, ct_cdf );
   obs_cdf_gr->SetFillColor(28);
   obs_cdf_gr->SetFillStyle(3001);
   obs_cdf_gr->SetLineColor(1);
   obs_cdf_gr->Draw("FLsames");

   c1a->Update() ;

   //************************** EXO-14-017*******************************//
   //Double_t exp_cms_conv8TeV[4]={198, 227., 227., 198};  // MET > 50 (only 4 points)
   //Double_t ct_conv8TeV[4]={1.0, 1.0, 50., 100.}; // MET > 50 (only 4 points)

   Double_t exp_cms_conv8TeV[6]={198, 227., 256., 256., 227., 198};  
   //Theoretical CTau
 //  Double_t ct_conv8TeV[6]={1.0, 1.0, 1.0, 45., 80., 140.};  // MET > 120
 //  Double_t ct_conv8TeV[6]={1.0, 1.0, 1.0, 65., 90., 170.};  // MET > 100
//   Double_t ct_conv8TeV[6]={1.0, 1.0, 1.0, 60., 90., 165.};  // MET > 80
//   Double_t ct_conv8TeV[6]={1.0, 1.0, 1.0, 70.0, 105., 185.}; // MET > 60
   
   //Real CTau with 1 mm
   //Double_t ct_conv8TeV[6]={0.0516, 0.0428, 0.08, 30., 45., 95.};  // MET > 60

   //Real CTau with 10 mm
   //Double_t ct_conv8TeV[6]={0.516, 0.428, 0.366, 30., 45., 95.};  // MET > 60

   //Real CTau with GMSB bin 1 set to 0
   Double_t ct_conv8TeV[6]={0.516, 0.428, 1.5, 30., 45., 95.};  // MET > 60

   TGraph* exp_cms8_conv_gr;
   exp_cms8_conv_gr = new TGraph(6, exp_cms_conv8TeV, ct_conv8TeV );
   exp_cms8_conv_gr->SetFillColor(kBlue);
   exp_cms8_conv_gr->SetLineColor(kBlue);
   exp_cms8_conv_gr->SetFillStyle(3244);
   exp_cms8_conv_gr->Draw("FLsames");
   c1a->Update() ;

   //************** Expected 8 TeV Limits ********************************//
   // Neutralino Mass = 1.45*Lambda -5
   // falling : ctau = -11.017*Mass +3813.5 , raising : ctau = 0.514*mass - 68.5  crossing : (336.6 , 104.5)
   //Double_t exp_cms_8TeV[12] = { 100., 120,  140,  160,  180,  220,           220    180,    160,    140,    120,    100 }; 
   Double_t exp_cms_8TeV[14] = {   140,  169,  198,  227,  256,  314, 378, 378, 314,    256,    227,    198,    169,    140 }; 
   Double_t exp_ct_8TeV[14]  = {  51.7, 52.1, 51.3, 46.8, 64.8, 92.1, 152.4, 156.9, 370.6,  943.6, 1345.6, 1881.4, 1601.6, 1964.5 }; 
   TGraph* exp_cms_gr = new TGraph(14, exp_cms_8TeV, exp_ct_8TeV );
   exp_cms_gr->SetFillColor(kRed);
   exp_cms_gr->SetFillStyle(3002);
   exp_cms_gr->SetLineColor(kRed);
   exp_cms_gr->SetLineWidth(0);
   exp_cms_gr->Draw("Fsames"); 
   c1a->Update() ;

   //*** ATLAS observed 8 TeV ****
   Double_t lambda_atlas_8TeV[14] = { 82.5 , 102.5,   140,   160,   180,   200,   220, 260,  300, 302.58, 
                                                                         300, 260, 220, 200 }; 
   Double_t t_atlas_8TeV[14] = { 121.81, 90.94, 46.63, 36.12, 27.18, 20.26, 14.59, 7.47, 2.6, 1.83, 
                                                                         1.31, 0.61, 0.39, 0.30 }; 
   Double_t obs_atlas_8TeV[14], mass_atlas_8TeV[14];
   for ( int i=0; i< 14; i++) {
        obs_atlas_8TeV[i]  = t_atlas_8TeV[i]*30. ;
        mass_atlas_8TeV[i] = (lambda_atlas_8TeV[i]*1.45) - 5 ;
   }

   TGraph* obs_atlas_gr = new TGraph(14, mass_atlas_8TeV, obs_atlas_8TeV );
   obs_atlas_gr->SetLineColor(8);
   obs_atlas_gr->SetLineWidth(3);
   obs_atlas_gr->SetLineStyle(5);
   
   //obs_atlas_gr->Draw("Lsames");
   //c1a->Update() ;

   TLegend* leg = new TLegend(0.4, 0.66, 0.7, 0.88);
   leg->SetFillStyle(0); 
   leg->SetBorderSize(0); 
   leg->SetFillColor(0);
   leg->SetTextSize(0.030) ;
 
   // leg ->SetTextFont(22);
   leg ->SetTextFont(42);
   leg->AddEntry(exp_cms_gr,      "CMS Timing Exp. #scale[0.7]{(19.1 fb^{-1} at 8 TeV)}",   "F" );
   leg->AddEntry(obs_cms_gr,      "CMS Timing Obs. #scale[0.7]{(19.1 fb^{-1} at 8 TeV)}",   "L" );
   leg->AddEntry(exp_cms8_conv_gr,"CMS Conversions Exp. #scale[0.7]{(19.7 fb^{-1} at 8 TeV)}","F"); 
   leg->AddEntry(obs_cms7_gr,     "CMS Timing Obs. #scale[0.7]{(4.9 fb^{-1} at 7 TeV)}",   "F");
   //leg->AddEntry(obs_atlas_gr,    "ATLAS Obs 20.3 fb^{-1} 8 TeV", "L" );
   leg->AddEntry(obs_cdf_gr,      "CDF Obs. #scale[0.7]{(2.6 fb^{-1} at 1.96 TeV)}", "F" ); 
   leg->Draw("same");
   c1a->Update() ;

   // new axis
   //TGaxis *lAxis = new TGaxis(140,0.16,430,0.16,100, 300, 8,"+L");
   TGaxis *lAxis = new TGaxis(140,3.303691,428.794,3.303691,100,300,8,"+L");
   lAxis->SetLabelOffset(0.005);
   lAxis->SetLabelSize(0.04);
   lAxis->SetTickSize(0.03);
   lAxis->SetGridLength(0);
   lAxis->SetTitleOffset(1);
   lAxis->SetTitleSize(0.04);
   lAxis->SetTitleColor(1);
   lAxis->SetTitleFont(42);
   lAxis->SetTitle("#Lambda (TeV)");
   lAxis->Draw("sames");


   gPad->RedrawAxis(); 

   CMS_lumi( c1a, 2, 11 ) ;
   c1a->Update();

   TString gPlotname = hfolder +  limitPlotName  ;
   c1a->Print( gPlotname +".png" ) ;
   //c1a->Print( gPlotname +".pdf") ;
   delete c1a ;

}


