// -*- C++ -*-
//
// Package:     L1Trigger
// Class  :     L1TkEGParticle
// 

#include "DataFormats/L1TrackTrigger/interface/L1TkEGParticle.h"


using namespace l1t ;


L1TkEGParticle::L1TkEGParticle()
{
}

L1TkEGParticle::L1TkEGParticle( const LorentzVector& p4,
				const std::vector< L1TTTrackRefPtr >& clustTracks,
				const std::vector< EGammaRef >& clustEGs,
				float vtxIso )
  : L1Candidate  ( p4 ),
    clustTracks_ ( clustTracks ),
    clustEGs_ ( clustEGs ),
    vtxIso_      ( vtxIso ) 
{

}





