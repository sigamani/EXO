//////////////////////////////////////////////////////////
// This class has been automatically generated on
// Thu Nov  7 21:12:12 2013 by ROOT version 5.32/00
// from TTree DPAnalysis/DPAnalysis
// found on file: /localgrid/wvandrie/CMSSW_5_3_11_patch4_2/src/EXO/DPAnalysis/test/Run2012Bdata.root
//////////////////////////////////////////////////////////

#ifndef GMSBTree_V1_h
#define GMSBTree_V1_h

#include <TROOT.h>
#include <TChain.h>
#include <TFile.h>

// Header file for the classes stored in the TTree if any.

// Fixed size dimensions of array or collections stored in the TTree if any.

class GMSBTree_V1 {
public :
   TTree          *fChain;   //!pointer to the analyzed TTree or TChain
   Int_t           fCurrent; //!current Tree number in a TChain

   // Declaration of leaf types
   UInt_t          runId;
   UInt_t          lumiSection;
   UInt_t          orbit;
   UInt_t          bx;
   UInt_t          eventId;
   Int_t           triggered;
   Int_t           L1a;
   Int_t           nMuons;
   Int_t           nElectrons;
   Int_t           nJets;
   Int_t           nPhotons;
   Int_t           nVertices;
   Int_t           totalNVtx;
   Int_t           nGen;
   Int_t           nOutTimeHits;
   Int_t           nHaloTrack;
   Float_t         z0Ratio;
   Float_t         met0Px;
   Float_t         met0Py;
   Float_t         met0;
   Float_t         metPx;
   Float_t         metPy;
   Float_t         met;
   Float_t         met_dx1;
   Float_t         met_dy1;
   Float_t         met_dx2;
   Float_t         met_dy2;
   Float_t         met_dx3;
   Float_t         met_dy3;
   Float_t         t_metPx;
   Float_t         t_metPy;
   Float_t         t_met;
   Float_t         t_metdR;
   Float_t         t_phoPx;
   Float_t         t_phoPy;
   Float_t         t_phoPz;
   Float_t         t_phoPt;
   Float_t         t_phoE;
   Float_t         t_phodR;
   Float_t         t_phoR;
   Float_t         t_phoDxy;
   Float_t         t_phoDz;
   Float_t         muPx[1];   //[nMuons]
   Float_t         muPy[1];   //[nMuons]
   Float_t         muPz[1];   //[nMuons]
   Float_t         muE[1];   //[nMuons]
   Float_t         muIso[1];   //[nMuons]
   Float_t         elePx[4];   //[nElectrons]
   Float_t         elePy[4];   //[nElectrons]
   Float_t         elePz[4];   //[nElectrons]
   Float_t         eleE[4];   //[nElectrons]
   Int_t           eleNLostHits[4];   //[nElectrons]
   Float_t         eleEcalIso[4];   //[nElectrons]
   Float_t         eleHcalIso[4];   //[nElectrons]
   Float_t         eleTrkIso[4];   //[nElectrons]
   Float_t         e_cHadIso[4];   //[nElectrons]
   Float_t         e_nHadIso[4];   //[nElectrons]
   Float_t         e_photIso[4];   //[nElectrons]
   Float_t         jetPx[40];   //[nJets]
   Float_t         jetPy[40];   //[nJets]
   Float_t         jetPz[40];   //[nJets]
   Float_t         jetE[40];   //[nJets]
   Int_t           jetNDau[40];   //[nJets]
   Int_t           jetCM[40];   //[nJets]
   Float_t         jetCEF[40];   //[nJets]
   Float_t         jetCHF[40];   //[nJets]
   Float_t         jetNHF[40];   //[nJets]
   Float_t         jetNEF[40];   //[nJets]
   Float_t         jerUnc[40];   //[nJets]
   Float_t         jecUnc[40];   //[nJets]
   Float_t         phoPx[40];   //[nPhotons]
   Float_t         phoPy[40];   //[nPhotons]
   Float_t         phoPz[40];   //[nPhotons]
   Float_t         phoPt[40];   //[nPhotons]
   Float_t         phoE[40];   //[nPhotons]
   Float_t         phoEcalIso[40];   //[nPhotons]
   Float_t         phoHcalIso[40];   //[nPhotons]
   Float_t         phoTrkIso[40];   //[nPhotons]
   Float_t         cHadIso[40];   //[nPhotons]
   Float_t         nHadIso[40];   //[nPhotons]
   Float_t         photIso[40];   //[nPhotons]
   Float_t         dR_TrkPho[40];   //[nPhotons]
   Float_t         pt_TrkPho[40];   //[nPhotons]
   Float_t         phoHoverE[40];   //[nPhotons]
   Float_t         sMinPho[40];   //[nPhotons]
   Float_t         sMajPho[40];   //[nPhotons]
   Float_t         seedTime[40];   //[nPhotons]
   Float_t         seedTimeErr[40];   //[nPhotons]
   Float_t         aveTime[40];   //[nPhotons]
   Float_t         aveTimeErr[40];   //[nPhotons]
   Float_t         aveTime1[40];   //[nPhotons]
   Float_t         aveTimeErr1[40];   //[nPhotons]
   Float_t         timeChi2[40];   //[nPhotons]
   Float_t         fSpike[40];   //[nPhotons]
   Float_t         maxSwissX[40];   //[nPhotons]
   Float_t         seedSwissX[40];   //[nPhotons]
   Int_t           nXtals[40];   //[nPhotons]
   Int_t           nBC[40];   //[nPhotons]
   Int_t           sigmaEta[40];   //[nPhotons]
   Int_t           sigmaIeta[40];   //[nPhotons]
   Float_t         cscRho[40];   //[nPhotons]
   Float_t         cscdPhi[40];   //[nPhotons]
   Float_t         cscTime[40];   //[nPhotons]
   Float_t         dtdPhi[40];   //[nPhotons]
   Float_t         dtdEta[40];   //[nPhotons]
   Float_t         phoDxy[40];   //[nPhotons]
   Float_t         phoDz[40];   //[nPhotons]
   Int_t           vtxNTracks[30];   //[nVertices]
   Float_t         vtxChi2[30];   //[nVertices]
   Float_t         vtxNdof[30];   //[nVertices]
   Float_t         vtxRho[30];   //[nVertices]
   Float_t         vtxZ[30];   //[nVertices]
   Int_t           pdgId[1];   //[nGen]
   Int_t           momId[1];   //[nGen]
   Float_t         genPx[1];   //[nGen]
   Float_t         genPy[1];   //[nGen]
   Float_t         genPz[1];   //[nGen]
   Float_t         genE[1];   //[nGen]
   Float_t         genM[1];   //[nGen]
   Float_t         genVx[1];   //[nGen]
   Float_t         genVy[1];   //[nGen]
   Float_t         genVz[1];   //[nGen]
   Float_t         genT[1];   //[nGen]

