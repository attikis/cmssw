import FWCore.ParameterSet.Config as cms

from Configuration.StandardSequences.Eras import eras

process = cms.Process("L1AlgoTest",eras.Phase2_trigger)

process.load('Configuration.StandardSequences.Services_cff')
process.load("FWCore.MessageService.MessageLogger_cfi")
process.load('Configuration.EventContent.EventContent_cff')
process.MessageLogger.categories = cms.untracked.vstring('L1EGRateStudies', 'FwkReport')
process.MessageLogger.cerr.FwkReport = cms.untracked.PSet(
   reportEvery = cms.untracked.int32(1)
)

process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(10) )

process.source = cms.Source("PoolSource",
   # Set to do test run on official Phase-2 L1T Ntuples
   #fileNames = cms.untracked.vstring('file:root://cmsxrootd.fnal.gov///store/mc/PhaseIIFall17D/TT_TuneCUETP8M2T4_14TeV-powheg-pythia8/GEN-SIM-DIGI-RAW/L1TPU200_93X_upgrade2023_realistic_v5-v2/30000/04998910-0755-E811-B1FC-EC0D9A822606.root'),
   #fileNames = cms.untracked.vstring('file:root://cmsxrootd.fnal.gov///store/mc/PhaseIISpring17D/SingleE_FlatPt-8to100/GEN-SIM-DIGI-RAW/PU200_90X_upgrade2023_realistic_v9-v1/120000/04B4BF1D-1E2C-E711-BE1C-7845C4FC39D1.root'),
   fileNames = cms.untracked.vstring('file:root://cmsxrootd.fnal.gov///store/mc/PhaseIIFall17D/GluGluHToTauTau_M125_14TeV_powheg_pythia8/GEN-SIM-DIGI-RAW/L1TPU200_93X_upgrade2023_realistic_v5-v1/90000/0C3B3628-A539-E811-873E-008CFA198258.root'),
   inputCommands = cms.untracked.vstring(
                    "keep *",
                    "drop l1tEMTFHitExtras_simEmtfDigis_CSC_HLT",
                    "drop l1tEMTFHitExtras_simEmtfDigis_RPC_HLT",
                    "drop l1tEMTFTrackExtras_simEmtfDigis__HLT",
                    "drop l1tEMTFHit2016Extras_simEmtfDigis_CSC_HLT",
                    "drop l1tEMTFHit2016Extras_simEmtfDigis_RPC_HLT",
                    "drop l1tEMTFHit2016s_simEmtfDigis__HLT",
                    "drop l1tEMTFTrack2016Extras_simEmtfDigis__HLT",
                    "drop l1tEMTFTrack2016s_simEmtfDigis__HLT"
                    )
)

# All this stuff just runs the various EG algorithms that we are studying
                         
# ---- Global Tag :
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_cff')
from Configuration.AlCa.GlobalTag import GlobalTag
process.GlobalTag = GlobalTag(process.GlobalTag, '100X_upgrade2023_realistic_v1', '')

# Choose a 2023 geometry!
process.load('Configuration.Geometry.GeometryExtended2023D17Reco_cff')
process.load('Configuration.StandardSequences.MagneticField_cff')

# Add HCAL Transcoder
process.load('SimCalorimetry.HcalTrigPrimProducers.hcaltpdigi_cff')
process.load('CalibCalorimetry.CaloTPG.CaloTPGTranscoder_cfi')

process.load('Configuration.StandardSequences.L1TrackTrigger_cff')




# --------------------------------------------------------------------------------------------
#
# ----    Produce the L1EGCrystal clusters using Emulator

process.load('L1Trigger.TrackFindingTracklet.L1TrackletTracks_cff')
process.L1TrackTrigger_step = cms.Path(process.L1TrackletTracks)

process.load('L1Trigger.L1CaloTrigger.L1EGammaCrystalsEmulatorProducer_cfi')
process.pL1EG = cms.Path( process.L1EGammaClusterEmuProducer )

# ----
process.load("L1Trigger.L1TTrackMatch.L1TkEGParticleProducer_cfi")
process.pL1TkEGTaus = cms.Path( process.L1TkEGTaus )

process.load("L1Trigger.L1TTrackMatch.L1TrkTauParticleProducer_cfi")
process.pL1TrkTaus = cms.Path( process.L1TrkTaus )


process.Out = cms.OutputModule( "PoolOutputModule",
    fileName = cms.untracked.string( "l1tausTest.root" ),
    fastCloning = cms.untracked.bool( False ),
    outputCommands = cms.untracked.vstring(
        "keep *_L1TkEGTaus_*_*",
        "keep *_L1TrkTaus_*_*"
        )
                                
)

process.end = cms.EndPath( process.Out )



dump_file = open("dump_file.py", "w")
dump_file.write(process.dumpPython())


