#include "EXO/DPAnalysis/interface/Ntuple.h"

void setBranchAddresses(TTree* chain, Ntuple& treeVars)
{
  chain -> SetBranchAddress("runId",       &treeVars.runId);
  chain -> SetBranchAddress("lumiSection", &treeVars.lumiSection);
  chain -> SetBranchAddress("orbit",       &treeVars.orbit);
  chain -> SetBranchAddress("bx",          &treeVars.bx);
  chain -> SetBranchAddress("eventId",     &treeVars.eventId);
  chain -> SetBranchAddress("triggered",   &treeVars.triggered);
  chain -> SetBranchAddress("L1a",         &treeVars.L1a );
  chain -> SetBranchAddress("PU_NumInter", &treeVars.PU_NumInter );
  
  // PAT VARIABLES
  chain -> SetBranchAddress("nMuons",      &treeVars.nMuons     );
  chain -> SetBranchAddress("nElectrons",  &treeVars.nElectrons );
  chain -> SetBranchAddress("nJets",       &treeVars.nJets      );
  chain -> SetBranchAddress("nPhotons",    &treeVars.nPhotons   );
  chain -> SetBranchAddress("nConversions",    &treeVars.nConversions   );
  chain -> SetBranchAddress("nVertices",   &treeVars.nVertices  );
  chain -> SetBranchAddress("nPU",   	   &treeVars.nPU  );
  chain -> SetBranchAddress("totalNVtx",   &treeVars.totalNVtx  );
  chain -> SetBranchAddress("nGen",        &treeVars.nGen       );
  chain -> SetBranchAddress("nOutTimeHits",  &treeVars.nOutTimeHits );
  chain -> SetBranchAddress("nHaloTrack",    &treeVars.nHaloTrack );
  //chain -> SetBranchAddress("haloPhi",       &treeVars.haloPhi    );
  //chain -> SetBranchAddress("haloRho",       &treeVars.haloRho    );
  chain -> SetBranchAddress("z0Ratio",       &treeVars.z0Ratio    );

  chain -> SetBranchAddress("met0Px",      &treeVars.met0Px     );
  chain -> SetBranchAddress("met0Py",      &treeVars.met0Py     );
  chain -> SetBranchAddress("met0",        &treeVars.met0       );
  chain -> SetBranchAddress("metPx",       &treeVars.metPx     );
  chain -> SetBranchAddress("metPy",       &treeVars.metPy     );
  chain -> SetBranchAddress("met",         &treeVars.met       );
  chain -> SetBranchAddress("met_dx1",     &treeVars.met_dx1    );
  chain -> SetBranchAddress("met_dy1",     &treeVars.met_dy1    );
  chain -> SetBranchAddress("met_dx2",     &treeVars.met_dx2    );
  chain -> SetBranchAddress("met_dy2",     &treeVars.met_dy2    );
  chain -> SetBranchAddress("met_dx3",     &treeVars.met_dx3    );
  chain -> SetBranchAddress("met_dy3",     &treeVars.met_dy3    );

  // trigger matched objects 
  chain -> SetBranchAddress("t_phoPx",      &treeVars.t_phoPx    );
  chain -> SetBranchAddress("t_phoPy",      &treeVars.t_phoPy    );
  chain -> SetBranchAddress("t_phoPz",      &treeVars.t_phoPz    );
  chain -> SetBranchAddress("t_phoE",       &treeVars.t_phoE     );
  chain -> SetBranchAddress("t_phoPt",      &treeVars.t_phoPt    );
  chain -> SetBranchAddress("t_metPx",      &treeVars.t_metPx    );
  chain -> SetBranchAddress("t_metPy",      &treeVars.t_metPy    );
  chain -> SetBranchAddress("t_met",        &treeVars.t_met      );
  chain -> SetBranchAddress("t_metdR",      &treeVars.t_metdR    );

  // vertex variables
  chain -> SetBranchAddress("vtxNTracks",   treeVars.vtxNTracks);
  chain -> SetBranchAddress("vtxChi2",      treeVars.vtxChi2   );
  chain -> SetBranchAddress("vtxNdof",      treeVars.vtxNdof   );
  chain -> SetBranchAddress("vtxRhi",       treeVars.vtxRho     );
  chain -> SetBranchAddress("vtxZ",         treeVars.vtxZ      );
  //chain -> SetBranchAddress("nTrkZ0",     treeVars.nTrkZ0   );

//  chain -> SetBranchAddress("PU_TrueNumInter", treeVars.PU_TrueNumInter      );
//  chain -> SetBranchAddress("PU_BX",           treeVars.PU_BX      );

  chain -> SetBranchAddress("muPx",        treeVars.muPx       );
  chain -> SetBranchAddress("muPy",        treeVars.muPy       );
  chain -> SetBranchAddress("muPz",        treeVars.muPz       );
  chain -> SetBranchAddress("muE",         treeVars.muE        );
  chain -> SetBranchAddress("muIso",       treeVars.muIso      );
  
  chain -> SetBranchAddress("elePx",        treeVars.elePx     );
  chain -> SetBranchAddress("elePy",        treeVars.elePy     );
  chain -> SetBranchAddress("elePz",        treeVars.elePz     );
  chain -> SetBranchAddress("eleE",         treeVars.eleE      );
  chain -> SetBranchAddress("eleNLostHits", treeVars.eleNLostHits );
  chain -> SetBranchAddress("eleEcalIso",   treeVars.eleEcalIso ) ;
  chain -> SetBranchAddress("eleHcalIso",   treeVars.eleHcalIso ) ;
  chain -> SetBranchAddress("eleTrkIso",    treeVars.eleTrkIso ) ;
  chain -> SetBranchAddress("e_cHadIso",    treeVars.e_cHadIso ) ;
  chain -> SetBranchAddress("e_nHadIso",    treeVars.e_nHadIso ) ;
  chain -> SetBranchAddress("e_photIso",    treeVars.e_photIso ) ;
  
  chain -> SetBranchAddress("jetPx",        treeVars.jetPx     );
  chain -> SetBranchAddress("jetPy",        treeVars.jetPy     );
  chain -> SetBranchAddress("jetPz",        treeVars.jetPz     );
  chain -> SetBranchAddress("jetE",         treeVars.jetE      );
  chain -> SetBranchAddress("jetNDau",      treeVars.jetNDau   );
  chain -> SetBranchAddress("jetCM",        treeVars.jetCM     );
  chain -> SetBranchAddress("jetCEF",       treeVars.jetCEF    );
  chain -> SetBranchAddress("jetCHF",       treeVars.jetCHF    );
  chain -> SetBranchAddress("jetNHF",       treeVars.jetNHF    );
  chain -> SetBranchAddress("jetNEF",       treeVars.jetNEF    );
  chain -> SetBranchAddress("jerUnc",        treeVars.jerUnc     );
  chain -> SetBranchAddress("jecUnc",       treeVars.jecUnc    );
  //chain -> SetBranchAddress("jecUncU",      treeVars.jecUncU  );
  //chain -> SetBranchAddress("jecUncD",      treeVars.jecUncD  );
  
  chain -> SetBranchAddress("convR",         treeVars.convR      );
  chain -> SetBranchAddress("convDxy",       treeVars.convDxy      );
  chain -> SetBranchAddress("convDz",        treeVars.convDz      );
  chain -> SetBranchAddress("convEta",       treeVars.convEta      );
  chain -> SetBranchAddress("convPhi",       treeVars.convPhi      );
  chain -> SetBranchAddress("convChi2",      treeVars.convChi2      );
  chain -> SetBranchAddress("convMatchedEle",      treeVars.convMatchedEle      );
  chain -> SetBranchAddress("phoPx",        treeVars.phoPx     );
  chain -> SetBranchAddress("phoPy",        treeVars.phoPy     );
  chain -> SetBranchAddress("phoPz",        treeVars.phoPz     );
  chain -> SetBranchAddress("phoPt",        treeVars.phoPt      );
  chain -> SetBranchAddress("phoE",         treeVars.phoE      );
  chain -> SetBranchAddress("phoEcalIso",   treeVars.phoEcalIso ) ;
  chain -> SetBranchAddress("phoHcalIso",   treeVars.phoHcalIso ) ;
  chain -> SetBranchAddress("phoTrkIso",    treeVars.phoTrkIso ) ;
  chain -> SetBranchAddress("cHadIso",      treeVars.cHadIso ) ;
  chain -> SetBranchAddress("nHadIso",      treeVars.nHadIso ) ;
  chain -> SetBranchAddress("photIso",      treeVars.photIso ) ;
  chain -> SetBranchAddress("dR_TrkPho",    treeVars.dR_TrkPho ) ;
  chain -> SetBranchAddress("pt_TrkPho",    treeVars.pt_TrkPho ) ;
  chain -> SetBranchAddress("phoHoverE",    treeVars.phoHoverE ) ;
  chain -> SetBranchAddress("sMinPho",      treeVars.sMinPho ) ;
  chain -> SetBranchAddress("sMajPho",      treeVars.sMajPho ) ;
  chain -> SetBranchAddress("seedTime",     treeVars.seedTime ) ;
  chain -> SetBranchAddress("seedTimeErr",  treeVars.seedTimeErr ) ;
  chain -> SetBranchAddress("aveTime",      treeVars.aveTime ) ;
  chain -> SetBranchAddress("aveTimeErr",   treeVars.aveTimeErr ) ;
  chain -> SetBranchAddress("aveTime1",     treeVars.aveTime1 ) ;
  chain -> SetBranchAddress("aveTimeErr1",  treeVars.aveTimeErr1 ) ;
  chain -> SetBranchAddress("timeChi2",     treeVars.timeChi2 ) ;
  chain -> SetBranchAddress("nXtals",       treeVars.nXtals ) ;
  chain -> SetBranchAddress("fSpike",       treeVars.fSpike ) ;
  chain -> SetBranchAddress("maxSwissX",    treeVars.maxSwissX ) ;
  chain -> SetBranchAddress("seedSwissX",   treeVars.seedSwissX ) ;
  chain -> SetBranchAddress("nBC",          treeVars.nBC ) ;
  chain -> SetBranchAddress("sigmaEta",     treeVars.sigmaEta ) ;
  chain -> SetBranchAddress("sigmaIeta",    treeVars.sigmaIeta ) ;
  chain -> SetBranchAddress("cscRho",       treeVars.cscRho ) ;
  chain -> SetBranchAddress("cscdPhi",      treeVars.cscdPhi ) ;
  chain -> SetBranchAddress("cscTime",      treeVars.cscTime ) ;
  chain -> SetBranchAddress("dtdPhi",       treeVars.dtdPhi ) ;
  chain -> SetBranchAddress("dtdEta",       treeVars.dtdEta ) ;
  chain -> SetBranchAddress("phoMatchedEle",treeVars.phoMatchedEle ) ;
  chain -> SetBranchAddress("conversionVeto",treeVars.conversionVeto ) ;

  chain -> SetBranchAddress("genPx",        treeVars.genPx       );
  chain -> SetBranchAddress("genPy",        treeVars.genPy       );
  chain -> SetBranchAddress("genPz",        treeVars.genPz       );
  chain -> SetBranchAddress("genE",         treeVars.genE        );
  chain -> SetBranchAddress("genM",         treeVars.genM        );
  chain -> SetBranchAddress("genVx",        treeVars.genVx       );
  chain -> SetBranchAddress("genVy",        treeVars.genVy       );
  chain -> SetBranchAddress("genVz",        treeVars.genVz       );
  chain -> SetBranchAddress("genT",         treeVars.genT        );
  chain -> SetBranchAddress("pdgId",        treeVars.pdgId       );
  chain -> SetBranchAddress("momId",        treeVars.momId       );
  
}