   // List of branches
   TBranch        *b_runId;   //!
   TBranch        *b_lumiSection;   //!
   TBranch        *b_orbit;   //!
   TBranch        *b_bx;   //!
   TBranch        *b_eventId;   //!
   TBranch        *b_triggered;   //!
   TBranch        *b_L1a;   //!
   TBranch        *b_nMuons;   //!
   TBranch        *b_nElectrons;   //!
   TBranch        *b_nJets;   //!
   TBranch        *b_nPhotons;   //!
   TBranch        *b_nVertices;   //!
   TBranch        *b_totalNVtx;   //!
   TBranch        *b_nGen;   //!
   TBranch        *b_nOutTimeHits;   //!
   TBranch        *b_nHaloTrack;   //!
   TBranch        *b_z0Ratio;   //!
   TBranch        *b_met0Px;   //!
   TBranch        *b_met0Py;   //!
   TBranch        *b_met0;   //!
   TBranch        *b_metPx;   //!
   TBranch        *b_metPy;   //!
   TBranch        *b_met;   //!
   TBranch        *b_met_dx1;   //!
   TBranch        *b_met_dy1;   //!
   TBranch        *b_met_dx2;   //!
   TBranch        *b_met_dy2;   //!
   TBranch        *b_met_dx3;   //!
   TBranch        *b_met_dy3;   //!
   TBranch        *b_t_metPx;   //!
   TBranch        *b_t_metPy;   //!
   TBranch        *b_t_met;   //!
   TBranch        *b_t_metdR;   //!
   TBranch        *b_t_phoPx;   //!
   TBranch        *b_t_phoPy;   //!
   TBranch        *b_t_phoPz;   //!
   TBranch        *b_t_phoPt;   //!
   TBranch        *b_t_phoE;   //!
   TBranch        *b_t_phodR;   //!
   TBranch        *b_t_phoR;   //!
   TBranch        *b_t_phoDxy;   //!
   TBranch        *b_t_phoDz;   //!
   TBranch        *b_muPx;   //!
   TBranch        *b_muPy;   //!
   TBranch        *b_muPz;   //!
   TBranch        *b_muE;   //!
   TBranch        *b_muIso;   //!
   TBranch        *b_elePx;   //!
   TBranch        *b_elePy;   //!
   TBranch        *b_elePz;   //!
   TBranch        *b_eleE;   //!
   TBranch        *b_eleNLostHits;   //!
   TBranch        *b_eleEcalIso;   //!
   TBranch        *b_eleHcalIso;   //!
   TBranch        *b_eleTrkIso;   //!
   TBranch        *b_e_cHadIso;   //!
   TBranch        *b_e_nHadIso;   //!
   TBranch        *b_e_photIso;   //!
   TBranch        *b_jetPx;   //!
   TBranch        *b_jetPy;   //!
   TBranch        *b_jetPz;   //!
   TBranch        *b_jetE;   //!
   TBranch        *b_jetNDau;   //!
   TBranch        *b_jetCM;   //!
   TBranch        *b_jetCEF;   //!
   TBranch        *b_jetCHF;   //!
   TBranch        *b_jetNHF;   //!
   TBranch        *b_jetNEF;   //!
   TBranch        *b_jerUnc;   //!
   TBranch        *b_jecUnc;   //!
   TBranch        *b_phoPx;   //!
   TBranch        *b_phoPy;   //!
   TBranch        *b_phoPz;   //!
   TBranch        *b_phoPt;   //!
   TBranch        *b_phoE;   //!
   TBranch        *b_phoEcalIso;   //!
   TBranch        *b_phoHcalIso;   //!
   TBranch        *b_phoTrkIso;   //!
   TBranch        *b_cHadIso;   //!
   TBranch        *b_nHadIso;   //!
   TBranch        *b_photIso;   //!
   TBranch        *b_dR_TrkPho;   //!
   TBranch        *b_pt_TrkPho;   //!
   TBranch        *b_phoHoverE;   //!
   TBranch        *b_sMinPho;   //!
   TBranch        *b_sMajPho;   //!
   TBranch        *b_seedTime;   //!
   TBranch        *b_seedTimeErr;   //!
   TBranch        *b_aveTime;   //!
   TBranch        *b_aveTimeErr;   //!
   TBranch        *b_aveTime1;   //!
   TBranch        *b_aveTimeErr1;   //!
   TBranch        *b_timeChi2;   //!
   TBranch        *b_fSpike;   //!
   TBranch        *b_maxSwissX;   //!
   TBranch        *b_seedSwissX;   //!
   TBranch        *b_nXtals;   //!
   TBranch        *b_nBC;   //!
   TBranch        *b_sigmaEta;   //!
   TBranch        *b_sigmaIeta;   //!
   TBranch        *b_cscRho;   //!
   TBranch        *b_cscdPhi;   //!
   TBranch        *b_cscTime;   //!
   TBranch        *b_dtdPhi;   //!
   TBranch        *b_dtdEta;   //!
   TBranch        *b_phoDxy;   //!
   TBranch        *b_phoDz;   //!
   TBranch        *b_vtxNTracks;   //!
   TBranch        *b_vtxChi2;   //!
   TBranch        *b_vtxNdof;   //!
   TBranch        *b_vtxRho;   //!
   TBranch        *b_vtxZ;   //!
   TBranch        *b_pdgId;   //!
   TBranch        *b_momId;   //!
   TBranch        *b_genPx;   //!
   TBranch        *b_genPy;   //!
   TBranch        *b_genPz;   //!
   TBranch        *b_genE;   //!
   TBranch        *b_genM;   //!
   TBranch        *b_genVx;   //!
   TBranch        *b_genVy;   //!
   TBranch        *b_genVz;   //!
   TBranch        *b_genT;   //!

