import FWCore.ParameterSet.Config as cms

cmgFiles = cms.untracked.vstring()
source = cms.Source("PoolSource",
                                                noEventSort = cms.untracked.bool(True),
                                                duplicateCheckMode = cms.untracked.string("noDuplicateCheck"),
                                                fileNames = cmgFiles
                                                )

cmgFiles.extend([

       '/store/group/phys_exotica/leptonsPlusJets/ExoDiBosonResonances/CMGtuple/shuai/production0307_AK7/Summer12/preselAK7//SingleTopBarTWchannel_xww/cmgTuple_0.root',
       '/store/group/phys_exotica/leptonsPlusJets/ExoDiBosonResonances/CMGtuple/shuai/production0307_AK7/Summer12/preselAK7//SingleTopBarTWchannel_xww/cmgTuple_1.root',
       '/store/group/phys_exotica/leptonsPlusJets/ExoDiBosonResonances/CMGtuple/shuai/production0307_AK7/Summer12/preselAK7//SingleTopBarTWchannel_xww/cmgTuple_2.root',
       '/store/group/phys_exotica/leptonsPlusJets/ExoDiBosonResonances/CMGtuple/shuai/production0307_AK7/Summer12/preselAK7//SingleTopBarTWchannel_xww/cmgTuple_3.root',
       '/store/group/phys_exotica/leptonsPlusJets/ExoDiBosonResonances/CMGtuple/shuai/production0307_AK7/Summer12/preselAK7//SingleTopBarTWchannel_xww/cmgTuple_4.root',
       '/store/group/phys_exotica/leptonsPlusJets/ExoDiBosonResonances/CMGtuple/shuai/production0307_AK7/Summer12/preselAK7//SingleTopBarTWchannel_xww/cmgTuple_5.root',
       '/store/group/phys_exotica/leptonsPlusJets/ExoDiBosonResonances/CMGtuple/shuai/production0307_AK7/Summer12/preselAK7//SingleTopBarTWchannel_xww/cmgTuple_6.root',
       '/store/group/phys_exotica/leptonsPlusJets/ExoDiBosonResonances/CMGtuple/shuai/production0307_AK7/Summer12/preselAK7//SingleTopBarTWchannel_xww/cmgTuple_7.root',
    ])