void setBranches(TTree* chain, Ntuple& treeVars)
{
  chain -> Branch("runId",         &treeVars.runId,                "runId/i");
  chain -> Branch("lumiSection",   &treeVars.lumiSection,    "lumiSection/i");
  chain -> Branch("orbit",         &treeVars.orbit,                "orbit/i");
  chain -> Branch("bx",            &treeVars.bx,                      "bx/i");
  chain -> Branch("eventId",       &treeVars.eventId,            "eventId/i");
  chain -> Branch("triggered",     &treeVars.triggered,        "triggered/I");
  chain -> Branch("L1a",           &treeVars.L1a,              "L1a/I");
  chain -> Branch("PU_NumInter",   &treeVars.PU_NumInter, 	"PU_NumInter/I");
  
  // RECO VARIABLES
  chain -> Branch("nMuons",      &treeVars.nMuons,               "nMuons/I");
  chain -> Branch("nElectrons",  &treeVars.nElectrons,           "nElectrons/I");
  chain -> Branch("nJets",       &treeVars.nJets,                "nJets/I");
  chain -> Branch("nPhotons",    &treeVars.nPhotons,             "nPhotons/I");
  chain -> Branch("nConversions",&treeVars.nConversions,         "nConversions/I");
  chain -> Branch("nVertices",   &treeVars.nVertices,            "nVertices/I");
  chain -> Branch("nPU",   	 &treeVars.nPU,            	 "nPU/I");
  chain -> Branch("totalNVtx",   &treeVars.totalNVtx,            "totalNVtx/I");
  chain -> Branch("nGen",        &treeVars.nGen,                 "nGen/I");

  chain -> Branch("nOutTimeHits",  &treeVars.nOutTimeHits, "nOutTimeHits/I" );
  chain -> Branch("nHaloTrack",    &treeVars.nHaloTrack,   "nHaloTrack/I" );
  //chain -> Branch("haloPhi",       &treeVars.haloPhi,      "haloPhi/F" );
  //chain -> Branch("haloRho",       &treeVars.haloRho,      "haloRho/F" );
  chain -> Branch("z0Ratio",     &treeVars.z0Ratio,        "z0Ratio/F" );

  chain -> Branch("met0Px",      &treeVars.met0Px,               "met0Px/F");
  chain -> Branch("met0Py",      &treeVars.met0Py,               "met0Py/F");
  chain -> Branch("met0",        &treeVars.met0,                 "met0/F");
  chain -> Branch("metPx",       &treeVars.metPx,                "metPx/F");
  chain -> Branch("metPy",       &treeVars.metPy,                "metPy/F");
  chain -> Branch("met",         &treeVars.met,                  "met/F");
  chain -> Branch("met_dx1",     &treeVars.met_dx1,              "met_dx1/F");
  chain -> Branch("met_dy1",     &treeVars.met_dy1,              "met_dy1/F");
  chain -> Branch("met_dx2",     &treeVars.met_dx2,              "met_dx2/F");
  chain -> Branch("met_dy2",     &treeVars.met_dy2,              "met_dy2/F");
  chain -> Branch("met_dx3",     &treeVars.met_dx3,              "met_dx3/F");
  chain -> Branch("met_dy3",     &treeVars.met_dy3,              "met_dy3/F");


  chain -> Branch("t_metPx",     &treeVars.t_metPx,              "t_metPx/F");
  chain -> Branch("t_metPy",     &treeVars.t_metPy,              "t_metPy/F");
  chain -> Branch("t_met",       &treeVars.t_met,                "t_met/F");
  chain -> Branch("t_metdR",     &treeVars.t_metdR,              "t_metdR/F");
  chain -> Branch("t_phoPz",     &treeVars.t_phoPz,              "t_phoPz/F");
  chain -> Branch("t_phoPt",     &treeVars.t_phoPt,              "t_phoPt/F");
  chain -> Branch("t_phoE",      &treeVars.t_phoE,               "t_phoE/F");
  chain -> Branch("t_phodR",     &treeVars.t_phodR,              "t_phodR/F");
  chain -> Branch("muPx",        treeVars.muPx,                 "muPx[nMuons]/F");
  chain -> Branch("muPy",        treeVars.muPy,                 "muPy[nMuons]/F");
  chain -> Branch("muPz",        treeVars.muPz,                 "muPz[nMuons]/F");
  chain -> Branch("muE",         treeVars.muE,                  "muE[nMuons]/F");
  chain -> Branch("muIso",       treeVars.muIso,                "muIso[nMuons]/F");
  
  chain -> Branch("elePx",        treeVars.elePx,                 "elePx[nElectrons]/F");
  chain -> Branch("elePy",        treeVars.elePy,                 "elePy[nElectrons]/F");
  chain -> Branch("elePz",        treeVars.elePz,                 "elePz[nElectrons]/F");
  chain -> Branch("eleE",         treeVars.eleE,                  "eleE[nElectrons]/F");
  chain -> Branch("eleNLostHits", treeVars.eleNLostHits,          "eleNLostHits[nElectrons]/I" );
  chain -> Branch("eleEcalIso",   treeVars.eleEcalIso,            "eleEcalIso[nElectrons]/F") ;
  chain -> Branch("eleHcalIso",   treeVars.eleHcalIso,            "eleHcalIso[nElectrons]/F") ;
  chain -> Branch("eleTrkIso",    treeVars.eleTrkIso,             "eleTrkIso[nElectrons]/F" ) ;
  chain -> Branch("e_cHadIso",    treeVars.e_cHadIso,             "e_cHadIso[nElectrons]/F") ;
  chain -> Branch("e_nHadIso",    treeVars.e_nHadIso,             "e_nHadIso[nElectrons]/F") ;
  chain -> Branch("e_photIso",    treeVars.e_photIso,             "e_photIso[nElectrons]/F") ;
  
  chain -> Branch("jetPx",        treeVars.jetPx,                 "jetPx[nJets]/F");
  chain -> Branch("jetPy",        treeVars.jetPy,                 "jetPy[nJets]/F");
  chain -> Branch("jetPz",        treeVars.jetPz,                 "jetPz[nJets]/F");
  chain -> Branch("jetE",         treeVars.jetE,                  "jetE[nJets]/F");
  chain -> Branch("jetNDau",      treeVars.jetNDau,               "jetNDau[nJets]/I");
  chain -> Branch("jetCM",        treeVars.jetCM,                 "jetCM[nJets]/I"  );
  chain -> Branch("jetCEF",       treeVars.jetCEF,                "jetCEF[nJets]/F" );
  chain -> Branch("jetCHF",       treeVars.jetCHF,                "jetCHF[nJets]/F" );
  chain -> Branch("jetNHF",       treeVars.jetNHF,                "jetNHF[nJets]/F" );
  chain -> Branch("jetNEF",       treeVars.jetNEF,                "jetNEF[nJets]/F" );
  chain -> Branch("jerUnc",       treeVars.jerUnc,                 "jerUnc[nJets]/F"  );
  chain -> Branch("jecUnc",       treeVars.jecUnc,                "jecUnc[nJets]/F" );
  
  chain -> Branch("convDxy",       treeVars.convDxy,                "convDxy[nConversions]/F");
  chain -> Branch("convDz",        treeVars.convDz,                 "convDz[nConversions]/F");
  chain -> Branch("convEta",       treeVars.convEta,               "convEta[nConversions]/F");
  chain -> Branch("convPhi",       treeVars.convPhi,                "convPhi[nConversions]/F");
  chain -> Branch("convChi2",       treeVars.convChi2,                "convChi2[nConversions]/F");
  chain -> Branch("convR",         treeVars.convR,                  "convR[nConversions]/F");
  chain -> Branch("convMatchedEle",       treeVars.convMatchedEle,                "convMatchedEle[nConversions]/F");

  chain -> Branch("phoPx",        treeVars.phoPx,                 "phoPx[nPhotons]/F");
  chain -> Branch("phoPy",        treeVars.phoPy,                 "phoPy[nPhotons]/F");
  chain -> Branch("phoPz",        treeVars.phoPz,                 "phoPz[nPhotons]/F");
  chain -> Branch("phoPt",        treeVars.phoPt,                  "phoPt[nPhotons]/F");
  chain -> Branch("phoE",         treeVars.phoE,                  "phoE[nPhotons]/F");
  chain -> Branch("phoEcalIso",   treeVars.phoEcalIso,            "phoEcalIso[nPhotons]/F") ;
  chain -> Branch("phoHcalIso",   treeVars.phoHcalIso,            "phoHcalIso[nPhotons]/F") ;
  chain -> Branch("phoTrkIso",    treeVars.phoTrkIso,             "phoTrkIso[nPhotons]/F") ;
  chain -> Branch("cHadIso",      treeVars.cHadIso,               "cHadIso[nPhotons]/F") ;
  chain -> Branch("nHadIso",      treeVars.nHadIso,               "nHadIso[nPhotons]/F") ;
  chain -> Branch("photIso",      treeVars.photIso,               "photIso[nPhotons]/F") ;
  chain -> Branch("dR_TrkPho",    treeVars.dR_TrkPho,             "dR_TrkPho[nPhotons]/F") ;
  chain -> Branch("pt_TrkPho",    treeVars.pt_TrkPho,             "pt_TrkPho[nPhotons]/F") ;
  chain -> Branch("phoHoverE",    treeVars.phoHoverE,             "phoHoverE[nPhotons]/F") ;
  chain -> Branch("sMinPho",      treeVars.sMinPho,               "sMinPho[nPhotons]/F") ;
  chain -> Branch("sMajPho",      treeVars.sMajPho,               "sMajPho[nPhotons]/F") ;
  chain -> Branch("seedTime",     treeVars.seedTime,              "seedTime[nPhotons]/F") ;
  chain -> Branch("seedTimeErr",  treeVars.seedTimeErr,           "seedTimeErr[nPhotons]/F") ;
  chain -> Branch("aveTime",      treeVars.aveTime,               "aveTime[nPhotons]/F") ;
  chain -> Branch("aveTimeErr",   treeVars.aveTimeErr,            "aveTimeErr[nPhotons]/F") ;
  chain -> Branch("aveTime1",     treeVars.aveTime1,              "aveTime1[nPhotons]/F") ;
  chain -> Branch("aveTimeErr1",  treeVars.aveTimeErr1,           "aveTimeErr1[nPhotons]/F") ;
  chain -> Branch("timeChi2",     treeVars.timeChi2,              "timeChi2[nPhotons]/F") ;
  chain -> Branch("fSpike",       treeVars.fSpike,                "fSpike[nPhotons]/F"  ) ;
  chain -> Branch("maxSwissX",    treeVars.maxSwissX,             "maxSwissX[nPhotons]/F"  ) ;
  chain -> Branch("seedSwissX",   treeVars.seedSwissX,            "seedSwissX[nPhotons]/F"  ) ;
  chain -> Branch("nXtals",       treeVars.nXtals,                "nXtals[nPhotons]/I"  ) ;
  chain -> Branch("nBC",          treeVars.nBC,                   "nBC[nPhotons]/I"  ) ;
  chain -> Branch("sigmaEta",     treeVars.sigmaEta,              "sigmaEta[nPhotons]/I"  ) ;
  chain -> Branch("sigmaIeta",    treeVars.sigmaIeta,             "sigmaIeta[nPhotons]/F"  ) ;
  chain -> Branch("cscRho",       treeVars.cscRho,                "cscRho[nPhotons]/F"  ) ;
  chain -> Branch("cscdPhi",      treeVars.cscdPhi,               "cscdPhi[nPhotons]/F"  ) ;
  chain -> Branch("cscTime",      treeVars.cscTime,               "cscTime[nPhotons]/F"  ) ;
  chain -> Branch("dtdPhi",       treeVars.dtdPhi,                "dtdPhi[nPhotons]/F"  ) ;
  chain -> Branch("dtdEta",       treeVars.dtdEta,                "dtdEta[nPhotons]/F"  ) ;
  chain -> Branch("phoMatchedEle",treeVars.phoMatchedEle,         "phoMatchedEle[nPhotons]/F"  ) ;
  chain -> Branch("conversionVeto",treeVars.conversionVeto,         "conversionVeto[nPhotons]/F"  ) ;
//  chain -> Branch("convDxy",       treeVars.convDxy,                "convDxy[nPhotons]/F");
//  chain -> Branch("convDz",        treeVars.convDz,                 "convDz[nPhotons]/F");
//  chain -> Branch("convEta",      treeVars.convEta,               "convEta[nPhotons]/F");
//  chain -> Branch("convPhi",       treeVars.convPhi,                "convPhi[nPhotons]/F");


  chain -> Branch("vtxNTracks",       treeVars.vtxNTracks,   "vtxNTracks[nVertices]/I");
  chain -> Branch("vtxChi2",          treeVars.vtxChi2,      "vtxChi2[nVertices]/F");
  chain -> Branch("vtxNdof",          treeVars.vtxNdof,      "vtxNdof[nVertices]/F");
  chain -> Branch("vtxRho",           treeVars.vtxRho,       "vtxRho[nVertices]/F");
  chain -> Branch("vtxZ",             treeVars.vtxZ,         "vtxZ[nVertices]/F");
  //chain -> Branch("nTrkZ0",           treeVars.nTrkZ0,       "nTrkZ0[33]/I");

//  chain -> Branch("PU_TrueNumInter",  treeVars.PU_TrueNumInter, "PU_TrueNumInter[nPU]/I");
//  chain -> Branch("PU_BX",            treeVars.PU_BX, 		"PU_BX[nPU]/I");
  
  chain -> Branch("pdgId",        treeVars.pdgId,                 "pdgId[nGen]/I");
  chain -> Branch("momId",        treeVars.momId,                 "momId[nGen]/I");
  chain -> Branch("genPx",        treeVars.genPx,                 "genPx[nGen]/F");
  chain -> Branch("genPy",        treeVars.genPy,                 "genPy[nGen]/F");
  chain -> Branch("genPz",        treeVars.genPz,                 "genPz[nGen]/F");
  chain -> Branch("genE",         treeVars.genE,                  "genE[nGen]/F");
  chain -> Branch("genM",         treeVars.genM,                  "genM[nGen]/F");
  chain -> Branch("genVx",        treeVars.genVx,                 "genVx[nGen]/F");
  chain -> Branch("genVy",        treeVars.genVy,                 "genVy[nGen]/F");
  chain -> Branch("genVz",        treeVars.genVz,                 "genVz[nGen]/F");
  chain -> Branch("genT",         treeVars.genT,                  "genT[nGen]/F");
  
}


