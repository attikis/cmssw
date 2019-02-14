#ifndef L1TkTrigger_L1TkEGParticle_h
#define L1TkTrigger_L1TkEGParticle_h

// -*- C++ -*-
//
// Package:     L1Trigger
// Class  :     L1TkEGParticle
// 

#include "DataFormats/L1Trigger/interface/L1Candidate.h"
#include "DataFormats/Common/interface/Ref.h"

#include "DataFormats/L1Trigger/interface/EGamma.h"
#include "DataFormats/HepMCCandidate/interface/GenParticle.h"

#include "DataFormats/L1TrackTrigger/interface/TTTrack.h"
#include "DataFormats/L1TrackTrigger/interface/TTTypes.h"

namespace l1t { 

  class L1TkEGParticle ;
  
  typedef std::vector< L1TkEGParticle > L1TkEGParticleCollection ;
  
  typedef edm::Ref< L1TkEGParticleCollection > L1TkEGParticleRef ;
  typedef edm::RefVector< L1TkEGParticleCollection > L1TkEGParticleRefVector ;
  typedef std::vector< L1TkEGParticleRef > L1TkEGParticleVectorRef ;
  
  typedef TTTrack< Ref_Phase2TrackerDigi_ >  L1TTTrackType;
  typedef std::vector< L1TTTrackType > L1TTTrackCollection;
  typedef edm::Ptr< L1TTTrackType > L1TTTrackRefPtr;
  typedef std::vector< L1TTTrackRefPtr > L1TTTrackRefPtr_Collection;
  typedef edm::Ref< EGammaBxCollection > EGammaRef ;
  typedef std::vector< EGammaRef > EGammaVectorRef ;

  class L1TkEGParticle : public L1Candidate
  {     
    
  public:
    
    L1TkEGParticle();
    

    L1TkEGParticle( const LorentzVector& p4,
		    const std::vector< L1TTTrackRefPtr >& clustTracks,
		    const std::vector< EGammaRef >& clustEGs,
		    float vtxIso = -999. );

    virtual ~L1TkEGParticle() {}
      
    // ---------- const member functions ---------------------
    /*
    const edm::Ref< EGammaBxCollection >& getEGRef() const
    { return egRef_ ; }
    
    const double l1RefEta() const
    { return egRef_->eta() ; }
    
    const double l1RefPhi() const
    { return egRef_->phi() ; }
    
    const double l1RefEt() const
    { return egRef_->et() ; }
    */

    float getVtxIso() const { return vtxIso_ ; } 
    
    // ---------- member functions ---------------------------
    
    void setVtxIso(float VtxIso)  { vtxIso_ = VtxIso ; }
    
    //	 int bx() const;
    
  private:
    std::vector< L1TTTrackRefPtr > clustTracks_;
    std::vector< EGammaRef > clustEGs_;
    float vtxIso_;

  };
}

#endif


