//////////////////////////////////////////////////////////
// This class has been automatically generated on
// Sat Nov 30 20:22:52 2013 by ROOT version 5.32/00
// from TTree DPAnalysis/DPAnalysis
// found on file: /localgrid/wvandrie/CMSSW_5_3_11_DP/src/EXO/DPAnalysis/test/v21/GMSB_L160-CTAU500.root
//////////////////////////////////////////////////////////

#ifndef GMSBTree_V3_h
#define GMSBTree_V3_h

#include <TROOT.h>
#include <TChain.h>
#include <TFile.h>

#define MAXVTX 30
#define MAXPU 30
#define MAXJET 15
#define MAXPHO 12
#define MAXMU 5
#define MAXELE 5
#define MAXGEN 20
#define MAXCONV 30

// Header file for the classes stored in the TTree if any.

// Fixed size dimensions of array or collections stored in the TTree if any.

class GMSBTree_V3 {
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
   Int_t           PU_NumInter;
   Int_t           nMuons;
   Int_t           nElectrons;
   Int_t           nJets;
   Int_t           nPhotons;
   Int_t           nConversions;
   Int_t           nVertices;
   Int_t           nPU;
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
   Float_t         t_phoPz;
   Float_t         t_phoPt;
   Float_t         t_phoE;
   Float_t         t_phodR;
   Float_t         muPx[MAXMU];   //[nMuons]
   Float_t         muPy[MAXMU];   //[nMuons]
   Float_t         muPz[MAXMU];   //[nMuons]
   Float_t         muE[MAXMU];   //[nMuons]
   Float_t         muIso[MAXMU];   //[nMuons]
   Float_t         elePx[MAXELE];   //[nElectrons]
   Float_t         elePy[MAXELE];   //[nElectrons]
   Float_t         elePz[MAXELE];   //[nElectrons]
   Float_t         eleE[MAXELE];   //[nElectrons]
   Int_t           eleNLostHits[MAXELE];   //[nElectrons]
   Float_t         eleEcalIso[MAXELE];   //[nElectrons]
   Float_t         eleHcalIso[MAXELE];   //[nElectrons]
   Float_t         eleTrkIso[MAXELE];   //[nElectrons]
   Float_t         e_cHadIso[MAXELE];   //[nElectrons]
   Float_t         e_nHadIso[MAXELE];   //[nElectrons]
   Float_t         e_photIso[MAXELE];   //[nElectrons]
   Float_t         jetPx[MAXJET];   //[nJets]
   Float_t         jetPy[MAXJET];   //[nJets]
   Float_t         jetPz[MAXJET];   //[nJets]
   Float_t         jetE[MAXJET];   //[nJets]
   Int_t           jetNDau[MAXJET];   //[nJets]
   Int_t           jetCM[MAXJET];   //[nJets]
   Float_t         jetCEF[MAXJET];   //[nJets]
   Float_t         jetCHF[MAXJET];   //[nJets]
   Float_t         jetNHF[MAXJET];   //[nJets]
   Float_t         jetNEF[MAXJET];   //[nJets]
   Float_t         jerUnc[MAXJET];   //[nJets]
   Float_t         jecUnc[MAXJET];   //[nJets]
   Float_t         convDxy[MAXCONV];   //[nConversions]
   Float_t         convDz[MAXCONV];   //[nConversions]
   Float_t         convPhi[MAXCONV];   //[nConversions]
   Float_t         convEta[MAXCONV];   //[nConversions]
   Float_t         convR[MAXCONV];   //[nConversions]
   Float_t         convMatchedEle[MAXCONV];   //[nConversions]
   Float_t         convChi2[MAXCONV];   //[nConversions]
   Float_t         convMomentum[MAXCONV];   //[nConversions]
   Float_t         convMomentum2[MAXCONV];   //[nConversions]
   Float_t         phoPx[MAXPHO];   //[nPhotons]
   Float_t         phoPy[MAXPHO];   //[nPhotons]
   Float_t         phoPz[MAXPHO];   //[nPhotons]
   Float_t         phoPt[MAXPHO];   //[nPhotons]
   Float_t         phoE[MAXPHO];   //[nPhotons]
   Float_t         phoEcalIso[MAXPHO];   //[nPhotons]
   Float_t         phoHcalIso[MAXPHO];   //[nPhotons]
   Float_t         phoTrkIso[MAXPHO];   //[nPhotons]
   Float_t         cHadIso[MAXPHO];   //[nPhotons]
   Float_t         nHadIso[MAXPHO];   //[nPhotons]
   Float_t         photIso[MAXPHO];   //[nPhotons]
   Float_t         dR_TrkPho[MAXPHO];   //[nPhotons]
   Float_t         pt_TrkPho[MAXPHO];   //[nPhotons]
   Float_t         phoHoverE[MAXPHO];   //[nPhotons]
   Float_t         sMinPho[MAXPHO];   //[nPhotons]
   Float_t         sMajPho[MAXPHO];   //[nPhotons]
   Float_t         seedTime[MAXPHO];   //[nPhotons]
   Float_t         seedTimeErr[MAXPHO];   //[nPhotons]
   Float_t         aveTime[MAXPHO];   //[nPhotons]
   Float_t         aveTimeErr[MAXPHO];   //[nPhotons]
   Float_t         aveTime1[MAXPHO];   //[nPhotons]
   Float_t         aveTimeErr1[MAXPHO];   //[nPhotons]
   Float_t         timeChi2[MAXPHO];   //[nPhotons]
   Float_t         fSpike[MAXPHO];   //[nPhotons]
   Float_t         maxSwissX[MAXPHO];   //[nPhotons]
   Float_t         seedSwissX[MAXPHO];   //[nPhotons]
   Int_t           nXtals[MAXPHO];   //[nPhotons]
   Int_t           nBC[MAXPHO];   //[nPhotons]
   Int_t           sigmaEta[MAXPHO];   //[nPhotons]
   Float_t         sigmaIeta[MAXPHO];   //[nPhotons]
   Float_t         cscRho[MAXPHO];   //[nPhotons]
   Float_t         cscdPhi[MAXPHO];   //[nPhotons]
   Float_t         cscTime[MAXPHO];   //[nPhotons]
   Float_t         dtdPhi[MAXPHO];   //[nPhotons]
   Float_t         dtdEta[MAXPHO];   //[nPhotons]
   Float_t         phoMatchedEle[MAXPHO];   //[nPhotons]
   Float_t         conversionVeto[MAXPHO];   //[nPhotons]
   Float_t         r9[MAXPHO];   //[nPhotons]
   Int_t           vtxNTracks[MAXVTX];   //[nVertices]
   Float_t         vtxChi2[MAXVTX];   //[nVertices]
   Float_t         vtxNdof[MAXVTX];   //[nVertices]
   Float_t         vtxRho[MAXVTX];   //[nVertices]
   Float_t         vtxZ[MAXVTX];   //[nVertices]
   Int_t           pdgId[MAXGEN];   //[nGen]
   Int_t           momId[MAXGEN];   //[nGen]
   Float_t         genPx[MAXGEN];   //[nGen]
   Float_t         genPy[MAXGEN];   //[nGen]
   Float_t         genPz[MAXGEN];   //[nGen]
   Float_t         genE[MAXGEN];   //[nGen]
   Float_t         genM[MAXGEN];   //[nGen]
   Float_t         genVx[MAXGEN];   //[nGen]
   Float_t         genVy[MAXGEN];   //[nGen]
   Float_t         genVz[MAXGEN];   //[nGen]
   Float_t         genT[MAXGEN];   //[nGen]

