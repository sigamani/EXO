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
void rootlogon();


TString savedir = "./img_fit/";
TString extra = "";

// TFile* file_CT1L140 = new TFile(("./exclusionfiles/higgsCombineL140CTau1shapedata"+extra+".Asymptotic.mH120.root"), "READ");
// TFile* file_CT10L140 = new TFile(("./exclusionfiles/higgsCombineL140CTau10shapedata"+extra+".Asymptotic.mH120.root"), "READ");
// TFile* file_CT100L140 = new TFile(("./exclusionfiles/higgsCombineL140CTau100shapedata"+extra+".Asymptotic.mH120.root"), "READ");
// TFile* file_CT500L140 = new TFile(("./exclusionfiles/higgsCombineL140CTau500shapedata"+extra+".Asymptotic.mH120.root"), "READ");
// TFile* file_CT1000L140 = new TFile(("./exclusionfiles/higgsCombineL140CTau1000shapedata"+extra+".Asymptotic.mH120.root"), "READ");
// TFile* file_CT2000L140 = new TFile(("./exclusionfiles/higgsCombineL140CTau2000shapedata"+extra+".Asymptotic.mH120.root"), "READ");

TFile* file_CT1L140 = new TFile(("./exclusionfiles/FULL_CLS_RESULT_L140CT1.root"), "READ");
TFile* file_CT10L140 = new TFile(("./exclusionfiles/FULL_CLS_RESULT_L140CT10.root"), "READ");
TFile* file_CT100L140 = new TFile(("./exclusionfiles/FULL_CLS_RESULT_L140CT100.root"), "READ");
TFile* file_CT500L140 = new TFile(("./exclusionfiles/FULL_CLS_RESULT_L140CT500.root"), "READ");
TFile* file_CT1000L140 = new TFile(("./exclusionfiles/FULL_CLS_RESULT_L140CT1000.root"), "READ");
TFile* file_CT2000L140 = new TFile(("./exclusionfiles/FULL_CLS_RESULT_L140CT2000.root"), "READ");

// TFile* file_CT1L140 = new TFile(("./exclusionfiles/ASYMPTOTIC_CLS_RESULT_L140CT1.root"), "READ");
// TFile* file_CT10L140 = new TFile(("./exclusionfiles/ASYMPTOTIC_CLS_RESULT_L140CT10.root"), "READ");
// TFile* file_CT100L140 = new TFile(("./exclusionfiles/ASYMPTOTIC_CLS_RESULT_L140CT100.root"), "READ");
// TFile* file_CT500L140 = new TFile(("./exclusionfiles/ASYMPTOTIC_CLS_RESULT_L140CT500.root"), "READ");
// TFile* file_CT1000L140 = new TFile(("./exclusionfiles/ASYMPTOTIC_CLS_RESULT_L140CT1000.root"), "READ");
// TFile* file_CT2000L140 = new TFile(("./exclusionfiles/ASYMPTOTIC_CLS_RESULT_L140CT2000.root"), "READ");


