import FWCore.ParameterSet.Config as cms

l1TrkEGAnalysis = cms.EDAnalyzer( 'L1TkEGAnalyzer' ,
    L1TkEGInputTag      = cms.InputTag("L1TkEGTaus", "TkEG"),

    L1TrackInputTag     = cms.InputTag("TTTracksFromTracklet", "Level1TTTracks"),
    GenParticleInputTag = cms.InputTag("genParticles",""),
    AnalysisOption      = cms.string("Efficiency"),
    ObjectType          = cms.string("Electron"),
    GenEtaCutOff        = cms.double(1.4),
    EtaCutOff           = cms.double(1.5),                            
    TrackPtCutOff       = cms.double(10.0),
    GenPtThreshold      = cms.double(0.0),
    EtThreshold         = cms.double(25.0)                              
    #Ntaus               = cms.uint32(0)
)
