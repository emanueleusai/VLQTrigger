# Auto generated configuration file
# using: 
# Revision: 1.19 
# Source: /local/reps/CMSSW/CMSSW/Configuration/Applications/python/ConfigBuilder.py,v 
# with command line options: Configuration/GenProduction/python/ThirteenTeV/Hadronizer_TuneCUETP8M1_13TeV_MLM_5f_max1j_LHE_pythia8_cff.py --filein file:gen.root --fileout file:sim.root --mc --eventcontent RAWSIM --customise SLHCUpgradeSimulations/Configuration/postLS1Customs.customisePostLS1,Configuration/DataProcessing/Utils.addMonitoring --datatier GEN-SIM --conditions auto:mc --step GEN,SIM --magField 38T_PostLS1 --geometry Extended2015 --python_filename sim4.py --no_exec -n -1
import FWCore.ParameterSet.Config as cms

process = cms.Process('SIM')

# import of standard configurations
process.load('Configuration.StandardSequences.Services_cff')
process.load('SimGeneral.HepPDTESSource.pythiapdt_cfi')
process.load('FWCore.MessageService.MessageLogger_cfi')
process.load('Configuration.EventContent.EventContent_cff')
process.load('SimGeneral.MixingModule.mixNoPU_cfi')
process.load('Configuration.Geometry.GeometryExtended2015Reco_cff')
process.load('Configuration.Geometry.GeometryExtended2015_cff')
process.load('Configuration.StandardSequences.MagneticField_38T_PostLS1_cff')
process.load('Configuration.StandardSequences.Generator_cff')
process.load('IOMC.EventVertexGenerators.VtxSmearedRealistic8TeVCollision_cfi')
process.load('GeneratorInterface.Core.genFilterSummary_cff')
process.load('Configuration.StandardSequences.SimIdeal_cff')
process.load('Configuration.StandardSequences.EndOfProcess_cff')
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_condDBv2_cff')

process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(10)
)

# Input source
process.source = cms.Source("PoolSource",
    fileNames = cms.untracked.vstring('file:/nfs/dust/cms/user/usaiem/gen/had.root'),
    secondaryFileNames = cms.untracked.vstring()
)

process.options = cms.untracked.PSet(

)

# Production Info
process.configurationMetadata = cms.untracked.PSet(
    annotation = cms.untracked.string('Configuration/GenProduction/python/ThirteenTeV/Hadronizer_TuneCUETP8M1_13TeV_MLM_5f_max1j_LHE_pythia8_cff.py nevts:-1'),
    name = cms.untracked.string('Applications'),
    version = cms.untracked.string('$Revision: 1.19 $')
)

# Output definition

process.RAWSIMoutput = cms.OutputModule("PoolOutputModule",
    SelectEvents = cms.untracked.PSet(
        SelectEvents = cms.vstring('generation_step')
    ),
    dataset = cms.untracked.PSet(
        dataTier = cms.untracked.string('GEN-SIM'),
        filterName = cms.untracked.string('')
    ),
    eventAutoFlushCompressedSize = cms.untracked.int32(5242880),
    fileName = cms.untracked.string('file:sim.root'),
    outputCommands = process.RAWSIMEventContent.outputCommands,
    splitLevel = cms.untracked.int32(0)
)

# Additional output definition

# Other statements
process.genstepfilter.triggerConditions=cms.vstring("generation_step")
from Configuration.AlCa.GlobalTag_condDBv2 import GlobalTag
process.GlobalTag = GlobalTag(process.GlobalTag, 'MCRUN2_74_V9A', '')

# process.generator = cms.EDFilter("Pythia8HadronizerFilter",
#     PythiaParameters = cms.PSet(
#         parameterSets = cms.vstring('pythia8CommonSettings', 
#             'pythia8CUEP8M1Settings', 
#             'processParameters'),
#         processParameters = cms.vstring('JetMatching:setMad = off', 
#             'JetMatching:scheme = 1', 
#             'JetMatching:merge = on', 
#             'JetMatching:jetAlgorithm = 2', 
#             'JetMatching:etaJetMax = 5.', 
#             'JetMatching:coneRadius = 1.', 
#             'JetMatching:slowJetPower = 1', 
#             'JetMatching:qCut = 40.', 
#             'JetMatching:nQmatch = 4', 
#             'JetMatching:nJetMax = 1',
#             'JetMatching:doShowerKt = off'),
#         pythia8CUEP8M1Settings = cms.vstring('Tune:pp 14', 
#             'Tune:ee 7', 
#             'MultipartonInteractions:pT0Ref=2.4024', 
#             'MultipartonInteractions:ecmPow=0.25208', 
#             'MultipartonInteractions:expPow=1.6'),
#         pythia8CommonSettings = cms.vstring('Main:timesAllowErrors = 10000', 
#             'Check:epTolErr = 0.01', 
#             'Beams:setProductionScalesFromLHEF = on', 
#             'SLHA:keepSM = on', 
#             'SLHA:minMassSM = 1000.', 
#             'ParticleDecays:limitTau0 = on', 
#             'ParticleDecays:tau0Max = 10', 
#             'ParticleDecays:allowPhotonRadiation = on')
#     ),
#     comEnergy = cms.double(13000.0),
#     filterEfficiency = cms.untracked.double(1.0),
#     maxEventsToPrint = cms.untracked.int32(1),
#     pythiaHepMCVerbosity = cms.untracked.bool(False),
#     pythiaPylistVerbosity = cms.untracked.int32(1),