void plot_limit_mass(std::string LAMBDA){

  rootlogon();
  
  double xsec;

  if ( LAMBDA=="140" ) {
    xsec = 0.0574;
    TTree * CT1 = (TTree*)file_CT1L140->Get("limit");
    TTree * CT10 = (TTree*)file_CT10L140->Get("limit");
    //TTree * CT50 = (TTree*)file_CT50L140->Get("limit");
    TTree * CT100 = (TTree*)file_CT100L140->Get("limit");
    TTree * CT500 = (TTree*)file_CT500L140->Get("limit");
    TTree * CT1000 = (TTree*)file_CT1000L140->Get("limit");
    TTree * CT2000 = (TTree*)file_CT2000L140->Get("limit");
  }

  Double_t obs_lim[6]= {0.};
  Double_t exp_lim[6]= {0.};

  TH1F* CT500histo1 = new TH1F("CT500histo1","",100,0,100.0);
  CT500->Draw("limit>>CT500histo1", "quantileExpected==-1");
  TH1F* CT500histo2 = new TH1F("CT500histo2","",100,0,100.0);
  CT500->Draw("limit>>CT500histo2", "quantileExpected>0.02 && quantileExpected<0.03");
  TH1F* CT500histo16 = new TH1F("CT500histo16","",100,0,100.0);
  CT500->Draw("limit>>CT500histo16", "quantileExpected>0.15 && quantileExpected<0.16");
  TH1F* CT500histo50 = new TH1F("CT500histo50","",100,0,100.0);
  CT500->Draw("limit>>CT500histo50", "quantileExpected==0.5");
  TH1F* CT500histo84 = new TH1F("CT500histo84","",100,0,100.0);
  CT500->Draw("limit>>CT500histo84", "quantileExpected>0.83 && quantileExpected<0.84");
  TH1F* CT500histo97 = new TH1F("CT500histo97","",100,0,100.0);
  CT500->Draw("limit>>CT500histo97", "quantileExpected>0.97 && quantileExpected<0.98");

  TH1F* CT1histo1 = new TH1F("CT1histo1","",100,0,100.0);
  CT1->Draw("limit>>CT1histo1", "quantileExpected==-1");
  TH1F* CT1histo2 = new TH1F("CT1histo2","",100,0,100.0);
  CT1->Draw("limit>>CT1histo2", "quantileExpected>0.02 && quantileExpected<0.03");
  TH1F* CT1histo16 = new TH1F("CT1histo16","",100,0,100.0);
  CT1->Draw("limit>>CT1histo16", "quantileExpected>0.15 && quantileExpected<0.16");
  TH1F* CT1histo50 = new TH1F("CT1histo50","",100,0,100.0);
  CT1->Draw("limit>>CT1histo50", "quantileExpected==0.5");
  TH1F* CT1histo84 = new TH1F("CT1histo84","",100,0,100.0);
  CT1->Draw("limit>>CT1histo84", "quantileExpected>0.83 && quantileExpected<0.84");
  TH1F* CT1histo97 = new TH1F("CT1histo97","",100,0,100.0);
  CT1->Draw("limit>>CT1histo97", "quantileExpected>0.97 && quantileExpected<0.98");

  TH1F* CT10histo1 = new TH1F("CT10histo1","",100,0,100.0);
  CT10->Draw("limit>>CT10histo1", "quantileExpected==-1");
  TH1F* CT10histo2 = new TH1F("CT10histo2","",100,0,100.0);
  CT10->Draw("limit>>CT10histo2", "quantileExpected>0.02 && quantileExpected<0.03");
  TH1F* CT10histo16 = new TH1F("CT10histo16","",100,0,100.0);
  CT10->Draw("limit>>CT10histo16", "quantileExpected>0.15 && quantileExpected<0.16");
  TH1F* CT10histo50 = new TH1F("CT10histo50","",100,0,100.0);
  CT10->Draw("limit>>CT10histo50", "quantileExpected==0.5");
  TH1F* CT10histo84 = new TH1F("CT10histo84","",100,0,100.0);
  CT10->Draw("limit>>CT10histo84", "quantileExpected>0.83 && quantileExpected<0.84");
  TH1F* CT10histo97 = new TH1F("CT10histo97","",100,0,100.0);
  CT10->Draw("limit>>CT10histo97", "quantileExpected>0.97 && quantileExpected<0.98");

  TH1F* CT100histo1 = new TH1F("CT100histo1","",100,0,100.0);
  CT100->Draw("limit>>CT100histo1", "quantileExpected==-1");
  TH1F* CT100histo2 = new TH1F("CT100histo2","",100,0,100.0);
  CT100->Draw("limit>>CT100histo2", "quantileExpected>0.02 && quantileExpected<0.03");
  TH1F* CT100histo16 = new TH1F("CT100histo16","",100,0,100.0);
  CT100->Draw("limit>>CT100histo16", "quantileExpected>0.15 && quantileExpected<0.16");
  TH1F* CT100histo50 = new TH1F("CT100histo50","",100,0,100.0);
  CT100->Draw("limit>>CT100histo50", "quantileExpected==0.5");
  TH1F* CT100histo84 = new TH1F("CT100histo84","",100,0,100.0);
  CT100->Draw("limit>>CT100histo84", "quantileExpected>0.83 && quantileExpected<0.84");
  TH1F* CT100histo97 = new TH1F("CT100histo97","",100,0,100.0);
  CT100->Draw("limit>>CT100histo97", "quantileExpected>0.97 && quantileExpected<0.98");

  // TH1F* CT50histo1 = new TH1F("CT50histo1","",100,0,100.0);
  // CT50->Draw("limit>>CT50histo1", "quantileExpected==-1");
  // TH1F* CT50histo2 = new TH1F("CT50histo2","",100,0,100.0);
  // CT50->Draw("limit>>CT50histo2", "quantileExpected>0.02 && quantileExpected<0.03");
  // TH1F* CT50histo16 = new TH1F("CT50histo16","",100,0,100.0);
  // CT50->Draw("limit>>CT50histo16", "quantileExpected>0.15 && quantileExpected<0.16");
  // TH1F* CT50histo50 = new TH1F("CT50histo50","",100,0,100.0);
  // CT50->Draw("limit>>CT50histo50", "quantileExpected==0.5");
  // TH1F* CT50histo84 = new TH1F("CT50histo84","",100,0,100.0);
  // CT50->Draw("limit>>CT50histo84", "quantileExpected>0.83 && quantileExpected<0.84");
  // TH1F* CT50histo97 = new TH1F("CT50histo97","",100,0,100.0);
  // CT50->Draw("limit>>CT50histo97", "quantileExpected>0.97 && quantileExpected<0.98");

  TH1F* CT2000histo1 = new TH1F("CT2000histo1","",100,0,100.0);
  CT2000->Draw("limit>>CT2000histo1", "quantileExpected==-1");
  TH1F* CT2000histo2 = new TH1F("CT2000histo2","",100,0,100.0);
  CT2000->Draw("limit>>CT2000histo2", "quantileExpected>0.02 && quantileExpected<0.03");
  TH1F* CT2000histo16 = new TH1F("CT2000histo16","",100,0,100.0);
  CT2000->Draw("limit>>CT2000histo16", "quantileExpected>0.15 && quantileExpected<0.16");
  TH1F* CT2000histo50 = new TH1F("CT2000histo50","",100,0,100.0);
  CT2000->Draw("limit>>CT2000histo50", "quantileExpected==0.5");
  TH1F* CT2000histo84 = new TH1F("CT2000histo84","",100,0,100.0);
  CT2000->Draw("limit>>CT2000histo84", "quantileExpected>0.83 && quantileExpected<0.84");
  TH1F* CT2000histo97 = new TH1F("CT2000histo97","",100,0,100.0);
  CT2000->Draw("limit>>CT2000histo97", "quantileExpected>0.97 && quantileExpected<0.98");

  TH1F* CT1000histo1 = new TH1F("CT1000histo1","",100,0,100.0);
  CT1000->Draw("limit>>CT1000histo1", "quantileExpected==-1");
  TH1F* CT1000histo2 = new TH1F("CT1000histo2","",100,0,100.0);
  CT1000->Draw("limit>>CT1000histo2", "quantileExpected>0.02 && quantileExpected<0.03");
  TH1F* CT1000histo16 = new TH1F("CT1000histo16","",100,0,100.0);
  CT1000->Draw("limit>>CT1000histo16", "quantileExpected>0.15 && quantileExpected<0.16");
  TH1F* CT1000histo50 = new TH1F("CT1000histo50","",100,0,100.0);
  CT1000->Draw("limit>>CT1000histo50", "quantileExpected==0.5");
  TH1F* CT1000histo84 = new TH1F("CT1000histo84","",100,0,100.0);
  CT1000->Draw("limit>>CT1000histo84", "quantileExpected>0.83 && quantileExpected<0.84");
  TH1F* CT1000histo97 = new TH1F("CT1000histo97","",100,0,100.0);
  CT1000->Draw("limit>>CT1000histo97", "quantileExpected>0.97 && quantileExpected<0.98");

  Float_t upperlimit500[5] = {
    CT500histo2->GetMean(), 
    CT500histo16->GetMean(),
    CT500histo50->GetMean(),
    CT500histo84->GetMean(),
    CT500histo97->GetMean(),
  };

  Float_t upperlimit1[5] = {
    CT1histo2->GetMean(),
    CT1histo16->GetMean(),
    CT1histo50->GetMean(),
    CT1histo84->GetMean(),
    CT1histo97->GetMean(),
  };

  Float_t upperlimit10[5] = {
    CT10histo2->GetMean(),
    CT10histo16->GetMean(),
    CT10histo50->GetMean(),
    CT10histo84->GetMean(),
    CT10histo97->GetMean(),
  };

  // Float_t upperlimit50[5] = {
  //   CT50histo2->GetMean(),
  //   CT50histo16->GetMean(),
  //   CT50histo50->GetMean(),
  //   CT50histo84->GetMean(),
  //   CT50histo97->GetMean(),
  // };

  Float_t upperlimit100[5] = {
    CT100histo2->GetMean(),
    CT100histo16->GetMean(),
    CT100histo50->GetMean(),
    CT100histo84->GetMean(),
    CT100histo97->GetMean(),
  };

  Float_t upperlimit1000[5] = {
    CT1000histo2->GetMean(),
    CT1000histo16->GetMean(),
    CT1000histo50->GetMean(),
    CT1000histo84->GetMean(),
    CT1000histo97->GetMean(),
  };

  Float_t upperlimit2000[5] = {
    CT2000histo2->GetMean(),
    CT2000histo16->GetMean(),
    CT2000histo50->GetMean(),
    CT2000histo84->GetMean(),
    CT2000histo97->GetMean(),
  };

  obs_lim[0] = xsec*CT1histo1->GetMean();
  obs_lim[1] = xsec*CT10histo1->GetMean();
  //obs_lim[1] = xsec*CT50histo1->GetMean();
  obs_lim[2] = xsec*CT100histo1->GetMean();
  obs_lim[3] = xsec*CT500histo1->GetMean();
  obs_lim[4] = xsec*CT1000histo1->GetMean();
  obs_lim[5] = xsec*CT2000histo1->GetMean();

  cout << upperlimit500[2] << endl;

  exp_lim[0] = xsec*upperlimit1[2];
  exp_lim[1] = xsec*upperlimit10[2];
  //exp_lim[1] = xsec*upperlimit50[2];
  exp_lim[2] = xsec*upperlimit100[2];
  exp_lim[3] = xsec*upperlimit500[2];
  exp_lim[4] = xsec*upperlimit1000[2];
  exp_lim[5] = xsec*upperlimit2000[2];

  
  ofstream myfile;
  myfile.open ("events_Lambda140.tex");

    myfile << "\\documentclass[11pt]{article}" << endl;
  myfile << "\\usepackage{multirow}" << endl;
  myfile << "\\begin{document}" << endl;

  myfile << "SIGNAL EVENTS: " << int(xsec*19700) << endl << endl;

  myfile << "\\begin{table}[h!]" << endl;
  myfile << "\\begin{tabular}{|c|c|c|}" << endl;
  myfile << "\\hline" << endl;
  myfile << "CTAU 1 & Expected & Observed \\\\ \\hline" << endl;
  myfile << "-2$\\sigma$ & " << int(xsec*upperlimit1[0]*19700) << " & \\multirow{3}{*}{" << int(obs_lim[0]*19700) << "} \\\\" << endl;
  myfile << "Events & " << int(exp_lim[0]*19700) << " & \\\\"<< endl;
  myfile << "+2$\\sigma$ & " << int(xsec*upperlimit1[4]*19700) <<" & \\\\"<< endl;
  myfile <<  "\\hline"<< endl;
  myfile << "\\end{tabular}"<< endl;
  myfile << "\\end{table}"<< endl<< endl;


  myfile << "\\begin{table}[h!]" << endl;
  myfile << "\\begin{tabular}{|c|c|c|}" << endl;
  myfile << "\\hline" << endl;
  myfile << "CTAU 10 & Expected & Observed \\\\ \\hline" << endl;
  myfile << "-2$\\sigma$ & " << int(xsec*upperlimit10[0]*19700) << " & \\multirow{3}{*}{" << int(obs_lim[1]*19700) << "}  \\\\" << endl;
  myfile << "Events & " << int(exp_lim[1]*19700) << " & \\\\"<< endl;
  myfile << "+2$\\sigma$ & " << int(xsec*upperlimit10[4]*19700) <<" & \\\\"<< endl;
  myfile <<  "\\hline"<< endl;
  myfile << "\\end{tabular}"<< endl;
  myfile << "\\end{table}"<< endl<< endl;


  myfile << "\\begin{table}[h!]" << endl;
  myfile << "\\begin{tabular}{|c|c|c|}" << endl;
  myfile << "\\hline" << endl;
  myfile << "CTAU 100 & Expected & Observed \\\\ \\hline" << endl;
  myfile << "-2$\\sigma$ & " << int(xsec*upperlimit100[0]*19700) << " & \\multirow{3}{*}{" << int(obs_lim[2]*19700) << "}  \\\\" << endl;
  myfile << "Events & " << int(exp_lim[2]*19700) << " & \\\\"<< endl;
  myfile << "+2$\\sigma$ & " << int(xsec*upperlimit100[4]*19700) << " & \\\\"<< endl;
  myfile <<  "\\hline"<< endl;
  myfile << "\\end{tabular}"<< endl;
  myfile << "\\end{table}"<< endl << endl;


  myfile << "\\begin{table}[h!]" << endl;
  myfile << "\\begin{tabular}{|c|c|c|}" << endl;
  myfile << "\\hline" << endl;
  myfile << "CTAU 500 & Expected & Observed \\\\ \\hline" << endl;
  myfile << "-2$\\sigma$ & " << int(xsec*upperlimit500[0]*19700) << " & \\multirow{3}{*}{" << int(obs_lim[3]*19700) << "}  \\\\" << endl;
  myfile << "Events & " << int(exp_lim[3]*19700) << " & \\\\"<< endl;
  myfile << "+2$\\sigma$ & " << int(xsec*upperlimit500[4]*19700) <<" & \\\\"<< endl;
  myfile <<  "\\hline"<< endl;
  myfile << "\\end{tabular}"<< endl;
  myfile << "\\end{table}"<< endl << endl;


  myfile << "\\begin{table}[h!]" << endl;
  myfile << "\\begin{tabular}{|c|c|c|}" << endl;
  myfile << "\\hline" << endl;
  myfile << "CTAU 1000 & Expected & Observed \\\\ \\hline" << endl;
  myfile << "-2$\\sigma$ & " << int(xsec*upperlimit1000[0]*19700) << " & \\multirow{3}{*}{" << int(obs_lim[4]*19700) << "}  \\\\" << endl;
  myfile << "Events & " << int(exp_lim[4]*19700) << " & \\\\"<< endl;
  myfile << "+2$\\sigma$ & " << int(xsec*upperlimit1000[4]*19700) <<" & \\\\"<< endl;
  myfile <<  "\\hline"<< endl;
  myfile << "\\end{tabular}"<< endl;
  myfile << "\\end{table}"<< endl << endl;


  myfile << "\\begin{table}[h!]" << endl;
  myfile << "\\begin{tabular}{|c|c|c|}" << endl;
  myfile << "\\hline" << endl;
  myfile << "CTAU 2000 & Expected & Observed \\\\ \\hline" << endl;
  myfile << "-2$\\sigma$ & " << int(xsec*upperlimit2000[0]*19700) << " & \\multirow{3}{*}{" << int(obs_lim[5]*19700) << "}  \\\\" << endl;
  myfile << "Events & " << int(exp_lim[5]*19700) << " & \\\\"<< endl;
  myfile << "+2$\\sigma$ & " << int(xsec*upperlimit2000[4]*19700) <<" & \\\\"<< endl;
  myfile <<  "\\hline"<< endl;
  myfile << "\\end{tabular}"<< endl;
  myfile << "\\end{table}"<< endl << endl;


  myfile << "\\end{document}"<< endl;


  myfile.close();



  //Theoretical CTAU
  //Double_t mTh[6] = {0.1,1.0,10.0,50.0,100.0,200.0};
  //Double_t x_pdf[12] = {0.1,1.0,10.0,50.0,100.0,200.0,200.0,100.0,50.0,10.0,1.0,0.1};

  //Real CTAU
  Double_t mTh[6] = {0.0516,0.516,5.16,25.8,51.6,103.0};
  Double_t x_pdf[12] = {0.0516,0.516,5.16,25.8,51.6,103.0,103.0,51.6,25.8,5.16,0.516,0.0516};


  Double_t xsTh[6] = {xsec,xsec,xsec,xsec,xsec,xsec};
  
  Double_t y_pdf_1sig[12] = {xsec*upperlimit1[1],
			     xsec*upperlimit10[1],
			     xsec*upperlimit100[1],
			     xsec*upperlimit500[1],
			     xsec*upperlimit1000[1],
			     xsec*upperlimit2000[1],
                             xsec*upperlimit2000[3],
                             xsec*upperlimit1000[3],
			     xsec*upperlimit500[3],
                             xsec*upperlimit100[3],
                             xsec*upperlimit10[3],
			     xsec*upperlimit1[3]};


  Double_t y_pdf_2sig[12] = {xsec*upperlimit1[0],
			     xsec*upperlimit10[0],
                             xsec*upperlimit100[0],
                             xsec*upperlimit500[0],
			     xsec*upperlimit1000[0],
                             xsec*upperlimit2000[0],
                             xsec*upperlimit2000[4],
                             xsec*upperlimit1000[4],
			     xsec*upperlimit500[4],
			     xsec*upperlimit100[4],
                             xsec*upperlimit10[4],
			     xsec*upperlimit1[4]}

  TGraph* Onesig_graph;
  Onesig_graph = new TGraph(12., x_pdf, y_pdf_1sig );

  TGraph* Twosig_graph;
  Twosig_graph = new TGraph(12., x_pdf, y_pdf_2sig );

  Onesig_graph->SetFillColor(kGreen);
  Twosig_graph->SetFillColor(kYellow);

  TGraph* exp_lim_graph;
  exp_lim_graph  = new TGraph(6, mTh, exp_lim);
  exp_lim_graph->SetMarkerStyle(19);
  exp_lim_graph->SetMarkerSize(1.5);
  exp_lim_graph->SetMarkerColor(kRed);
  exp_lim_graph->SetLineWidth(2.5);
  exp_lim_graph->SetLineStyle(kDashed);
  exp_lim_graph->SetTitle("");

  TGraph* ul_lim_graph;
  ul_lim_graph  = new TGraph(6, mTh, obs_lim);
  ul_lim_graph->SetMarkerStyle(22);
  ul_lim_graph->SetMarkerSize(1.5);
  ul_lim_graph->SetLineColor(kBlack);
  ul_lim_graph->SetLineWidth(2);

  TMultiGraph* mg = new TMultiGraph;
 
  mg->Add(exp_lim_graph);
  mg->Add(ul_lim_graph);


  TCanvas* c0 = new TCanvas("exclusion limit", "exclusion limit", 1);
  c0->cd();
  c0->SetLogy();
  c0->SetLogx();
  c0->Range(83.19049,-3.60972,185.6367,1.040413);
  c0->SetFillColor(0);
  c0->SetBorderMode(0);
  c0->SetBorderSize(2);
  c0->SetTickx(1);
  c0->SetTicky(1);
  c0->SetLeftMargin(0.159396);
  c0->SetRightMargin(0.05033557);
  c0->SetTopMargin(0.07342657);
  c0->SetBottomMargin(0.1311189);
  c0->SetFrameFillStyle(0);
  c0->SetFrameBorderMode(0);
  c0->SetFrameFillStyle(0);
  c0->SetFrameBorderMode(0); 

  exp_lim_graph->Draw("LA");
  Twosig_graph->Draw("Fsame");
  Onesig_graph->Draw("Fsame");
  ul_lim_graph->Draw("Lsame");
  exp_lim_graph->Draw("Lsame");

  exp_lim_graph->GetXaxis()->SetTitle("c#tau_{#tilde{#chi^{0}_{1}}} (cm)");
  exp_lim_graph->GetYaxis()->SetTitle("#sigma ( #tilde{#chi^{0}_{1}} #rightarrow #tilde{G}#gamma) (pb)");
  exp_lim_graph->GetYaxis()->SetRangeUser(0.0005, 100);
  exp_lim_graph->GetXaxis()->SetRangeUser(0.01, 9000.);
  exp_lim_graph->GetXaxis()->SetTitleSize(0.048);
  exp_lim_graph->GetXaxis()->SetTitleOffset(1.24);
  exp_lim_graph->GetYaxis()->SetTitleSize(0.048);
  exp_lim_graph->GetYaxis()->SetTitleOffset(1.6);

  ul_lim_graph->Draw("same");

  // integrated luminosity
  std::string s_lumi;
  s_lumi = "19.7";
  std::string lint = "#intL = "+s_lumi+" fb^{-1}";
  TLatex l1;
  l1.SetTextAlign(12);
  l1.SetTextSize(0.027);
  l1.SetTextFont(22);
  l1.SetNDC();
  l1.DrawLatex(0.155, 0.964, "CMS Preliminary");
  l1.DrawLatex(0.75, 0.958, lint.c_str());
 

  TGraph *xsTh_vs_m = new TGraph(6, mTh, xsTh);
  xsTh_vs_m->SetLineWidth(2);
  xsTh_vs_m->SetLineColor(kRed);
  
  xsTh_vs_m->SetMarkerSize(1.);
  xsTh_vs_m->SetMarkerStyle(22);
  xsTh_vs_m->SetMarkerColor(kRed);
  xsTh_vs_m->Draw("Csame");
   
   
  TLegend* leg = new TLegend(0.45,0.6,0.9,0.93);
  leg->SetFillStyle(0); leg->SetBorderSize(0);
  leg->SetFillColor(0);

  TString massLeg;

  if ( LAMBDA=="140" ) { massLeg = "#Lambda = 140: M_{#tilde{#chi}^{0}_{1}} =  198 GeV/c^{2}";}
 
  leg->SetHeader(massLeg);
  leg->SetTextFont(22);
  leg->AddEntry(xsTh_vs_m,"Theoretical LO cross-section","L");
  leg->AddEntry(ul_lim_graph, "Observed  95% CL upper limit", "L");
  leg->AddEntry(exp_lim_graph, "Expected 95% CL upper limit", "L");
  leg->AddEntry(Onesig_graph, "#pm 1 #sigma Expected", "F");
  leg->AddEntry(Twosig_graph, "#pm 2 #sigma Expected", "F");
  leg->Draw("same");

  //c0->SaveAs("exclusion_limit_L140"+extra+".pdf");
  c0->SaveAs("exclusion_limit_L140"+extra+".png");
  
}

