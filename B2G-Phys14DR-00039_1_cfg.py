# Auto generated configuration file
# using: 
# Revision: 1.19 
# Source: /local/reps/CMSSW/CMSSW/Configuration/Applications/python/ConfigBuilder.py,v 
# with command line options: step1 --filein dbs:/TprimeTprime_M_1000_Tune4C_13TeV-madgraph/Phys14DR-PU20bx25_PHYS14_25_V1-v1/GEN-SIM-RAW --fileout file:B2G-Phys14DR-00039_step1.root --pileup_input dbs:/MinBias_TuneA2MB_13TeV-pythia8/Fall13-POSTLS162_V1-v1/GEN-SIM --mc --eventcontent RAWSIM --inputEventContent REGEN --pileup AVE_20_BX_25ns --customise SLHCUpgradeSimulations/Configuration/postLS1Customs.customisePostLS1,Configuration/DataProcessing/Utils.addMonitoring --datatier GEN-SIM-RAW --conditions PHYS14_25_V2 --step DIGI,L1,DIGI2RAW,HLT:User --magField 38T_PostLS1 --python_filename B2G-Phys14DR-00039_1_cfg.py --processName=HLT2 --no_exec -n 3
import FWCore.ParameterSet.Config as cms

process = cms.Process('HLT2')

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
process.load('Configuration.StandardSequences.EndOfProcess_cff')
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_condDBv2_cff')

process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(3)
)

# Input source
process.source = cms.Source("PoolSource",
    secondaryFileNames = cms.untracked.vstring(),
    fileNames = cms.untracked.vstring('/store/mc/Phys14DR/TprimeTprime_M_1000_Tune4C_13TeV-madgraph/GEN-SIM-RAW/PU20bx25_PHYS14_25_V1-v1/00000/00236237-FB66-E411-9F51-485B39800BF2.root', 
        '/store/mc/Phys14DR/TprimeTprime_M_1000_Tune4C_13TeV-madgraph/GEN-SIM-RAW/PU20bx25_PHYS14_25_V1-v1/00000/026EDAA9-E166-E411-8FDC-002590D0B00C.root', 
        '/store/mc/Phys14DR/TprimeTprime_M_1000_Tune4C_13TeV-madgraph/GEN-SIM-RAW/PU20bx25_PHYS14_25_V1-v1/00000/02DF97F6-F766-E411-A680-E0CB4E29C4D8.root', 
        '/store/mc/Phys14DR/TprimeTprime_M_1000_Tune4C_13TeV-madgraph/GEN-SIM-RAW/PU20bx25_PHYS14_25_V1-v1/00000/0421B8A8-E166-E411-B4CB-002590D0AFC8.root', 
        '/store/mc/Phys14DR/TprimeTprime_M_1000_Tune4C_13TeV-madgraph/GEN-SIM-RAW/PU20bx25_PHYS14_25_V1-v1/00000/042F974A-EE66-E411-821E-20CF3027A5DC.root', 
        '/store/mc/Phys14DR/TprimeTprime_M_1000_Tune4C_13TeV-madgraph/GEN-SIM-RAW/PU20bx25_PHYS14_25_V1-v1/00000/043751A9-E166-E411-87D2-0025905280BE.root', 
        '/store/mc/Phys14DR/TprimeTprime_M_1000_Tune4C_13TeV-madgraph/GEN-SIM-RAW/PU20bx25_PHYS14_25_V1-v1/00000/0A1688B0-E166-E411-A274-00259074AE7A.root', 
        '/store/mc/Phys14DR/TprimeTprime_M_1000_Tune4C_13TeV-madgraph/GEN-SIM-RAW/PU20bx25_PHYS14_25_V1-v1/00000/0A3BA414-F166-E411-8E37-20CF30724B0A.root', 
        '/store/mc/Phys14DR/TprimeTprime_M_1000_Tune4C_13TeV-madgraph/GEN-SIM-RAW/PU20bx25_PHYS14_25_V1-v1/00000/0AC0F0A2-0967-E411-A299-0025907B4ECA.root', 
        '/store/mc/Phys14DR/TprimeTprime_M_1000_Tune4C_13TeV-madgraph/GEN-SIM-RAW/PU20bx25_PHYS14_25_V1-v1/00000/0ACC4F06-E166-E411-8EBD-E0CB4EA0A8FA.root'),
    inputCommands = cms.untracked.vstring('keep *', 
        'drop *_genParticles_*_*', 
        'drop *_genParticlesForJets_*_*', 
        'drop *_kt4GenJets_*_*', 
        'drop *_kt6GenJets_*_*', 
        'drop *_iterativeCone5GenJets_*_*', 
        'drop *_ak4GenJets_*_*', 
        'drop *_ak7GenJets_*_*', 
        'drop *_genCandidatesForMET_*_*', 
        'drop *_genParticlesForMETAllVisible_*_*', 
        'drop *_genMetCalo_*_*', 
        'drop *_genMetCaloAndNonPrompt_*_*', 
        'drop *_genMetTrue_*_*', 
        'drop *_genMetIC5GenJs_*_*'),
    dropDescendantsOfDroppedBranches = cms.untracked.bool(False)
)

