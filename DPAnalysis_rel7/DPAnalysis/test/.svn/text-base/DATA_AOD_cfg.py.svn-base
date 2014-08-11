import FWCore.ParameterSet.Config as cms

process = cms.Process("test")

process.load("FWCore.MessageService.MessageLogger_cfi")

process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(1000) )

process.source = cms.Source("PoolSource",

    fileNames = cms.untracked.vstring(
    #'file:SinglePhoton_Run2012B-20Nov2012-v2_AOD.root'
    #'root://xrootd.unl.edu//store/data/Run2012B/SinglePhoton/AOD/22Jan2013-v1/20000/0029D61A-FE71-E211-9B83-0026189438C0.root'
     'root://xrootd.unl.edu//store/data/Run2012C/DoublePhoton/AOD/22Jan2013-v2/20000/00156CC5-AF70-E211-A09E-0026189438EA.root'
    ),

    # explicitly drop photons resident in AOD/RECO, to make sure only those locally re-made (uncleaned photons) are used
    inputCommands = cms.untracked.vstring('keep *'
                                          #,'drop  *_photonCore_*_RECO' # drop hfRecoEcalCandidate as remade in this process
                                          #, 'drop *_photons_*_RECO' # drop photons as remade in this process
                                          )

)


#import EXO.DPAnalysis.skim2012c as fileList
#process.source.fileNames = fileList.fileNames

process.options   = cms.untracked.PSet(
                    wantSummary = cms.untracked.bool(True),  
                    SkipEvent = cms.untracked.vstring('ProductNotFound')
)   

process.load("FWCore.MessageService.MessageLogger_cfi")
process.MessageLogger.cerr.FwkReport.reportEvery = cms.untracked.int32(1000)

process.ana = cms.EDAnalyzer('DPAnalysis',
    rootFileName     = cms.untracked.string('Step1.root'),
    triggerName      = cms.vstring('HLT_DoublePhoton40_CaloIdL_Rsq0p035'),
    #triggerName      = cms.vstring('HLT_DisplacedPhoton65_CaloIdVL_IsoL_PFMET25'),
    #L1GTSource       = cms.string('L1_SingleEG22'),
    L1GTSource       = cms.string('L1_DoubleEG_13_7'),
    L1Select         = cms.bool( False ),
    isData           = cms.bool( True ),
    isRECO           = cms.bool( False ),
    cscHaloData      = cms.InputTag("CSCHaloData"),
    staMuons         = cms.InputTag("standAloneMuons"),
    addPileupInfo    = cms.InputTag("addPileupInfo"),
    muonSource  = cms.InputTag("muonsFromCosmics"),
    trigSource = cms.InputTag("TriggerResults","","HLT"),
    jetSource   = cms.InputTag("ak5PFJets"),
    patJetSource = cms.InputTag("selectedPatJetsPFlow"),
    metSource   = cms.InputTag("pfMet"),
    type1metSource   = cms.InputTag("pfType1CorrectedMet"),
    trackSource = cms.InputTag("generalTracks"),
    electronSource   = cms.InputTag("gsfElectrons"),
    photonSource     = cms.InputTag("myphotons"),
    pvSource         = cms.InputTag("offlinePrimaryVerticesWithBS"),
    beamSpotSource   = cms.InputTag("offlineBeamSpot"),
    EBRecHitCollection = cms.InputTag("reducedEcalRecHitsEB"),
    EERecHitCollection = cms.InputTag("reducedEcalRecHitsEE"),
    tau                = cms.double( 1000 ), 
    genParticles = cms.InputTag("genParticles"),

    #DTSegmentCollection = cms.InputTag("dt4DCosmicSegments"),
    #CSCSegmentCollection = cms.InputTag("cscSegments"),

    # Set up cuts for physics objects
    # vertex cuts                z   ndof   d0
    vtxCuts       = cms.vdouble( 99,    0,  99 ),
    # photon cuts                pt   eta  sMajMax,  sMinMin, sMinMax,   dR,  Num  leadingPt
    photonCuts    = cms.vdouble( 45,  2.4,     99.,      -1.,     99.,   0.0,  1,    45  ),
    # photon isolation           trkR,  ecalSumEt, ecalR, hcalSumEt, hcalR
    photonIso     = cms.vdouble(  1.,       5.0,   1.,       5.0,   1. ),
  #  photonIso     = cms.vdouble(  1000.,       1000.0,   1000.,       1000.0,   1000. ),
    # jet cuts                   pt    eta    dR,  nJets
    jetCuts       = cms.vdouble( 30. , 2.4,  0.3,    0 ),
    metCuts       = cms.vdouble( 0. ),
    # electron cuts              pt  eta  EBIso  EEIso nLostHit
    electronCuts  = cms.vdouble( 25, 2.4,  0.15,   0.1,      2 ),
    # muon cuts                  pt  eta  Iso  dR
    muonCuts      = cms.vdouble( 25, 2.1, 0.2, 0.3 ),
)

