# Auto generated configuration file
# using: 
# Revision: 1.19 
# Source: /local/reps/CMSSW/CMSSW/Configuration/Applications/python/ConfigBuilder.py,v 
# with command line options: step1 --filein dbs:/SingletopWprime_M2700GeV_right_Tune4C_13TeV-comphep/Fall13-POSTLS162_V1-v1/GEN-SIM --fileout file:B2G-Spring14dr-00115_step1.root --pileup_input dbs:/MinBias_TuneA2MB_13TeV-pythia8/Fall13-POSTLS162_V1-v1/GEN-SIM --mc --eventcontent FEVTDEBUG --pileup AVE_20_BX_25ns --customise SLHCUpgradeSimulations/Configuration/postLS1Customs.customisePostLS1,Configuration/DataProcessing/Utils.addMonitoring --datatier GEN-SIM-DIGI-RAW-HLT --conditions POSTLS170_V5::All --step DIGI,L1,DIGI2RAW,HLT:User,RAW2DIGI,L1Reco --magField 38T_PostLS1 --geometry DBExtendedPostLS1 --python_filename B2G-Spring14dr-00115_1_cfg.py --no_exec -n 73
import FWCore.ParameterSet.Config as cms

process = cms.Process('HLT')

# import of standard configurations
process.load('Configuration.StandardSequences.Services_cff')
process.load('SimGeneral.HepPDTESSource.pythiapdt_cfi')
process.load('FWCore.MessageService.MessageLogger_cfi')
process.load('Configuration.EventContent.EventContent_cff')
process.load('SimGeneral.MixingModule.mix_POISSON_average_cfi')
process.load('Configuration.StandardSequences.GeometryRecoDB_cff')
process.load('Configuration.StandardSequences.MagneticField_38T_PostLS1_cff')
process.load('Configuration.StandardSequences.Digi_cff')
process.load('Configuration.StandardSequences.SimL1Emulator_cff')
process.load('Configuration.StandardSequences.DigiToRaw_cff')
process.load('HLTrigger.Configuration.HLT_User_cff')
process.load('Configuration.StandardSequences.RawToDigi_cff')
process.load('Configuration.StandardSequences.L1Reco_cff')
process.load('Configuration.StandardSequences.EndOfProcess_cff')
#process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_condDBv2_cff')
process.load("Configuration.StandardSequences.FrontierConditions_GlobalTag_cff")
process.load('CondCore.DBCommon.CondDBSetup_cfi')

process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(-1)
)

# Input source
process.source = cms.Source("PoolSource",
    secondaryFileNames = cms.untracked.vstring(),
    fileNames = cms.untracked.vstring('file:localfilelocation')
)

process.options = cms.untracked.PSet(

)

# Production Info
process.configurationMetadata = cms.untracked.PSet(
    version = cms.untracked.string('$Revision: 1.19 $'),
    annotation = cms.untracked.string('step1 nevts:73'),
    name = cms.untracked.string('Applications')
)

from SLHCUpgradeSimulations.Configuration.postLS1Customs import *
process = customise_HLT( process )

# Output definition

process.FEVTDEBUGoutput = cms.OutputModule("PoolOutputModule",
    splitLevel = cms.untracked.int32(0),
    eventAutoFlushCompressedSize = cms.untracked.int32(5242880),
    outputCommands = process.FEVTDEBUGEventContent.outputCommands,
    fileName = cms.untracked.string('file:outputfilelocation'),
    dataset = cms.untracked.PSet(
        filterName = cms.untracked.string(''),
        dataTier = cms.untracked.string('GEN-SIM-DIGI-RAW-HLT')
    )
)

# Additional output definition

