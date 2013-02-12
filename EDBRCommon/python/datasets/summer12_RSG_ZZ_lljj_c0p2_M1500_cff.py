import FWCore.ParameterSet.Config as cms
maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ('PoolSource',fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend([
'/store/group/phys_exotica/leptonsPlusJets/ExoDiBosonResonances/santanas/EDBR_PATtuple_edbr_zz_20130113_Summer12MC_RSGravitonsZZ_20130206_182339/santanas/RSGraviton_ZZlljj_kMpl02_M-1500_TuneZ2star_8TeV-MG/EDBR_PATtuple_edbr_zz_20130113/a2df48025a27dd8dc244a890c390dec0/RSGraviton_ZZlljj_kMpl02_M-1500_TuneZ2star_8TeV-MG__qili-RSZZ_1500_02_AODSIM-c8f8ed334db8a7d6f56c62266b1dfa5b__USER_1_1_rmp.root',
'/store/group/phys_exotica/leptonsPlusJets/ExoDiBosonResonances/santanas/EDBR_PATtuple_edbr_zz_20130113_Summer12MC_RSGravitonsZZ_20130206_182339/santanas/RSGraviton_ZZlljj_kMpl02_M-1500_TuneZ2star_8TeV-MG/EDBR_PATtuple_edbr_zz_20130113/a2df48025a27dd8dc244a890c390dec0/RSGraviton_ZZlljj_kMpl02_M-1500_TuneZ2star_8TeV-MG__qili-RSZZ_1500_02_AODSIM-c8f8ed334db8a7d6f56c62266b1dfa5b__USER_2_1_QBK.root',
'/store/group/phys_exotica/leptonsPlusJets/ExoDiBosonResonances/santanas/EDBR_PATtuple_edbr_zz_20130113_Summer12MC_RSGravitonsZZ_20130206_182339/santanas/RSGraviton_ZZlljj_kMpl02_M-1500_TuneZ2star_8TeV-MG/EDBR_PATtuple_edbr_zz_20130113/a2df48025a27dd8dc244a890c390dec0/RSGraviton_ZZlljj_kMpl02_M-1500_TuneZ2star_8TeV-MG__qili-RSZZ_1500_02_AODSIM-c8f8ed334db8a7d6f56c62266b1dfa5b__USER_3_1_b51.root',
'/store/group/phys_exotica/leptonsPlusJets/ExoDiBosonResonances/santanas/EDBR_PATtuple_edbr_zz_20130113_Summer12MC_RSGravitonsZZ_20130206_182339/santanas/RSGraviton_ZZlljj_kMpl02_M-1500_TuneZ2star_8TeV-MG/EDBR_PATtuple_edbr_zz_20130113/a2df48025a27dd8dc244a890c390dec0/RSGraviton_ZZlljj_kMpl02_M-1500_TuneZ2star_8TeV-MG__qili-RSZZ_1500_02_AODSIM-c8f8ed334db8a7d6f56c62266b1dfa5b__USER_4_1_BBF.root',
'/store/group/phys_exotica/leptonsPlusJets/ExoDiBosonResonances/santanas/EDBR_PATtuple_edbr_zz_20130113_Summer12MC_RSGravitonsZZ_20130206_182339/santanas/RSGraviton_ZZlljj_kMpl02_M-1500_TuneZ2star_8TeV-MG/EDBR_PATtuple_edbr_zz_20130113/a2df48025a27dd8dc244a890c390dec0/RSGraviton_ZZlljj_kMpl02_M-1500_TuneZ2star_8TeV-MG__qili-RSZZ_1500_02_AODSIM-c8f8ed334db8a7d6f56c62266b1dfa5b__USER_5_1_81Q.root',
'/store/group/phys_exotica/leptonsPlusJets/ExoDiBosonResonances/santanas/EDBR_PATtuple_edbr_zz_20130113_Summer12MC_RSGravitonsZZ_20130206_182339/santanas/RSGraviton_ZZlljj_kMpl02_M-1500_TuneZ2star_8TeV-MG/EDBR_PATtuple_edbr_zz_20130113/a2df48025a27dd8dc244a890c390dec0/RSGraviton_ZZlljj_kMpl02_M-1500_TuneZ2star_8TeV-MG__qili-RSZZ_1500_02_AODSIM-c8f8ed334db8a7d6f56c62266b1dfa5b__USER_6_1_9se.root',
'/store/group/phys_exotica/leptonsPlusJets/ExoDiBosonResonances/santanas/EDBR_PATtuple_edbr_zz_20130113_Summer12MC_RSGravitonsZZ_20130206_182339/santanas/RSGraviton_ZZlljj_kMpl02_M-1500_TuneZ2star_8TeV-MG/EDBR_PATtuple_edbr_zz_20130113/a2df48025a27dd8dc244a890c390dec0/RSGraviton_ZZlljj_kMpl02_M-1500_TuneZ2star_8TeV-MG__qili-RSZZ_1500_02_AODSIM-c8f8ed334db8a7d6f56c62266b1dfa5b__USER_7_1_Ebc.root',
'/store/group/phys_exotica/leptonsPlusJets/ExoDiBosonResonances/santanas/EDBR_PATtuple_edbr_zz_20130113_Summer12MC_RSGravitonsZZ_20130206_182339/santanas/RSGraviton_ZZlljj_kMpl02_M-1500_TuneZ2star_8TeV-MG/EDBR_PATtuple_edbr_zz_20130113/a2df48025a27dd8dc244a890c390dec0/RSGraviton_ZZlljj_kMpl02_M-1500_TuneZ2star_8TeV-MG__qili-RSZZ_1500_02_AODSIM-c8f8ed334db8a7d6f56c62266b1dfa5b__USER_8_1_wgb.root',
'/store/group/phys_exotica/leptonsPlusJets/ExoDiBosonResonances/santanas/EDBR_PATtuple_edbr_zz_20130113_Summer12MC_RSGravitonsZZ_20130206_182339/santanas/RSGraviton_ZZlljj_kMpl02_M-1500_TuneZ2star_8TeV-MG/EDBR_PATtuple_edbr_zz_20130113/a2df48025a27dd8dc244a890c390dec0/RSGraviton_ZZlljj_kMpl02_M-1500_TuneZ2star_8TeV-MG__qili-RSZZ_1500_02_AODSIM-c8f8ed334db8a7d6f56c62266b1dfa5b__USER_9_1_mRl.root'
]);
