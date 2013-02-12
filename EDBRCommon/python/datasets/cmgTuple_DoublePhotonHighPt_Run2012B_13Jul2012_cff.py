import FWCore.ParameterSet.Config as cms
maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ('PoolSource',fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend([
'/store/group/phys_exotica/leptonsPlusJets/ExoDiBosonResonances/CMGtuple/productionV1/Run2012/preselCA8//DoublePhotonHighPt_Run2012B_13Jul2012/cmgTuple_0.root',
'/store/group/phys_exotica/leptonsPlusJets/ExoDiBosonResonances/CMGtuple/productionV1/Run2012/preselCA8//DoublePhotonHighPt_Run2012B_13Jul2012/cmgTuple_1.root',
'/store/group/phys_exotica/leptonsPlusJets/ExoDiBosonResonances/CMGtuple/productionV1/Run2012/preselCA8//DoublePhotonHighPt_Run2012B_13Jul2012/cmgTuple_10.root',
'/store/group/phys_exotica/leptonsPlusJets/ExoDiBosonResonances/CMGtuple/productionV1/Run2012/preselCA8//DoublePhotonHighPt_Run2012B_13Jul2012/cmgTuple_11.root',
'/store/group/phys_exotica/leptonsPlusJets/ExoDiBosonResonances/CMGtuple/productionV1/Run2012/preselCA8//DoublePhotonHighPt_Run2012B_13Jul2012/cmgTuple_12.root',
'/store/group/phys_exotica/leptonsPlusJets/ExoDiBosonResonances/CMGtuple/productionV1/Run2012/preselCA8//DoublePhotonHighPt_Run2012B_13Jul2012/cmgTuple_13.root',
'/store/group/phys_exotica/leptonsPlusJets/ExoDiBosonResonances/CMGtuple/productionV1/Run2012/preselCA8//DoublePhotonHighPt_Run2012B_13Jul2012/cmgTuple_14.root',
'/store/group/phys_exotica/leptonsPlusJets/ExoDiBosonResonances/CMGtuple/productionV1/Run2012/preselCA8//DoublePhotonHighPt_Run2012B_13Jul2012/cmgTuple_15.root',
'/store/group/phys_exotica/leptonsPlusJets/ExoDiBosonResonances/CMGtuple/productionV1/Run2012/preselCA8//DoublePhotonHighPt_Run2012B_13Jul2012/cmgTuple_16.root',
'/store/group/phys_exotica/leptonsPlusJets/ExoDiBosonResonances/CMGtuple/productionV1/Run2012/preselCA8//DoublePhotonHighPt_Run2012B_13Jul2012/cmgTuple_17.root',
'/store/group/phys_exotica/leptonsPlusJets/ExoDiBosonResonances/CMGtuple/productionV1/Run2012/preselCA8//DoublePhotonHighPt_Run2012B_13Jul2012/cmgTuple_18.root',
'/store/group/phys_exotica/leptonsPlusJets/ExoDiBosonResonances/CMGtuple/productionV1/Run2012/preselCA8//DoublePhotonHighPt_Run2012B_13Jul2012/cmgTuple_19.root',
'/store/group/phys_exotica/leptonsPlusJets/ExoDiBosonResonances/CMGtuple/productionV1/Run2012/preselCA8//DoublePhotonHighPt_Run2012B_13Jul2012/cmgTuple_2.root',
'/store/group/phys_exotica/leptonsPlusJets/ExoDiBosonResonances/CMGtuple/productionV1/Run2012/preselCA8//DoublePhotonHighPt_Run2012B_13Jul2012/cmgTuple_20.root',
'/store/group/phys_exotica/leptonsPlusJets/ExoDiBosonResonances/CMGtuple/productionV1/Run2012/preselCA8//DoublePhotonHighPt_Run2012B_13Jul2012/cmgTuple_21.root',
'/store/group/phys_exotica/leptonsPlusJets/ExoDiBosonResonances/CMGtuple/productionV1/Run2012/preselCA8//DoublePhotonHighPt_Run2012B_13Jul2012/cmgTuple_22.root',
'/store/group/phys_exotica/leptonsPlusJets/ExoDiBosonResonances/CMGtuple/productionV1/Run2012/preselCA8//DoublePhotonHighPt_Run2012B_13Jul2012/cmgTuple_23.root',
'/store/group/phys_exotica/leptonsPlusJets/ExoDiBosonResonances/CMGtuple/productionV1/Run2012/preselCA8//DoublePhotonHighPt_Run2012B_13Jul2012/cmgTuple_24.root',
'/store/group/phys_exotica/leptonsPlusJets/ExoDiBosonResonances/CMGtuple/productionV1/Run2012/preselCA8//DoublePhotonHighPt_Run2012B_13Jul2012/cmgTuple_25.root',
'/store/group/phys_exotica/leptonsPlusJets/ExoDiBosonResonances/CMGtuple/productionV1/Run2012/preselCA8//DoublePhotonHighPt_Run2012B_13Jul2012/cmgTuple_26.root',
'/store/group/phys_exotica/leptonsPlusJets/ExoDiBosonResonances/CMGtuple/productionV1/Run2012/preselCA8//DoublePhotonHighPt_Run2012B_13Jul2012/cmgTuple_27.root',
'/store/group/phys_exotica/leptonsPlusJets/ExoDiBosonResonances/CMGtuple/productionV1/Run2012/preselCA8//DoublePhotonHighPt_Run2012B_13Jul2012/cmgTuple_28.root',
'/store/group/phys_exotica/leptonsPlusJets/ExoDiBosonResonances/CMGtuple/productionV1/Run2012/preselCA8//DoublePhotonHighPt_Run2012B_13Jul2012/cmgTuple_29.root',
'/store/group/phys_exotica/leptonsPlusJets/ExoDiBosonResonances/CMGtuple/productionV1/Run2012/preselCA8//DoublePhotonHighPt_Run2012B_13Jul2012/cmgTuple_3.root',
'/store/group/phys_exotica/leptonsPlusJets/ExoDiBosonResonances/CMGtuple/productionV1/Run2012/preselCA8//DoublePhotonHighPt_Run2012B_13Jul2012/cmgTuple_30.root',
'/store/group/phys_exotica/leptonsPlusJets/ExoDiBosonResonances/CMGtuple/productionV1/Run2012/preselCA8//DoublePhotonHighPt_Run2012B_13Jul2012/cmgTuple_31.root',
'/store/group/phys_exotica/leptonsPlusJets/ExoDiBosonResonances/CMGtuple/productionV1/Run2012/preselCA8//DoublePhotonHighPt_Run2012B_13Jul2012/cmgTuple_32.root',
'/store/group/phys_exotica/leptonsPlusJets/ExoDiBosonResonances/CMGtuple/productionV1/Run2012/preselCA8//DoublePhotonHighPt_Run2012B_13Jul2012/cmgTuple_33.root',
'/store/group/phys_exotica/leptonsPlusJets/ExoDiBosonResonances/CMGtuple/productionV1/Run2012/preselCA8//DoublePhotonHighPt_Run2012B_13Jul2012/cmgTuple_4.root',
'/store/group/phys_exotica/leptonsPlusJets/ExoDiBosonResonances/CMGtuple/productionV1/Run2012/preselCA8//DoublePhotonHighPt_Run2012B_13Jul2012/cmgTuple_5.root',
'/store/group/phys_exotica/leptonsPlusJets/ExoDiBosonResonances/CMGtuple/productionV1/Run2012/preselCA8//DoublePhotonHighPt_Run2012B_13Jul2012/cmgTuple_6.root',
'/store/group/phys_exotica/leptonsPlusJets/ExoDiBosonResonances/CMGtuple/productionV1/Run2012/preselCA8//DoublePhotonHighPt_Run2012B_13Jul2012/cmgTuple_7.root',
'/store/group/phys_exotica/leptonsPlusJets/ExoDiBosonResonances/CMGtuple/productionV1/Run2012/preselCA8//DoublePhotonHighPt_Run2012B_13Jul2012/cmgTuple_8.root',
'/store/group/phys_exotica/leptonsPlusJets/ExoDiBosonResonances/CMGtuple/productionV1/Run2012/preselCA8//DoublePhotonHighPt_Run2012B_13Jul2012/cmgTuple_9.root',
]);