   GMSBTree_V1(TTree *tree=0);
   virtual ~GMSBTree_V1();
   virtual Int_t    Cut(Long64_t entry);
   virtual Int_t    GetEntry(Long64_t entry);
   virtual Long64_t LoadTree(Long64_t entry);
   virtual void     Init(TTree *tree);
   virtual void     Loop();
   virtual Bool_t   Notify();
   virtual void     Show(Long64_t entry = -1);
};

#endif

#ifdef GMSBTree_V1_cxx
GMSBTree_V1::GMSBTree_V1(TTree *tree) : fChain(0) 
{
// if parameter tree is not specified (or zero), connect the file
// used to generate this class and read the Tree.
   if (tree == 0) {
      TFile *f = (TFile*)gROOT->GetListOfFiles()->FindObject("/localgrid/wvandrie/CMSSW_5_3_11_patch4_2/src/EXO/DPAnalysis/test/Run2012Bdata.root");
      if (!f || !f->IsOpen()) {
         f = new TFile("/localgrid/wvandrie/CMSSW_5_3_11_patch4_2/src/EXO/DPAnalysis/test/Run2012Bdata.root");
      }
      f->GetObject("DPAnalysis",tree);

   }
   Init(tree);
}

GMSBTree_V1::~GMSBTree_V1()
{
   if (!fChain) return;
   delete fChain->GetCurrentFile();
}