###########  USE UNCLEANED SUPERCLUSTERS  ######################### 
# Global Tag
process.load("Configuration.StandardSequences.FrontierConditions_GlobalTag_cff")
#process.load("Configuration.StandardSequences.FrontierConditions_GlobalTag_noesprefer_cff")
#process.GlobalTag.globaltag = 'GR_R_53_V18::All'
from Configuration.AlCa.GlobalTag import GlobalTag
process.GlobalTag = GlobalTag( process.GlobalTag, 'GR_R_53_V18::All' )


# to get clustering
process.load("Configuration.Geometry.GeometryIdeal_cff")
#process.load("Configuration.StandardSequences.Geometry_cff")
process.load('Configuration/StandardSequences/GeometryExtended_cff')

# Geometry
process.load("Geometry.CaloEventSetup.CaloTopology_cfi")
process.load("Geometry.CaloEventSetup.CaloGeometry_cff")
process.load("Geometry.CaloEventSetup.CaloGeometry_cfi")
process.load("Geometry.EcalMapping.EcalMapping_cfi")
process.load("Geometry.EcalMapping.EcalMappingRecord_cfi")
process.load("Geometry.MuonNumbering.muonNumberingInitialization_cfi") # gfwork: need this?


process.CaloTowerConstituentsMapBuilder = cms.ESProducer("CaloTowerConstituentsMapBuilder")

process.load("RecoEcal.EgammaClusterProducers.uncleanSCRecovery_cfi")
process.uncleanSCRecovered.cleanScCollection=cms.InputTag ("correctedHybridSuperClusters")

# myPhoton sequence
process.load("RecoEgamma.PhotonIdentification.photonId_cff")
process.load("RecoLocalCalo.EcalRecAlgos.EcalSeverityLevelESProducer_cfi")

process.load("Recommended2012Filters_cfi")

import RecoEgamma.EgammaPhotonProducers.photonCore_cfi
import RecoEgamma.EgammaPhotonProducers.photons_cfi

process.myphotonCores=RecoEgamma.EgammaPhotonProducers.photonCore_cfi.photonCore.clone()
process.myphotonCores.scHybridBarrelProducer=cms.InputTag ("uncleanSCRecovered:uncleanHybridSuperClusters")

from RecoEgamma.PhotonIdentification.mipVariable_cfi import *
newMipVariable = mipVariable.clone()
newMipVariable.barrelEcalRecHitCollection = cms.InputTag('reducedEcalRecHitsEB')
newMipVariable.endcapEcalRecHitCollection = cms.InputTag('reducedEcalRecHitsEE')

from RecoEgamma.PhotonIdentification.isolationCalculator_cfi import*
newisolationSumsCalculator = isolationSumsCalculator.clone()
newisolationSumsCalculator.barrelEcalRecHitCollection = cms.InputTag('reducedEcalRecHitsEB')
newisolationSumsCalculator.endcapEcalRecHitCollection = cms.InputTag('reducedEcalRecHitsEE')

process.myphotons=RecoEgamma.EgammaPhotonProducers.photons_cfi.photons.clone()
process.myphotons.barrelEcalHits=cms.InputTag("reducedEcalRecHitsEB")
process.myphotons.endcapEcalHits=cms.InputTag("reducedEcalRecHitsEE")
process.myphotons.isolationSumsCalculatorSet=newisolationSumsCalculator
process.myphotons.mipVariableSet = newMipVariable
process.myphotons.photonCoreProducer=cms.InputTag("myphotonCores")

process.myPhotonSequence = cms.Sequence(process.myphotonCores+
                                        process.myphotons)
# photonID sequence
from RecoEgamma.PhotonIdentification.photonId_cfi import *
process.myPhotonIDSequence = cms.Sequence(PhotonIDProd)
process.PhotonIDProd.photonProducer=cms.string("myphotons")

process.uncleanPhotons = cms.Sequence(
               process.uncleanSCRecovered *
               process.myPhotonSequence *
               process.myPhotonIDSequence
               )

# PFIso 
#from CommonTools.ParticleFlow.Tools.pfIsolation import setupPFElectronIso, setupPFPhotonIso
#process.phoIsoSequence = setupPFPhotonIso(process, 'photons')

# typeI MET correction 
process.load("JetMETCorrections.Type1MET.pfMETCorrections_cff")

# pat process

# conditions
process.load( "Configuration.Geometry.GeometryIdeal_cff" )
process.load( "Configuration.StandardSequences.MagneticField_AutoFromDBCurrent_cff" )

# load the PAT config
process.load("PhysicsTools.PatAlgos.patSequences_cff")

process.patElectrons.addGenMatch  = False
process.patJets.addGenPartonMatch = False
process.patJets.addGenJetMatch    = False
process.patMETs.addGenMET         = False
process.patMuons.addGenMatch      = False
process.patPhotons.addGenMatch    = False
process.patTaus.addGenMatch       = False
process.patTaus.addGenJetMatch    = False
process.patJetCorrFactors.levels.append( 'L2L3Residual' )

