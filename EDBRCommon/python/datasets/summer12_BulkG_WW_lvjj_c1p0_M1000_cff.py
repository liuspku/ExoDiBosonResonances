import FWCore.ParameterSet.Config as cms
maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ('PoolSource',fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend([
'/store/group/phys_exotica/leptonsPlusJets/ExoDiBosonResonances/santanas/EDBR_PATtuple_edbr_zz_20130113_Summer12MC_BulkGravitonsWW_20130206_201207/santanas/BulkG_WWlvjj_kMpl1_M-1000_TuneZ2star_8TeV-JHUGen/EDBR_PATtuple_edbr_zz_20130113/a2df48025a27dd8dc244a890c390dec0/BulkG_WWlvjj_kMpl1_M-1000_TuneZ2star_8TeV-JHUGen__caber-BulkG1000_kMpl1_WWlvjj_AODSIM-c8f8ed334db8a7d6f56c62266b1dfa5b__USER_1_1_TTC.root',
'/store/group/phys_exotica/leptonsPlusJets/ExoDiBosonResonances/santanas/EDBR_PATtuple_edbr_zz_20130113_Summer12MC_BulkGravitonsWW_20130206_201207/santanas/BulkG_WWlvjj_kMpl1_M-1000_TuneZ2star_8TeV-JHUGen/EDBR_PATtuple_edbr_zz_20130113/a2df48025a27dd8dc244a890c390dec0/BulkG_WWlvjj_kMpl1_M-1000_TuneZ2star_8TeV-JHUGen__caber-BulkG1000_kMpl1_WWlvjj_AODSIM-c8f8ed334db8a7d6f56c62266b1dfa5b__USER_2_1_0Fw.root',
'/store/group/phys_exotica/leptonsPlusJets/ExoDiBosonResonances/santanas/EDBR_PATtuple_edbr_zz_20130113_Summer12MC_BulkGravitonsWW_20130206_201207/santanas/BulkG_WWlvjj_kMpl1_M-1000_TuneZ2star_8TeV-JHUGen/EDBR_PATtuple_edbr_zz_20130113/a2df48025a27dd8dc244a890c390dec0/BulkG_WWlvjj_kMpl1_M-1000_TuneZ2star_8TeV-JHUGen__caber-BulkG1000_kMpl1_WWlvjj_AODSIM-c8f8ed334db8a7d6f56c62266b1dfa5b__USER_3_1_F7E.root',
'/store/group/phys_exotica/leptonsPlusJets/ExoDiBosonResonances/santanas/EDBR_PATtuple_edbr_zz_20130113_Summer12MC_BulkGravitonsWW_20130206_201207/santanas/BulkG_WWlvjj_kMpl1_M-1000_TuneZ2star_8TeV-JHUGen/EDBR_PATtuple_edbr_zz_20130113/a2df48025a27dd8dc244a890c390dec0/BulkG_WWlvjj_kMpl1_M-1000_TuneZ2star_8TeV-JHUGen__caber-BulkG1000_kMpl1_WWlvjj_AODSIM-c8f8ed334db8a7d6f56c62266b1dfa5b__USER_4_1_le6.root',
'/store/group/phys_exotica/leptonsPlusJets/ExoDiBosonResonances/santanas/EDBR_PATtuple_edbr_zz_20130113_Summer12MC_BulkGravitonsWW_20130206_201207/santanas/BulkG_WWlvjj_kMpl1_M-1000_TuneZ2star_8TeV-JHUGen/EDBR_PATtuple_edbr_zz_20130113/a2df48025a27dd8dc244a890c390dec0/BulkG_WWlvjj_kMpl1_M-1000_TuneZ2star_8TeV-JHUGen__caber-BulkG1000_kMpl1_WWlvjj_AODSIM-c8f8ed334db8a7d6f56c62266b1dfa5b__USER_5_1_hC9.root',
'/store/group/phys_exotica/leptonsPlusJets/ExoDiBosonResonances/santanas/EDBR_PATtuple_edbr_zz_20130113_Summer12MC_BulkGravitonsWW_20130206_201207/santanas/BulkG_WWlvjj_kMpl1_M-1000_TuneZ2star_8TeV-JHUGen/EDBR_PATtuple_edbr_zz_20130113/a2df48025a27dd8dc244a890c390dec0/BulkG_WWlvjj_kMpl1_M-1000_TuneZ2star_8TeV-JHUGen__caber-BulkG1000_kMpl1_WWlvjj_AODSIM-c8f8ed334db8a7d6f56c62266b1dfa5b__USER_6_1_wzN.root',
'/store/group/phys_exotica/leptonsPlusJets/ExoDiBosonResonances/santanas/EDBR_PATtuple_edbr_zz_20130113_Summer12MC_BulkGravitonsWW_20130206_201207/santanas/BulkG_WWlvjj_kMpl1_M-1000_TuneZ2star_8TeV-JHUGen/EDBR_PATtuple_edbr_zz_20130113/a2df48025a27dd8dc244a890c390dec0/BulkG_WWlvjj_kMpl1_M-1000_TuneZ2star_8TeV-JHUGen__caber-BulkG1000_kMpl1_WWlvjj_AODSIM-c8f8ed334db8a7d6f56c62266b1dfa5b__USER_7_1_vFH.root',
'/store/group/phys_exotica/leptonsPlusJets/ExoDiBosonResonances/santanas/EDBR_PATtuple_edbr_zz_20130113_Summer12MC_BulkGravitonsWW_20130206_201207/santanas/BulkG_WWlvjj_kMpl1_M-1000_TuneZ2star_8TeV-JHUGen/EDBR_PATtuple_edbr_zz_20130113/a2df48025a27dd8dc244a890c390dec0/BulkG_WWlvjj_kMpl1_M-1000_TuneZ2star_8TeV-JHUGen__caber-BulkG1000_kMpl1_WWlvjj_AODSIM-c8f8ed334db8a7d6f56c62266b1dfa5b__USER_8_1_aXg.root',
'/store/group/phys_exotica/leptonsPlusJets/ExoDiBosonResonances/santanas/EDBR_PATtuple_edbr_zz_20130113_Summer12MC_BulkGravitonsWW_20130206_201207/santanas/BulkG_WWlvjj_kMpl1_M-1000_TuneZ2star_8TeV-JHUGen/EDBR_PATtuple_edbr_zz_20130113/a2df48025a27dd8dc244a890c390dec0/BulkG_WWlvjj_kMpl1_M-1000_TuneZ2star_8TeV-JHUGen__caber-BulkG1000_kMpl1_WWlvjj_AODSIM-c8f8ed334db8a7d6f56c62266b1dfa5b__USER_9_1_56G.root',
]);
