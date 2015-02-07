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
#include "setTDRStyle.C"
#include "TF1.h"
#include "TGaxis.h"

using namespace std;




void plot_limit_mass(std::string LAMBDA){

  gStyle->SetCanvasColor(0);
  gStyle->SetPadColor(0);
  gStyle->SetMarkerStyle(15);
  gStyle->SetMarkerSize(0.25);
  gStyle->SetPalette(1);
  gStyle->SetTextFont(42);
  gStyle->SetMarkerColor(37);

  if ( LAMBDA=="180" ) {
    // L180
    Double_t gev30[4] = {};
    Double_t gev50[4] = {4.5,8.,8.,4.5};
    Double_t gev60[4] = {1.,70.,70.,1.};
    Double_t gev80[4] = {1.,70.,70.,1.};
    Double_t gev100[4] = {1.,70.,70.,1.};
    Double_t gev140[4] = {1.,50.,50.,1.};  
    Double_t gev160[4] = {1.,40.,40.,1.};
    Double_t gev170[4] = {2.,30.,30.,2.};
    Double_t gev180[4] = {};
  }

  if ( LAMBDA=="160" ) {
    // L160
    Double_t gev30[4] = {};
    Double_t gev50[4] = {1.,60.,60.,1.};
    Double_t gev60[4] = {1.,105.,105.,1.};
    Double_t gev80[4] = {1.,100.,100.,1.};
    Double_t gev100[4] = {1.,100.,100.,1.};
    Double_t gev140[4] = {1.,75.,75.,1.};
    Double_t gev160[4] = {1.,65.,65.,1.};
    Double_t gev170[4] = {1.,55.,55.,1.};
    Double_t gev180[4] = {};
  }

  if ( LAMBDA=="140" ) {
    // L140 
    Double_t gev30[4] = {};
    Double_t gev50[4] = {1.,100.,100.,1.};
    Double_t gev60[4] = {1.,180.,180.,1.};
    Double_t gev80[4] = {1.,170.,170.,1.};
    Double_t gev100[4] = {1.,170.,170.,1.};
    Double_t gev140[4] = {1.,110.,110.,1.};
    Double_t gev160[4] = {1.,100.,100.,1.};
    Double_t gev170[4] = {1.,80.,80.,1.};
    Double_t gev180[4] = {};
  }


  Double_t mTh[7] = {50,60,80,100,140,160,170};

  Double_t x_pdf[15] = {50,60,80,100,140,160,170,170,160,140,100,80,60,50,50};

  
  Double_t y_pdf_exp[15] = { gev50[0],
			     gev60[0],
			     gev80[0],
			     gev100[0],
			     gev140[0],
			     gev160[0],
			     gev170[0],
			     gev170[1],
			     gev160[1],
			     gev140[1],
			     gev100[1],
			     gev80[1],
			     gev60[1],
			     gev50[1],
			     gev50[0]};

  Double_t y_pdf_obs[15] = { gev50[3],
                             gev60[3],
                             gev80[3],
                             gev100[3],
                             gev140[3],
                             gev160[3],
			     gev170[3],
			     gev170[2],
                             gev160[2],
                             gev140[2],
                             gev100[2],
                             gev80[2],
                             gev60[2],
                             gev50[2],
                             gev50[3]};


  TGraph* Exp_graph;
  Exp_graph = new TGraph(15, x_pdf, y_pdf_exp );
  Exp_graph->SetFillStyle(3012);
  Exp_graph->SetFillColor(kRed);


  double METcut_optimal = 60; 
  

  TLine *line = new TLine(METcut_optimal,10e-2,METcut_optimal,10e2);
  line->SetLineColor(kBlue);
  line->SetLineStyle(2);
  line->SetLineWidth(5);
 
  
  TCanvas* c0 = new TCanvas("exclusion limit", "exclusion limit", 700, 600);

  c0->SetLogy();

  Exp_graph->SetTitle("");
  Exp_graph->GetXaxis()->SetTitle("MET cut (GeV)");
  Exp_graph->GetYaxis()->SetTitle("#tilde{#chi}^{0}_{1} Mean Proper Decay Length (cm)");
  Exp_graph->GetYaxis()->SetRangeUser(0.1, 1000);
  Exp_graph->GetXaxis()->SetRangeUser(0,200);

  Exp_graph->Draw("AF");
  line->Draw("same");

  c0->Update();
  c0->RedrawAxis();

   
  TLegend* leg = new TLegend(0.3,0.8,0.65,0.93);
  leg->SetFillStyle(0); leg->SetBorderSize(0);
  leg->SetFillColor(0);

 
  leg->SetHeader("");
  leg->SetTextFont(22);
  leg->SetTextSize(0.04);
  leg->AddEntry(Exp_graph, "Exp. exclusion (#Lambda = 180 TeV)", "F");
  leg->Draw("same");

  c0->SaveAs("~/www/2Dexclusion_limit.pdf");
  c0->SaveAs("~/www/2Dexclusion_limit.png");

}