void rootlogon() {
  gROOT->SetStyle("Plain");
  gStyle->SetPalette(1);
  gStyle->SetOptStat(1111111);  // Show overflow, underflow + SumOfWeights 
  gStyle->SetOptFit(111110);
  gStyle->SetOptFile(1);
  gStyle->SetMarkerStyle(20);
  gStyle->SetMarkerSize(2.);
  gStyle->SetMarkerColor(1);
  gStyle->SetTitleOffset(1.20,"Y");

  //define high def color palette
  const Int_t NRGBs = 5;
  const Int_t NCont = 255;

  Double_t stops[NRGBs] = { 0.00, 0.34, 0.61, 0.84, 1.00 };
  Double_t red[NRGBs]   = { 0.00, 0.00, 0.87, 1.00, 0.51 };
  Double_t green[NRGBs] = { 0.00, 0.81, 1.00, 0.20, 0.00 };
  Double_t blue[NRGBs]  = { 0.51, 1.00, 0.12, 0.00, 0.00 };
  TColor::CreateGradientColorTable(NRGBs, stops, red, green, blue, NCont);
  gStyle->SetNumberContours(NCont);

  cout << "loading TDR style and setting as default" << endl;
  gROOT->ProcessLine(".L tdrstyle.C");
  setTDRStyle();

}