# Other statements
process.mix.input.nbPileupEvents.averageNumber = cms.double(20.000000)
process.mix.bunchspace = cms.int32(25)
process.mix.minBunch = cms.int32(-12)
process.mix.maxBunch = cms.int32(3)
process.mix.input.fileNames = cms.untracked.vstring(
'/store/mc/Fall13/MinBias_TuneA2MB_13TeV-pythia8/GEN-SIM/POSTLS162_V1-v1/20000/0E0254B5-5E25-E311-9C87-0026B93F4A37.root',
'/store/mc/Fall13/MinBias_TuneA2MB_13TeV-pythia8/GEN-SIM/POSTLS162_V1-v1/20000/148F0A95-5D25-E311-BED9-00145EDD77B9.root',
'/store/mc/Fall13/MinBias_TuneA2MB_13TeV-pythia8/GEN-SIM/POSTLS162_V1-v1/20000/181B59DC-5F25-E311-BB40-00A0D1EE2F94.root',
'/store/mc/Fall13/MinBias_TuneA2MB_13TeV-pythia8/GEN-SIM/POSTLS162_V1-v1/20000/2AC5C69B-5D25-E311-8D9F-00145EFB6930.root',
'/store/mc/Fall13/MinBias_TuneA2MB_13TeV-pythia8/GEN-SIM/POSTLS162_V1-v1/20000/32C1CE11-5E25-E311-BB5E-00266CF830FC.root',
'/store/mc/Fall13/MinBias_TuneA2MB_13TeV-pythia8/GEN-SIM/POSTLS162_V1-v1/20000/365DB59A-5D25-E311-B050-00145EDD76FD.root',
'/store/mc/Fall13/MinBias_TuneA2MB_13TeV-pythia8/GEN-SIM/POSTLS162_V1-v1/20000/42FBB09A-5D25-E311-9B77-00145EDD784D.root',
'/store/mc/Fall13/MinBias_TuneA2MB_13TeV-pythia8/GEN-SIM/POSTLS162_V1-v1/20000/4A40B231-5F25-E311-9EEF-7845C4FC3C8C.root',
'/store/mc/Fall13/MinBias_TuneA2MB_13TeV-pythia8/GEN-SIM/POSTLS162_V1-v1/20000/4AE67893-5E25-E311-A288-00266CF89604.root',
'/store/mc/Fall13/MinBias_TuneA2MB_13TeV-pythia8/GEN-SIM/POSTLS162_V1-v1/20000/523F35DF-5E25-E311-9905-00145EDD7355.root',
'/store/mc/Fall13/MinBias_TuneA2MB_13TeV-pythia8/GEN-SIM/POSTLS162_V1-v1/20000/5661CB97-5D25-E311-8E4D-000AE488B8B8.root',
'/store/mc/Fall13/MinBias_TuneA2MB_13TeV-pythia8/GEN-SIM/POSTLS162_V1-v1/20000/58191637-5F25-E311-B5AB-00145EDD732D.root',
'/store/mc/Fall13/MinBias_TuneA2MB_13TeV-pythia8/GEN-SIM/POSTLS162_V1-v1/20000/82ED44EC-5E25-E311-800C-00145EDD7635.root',
'/store/mc/Fall13/MinBias_TuneA2MB_13TeV-pythia8/GEN-SIM/POSTLS162_V1-v1/20000/863450AA-5E25-E311-B90F-00145EDD72F1.root',
'/store/mc/Fall13/MinBias_TuneA2MB_13TeV-pythia8/GEN-SIM/POSTLS162_V1-v1/20000/A02DB1B8-5E25-E311-BA1D-00145EFB6930.root',
'/store/mc/Fall13/MinBias_TuneA2MB_13TeV-pythia8/GEN-SIM/POSTLS162_V1-v1/20000/A283B485-5E25-E311-BDB9-000AE488B8B8.root',
'/store/mc/Fall13/MinBias_TuneA2MB_13TeV-pythia8/GEN-SIM/POSTLS162_V1-v1/20000/A8DDF385-5F25-E311-81A1-000AE488B8B8.root',
'/store/mc/Fall13/MinBias_TuneA2MB_13TeV-pythia8/GEN-SIM/POSTLS162_V1-v1/20000/B4B834BA-5D25-E311-B320-0026B93F4A37.root',
'/store/mc/Fall13/MinBias_TuneA2MB_13TeV-pythia8/GEN-SIM/POSTLS162_V1-v1/20000/C69214B1-5E25-E311-B2F8-00145EDD77B9.root',
'/store/mc/Fall13/MinBias_TuneA2MB_13TeV-pythia8/GEN-SIM/POSTLS162_V1-v1/20000/C6DB31DD-5D25-E311-9A64-00145EDD732D.root',
'/store/mc/Fall13/MinBias_TuneA2MB_13TeV-pythia8/GEN-SIM/POSTLS162_V1-v1/20000/CC8E57F9-5D25-E311-BBD1-00145EDD7881.root',
'/store/mc/Fall13/MinBias_TuneA2MB_13TeV-pythia8/GEN-SIM/POSTLS162_V1-v1/20000/CE2A233F-5E25-E311-A248-7845C4FC3C8C.root',
'/store/mc/Fall13/MinBias_TuneA2MB_13TeV-pythia8/GEN-SIM/POSTLS162_V1-v1/20000/F0BA29B8-5E25-E311-BBE3-00145EDD740F.root',
'/store/mc/Fall13/MinBias_TuneA2MB_13TeV-pythia8/GEN-SIM/POSTLS162_V1-v1/20000/F265F6AD-5D25-E311-B2DC-00145EDD7759.root'
)
#from Configuration.AlCa.GlobalTag_condDBv2 import GlobalTag
#process.GlobalTag = GlobalTag(process.GlobalTag, 'POSTLS170_V5::All', '')