process.out = cms.OutputModule("PoolOutputModule" ,
                fileName = cms.untracked.string( 'patTuple_data.root' ) ,
		outputCommands = cms.untracked.vstring(
			'keep *'
			#               'keep *_cscSegments_*_*'
			#               *patEventContentNoCleaning
			)
																                 )


# this function will modify the PAT sequences.
from PhysicsTools.PatAlgos.tools.pfTools import *

postfix = "PFlow"

usePF2PAT( process
		, runPF2PAT = True
		, jetAlgo   = 'AK5'
		, runOnMC   = False
		, postfix   = postfix
		# for MC
		#, jetCorrections=('AK5PFchs', ['L1FastJet','L2Relative','L3Absolute'])
		# for data
		, jetCorrections=('AK5PFchs', ['L2L3Residual'])
	 )

process.primaryVertexFilter = cms.EDFilter(
        "VertexSelector",
            src = cms.InputTag("offlinePrimaryVertices"),
            cut = cms.string("!isFake && ndof > 4 && abs(z) <= 24 && position.Rho <= 2"),
            filter = cms.bool(True)
            )

 ## The beam scraping filter __________________________________________________||
process.noscraping = cms.EDFilter(
        "FilterOutScraping",
            applyfilter = cms.untracked.bool(True),
            debugOn = cms.untracked.bool(False),
            numtrack = cms.untracked.uint32(10),
            thresh = cms.untracked.double(0.25)
            )

 ## The iso-based HBHE noise filter ___________________________________________||
process.load('CommonTools.RecoAlgos.HBHENoiseFilter_cfi')

 ## The CSC beam halo tight filter ____________________________________________||
process.load('RecoMET.METAnalyzers.CSCHaloFilter_cfi')

 ## The HCAL laser filter _____________________________________________________||
process.load("RecoMET.METFilters.hcalLaserEventFilter_cfi")

 ## The ECAL dead cell trigger primitive filter _______________________________||
process.load('RecoMET.METFilters.EcalDeadCellTriggerPrimitiveFilter_cfi')

 ## The EE bad SuperCrystal filter ____________________________________________||
process.load('RecoMET.METFilters.eeBadScFilter_cfi')

 ## The ECAL laser correction filter
process.load('RecoMET.METFilters.ecalLaserCorrFilter_cfi')

 ## The Good vertices collection needed by the tracking failure filter ________||
process.goodVertices = cms.EDFilter(
      "VertexSelector",
        filter = cms.bool(False),
        src = cms.InputTag("offlinePrimaryVertices"),
        cut = cms.string("!isFake && ndof > 4 && abs(z) <= 24 && position.rho < 2")
      )

 ## The tracking failure filter _______________________________________________||
process.load('RecoMET.METFilters.trackingFailureFilter_cfi')

 ## The tracking POG filters __________________________________________________||
process.load('RecoMET.METFilters.trackingPOGFilters_cff')
## NOTE: to make tagging mode of the tracking POG filters (three of them), please do:
##    process.manystripclus53X.taggedMode = cms.untracked.bool(True)
##    process.manystripclus53X.forcedValue = cms.untracked.bool(False)
##    process.toomanystripclus53X.taggedMode = cms.untracked.bool(True)
##    process.toomanystripclus53X.forcedValue = cms.untracked.bool(False)
##    process.logErrorTooManyClusters.taggedMode = cms.untracked.bool(True)
##    process.logErrorTooManyClusters.forcedValue = cms.untracked.bool(False)
## Also the stored boolean for the three filters is opposite to what we usually
## have for other filters, i.e., true means rejected bad events while false means
## good events.

process.filtersSeq = cms.Sequence(
    process.primaryVertexFilter *
    process.noscraping *
    process.HBHENoiseFilter *
    process.CSCTightHaloFilter *
    process.hcalLaserEventFilter *
    process.EcalDeadCellTriggerPrimitiveFilter *
    process.goodVertices * process.trackingFailureFilter *
    process.eeBadScFilter *
    process.ecalLaserCorrFilter *
    process.trkPOGFilters
    )

process.p = cms.Path(
                     process.filtersSeq *
                     process.uncleanPhotons*
		     getattr(process,"patPF2PATSequence"+postfix)*
                     process.producePFMETCorrections *
                     process.ana
                    )

# top projections in PF2PAT:
getattr(process,"pfNoPileUp"+postfix).enable = True
getattr(process,"pfNoMuon"+postfix).enable = True
getattr(process,"pfNoElectron"+postfix).enable = True
getattr(process,"pfNoTau"+postfix).enable = False
getattr(process,"pfNoJet"+postfix).enable = True

# verbose flags for the PF2PAT modules
getattr(process,"pfNoMuon"+postfix).verbose = False

# enable delta beta correction for muon selection in PF2PAT?
getattr(process,"pfIsolatedMuons"+postfix).doDeltaBetaCorrection = False

process.out.outputCommands.extend( [ 'drop *_*_*_*' ] )