Int_t GMSBTree_V1::GetEntry(Long64_t entry)
{
// Read contents of entry.
   if (!fChain) return 0;
   return fChain->GetEntry(entry);
}
Long64_t GMSBTree_V1::LoadTree(Long64_t entry)
{
// Set the environment to read one entry
   if (!fChain) return -5;
   Long64_t centry = fChain->LoadTree(entry);
   if (centry < 0) return centry;
   if (fChain->GetTreeNumber() != fCurrent) {
      fCurrent = fChain->GetTreeNumber();
      Notify();
   }
   return centry;
}

void GMSBTree_V1::Init(TTree *tree)
{
   // The Init() function is called when the selector needs to initialize
   // a new tree or chain. Typically here the branch addresses and branch
   // pointers of the tree will be set.
   // It is normally not necessary to make changes to the generated
   // code, but the routine can be extended by the user if needed.
   // Init() will be called many times when running on PROOF
   // (once per file to be processed).

   // Set branch addresses and branch pointers
   if (!tree) return;
   fChain = tree;
   fCurrent = -1;
   fChain->SetMakeClass(1);

   fChain->SetBranchAddress("runId", &runId, &b_runId);
   fChain->SetBranchAddress("lumiSection", &lumiSection, &b_lumiSection);
   fChain->SetBranchAddress("orbit", &orbit, &b_orbit);
   fChain->SetBranchAddress("bx", &bx, &b_bx);
   fChain->SetBranchAddress("eventId", &eventId, &b_eventId);
   fChain->SetBranchAddress("triggered", &triggered, &b_triggered);
   fChain->SetBranchAddress("L1a", &L1a, &b_L1a);
   fChain->SetBranchAddress("nMuons", &nMuons, &b_nMuons);
   fChain->SetBranchAddress("nElectrons", &nElectrons, &b_nElectrons);
   fChain->SetBranchAddress("nJets", &nJets, &b_nJets);
   fChain->SetBranchAddress("nPhotons", &nPhotons, &b_nPhotons);
   fChain->SetBranchAddress("nVertices", &nVertices, &b_nVertices);
   fChain->SetBranchAddress("totalNVtx", &totalNVtx, &b_totalNVtx);
   fChain->SetBranchAddress("nGen", &nGen, &b_nGen);
   fChain->SetBranchAddress("nOutTimeHits", &nOutTimeHits, &b_nOutTimeHits);
   fChain->SetBranchAddress("nHaloTrack", &nHaloTrack, &b_nHaloTrack);
   fChain->SetBranchAddress("z0Ratio", &z0Ratio, &b_z0Ratio);
   fChain->SetBranchAddress("met0Px", &met0Px, &b_met0Px);
   fChain->SetBranchAddress("met0Py", &met0Py, &b_met0Py);
   fChain->SetBranchAddress("met0", &met0, &b_met0);
   fChain->SetBranchAddress("metPx", &metPx, &b_metPx);
   fChain->SetBranchAddress("metPy", &metPy, &b_metPy);
   fChain->SetBranchAddress("met", &met, &b_met);
   fChain->SetBranchAddress("met_dx1", &met_dx1, &b_met_dx1);
   fChain->SetBranchAddress("met_dy1", &met_dy1, &b_met_dy1);
   fChain->SetBranchAddress("met_dx2", &met_dx2, &b_met_dx2);
   fChain->SetBranchAddress("met_dy2", &met_dy2, &b_met_dy2);
   fChain->SetBranchAddress("met_dx3", &met_dx3, &b_met_dx3);
   fChain->SetBranchAddress("met_dy3", &met_dy3, &b_met_dy3);
   fChain->SetBranchAddress("t_metPx", &t_metPx, &b_t_metPx);
   fChain->SetBranchAddress("t_metPy", &t_metPy, &b_t_metPy);
   fChain->SetBranchAddress("t_met", &t_met, &b_t_met);
   fChain->SetBranchAddress("t_metdR", &t_metdR, &b_t_metdR);
   fChain->SetBranchAddress("t_phoPx", &t_phoPx, &b_t_phoPx);
   fChain->SetBranchAddress("t_phoPy", &t_phoPy, &b_t_phoPy);
   fChain->SetBranchAddress("t_phoPz", &t_phoPz, &b_t_phoPz);
   fChain->SetBranchAddress("t_phoPt", &t_phoPt, &b_t_phoPt);
   fChain->SetBranchAddress("t_phoE", &t_phoE, &b_t_phoE);
   fChain->SetBranchAddress("t_phodR", &t_phodR, &b_t_phodR);
   fChain->SetBranchAddress("t_phoR", &t_phoR, &b_t_phoR);
   fChain->SetBranchAddress("t_phoDxy", &t_phoDxy, &b_t_phoDxy);
   fChain->SetBranchAddress("t_phoDz", &t_phoDz, &b_t_phoDz);
   fChain->SetBranchAddress("muPx", &muPx, &b_muPx);
   fChain->SetBranchAddress("muPy", &muPy, &b_muPy);
   fChain->SetBranchAddress("muPz", &muPz, &b_muPz);
   fChain->SetBranchAddress("muE", &muE, &b_muE);
   fChain->SetBranchAddress("muIso", &muIso, &b_muIso);
   fChain->SetBranchAddress("elePx", elePx, &b_elePx);
   fChain->SetBranchAddress("elePy", elePy, &b_elePy);
   fChain->SetBranchAddress("elePz", elePz, &b_elePz);
   fChain->SetBranchAddress("eleE", eleE, &b_eleE);
   fChain->SetBranchAddress("eleNLostHits", eleNLostHits, &b_eleNLostHits);
   fChain->SetBranchAddress("eleEcalIso", eleEcalIso, &b_eleEcalIso);
   fChain->SetBranchAddress("eleHcalIso", eleHcalIso, &b_eleHcalIso);
   fChain->SetBranchAddress("eleTrkIso", eleTrkIso, &b_eleTrkIso);
   fChain->SetBranchAddress("e_cHadIso", e_cHadIso, &b_e_cHadIso);
   fChain->SetBranchAddress("e_nHadIso", e_nHadIso, &b_e_nHadIso);
   fChain->SetBranchAddress("e_photIso", e_photIso, &b_e_photIso);
   fChain->SetBranchAddress("jetPx", jetPx, &b_jetPx);
   fChain->SetBranchAddress("jetPy", jetPy, &b_jetPy);
   fChain->SetBranchAddress("jetPz", jetPz, &b_jetPz);
   fChain->SetBranchAddress("jetE", jetE, &b_jetE);
   fChain->SetBranchAddress("jetNDau", jetNDau, &b_jetNDau);
   fChain->SetBranchAddress("jetCM", jetCM, &b_jetCM);
   fChain->SetBranchAddress("jetCEF", jetCEF, &b_jetCEF);
   fChain->SetBranchAddress("jetCHF", jetCHF, &b_jetCHF);
   fChain->SetBranchAddress("jetNHF", jetNHF, &b_jetNHF);
   fChain->SetBranchAddress("jetNEF", jetNEF, &b_jetNEF);
   fChain->SetBranchAddress("jerUnc", jerUnc, &b_jerUnc);
   fChain->SetBranchAddress("jecUnc", jecUnc, &b_jecUnc);
   fChain->SetBranchAddress("phoPx", phoPx, &b_phoPx);
   fChain->SetBranchAddress("phoPy", phoPy, &b_phoPy);
   fChain->SetBranchAddress("phoPz", phoPz, &b_phoPz);
   fChain->SetBranchAddress("phoPt", phoPt, &b_phoPt);
   fChain->SetBranchAddress("phoE", phoE, &b_phoE);
   fChain->SetBranchAddress("phoEcalIso", phoEcalIso, &b_phoEcalIso);
   fChain->SetBranchAddress("phoHcalIso", phoHcalIso, &b_phoHcalIso);
   fChain->SetBranchAddress("phoTrkIso", phoTrkIso, &b_phoTrkIso);
   fChain->SetBranchAddress("cHadIso", cHadIso, &b_cHadIso);
   fChain->SetBranchAddress("nHadIso", nHadIso, &b_nHadIso);
   fChain->SetBranchAddress("photIso", photIso, &b_photIso);
   fChain->SetBranchAddress("dR_TrkPho", dR_TrkPho, &b_dR_TrkPho);
   fChain->SetBranchAddress("pt_TrkPho", pt_TrkPho, &b_pt_TrkPho);
   fChain->SetBranchAddress("phoHoverE", phoHoverE, &b_phoHoverE);
   fChain->SetBranchAddress("sMinPho", sMinPho, &b_sMinPho);
   fChain->SetBranchAddress("sMajPho", sMajPho, &b_sMajPho);
   fChain->SetBranchAddress("seedTime", seedTime, &b_seedTime);
   fChain->SetBranchAddress("seedTimeErr", seedTimeErr, &b_seedTimeErr);
   fChain->SetBranchAddress("aveTime", aveTime, &b_aveTime);
   fChain->SetBranchAddress("aveTimeErr", aveTimeErr, &b_aveTimeErr);
   fChain->SetBranchAddress("aveTime1", aveTime1, &b_aveTime1);
   fChain->SetBranchAddress("aveTimeErr1", aveTimeErr1, &b_aveTimeErr1);
   fChain->SetBranchAddress("timeChi2", timeChi2, &b_timeChi2);
   fChain->SetBranchAddress("fSpike", fSpike, &b_fSpike);
   fChain->SetBranchAddress("maxSwissX", maxSwissX, &b_maxSwissX);
   fChain->SetBranchAddress("seedSwissX", seedSwissX, &b_seedSwissX);
   fChain->SetBranchAddress("nXtals", nXtals, &b_nXtals);
   fChain->SetBranchAddress("nBC", nBC, &b_nBC);
   fChain->SetBranchAddress("sigmaEta", sigmaEta, &b_sigmaEta);
   fChain->SetBranchAddress("sigmaIeta", sigmaIeta, &b_sigmaIeta);
   fChain->SetBranchAddress("cscRho", cscRho, &b_cscRho);
   fChain->SetBranchAddress("cscdPhi", cscdPhi, &b_cscdPhi);
   fChain->SetBranchAddress("cscTime", cscTime, &b_cscTime);
   fChain->SetBranchAddress("dtdPhi", dtdPhi, &b_dtdPhi);
   fChain->SetBranchAddress("dtdEta", dtdEta, &b_dtdEta);
   fChain->SetBranchAddress("phoDxy", phoDxy, &b_phoDxy);
   fChain->SetBranchAddress("phoDz", phoDz, &b_phoDz);
   fChain->SetBranchAddress("vtxNTracks", vtxNTracks, &b_vtxNTracks);
   fChain->SetBranchAddress("vtxChi2", vtxChi2, &b_vtxChi2);
   fChain->SetBranchAddress("vtxNdof", vtxNdof, &b_vtxNdof);
   fChain->SetBranchAddress("vtxRho", vtxRho, &b_vtxRho);
   fChain->SetBranchAddress("vtxZ", vtxZ, &b_vtxZ);
   fChain->SetBranchAddress("pdgId", &pdgId, &b_pdgId);
   fChain->SetBranchAddress("momId", &momId, &b_momId);
   fChain->SetBranchAddress("genPx", &genPx, &b_genPx);
   fChain->SetBranchAddress("genPy", &genPy, &b_genPy);
   fChain->SetBranchAddress("genPz", &genPz, &b_genPz);
   fChain->SetBranchAddress("genE", &genE, &b_genE);
   fChain->SetBranchAddress("genM", &genM, &b_genM);
   fChain->SetBranchAddress("genVx", &genVx, &b_genVx);
   fChain->SetBranchAddress("genVy", &genVy, &b_genVy);
   fChain->SetBranchAddress("genVz", &genVz, &b_genVz);
   fChain->SetBranchAddress("genT", &genT, &b_genT);
   Notify();
}


  

Bool_t GMSBTree_V1::Notify()
{
   // The Notify() function is called when a new file is opened. This
   // can be either for a new TTree in a TChain or when when a new TTree
   // is started when using PROOF. It is normally not necessary to make changes
   // to the generated code, but the routine can be extended by the
   // user if needed. The return value is currently not used.

   return kTRUE;
}

void GMSBTree_V1::Show(Long64_t entry)
{
// Print contents of entry.
// If entry is not specified, print current entry
   if (!fChain) return;
   fChain->Show(entry);
}
Int_t GMSBTree_V1::Cut(Long64_t entry)
{
// This function may be called from Loop.
// returns  1 if entry is accepted.
// returns -1 otherwise.
   return 1;
}
#endif // #ifdef GMSBTree_V1_cxx
