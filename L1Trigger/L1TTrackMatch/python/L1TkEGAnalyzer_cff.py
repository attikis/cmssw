import FWCore.ParameterSet.Config as cms

from L1Trigger.L1TTrackMatch.L1TkEGAnalyzer_cfi import l1TrkEGAnalysis
TkEGEff                 = l1TrkEGAnalysis.clone()
TkEGEff.ObjectType      = cms.string("TkEG")
TkEGEff.AnalysisOption  = cms.string("Efficiency")
 
TkEGRate                = l1TrkEGAnalysis.clone()
TkEGRate.ObjectType     = cms.string("TkEG")
TkEGRate.AnalysisOption = cms.string("Rate")