process.GlobalTag.globaltag= 'PRE_LS172_V16::All'

#process.GlobalTag.globaltag = 'POSTLS170_V5::All'

# Path and EndPath definitions
process.digitisation_step = cms.Path(process.pdigi)
process.L1simulation_step = cms.Path(process.SimL1Emulator)
process.digi2raw_step = cms.Path(process.DigiToRaw)
process.HLT_AK8PFJet300TrimMod_Mass30_AK4PFJet250_v1 = cms.Path(process.HLTBeginSequence+process.hltL1sL1SingleJet176+process.hltPreAK8PFJet300TrimModMass30AK4PFJet250+process.HLTAK8CaloJetsSequence+process.hltAK8SingleCaloJet240+process.HLTAK8PFJetsSequence+process.hltAK8PFJetsCorrectedMatchedToCaloJets240+process.hltAK8TrimModJets+process.hltAK8SinglePFJet300TrimModMass30+process.HLTAK4PFJetsSequence+process.hltAK4DiPFJet250+process.HLTEndSequence)
process.HLT_AK8PFJet300TrimMod_Mass30_AK4PFJet200_v1 = cms.Path(process.HLTBeginSequence+process.hltL1sL1SingleJet176+process.hltPreAK8PFJet300TrimModMass30AK4PFJet200+process.HLTAK8CaloJetsSequence+process.hltAK8SingleCaloJet240+process.HLTAK8PFJetsSequence+process.hltAK8PFJetsCorrectedMatchedToCaloJets240+process.hltAK8TrimModJets+process.hltAK8SinglePFJet300TrimModMass30+process.HLTAK4PFJetsSequence+process.hltAK4DiPFJet200+process.HLTEndSequence)
process.HLT_IsoMu24_IterTrk02_TriCentralPFJet40_v1 = cms.Path(process.HLTBeginSequence+process.hltL1sL1SingleMu16+process.hltPreIsoMu24IterTrk02TriCentralPFJet40+process.hltL1fL1sMu16L1Filtered0+process.HLTL2muonrecoSequence+process.hltL2fL1sMu16L1f0L2Filtered16Q+process.HLTL3muonrecoSequence+process.hltL3fL1sMu16L1f0L2f16QL3Filtered24Q+process.HLTL3muoncaloisorecoSequenceNoBools+process.HLTTrackReconstructionForIsoL3MuonIter02+process.hltL3crIsoL1sMu16L1f0L2f16QL3f24QL3crIsoRhoFiltered0p15IterTrk02+process.HLTAK4PFJetsSequence+process.hltIsoMu24Trk02JetCollectionsForLeptonPlusPFJets+process.hltIsoMu24Trk02TriCentralPFJet40MuCleaned+process.HLTEndSequence)
process.HLT_AK8DiPFJet300_200TrimMod_Mass30_InvMass400_v1 = cms.Path(process.HLTBeginSequence+process.hltL1sL1SingleJet176+process.hltPreAK8DiPFJet300200TrimModMass30InvMass400+process.HLTAK8CaloJetsSequence+process.hltAK8SingleCaloJet240+process.HLTAK8PFJetsSequence+process.hltAK8PFJetsCorrectedMatchedToCaloJets240+process.hltAK8TrimModJets+process.hltAK8DiPFJet200TrimMod+process.hltAK8SinglePFJet300TrimModMass30+process.hltAK8DiPFJet200TrimModMinv400+process.HLTEndSequence)
process.HLT_AK8PFJet280TrimMod_Mass30_AK4PFJet250_v1 = cms.Path(process.HLTBeginSequence+process.hltL1sL1SingleJet176+process.hltPreAK8PFJet280TrimModMass30AK4PFJet250+process.HLTAK8CaloJetsSequence+process.hltAK8SingleCaloJet240+process.HLTAK8PFJetsSequence+process.hltAK8PFJetsCorrectedMatchedToCaloJets240+process.hltAK8TrimModJets+process.hltAK8SinglePFJet280TrimModMass30+process.HLTAK4PFJetsSequence+process.hltAK4DiPFJet250+process.HLTEndSequence)
process.HLT_Ele27_eta2p1_WP85_Gsf_TriCentralPFJet60_50_35_v1 = cms.Path(process.HLTBeginSequence+process.hltL1sL1SingleIsoEG25er+process.hltPreEle27eta2p1WP85GsfTriCentralPFJet605035+process.HLTEle27erWP85GsfSequence+process.HLTAK4PFJetsSequence+process.hltEle27JetCollectionsForLeptonPlusPFJets+process.hltEle27TriCentralPFJet35EleCleaned+process.hltEle27DiCentralPFJet50EleCleaned+process.hltEle27CentralPFJet60EleCleaned+process.HLTEndSequence)
process.HLT_AK8DiPFJet300_200TrimMod_DiMass30_v1 = cms.Path(process.HLTBeginSequence+process.hltL1sL1SingleJet176+process.hltPreAK8DiPFJet300200TrimModDiMass30+process.HLTAK8CaloJetsSequence+process.hltAK8SingleCaloJet240+process.HLTAK8PFJetsSequence+process.hltAK8PFJetsCorrectedMatchedToCaloJets240+process.hltAK8TrimModJets+process.hltAK8DiPFJet200TrimModMass30+process.hltAK8SinglePFJet300TrimModMass30+process.HLTEndSequence)
process.HLT_PFHT350_PFMET120_NoiseCleaned_v1 = cms.Path(process.HLTBeginSequence+process.hltL1sL1HTT150+process.hltPrePFHT350PFMET120NoiseCleaned+process.HLTRecoMETSequence+process.hltMET70+process.HLTHBHENoiseCleanerSequence+process.hltMetClean+process.hltMETClean60+process.HLTAK4CaloJetsSequence+process.hltMetCleanUsingJetID+process.hltMETCleanUsingJetID60+process.hltHtMht+process.hltHt280+process.HLTAK4PFJetsSequence+process.hltPFMETProducer+process.hltPFMET120Filter+process.hltPFHT+process.hltPFHT350+process.HLTEndSequence)
process.HLT_FatDiPFJetMass850_DR1p1_Deta1p5_v1 = cms.Path(process.HLTBeginSequence+process.hltL1sL1HTT175+process.hltPreFatDiPFJetMass850DR1p1Deta1p5+process.HLTAK4CaloJetsSequence+process.hltHtMht+process.hltHt550+process.HLTAK4PFJetsSequence+process.hltDiCentralPFJet30+process.hltFatDiPFJetMass850DR1p1Deta1p5+process.HLTEndSequence)
process.HLT_AK8DiPFJet280_250TrimMod_Dphi1p5_Mass30_v1 = cms.Path(process.HLTBeginSequence+process.hltL1sL1SingleJet176+process.hltPreAK8DiPFJet280250TrimModDphi1p5Mass30+process.HLTAK8CaloJetsSequence+process.hltAK8SingleCaloJet240+process.HLTAK8PFJetsSequence+process.hltAK8PFJetsCorrectedMatchedToCaloJets240+process.hltAK8TrimModJets+process.hltAK8DiPFJet250TrimMod+process.hltAK8DiPFJet250TrimModDphi1p5+process.hltAK8SinglePFJet280TrimModMass30+process.HLTEndSequence)
process.HLT_FatDiPFJetMass750_DR1p1_Deta1p5_v1 = cms.Path(process.HLTBeginSequence+process.hltL1sL1HTT175+process.hltPreAK8DiPFJetTrimModMass750Deta1p5+process.HLTAK4CaloJetsSequence+process.hltHtMht+process.hltHt550+process.HLTAK4PFJetsSequence+process.hltDiCentralPFJet30+process.hltFatDiPFJetMass750DR1p1Deta1p5+process.HLTEndSequence)
process.HLT_AK8PFJet360TrimMod_Mass30_v1 = cms.Path(process.HLTBeginSequence+process.hltL1sL1SingleJet176+process.hltPreAK8PFJet360TrimModMass30+process.HLTAK8CaloJetsSequence+process.hltAK8SingleCaloJet260+process.HLTAK8PFJetsSequence+process.hltAK8PFJetsCorrectedMatchedToCaloJets260+process.hltAK8TrimModJets+process.hltAK8SinglePFJet360TrimModMass30+process.HLTEndSequence)
process.HLT_AK8DiPFJet300_200TrimMod_Mass30_v1 = cms.Path(process.HLTBeginSequence+process.hltL1sL1SingleJet176+process.hltPreAK8DiPFJet300200TrimModMass30+process.HLTAK8CaloJetsSequence+process.hltAK8SingleCaloJet240+process.HLTAK8PFJetsSequence+process.hltAK8PFJetsCorrectedMatchedToCaloJets240+process.hltAK8TrimModJets+process.hltAK8DiPFJet200TrimMod+process.hltAK8SinglePFJet300TrimModMass30+process.HLTEndSequence)
process.HLT_AK8DiPFJet300_250TrimMod_Dphi1p5_Mass30_v1 = cms.Path(process.HLTBeginSequence+process.hltL1sL1SingleJet176+process.hltPreAK8DiPFJet300250TrimModDphi1p5Mass30+process.HLTAK8CaloJetsSequence+process.hltAK8SingleCaloJet240+process.HLTAK8PFJetsSequence+process.hltAK8PFJetsCorrectedMatchedToCaloJets240+process.hltAK8TrimModJets+process.hltAK8DiPFJet250TrimMod+process.hltAK8DiPFJet250TrimModDphi1p5+process.hltAK8SinglePFJet300TrimModMass30+process.HLTEndSequence)
process.HLT_Ele27_eta2p1_WP85_Gsf_TriCentralPFJet40_v1 = cms.Path(process.HLTBeginSequence+process.hltL1sL1SingleIsoEG25er+process.hltPreEle27eta2p1WP85GsfTriCentralPFJet40+process.HLTEle27erWP85GsfSequence+process.HLTAK4PFJetsSequence+process.hltEle27JetCollectionsForLeptonPlusPFJets+process.hltEle27TriCentralPFJet40EleCleaned+process.HLTEndSequence)
process.HLT_AK8DiPFJet300_200TrimMod_Dphi1p5_Mass30_v1 = cms.Path(process.HLTBeginSequence+process.hltL1sL1SingleJet176+process.hltPreAK8DiPFJet300200TrimModDphi1p5Mass30+process.HLTAK8CaloJetsSequence+process.hltAK8SingleCaloJet240+process.HLTAK8PFJetsSequence+process.hltAK8PFJetsCorrectedMatchedToCaloJets240+process.hltAK8TrimModJets+process.hltAK8DiPFJet200TrimMod+process.hltAK8DiPFJet200TrimModDphi1p5+process.hltAK8SinglePFJet300TrimModMass30+process.HLTEndSequence)
process.HLT_AK8DiPFJet280_250TrimMod_DiMass30_v1 = cms.Path(process.HLTBeginSequence+process.hltL1sL1SingleJet176+process.hltPreAK8DiPFJet280250TrimModDiMass30+process.HLTAK8CaloJetsSequence+process.hltAK8SingleCaloJet240+process.HLTAK8PFJetsSequence+process.hltAK8PFJetsCorrectedMatchedToCaloJets240+process.hltAK8TrimModJets+process.hltAK8DiPFJet250TrimModMass30+process.hltAK8SinglePFJet280TrimModMass30+process.HLTEndSequence)
process.HLT_AK8DiPFJet320_280TrimMod_Mass30_v1 = cms.Path(process.HLTBeginSequence+process.hltL1sL1SingleJet176+process.hltPreAK8DiPFJet320280TrimModMass30+process.HLTAK8CaloJetsSequence+process.hltAK8SingleCaloJet240+process.HLTAK8PFJetsSequence+process.hltAK8PFJetsCorrectedMatchedToCaloJets240+process.hltAK8TrimModJets+process.hltAK8DiPFJet280TrimMod+process.hltAK8SinglePFJet320TrimModMass30+process.HLTEndSequence)
process.HLT_AK8DiPFJet280_250TrimMod_Mass30_v1 = cms.Path(process.HLTBeginSequence+process.hltL1sL1SingleJet176+process.hltPreAK8DiPFJet280250TrimModMass30+process.HLTAK8CaloJetsSequence+process.hltAK8SingleCaloJet240+process.HLTAK8PFJetsSequence+process.hltAK8PFJetsCorrectedMatchedToCaloJets240+process.hltAK8TrimModJets+process.hltAK8DiPFJet250TrimMod+process.hltAK8SinglePFJet280TrimModMass30+process.HLTEndSequence)
process.HLT_Ele45_CaloIdVT_GsfTrkIdT_PFJet200_PFJet50_v1 = cms.Path(process.HLTBeginSequence+process.hltL1sL1SingleEG35+process.hltPreEle45CaloIdVTGsfTrkIdTPFJet200PFJet50+process.HLTEle45CaloIdVTGsfTrkIdTGsfSequence+process.HLTAK4PFJetsSequence+process.hltPFJetsCorrectedMatchedToL1+process.hltDiPFJet50+process.hltEle45CaloIdVTGsfTrkIdTCleanAK4PFJet+process.hltEle45CaloIdVTGsfTrkIdTDiCentralPFJet50EleCleaned+process.hltEle45CaloIdVTGsfTrkIdTCentralPFJet200EleCleaned+process.HLTEndSequence)
process.HLT_AK8DiPFJet280_250TrimMod_Mass30_InvMass400_v1 = cms.Path(process.HLTBeginSequence+process.hltL1sL1SingleJet176+process.hltPreHLTAK8DiPFJet280250TrimModMass30InvMass400+process.HLTAK8CaloJetsSequence+process.hltAK8SingleCaloJet240+process.HLTAK8PFJetsSequence+process.hltAK8PFJetsCorrectedMatchedToCaloJets240+process.hltAK8TrimModJets+process.hltAK8DiPFJet250TrimMod+process.hltAK8SinglePFJet280TrimModMass30+process.hltAK8DiPFJet250TrimModMinv400+process.HLTEndSequence)
process.HLT_IsoMu24_IterTrk02_TriCentralPFJet60_50_35_v1 = cms.Path(process.HLTBeginSequence+process.hltL1sL1SingleMu16+process.hltPreIsoMu24IterTrk02TriCentralPFJet605035+process.hltL1fL1sMu16L1Filtered0+process.HLTL2muonrecoSequence+process.hltL2fL1sMu16L1f0L2Filtered16Q+process.HLTL3muonrecoSequence+process.hltL3fL1sMu16L1f0L2f16QL3Filtered24Q+process.HLTL3muoncaloisorecoSequenceNoBools+process.HLTTrackReconstructionForIsoL3MuonIter02+process.hltL3crIsoL1sMu16L1f0L2f16QL3f24QL3crIsoRhoFiltered0p15IterTrk02+process.HLTAK4PFJetsSequence+process.hltIsoMu24Trk02JetCollectionsForLeptonPlusPFJets+process.hltIsoMu24Trk02TriCentralPFJet35MuCleaned+process.hltIsoMu24Trk02DiCentralPFJet50MuCleaned+process.hltIsoMu24Trk02CentralPFJet60MuCleaned+process.HLTEndSequence)
process.HLT_PFHT900_v1 = cms.Path(process.HLTBeginSequence+process.hltL1sL1HTT175+process.hltPrePFHT900+process.HLTAK4CaloJetsSequence+process.hltHtMht+process.hltHt700+process.HLTAK4PFJetsSequence+process.hltPFHT+process.hltPFHT900+process.HLTEndSequence)
process.HLT_FatDiPFJetTrimModMass750_DR1p1_Deta1p5_v1 = cms.Path(process.HLTBeginSequence+process.hltL1sL1HTT175+process.hltPreFatDiPFJetTrimModMass750DR1p1Deta1p5+process.HLTAK4CaloJetsSequence+process.hltHtMht+process.hltHt550+process.HLTAK8PFJetsSequence+process.hltAK8TrimModJets+process.hltDiCentralPFJet30TrimMod+process.hltFatDiPFJetTrimModMass750DR1p1Deta1p5+process.HLTEndSequence)
process.HLT_AK8DiPFJetAve300TrimMod_Mass30_v1 = cms.Path(process.HLTBeginSequence+process.hltL1sL1SingleJet176+process.hltPreAK8DiPFJetAve300TrimModMass30+process.HLTAK8CaloJetsSequence+process.hltAK8SingleCaloJet240+process.HLTAK8PFJetsSequence+process.hltAK8PFJetsCorrectedMatchedToCaloJets240+process.hltAK8TrimModJets+process.hltAK8SinglePFJet320TrimModMass30+process.hltDiPFJetAve300TrimMod+process.HLTEndSequence)
process.HLT_AK8PFHT850_TrimR0p1PT0p03Mass50_v1 = cms.Path(process.HLTBeginSequence+process.hltL1sL1HTT175+process.hltPreAK8PFHT850TrimR0p1PT0p03Mass50+process.HLTAK8CaloJetsSequence+process.hltAK8HtMht+process.hltAK8Ht750+process.HLTAK8PFJetsSequence+process.hltAK8PFHT+process.hltAK8PFJetsTrimR0p1PT0p03+process.hlt1AK8PFJetsTrimR0p1PT0p03Mass50+process.hltAK8PFHT850+process.HLTEndSequence)
process.HLT_Mu40_eta2p1_PFJet200_PFJet50_v1 = cms.Path(process.HLTBeginSequence+process.hltL1sL1SingleMu16+process.hltPreMu40eta2p1PFJet200PFJet50+process.hltL1fL1sMu16Eta2p1L1Filtered0+process.HLTL2muonrecoSequence+process.hltL2fL1sMu16Eta2p1L1f0L2Filtered16Q+process.HLTL3muonrecoSequence+process.hltL3fL1sMu16Eta2p1L1f0L2f16QL3Filtered40Q+process.HLTAK4PFJetsSequence+process.hltPFJetsCorrectedMatchedToL1+process.hltMu40eta2p1CleanAK4PFJet+process.hltMu40eta2p1DiCentralPFJet50MuCleaned+process.hltMu40eta2p1CentralPFJet200MuCleaned+process.HLTEndSequence)
process.HLT_AK8DiPFJet300_250TrimMod_Mass30_v1 = cms.Path(process.HLTBeginSequence+process.hltL1sL1SingleJet176+process.hltPreAK8DiPFJet300250TrimModMass30+process.HLTAK8CaloJetsSequence+process.hltAK8SingleCaloJet240+process.HLTAK8PFJetsSequence+process.hltAK8PFJetsCorrectedMatchedToCaloJets240+process.hltAK8TrimModJets+process.hltAK8DiPFJet250TrimMod+process.hltAK8SinglePFJet300TrimModMass30+process.HLTEndSequence)
process.HLT_AK8DiPFJet300_250TrimMod_Mass30_InvMass400_v1 = cms.Path(process.HLTBeginSequence+process.hltL1sL1SingleJet176+process.hltPreHLTAK8DiPFJet300250TrimModMass30InvMass400+process.HLTAK8CaloJetsSequence+process.hltAK8SingleCaloJet240+process.HLTAK8PFJetsSequence+process.hltAK8PFJetsCorrectedMatchedToCaloJets240+process.hltAK8TrimModJets+process.hltAK8DiPFJet250TrimMod+process.hltAK8SinglePFJet300TrimModMass30+process.hltAK8DiPFJet250TrimModMinv400+process.HLTEndSequence)
process.HLT_AK8DiPFJet300_250TrimMod_DiMass30_v1 = cms.Path(process.HLTBeginSequence+process.hltL1sL1SingleJet176+process.hltPreAK8DiPFJet300250TrimModDiMass30+process.HLTAK8CaloJetsSequence+process.hltAK8SingleCaloJet240+process.HLTAK8PFJetsSequence+process.hltAK8PFJetsCorrectedMatchedToCaloJets240+process.hltAK8TrimModJets+process.hltAK8DiPFJet250TrimModMass30+process.hltAK8SinglePFJet300TrimModMass30+process.HLTEndSequence)
process.HLT_AK8DiPFJetTrimMod_Mass750_Deta1p5_v1 = cms.Path(process.HLTBeginSequence+process.hltL1sL1HTT175+process.hltPreAK8DiPFJetTrimModMass750Deta1p5+process.HLTAK4CaloJetsSequence+process.hltHtMht+process.hltHt550+process.HLTAK8PFJetsSequence+process.hltAK8TrimModJets+process.hltDiCentralPFJet30TrimMod+process.hltAK8DiPFJetTrimModMinv750Deta1p5+process.HLTEndSequence)
process.raw2digi_step = cms.Path(process.RawToDigi)
process.L1Reco_step = cms.Path(process.L1Reco)
process.endjob_step = cms.EndPath(process.endOfProcess)
process.FEVTDEBUGoutput_step = cms.EndPath(process.FEVTDEBUGoutput)

# Schedule definition
process.schedule = cms.Schedule(process.digitisation_step,process.L1simulation_step,process.digi2raw_step)
process.schedule.extend(process.HLTSchedule)
process.schedule.extend([process.raw2digi_step,process.L1Reco_step,process.endjob_step,process.FEVTDEBUGoutput_step])

# customisation of the process.

# Automatic addition of the customisation function from HLTrigger.Configuration.customizeHLTforMC
from HLTrigger.Configuration.customizeHLTforMC import customizeHLTforMC 

#call to customisation function customizeHLTforMC imported from HLTrigger.Configuration.customizeHLTforMC
process = customizeHLTforMC(process)

# Automatic addition of the customisation function from Configuration.DataProcessing.Utils
from Configuration.DataProcessing.Utils import addMonitoring 

#call to customisation function addMonitoring imported from Configuration.DataProcessing.Utils
process = addMonitoring(process)

# Automatic addition of the customisation function from SLHCUpgradeSimulations.Configuration.postLS1Customs
from SLHCUpgradeSimulations.Configuration.postLS1Customs import customisePostLS1 

#call to customisation function customisePostLS1 imported from SLHCUpgradeSimulations.Configuration.postLS1Customs
process = customisePostLS1(process)

# End of customisation functions

