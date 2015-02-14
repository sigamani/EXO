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




void plot_limit_mass(){

  gStyle->SetCanvasColor(0);
  gStyle->SetPadColor(0);
  gStyle->SetMarkerStyle(15);
  gStyle->SetMarkerSize(0.25);
  gStyle->SetPalette(1);
  gStyle->SetTextFont(42);
  gStyle->SetMarkerColor(37);

    Double_t Lambda180_30GeV[4] = {};
    Double_t Lambda180_50GeV[4] = {4.5,8.,8.,4.5};
    Double_t Lambda180_60GeV[4] = {1.,70.,70.,1.};
    Double_t Lambda180_80GeV[4] = {1.,70.,70.,1.};
    Double_t Lambda180_100GeV[4] = {1.,70.,70.,1.};
    Double_t Lambda180_140GeV[4] = {1.,50.,50.,1.};  
    Double_t Lambda180_160GeV[4] = {1.,40.,40.,1.};
    Double_t Lambda180_170GeV[4] = {2.,30.,30.,2.};
    Double_t Lambda180_180GeV[4] = {};

    Double_t Lambda160_30GeV[4] = {};
    Double_t Lambda160_50GeV[4] = {1.,60.,60.,1.};
    Double_t Lambda160_60GeV[4] = {1.,105.,105.,1.};
    Double_t Lambda160_80GeV[4] = {1.,100.,100.,1.};
    Double_t Lambda160_100GeV[4] = {1.,100.,100.,1.};
    Double_t Lambda160_140GeV[4] = {1.,75.,75.,1.};
    Double_t Lambda160_160GeV[4] = {1.,65.,65.,1.};
    Double_t Lambda160_170GeV[4] = {1.,55.,55.,1.};
    Double_t Lambda160_180GeV[4] = {};

    Double_t Lambda140_30GeV[4] = {};
    Double_t Lambda140_50GeV[4] = {1.,100.,100.,1.};
    Double_t Lambda140_60GeV[4] = {1.,180.,180.,1.};
    Double_t Lambda140_80GeV[4] = {1.,170.,170.,1.};
    Double_t Lambda140_100GeV[4] = {1.,170.,170.,1.};
    Double_t Lambda140_140GeV[4] = {1.,110.,110.,1.};
    Double_t Lambda140_160GeV[4] = {1.,100.,100.,1.};
    Double_t Lambda140_170GeV[4] = {1.,80.,80.,1.};
    Double_t Lambda140_180GeV[4] = {};


  Double_t mTh[7] = {50,60,80,100,140,160,170};

  Double_t x_pdf[15] = {50,60,80,100,140,160,170,170,160,140,100,80,60,50,50};

  
  Double_t y_pdf_Lambda180[15]={ Lambda180_50GeV[0],
								 Lambda180_60GeV[0],
								 Lambda180_80GeV[0],
								 Lambda180_100GeV[0],
								 Lambda180_140GeV[0],
								 Lambda180_160GeV[0],
								 Lambda180_170GeV[0],
								 Lambda180_170GeV[1],
								 Lambda180_160GeV[1],
								 Lambda180_140GeV[1],
								 Lambda180_100GeV[1],
								 Lambda180_80GeV[1],
								 Lambda180_60GeV[1],
								 Lambda180_50GeV[1],
								 Lambda180_50GeV[0] };

  Double_t y_pdf_Lambda160[15]={ Lambda160_50GeV[0],
								 Lambda160_60GeV[0],
								 Lambda160_80GeV[0],
								 Lambda160_100GeV[0],
								 Lambda160_140GeV[0],
								 Lambda160_160GeV[0],
								 Lambda160_170GeV[0],
								 Lambda160_170GeV[1],
								 Lambda160_160GeV[1],
								 Lambda160_140GeV[1],
								 Lambda160_100GeV[1],
								 Lambda160_80GeV[1],
								 Lambda160_60GeV[1],
								 Lambda160_50GeV[1],
								 Lambda160_50GeV[0] };

  Double_t y_pdf_Lambda140[15]={ Lambda140_50GeV[0],
								 Lambda140_60GeV[0],
								 Lambda140_80GeV[0],
								 Lambda140_100GeV[0],
								 Lambda140_140GeV[0],
								 Lambda140_160GeV[0],
								 Lambda140_170GeV[0],
								 Lambda140_170GeV[1],
								 Lambda140_160GeV[1],
								 Lambda140_140GeV[1],
								 Lambda140_100GeV[1],
								 Lambda140_80GeV[1],
								 Lambda140_60GeV[1],
								 Lambda140_50GeV[1],
								 Lambda140_50GeV[0] };




  TGraph* Exp_graph;
  Exp_graph_Lambda180 = new TGraph(15, x_pdf, y_pdf_Lambda180 );
  Exp_graph_Lambda160 = new TGraph(15, x_pdf, y_pdf_Lambda160 );
  Exp_graph_Lambda140 = new TGraph(15, x_pdf, y_pdf_Lambda140 );
  Exp_graph_Lambda180->SetFillStyle(3012);
  Exp_graph_Lambda180->SetFillColor(kRed);
  Exp_graph_Lambda160->SetFillStyle(3004);
  Exp_graph_Lambda160->SetFillColor(kBlue);
  Exp_graph_Lambda140->SetFillStyle(3005);
  Exp_graph_Lambda140->SetFillColor(8);

  double METcut_optimal = 60; 
  

  TLine *line = new TLine(METcut_optimal,1,METcut_optimal,10e2);
  line->SetLineColor(kBlue);
  line->SetLineStyle(2);
  line->SetLineWidth(5);
 
  
  TCanvas* c0 = new TCanvas("exclusion limit", "exclusion limit", 700, 600);

  c0->SetLogy();

  Exp_graph_Lambda180->SetTitle("");
  Exp_graph_Lambda180->GetXaxis()->SetTitle("MET cut (GeV)");
  Exp_graph_Lambda180->GetYaxis()->SetTitle("#tilde{#chi}^{0}_{1} Mean Proper Decay Length (cm)");
  Exp_graph_Lambda180->GetYaxis()->SetRangeUser(1, 1000);
  Exp_graph_Lambda180->GetXaxis()->SetRangeUser(0,200);

  Exp_graph_Lambda180->Draw("AF");
  Exp_graph_Lambda160->Draw("Fsame");
  Exp_graph_Lambda140->Draw("Fsame");
  line->Draw("same");

  c0->Update();
  c0->RedrawAxis();

   
  TLegend* leg = new TLegend(0.3,0.75,0.65,0.99);
  leg->SetFillStyle(0); leg->SetBorderSize(0);
  leg->SetFillColor(0);

 
  leg->SetHeader("");
//  leg->SetTextFont(22);
  leg->SetTextSize(0.04);
  leg->AddEntry(Exp_graph_Lambda180, "Exp. exclusion (#Lambda = 180 TeV)", "F");
  leg->AddEntry(Exp_graph_Lambda160, "Exp. exclusion (#Lambda = 160 TeV)", "F");
  leg->AddEntry(Exp_graph_Lambda140, "Exp. exclusion (#Lambda = 140 TeV)", "F");
  leg->Draw("same");

  c0->SaveAs("~/www/2Dexclusion_limit.pdf");
  c0->SaveAs("~/www/2Dexclusion_limit.png");

}


