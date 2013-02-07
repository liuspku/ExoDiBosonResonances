import FWCore.ParameterSet.Config as cms
maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ('PoolSource',fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend([
'/store/group/phys_exotica/leptonsPlusJets/ExoDiBosonResonances/santanas/EDBR_PATtuple_edbr_zz_20130113_Summer12MC_RSGravitonsWW_20130206_193221/santanas/RSGraviton_WWlvjj_kMpl-005_M-1000_TuneZ2star_8TeV-MG/EDBR_PATtuple_edbr_zz_20130113/a2df48025a27dd8dc244a890c390dec0/RSGraviton_WWlvjj_kMpl-005_M-1000_TuneZ2star_8TeV-MG__qili-RSWW_1000_005_AODSIM-c8f8ed334db8a7d6f56c62266b1dfa5b__USER_1_1_Yi4.root',
'/store/group/phys_exotica/leptonsPlusJets/ExoDiBosonResonances/santanas/EDBR_PATtuple_edbr_zz_20130113_Summer12MC_RSGravitonsWW_20130206_193221/santanas/RSGraviton_WWlvjj_kMpl-005_M-1000_TuneZ2star_8TeV-MG/EDBR_PATtuple_edbr_zz_20130113/a2df48025a27dd8dc244a890c390dec0/RSGraviton_WWlvjj_kMpl-005_M-1000_TuneZ2star_8TeV-MG__qili-RSWW_1000_005_AODSIM-c8f8ed334db8a7d6f56c62266b1dfa5b__USER_2_1_lTu.root',
'/store/group/phys_exotica/leptonsPlusJets/ExoDiBosonResonances/santanas/EDBR_PATtuple_edbr_zz_20130113_Summer12MC_RSGravitonsWW_20130206_193221/santanas/RSGraviton_WWlvjj_kMpl-005_M-1000_TuneZ2star_8TeV-MG/EDBR_PATtuple_edbr_zz_20130113/a2df48025a27dd8dc244a890c390dec0/RSGraviton_WWlvjj_kMpl-005_M-1000_TuneZ2star_8TeV-MG__qili-RSWW_1000_005_AODSIM-c8f8ed334db8a7d6f56c62266b1dfa5b__USER_3_1_1rj.root',
'/store/group/phys_exotica/leptonsPlusJets/ExoDiBosonResonances/santanas/EDBR_PATtuple_edbr_zz_20130113_Summer12MC_RSGravitonsWW_20130206_193221/santanas/RSGraviton_WWlvjj_kMpl-005_M-1000_TuneZ2star_8TeV-MG/EDBR_PATtuple_edbr_zz_20130113/a2df48025a27dd8dc244a890c390dec0/RSGraviton_WWlvjj_kMpl-005_M-1000_TuneZ2star_8TeV-MG__qili-RSWW_1000_005_AODSIM-c8f8ed334db8a7d6f56c62266b1dfa5b__USER_4_1_X8O.root',
'/store/group/phys_exotica/leptonsPlusJets/ExoDiBosonResonances/santanas/EDBR_PATtuple_edbr_zz_20130113_Summer12MC_RSGravitonsWW_20130206_193221/santanas/RSGraviton_WWlvjj_kMpl-005_M-1000_TuneZ2star_8TeV-MG/EDBR_PATtuple_edbr_zz_20130113/a2df48025a27dd8dc244a890c390dec0/RSGraviton_WWlvjj_kMpl-005_M-1000_TuneZ2star_8TeV-MG__qili-RSWW_1000_005_AODSIM-c8f8ed334db8a7d6f56c62266b1dfa5b__USER_5_1_qHA.root',
'/store/group/phys_exotica/leptonsPlusJets/ExoDiBosonResonances/santanas/EDBR_PATtuple_edbr_zz_20130113_Summer12MC_RSGravitonsWW_20130206_193221/santanas/RSGraviton_WWlvjj_kMpl-005_M-1000_TuneZ2star_8TeV-MG/EDBR_PATtuple_edbr_zz_20130113/a2df48025a27dd8dc244a890c390dec0/RSGraviton_WWlvjj_kMpl-005_M-1000_TuneZ2star_8TeV-MG__qili-RSWW_1000_005_AODSIM-c8f8ed334db8a7d6f56c62266b1dfa5b__USER_6_1_vUL.root',
'/store/group/phys_exotica/leptonsPlusJets/ExoDiBosonResonances/santanas/EDBR_PATtuple_edbr_zz_20130113_Summer12MC_RSGravitonsWW_20130206_193221/santanas/RSGraviton_WWlvjj_kMpl-005_M-1000_TuneZ2star_8TeV-MG/EDBR_PATtuple_edbr_zz_20130113/a2df48025a27dd8dc244a890c390dec0/RSGraviton_WWlvjj_kMpl-005_M-1000_TuneZ2star_8TeV-MG__qili-RSWW_1000_005_AODSIM-c8f8ed334db8a7d6f56c62266b1dfa5b__USER_7_1_EGb.root',
'/store/group/phys_exotica/leptonsPlusJets/ExoDiBosonResonances/santanas/EDBR_PATtuple_edbr_zz_20130113_Summer12MC_RSGravitonsWW_20130206_193221/santanas/RSGraviton_WWlvjj_kMpl-005_M-1000_TuneZ2star_8TeV-MG/EDBR_PATtuple_edbr_zz_20130113/a2df48025a27dd8dc244a890c390dec0/RSGraviton_WWlvjj_kMpl-005_M-1000_TuneZ2star_8TeV-MG__qili-RSWW_1000_005_AODSIM-c8f8ed334db8a7d6f56c62266b1dfa5b__USER_8_1_iQz.root',
'/store/group/phys_exotica/leptonsPlusJets/ExoDiBosonResonances/santanas/EDBR_PATtuple_edbr_zz_20130113_Summer12MC_RSGravitonsWW_20130206_193221/santanas/RSGraviton_WWlvjj_kMpl-005_M-1000_TuneZ2star_8TeV-MG/EDBR_PATtuple_edbr_zz_20130113/a2df48025a27dd8dc244a890c390dec0/RSGraviton_WWlvjj_kMpl-005_M-1000_TuneZ2star_8TeV-MG__qili-RSWW_1000_005_AODSIM-c8f8ed334db8a7d6f56c62266b1dfa5b__USER_9_1_95c.root',
]);