   // List of branches
   TBranch        *b_runId;   //!
   TBranch        *b_lumiSection;   //!
   TBranch        *b_orbit;   //!
   TBranch        *b_bx;   //!
   TBranch        *b_eventId;   //!
   TBranch        *b_triggered;   //!
   TBranch        *b_L1a;   //!
   TBranch        *b_PU_NumInter;   //!
   TBranch        *b_nMuons;   //!
   TBranch        *b_nElectrons;   //!
   TBranch        *b_nJets;   //!
   TBranch        *b_nPhotons;   //!
   TBranch        *b_nConversions;   //!
   TBranch        *b_nVertices;   //!
   TBranch        *b_nPU;   //!
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
   TBranch        *b_t_phoPz;   //!
   TBranch        *b_t_phoPt;   //!
   TBranch        *b_t_phoE;   //!
   TBranch        *b_t_phodR;   //!
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
   TBranch        *b_convDxy;   //!
   TBranch        *b_convDz;   //!
   TBranch        *b_convPhi;   //!
   TBranch        *b_convEta;   //!
   TBranch        *b_convR;   //!
   TBranch        *b_convMatchedEle;   //!
   TBranch        *b_convChi2; //!
   TBranch        *b_convMomentum; //!
   TBranch        *b_convMomentum2; //!
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
   TBranch        *b_phoMatchedEle;  //!
   TBranch        *b_conversionVeto;  //!
   TBranch        *b_r9;  //!
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

   GMSBTree_V3(TTree *tree=0);
   virtual ~GMSBTree_V3();
   virtual Int_t    Cut(Long64_t entry);
   virtual Int_t    GetEntry(Long64_t entry);
   virtual Long64_t LoadTree(Long64_t entry);
   virtual void     Init(TTree *tree);
   virtual void     Loop();
   virtual Bool_t   Notify();
   virtual void     Show(Long64_t entry = -1);
};

#endif

#ifdef GMSBTree_V3_cxx
GMSBTree_V3::GMSBTree_V3(TTree *tree) : fChain(0) 
{
// if parameter tree is not specified (or zero), connect the file
// used to generate this class and read the Tree.
   if (tree == 0) {
      TFile *f = (TFile*)gROOT->GetListOfFiles()->FindObject("/afs/cern.ch/work/w/wvandrie/public/EXO/CMSSW_7_1_8/src/EXO/DPAnalysis/test/v24/Run2012B.root");
      if (!f || !f->IsOpen()) {
         f = new TFile("/afs/cern.ch/work/w/wvandrie/public/EXO/CMSSW_7_1_8/src/EXO/DPAnalysis/test/v24/Run2012B.root");
      }
      f->GetObject("DPAnalysis",tree);

   }
   Init(tree);
}

