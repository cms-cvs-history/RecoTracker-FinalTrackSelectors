import FWCore.ParameterSet.Config as cms


import RecoTracker.FinalTrackSelectors.simpleTrackListMerger_cfi
firstStepTracksWithQuality = RecoTracker.FinalTrackSelectors.simpleTrackListMerger_cfi.simpleTrackListMerger.clone(
    TrackProducer1 = 'zeroStepTracksWithQuality',
    TrackProducer2 = 'preMergingFirstStepTracksWithQuality',
    promoteTrackQuality = False
    )


# new merging module
import RecoTracker.FinalTrackSelectors.trackListMerger_cfi
generalTracks = RecoTracker.FinalTrackSelectors.trackListMerger_cfi.trackListMerger.clone(
    TrackProducers = ('firstStepTracksWithQuality','secStep','thStep','pixellessStep','tobtecStep'),
    hasSelector=cms.vint32(0,0,0,0,0),
    selectedTrackQuals = cms.VInputTag(cms.InputTag(""),cms.InputTag(""),cms.InputTag(""),cms.InputTag(""),cms.InputTag("")),
    setsToMerge = cms.VPSet( cms.PSet( tLists=cms.vint32(1,2), pQual=cms.bool(True) ),
                             cms.PSet( tLists=cms.vint32(3,4), pQual=cms.bool(True) ),
                             cms.PSet( tLists=cms.vint32(1,2,3,4), pQual=cms.bool(True) ),
                             cms.PSet( tLists=cms.vint32(0,1,2,3,4), pQual=cms.bool(True) )
                             ),
    
    #this could work if the firstStepTracksWithQuality module above could be removed
    #    TrackProducers = ('zeroStepTracksWithQuality','preMergingFirstStepTracksWithQuality','secStep','thStep','pixellessStep','tobtecStep'),
    #        setsToMerge = cms.VPSet( cms.PSet( tLists=cms.vint32(0,1), pQual=cms.bool(False)),
    #                             cms.PSet( tLists=cms.vint32(2,3), pQual=cms.bool(True) ),
    #                             cms.PSet( tLists=cms.vint32(4,5), pQual=cms.bool(True) ),
    #                             cms.PSet( tLists=cms.vint32(2,3,4,5), pQual=cms.bool(True) ),
    #                             cms.PSet( tLists=cms.vint32(0,1,2,3,4,5), pQual=cms.bool(True) )
    #                             ),
    
    copyExtras = True,
    makeReKeyedSeeds = cms.untracked.bool(True)
    )

trackCollectionMerging = cms.Sequence(generalTracks)