process.options = cms.untracked.PSet(

)

# Production Info
process.configurationMetadata = cms.untracked.PSet(
    version = cms.untracked.string('$Revision: 1.19 $'),
    annotation = cms.untracked.string('step1 nevts:3'),
    name = cms.untracked.string('Applications')
)

# Output definition

process.RAWSIMoutput = cms.OutputModule("PoolOutputModule",
    splitLevel = cms.untracked.int32(0),
    eventAutoFlushCompressedSize = cms.untracked.int32(5242880),
    outputCommands = process.RAWSIMEventContent.outputCommands,
    fileName = cms.untracked.string('file:B2G-Phys14DR-00039_step1.root'),
    dataset = cms.untracked.PSet(
        filterName = cms.untracked.string(''),
        dataTier = cms.untracked.string('GEN-SIM-RAW')
    )
)

# Additional output definition

# Other statements
process.mix.input.nbPileupEvents.averageNumber = cms.double(20.000000)
process.mix.bunchspace = cms.int32(25)
process.mix.minBunch = cms.int32(-12)
process.mix.maxBunch = cms.int32(3)
process.mix.input.fileNames = cms.untracked.vstring(['/store/mc/Fall13/MinBias_TuneA2MB_13TeV-pythia8/GEN-SIM/POSTLS162_V1-v1/20000/0E0254B5-5E25-E311-9C87-0026B93F4A37.root',
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
'/store/mc/Fall13/MinBias_TuneA2MB_13TeV-pythia8/GEN-SIM/POSTLS162_V1-v1/20000/F265F6AD-5D25-E311-B2DC-00145EDD7759.root',
'/store/mc/Fall13/MinBias_TuneA2MB_13TeV-pythia8/GEN-SIM/POSTLS162_V1-v1/20001/28A40571-1C2A-E311-B016-0026B935A46C.root'])
from HLTrigger.Configuration.CustomConfigs import ProcessName
process = ProcessName(process)

from Configuration.AlCa.GlobalTag_condDBv2 import GlobalTag
process.GlobalTag = GlobalTag(process.GlobalTag, 'PHYS14_25_V2', '')

# Path and EndPath definitions
process.digitisation_step = cms.Path(process.pdigi)
process.L1simulation_step = cms.Path(process.SimL1Emulator)
process.digi2raw_step = cms.Path(process.DigiToRaw)
process.endjob_step = cms.EndPath(process.endOfProcess)
process.RAWSIMoutput_step = cms.EndPath(process.RAWSIMoutput)

# Schedule definition
process.schedule = cms.Schedule(process.digitisation_step,process.L1simulation_step,process.digi2raw_step)
process.schedule.extend(process.HLTSchedule)
process.schedule.extend([process.endjob_step,process.RAWSIMoutput_step])

# customisation of the process.

# Automatic addition of the customisation function from SLHCUpgradeSimulations.Configuration.postLS1Customs
from SLHCUpgradeSimulations.Configuration.postLS1Customs import customisePostLS1 

#call to customisation function customisePostLS1 imported from SLHCUpgradeSimulations.Configuration.postLS1Customs
process = customisePostLS1(process)

# Automatic addition of the customisation function from Configuration.DataProcessing.Utils
from Configuration.DataProcessing.Utils import addMonitoring 

#call to customisation function addMonitoring imported from Configuration.DataProcessing.Utils
process = addMonitoring(process)

# Automatic addition of the customisation function from HLTrigger.Configuration.customizeHLTforMC
from HLTrigger.Configuration.customizeHLTforMC import customizeHLTforMC 

#call to customisation function customizeHLTforMC imported from HLTrigger.Configuration.customizeHLTforMC
process = customizeHLTforMC(process)

# End of customisation functions

process.RAWSIMoutput.outputCommands.append('drop *_*_*_HLT')