GMSBTree_V3::~GMSBTree_V3()
{
   if (!fChain) return;
   delete fChain->GetCurrentFile();
}

Int_t GMSBTree_V3::GetEntry(Long64_t entry)
{
// Read contents of entry.
   if (!fChain) return 0;
   return fChain->GetEntry(entry);
}
Long64_t GMSBTree_V3::LoadTree(Long64_t entry)
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

void GMSBTree_V3::Init(TTree *tree)
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
   fChain->SetBranchAddress("PU_NumInter", &PU_NumInter, &b_PU_NumInter);
   fChain->SetBranchAddress("nMuons", &nMuons, &b_nMuons);
   fChain->SetBranchAddress("nElectrons", &nElectrons, &b_nElectrons);
   fChain->SetBranchAddress("nJets", &nJets, &b_nJets);
   fChain->SetBranchAddress("nPhotons", &nPhotons, &b_nPhotons);
   fChain->SetBranchAddress("nConversions", &nConversions, &b_nConversions);
   fChain->SetBranchAddress("nVertices", &nVertices, &b_nVertices);
   fChain->SetBranchAddress("nPU", &nPU, &b_nPU);
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
   fChain->SetBranchAddress("t_phoPz", &t_phoPz, &b_t_phoPz);
   fChain->SetBranchAddress("t_phoPt", &t_phoPt, &b_t_phoPt);
   fChain->SetBranchAddress("t_phoE", &t_phoE, &b_t_phoE);
   fChain->SetBranchAddress("t_phodR", &t_phodR, &b_t_phodR);
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
   fChain->SetBranchAddress("convDxy", convDxy, &b_convDxy);
   fChain->SetBranchAddress("convDz", convDz, &b_convDz);
   fChain->SetBranchAddress("convPhi", convPhi, &b_convPhi);
   fChain->SetBranchAddress("convEta", convEta, &b_convEta);
   fChain->SetBranchAddress("convR", convR, &b_convR);
   fChain->SetBranchAddress("convMatchedEle", convMatchedEle, &b_convMatchedEle);
   fChain->SetBranchAddress("convChi2", convChi2, &b_convChi2);
   fChain->SetBranchAddress("convMomentum", convMomentum, &b_convMomentum);
   fChain->SetBranchAddress("convMomentum2", convMomentum2, &b_convMomentum2);
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
   fChain->SetBranchAddress("phoMatchedEle", phoMatchedEle, &b_phoMatchedEle);
   fChain->SetBranchAddress("conversionVeto", conversionVeto, &b_conversionVeto);
   fChain->SetBranchAddress("r9", r9, &b_r9);
   fChain->SetBranchAddress("vtxNTracks", vtxNTracks, &b_vtxNTracks);
   fChain->SetBranchAddress("vtxChi2", vtxChi2, &b_vtxChi2);
   fChain->SetBranchAddress("vtxNdof", vtxNdof, &b_vtxNdof);
   fChain->SetBranchAddress("vtxRho", vtxRho, &b_vtxRho);
   fChain->SetBranchAddress("vtxZ", vtxZ, &b_vtxZ);
   fChain->SetBranchAddress("pdgId", pdgId, &b_pdgId);
   fChain->SetBranchAddress("momId", momId, &b_momId);
   fChain->SetBranchAddress("genPx", genPx, &b_genPx);
   fChain->SetBranchAddress("genPy", genPy, &b_genPy);
   fChain->SetBranchAddress("genPz", genPz, &b_genPz);
   fChain->SetBranchAddress("genE", genE, &b_genE);
   fChain->SetBranchAddress("genM", genM, &b_genM);
   fChain->SetBranchAddress("genVx", genVx, &b_genVx);
   fChain->SetBranchAddress("genVy", genVy, &b_genVy);
   fChain->SetBranchAddress("genVz", genVz, &b_genVz);
   fChain->SetBranchAddress("genT", genT, &b_genT);
   Notify();
}

Bool_t GMSBTree_V3::Notify()
{
   // The Notify() function is called when a new file is opened. This
   // can be either for a new TTree in a TChain or when when a new TTree
   // is started when using PROOF. It is normally not necessary to make changes
   // to the generated code, but the routine can be extended by the
   // user if needed. The return value is currently not used.

   return kTRUE;
}

void GMSBTree_V3::Show(Long64_t entry)
{
// Print contents of entry.
// If entry is not specified, print current entry
   if (!fChain) return;
   fChain->Show(entry);
}
Int_t GMSBTree_V3::Cut(Long64_t entry)
{
// This function may be called from Loop.
// returns  1 if entry is accepted.
// returns -1 otherwise.
   return 1;
}
#endif // #ifdef GMSBTree_V3_cxx