void initializeBranches(TTree* chain, Ntuple& treeVars)
{
  treeVars.runId = 0;
  treeVars.lumiSection = 0;
  treeVars.orbit = 0;
  treeVars.bx = 0;
  treeVars.eventId = 0; 
  treeVars.triggered = 0; 
  treeVars.L1a = 0; 
  
  treeVars.nJets      = 0 ; 
  treeVars.nElectrons = 0 ; 
  treeVars.nMuons     = 0 ; 
  treeVars.nPhotons   = 0 ; 
  treeVars.nConversions= 0 ; 
  treeVars.nVertices  = 0 ;
  treeVars.nPU        = 0 ;
  treeVars.totalNVtx  = 0 ;
  treeVars.nGen       = 0 ; 

  treeVars.nOutTimeHits = -1 ;
  treeVars.nHaloTrack   = -1 ;
  //treeVars.haloPhi      = -1 ;
  //treeVars.haloRho      = -1 ;
  treeVars.z0Ratio    = -1 ;

  treeVars.met0Px = 0 ;
  treeVars.met0Py = 0 ;
  treeVars.met0   = 0 ;
  treeVars.metPx = 0 ;
  treeVars.metPy = 0 ;
  treeVars.met   = 0 ;
  treeVars.met_dx1 = 0 ;
  treeVars.met_dy1 = 0 ;
  treeVars.met_dx2 = 0 ;
  treeVars.met_dy2 = 0 ;
  treeVars.met_dx3 = 0 ;
  treeVars.met_dy3 = 0 ;

  treeVars.t_metPx = 0 ;
  treeVars.t_metPy = 0 ;
  treeVars.t_met   = 0 ;
  treeVars.t_metdR = 99. ;
  treeVars.t_phoPx = 0 ;
  treeVars.t_phoPy = 0 ;
  treeVars.t_phoPz = 0 ;
  treeVars.t_phoE  = 0 ;
  treeVars.t_phoPt  = 0 ;
  treeVars.t_phodR = 99 ;

  for ( int i=0; i< MAXJET; i++) {
      treeVars.jetPx[i] = 0 ;
      treeVars.jetPy[i] = 0 ;
      treeVars.jetPz[i] = 0 ;
      treeVars.jetE[i] = 0 ;
      treeVars.jetNDau[i] = 0 ;
      treeVars.jetCM[i] = 0 ;
      treeVars.jetCEF[i] = 0 ;
      treeVars.jetCHF[i] = 0 ;
      treeVars.jetNHF[i] = 0 ;
      treeVars.jetNEF[i] = 0 ;
      treeVars.jerUnc[i] = 0 ;
      treeVars.jecUnc[i] = 0 ;
      //treeVars.jecUncU[i] = 0 ;
      //treeVars.jecUncD[i] = 0 ;
  }

  for ( int i=0; i< MAXELE; i++) {
      treeVars.elePx[i] = 0 ;
      treeVars.elePy[i] = 0 ;
      treeVars.elePz[i] = 0 ;
      treeVars.eleE[i] = 0 ;
      treeVars.eleEcalIso[i] = -1 ;
      treeVars.eleHcalIso[i] = -1 ;
      treeVars.eleTrkIso[i]  = -1 ;
      treeVars.eleNLostHits[i]  = -1 ;
      treeVars.e_cHadIso[i]    = -1 ;
      treeVars.e_nHadIso[i]    = -1 ;
      treeVars.e_photIso[i]    = -1 ;
  }
  for ( int i=0; i< MAXMU; i++) {
      treeVars.muPx[i] = 0 ;
      treeVars.muPy[i] = 0 ;
      treeVars.muPz[i] = 0 ;
      treeVars.muE[i] = 0 ;
      treeVars.muIso[i] = -1 ;
  } 
  for ( int i=0; i< MAXPHO; i++) {
      treeVars.phoPx[i] = 0 ;
      treeVars.phoPy[i] = 0 ;
      treeVars.phoPz[i] = 0 ;
      treeVars.phoE[i] = 0 ;
      treeVars.phoPt[i] = 0 ;
      treeVars.convR[i] = 0 ;
      treeVars.phoEcalIso[i] = -1 ;
      treeVars.phoHcalIso[i] = -1 ;
      treeVars.phoTrkIso[i]  = -1 ;
      treeVars.cHadIso[i]    = -1 ;
      treeVars.nHadIso[i]    = -1 ;
      treeVars.photIso[i]    = -1 ;
      treeVars.dR_TrkPho[i]  = -1 ;
      treeVars.pt_TrkPho[i]  = -1 ;
      treeVars.phoHoverE[i]  = -1 ;
      treeVars.sMinPho[i]    = -1 ;
      treeVars.sMajPho[i]    = -1 ;
      treeVars.seedTime[i]   = -25 ;
      treeVars.seedTimeErr[i] = -25 ;
      treeVars.aveTime[i]     = -25 ;
      treeVars.aveTimeErr[i]  = -25 ;
      treeVars.aveTime1[i]    = -25 ;
      treeVars.aveTimeErr1[i] = -25 ;
      treeVars.timeChi2[i]    = -1 ;
      treeVars.fSpike[i]      = -1 ;
      treeVars.maxSwissX[i]   = 0 ;
      treeVars.seedSwissX[i]  = 0 ;
      treeVars.nXtals[i]      = 0 ;
      treeVars.nBC[i]         = 0 ;
      treeVars.sigmaEta[i]    = -1. ;
      treeVars.sigmaIeta[i]   = -1. ;
      treeVars.cscRho[i]      = -1. ;
      treeVars.cscdPhi[i]     = 99. ;
      treeVars.cscTime[i]     = 99. ;
      treeVars.dtdPhi[i]      = 99. ;
      treeVars.dtdEta[i]      = 99. ;
      treeVars.phoMatchedEle[i] = 99. ;
      treeVars.conversionVeto[i] = 99. ;
  }
  for ( int i=0; i< MAXCONV; i++) {
      treeVars.convDxy[i] = 0 ;
      treeVars.convDz[i] = 0 ;
      treeVars.convEta[i] = 0 ;
      treeVars.convPhi[i] = 0 ;
      treeVars.convChi2[i] = 0 ;
      treeVars.convMatchedEle[i] = 0 ;
      treeVars.convR[i] = 0 ;
  }
  for(int i=0; i<MAXVTX; i++) {
      treeVars.vtxNTracks[i]=0;
      treeVars.vtxChi2[i]=0;
      treeVars.vtxNdof[i]=0;
      treeVars.vtxRho[i]=0;
      treeVars.vtxZ[i]=0;
  }
/*  for(int i=0; i<MAXPU; i++) {
      treeVars.PU_NumInter[i]=0;
      treeVars.PU_TrueNumInter[i]=0;
      treeVars.PU_BX[i]=0;

  }*/
  //for(int i=0; i<33; i++) {
  //    treeVars.nTrkZ0[i]=0;
  //}
  for ( int i=0; i< MAXGEN; i++) {
      treeVars.pdgId[i] = 0 ;
      treeVars.momId[i] = 0 ;
      treeVars.genPx[i] = 0 ;
      treeVars.genPy[i] = 0 ;
      treeVars.genPz[i] = 0 ;
      treeVars.genE[i] = 0 ;
      treeVars.genM[i] = 0 ;
      treeVars.genVx[i] = 0 ;
      treeVars.genVy[i] = 0 ;
      treeVars.genVz[i] = 0 ;
      treeVars.genT[i] = 0 ;
  }
}