#     # jetMatching = cms.untracked.PSet(
#     #     outTree_flag = cms.int32(1) # 1=yes, write out the tree for future sanity check
#     # ),
#     jetMatching = cms.untracked.PSet(
#        scheme = cms.string("Madgraph"),
#        mode = cms.string("auto"),   # soup, or "inclusive" / "exclusive"
#        MEMAIN_nqmatch = cms.int32(4),
#        MEMAIN_etaclmax = cms.double(-1),
#        MEMAIN_qcut = cms.double(40),
#        MEMAIN_minjets = cms.int32(-1),
#        MEMAIN_maxjets = cms.int32(1),
#        MEMAIN_showerkt = cms.double(0),
#        MEMAIN_excres = cms.string(""),
#        outTree_flag = cms.int32(1)
#     )
# )

process.generator = cms.EDFilter("Pythia8HadronizerFilter",
    maxEventsToPrint = cms.untracked.int32(1),
    pythiaPylistVerbosity = cms.untracked.int32(1),
    filterEfficiency = cms.untracked.double(1.0),
    pythiaHepMCVerbosity = cms.untracked.bool(False),
    comEnergy = cms.double(13000.),
    jetMatching = cms.untracked.PSet(
        scheme = cms.string("Madgraph"),
        mode = cms.string("auto"),# soup, or "inclusive" / "exclusive"
        MEMAIN_etaclmax = cms.double(5),
        MEMAIN_qcut = cms.double(40),
        MEMAIN_minjets = cms.int32(0),
        MEMAIN_maxjets = cms.int32(1),
        MEMAIN_showerkt = cms.double(0), # use 1=yes only for pt-ordered showers !
        MEMAIN_nqmatch = cms.int32(4),   #PID of the flavor until which the QCD radiation are kept in the matching procedure;
                                         # if nqmatch=4, then all showered partons from b's are NOT taken into account
         # Note (JY): I think the default should be 5 (b); anyway, don't try -1  as it'll result in a throw...
        MEMAIN_excres = cms.string(""),
        outTree_flag = cms.int32(1)      # 1=yes, write out the tree for future sanity check
    ),
    PythiaParameters = cms.PSet(
        processParameters = cms.vstring(
        'Main:timesAllowErrors    = 10000', 
        'ParticleDecays:limitTau0 = on',
        'ParticleDecays:tauMax = 10',
        'Tune:ee 3',
        'Tune:pp 5'),
        parameterSets = cms.vstring('processParameters')
    )
)



# Path and EndPath definitions
process.generation_step = cms.Path(process.pgen)
process.simulation_step = cms.Path(process.psim)
process.genfiltersummary_step = cms.EndPath(process.genFilterSummary)
process.endjob_step = cms.EndPath(process.endOfProcess)
process.RAWSIMoutput_step = cms.EndPath(process.RAWSIMoutput)

# Schedule definition
process.schedule = cms.Schedule(process.generation_step,process.genfiltersummary_step,process.simulation_step,process.endjob_step,process.RAWSIMoutput_step)
# filter all path with the production filter sequence
for path in process.paths:
	getattr(process,path)._seq = process.generator * getattr(process,path)._seq 

# customisation of the process.

# Automatic addition of the customisation function from SLHCUpgradeSimulations.Configuration.postLS1Customs
from SLHCUpgradeSimulations.Configuration.postLS1Customs import customisePostLS1 

#call to customisation function customisePostLS1 imported from SLHCUpgradeSimulations.Configuration.postLS1Customs
process = customisePostLS1(process)

# Automatic addition of the customisation function from Configuration.DataProcessing.Utils
from Configuration.DataProcessing.Utils import addMonitoring 

#call to customisation function addMonitoring imported from Configuration.DataProcessing.Utils
process = addMonitoring(process)

# End of customisation functions


def customise_for_gc(process):
	import FWCore.ParameterSet.Config as cms
	from IOMC.RandomEngine.RandomServiceHelper import RandomNumberServiceHelper

	try:
		maxevents = 10
		process.maxEvents = cms.untracked.PSet(
			input = cms.untracked.int32(max(-1, maxevents))
		)
	except:
		pass

	# Dataset related setup
	try:
		primaryFiles = ["file:/nfs/dust/cms/user/usaiem/gen/had.root"]
		process.source = cms.Source('PoolSource',
			skipEvents = cms.untracked.uint32(4000),
			fileNames = cms.untracked.vstring(primaryFiles)
		)
		try:
			secondaryFiles = [__FILE_NAMES2__]
			process.source.secondaryFileNames = cms.untracked.vstring(secondaryFiles)
		except:
			pass
		try:
			lumirange = [__LUMI_RANGE__]
			if len(lumirange) > 0:
				process.source.lumisToProcess = cms.untracked.VLuminosityBlockRange(lumirange)
				process.maxEvents = cms.untracked.PSet(input = cms.untracked.int32(-1))
		except:
			pass
	except:
		pass

	if hasattr(process, 'RandomNumberGeneratorService'):
		randSvc = RandomNumberServiceHelper(process.RandomNumberGeneratorService)
		randSvc.populate()

	process.AdaptorConfig = cms.Service('AdaptorConfig',
		enable = cms.untracked.bool(True),
		stats = cms.untracked.bool(True),
	)

	# Generator related setup
	try:
		if hasattr(process, 'generator') and process.source.type_() != 'PoolSource':
			process.source.firstLuminosityBlock = cms.untracked.uint32(1 + 80)
			print 'Generator random seed:', process.RandomNumberGeneratorService.generator.initialSeed
	except:
		pass

	return (process)

process = customise_for_gc(process)

# grid-control: https://ekptrac.physik.uni-karlsruhe.de/trac/grid-control
