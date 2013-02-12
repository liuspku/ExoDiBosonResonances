import FWCore.ParameterSet.Config as cms
maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ('PoolSource',fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend([
'/store/group/phys_exotica/leptonsPlusJets/ExoDiBosonResonances/santanas/EDBR_PATtuple_edbr_zz_20130113_Summer12MC_BulkGravitonsZZ_20130206_194506/santanas/JHU_Bulk1000_ZZ_c1_v2/EDBR_PATtuple_edbr_zz_20130113/a2df48025a27dd8dc244a890c390dec0/JHU_Bulk1000_ZZ_c1_v2__tomei-JHU_Bulk1000_ZZ_c1_STEP3-c8f8ed334db8a7d6f56c62266b1dfa5b__USER_1_1_Lov.root',
'/store/group/phys_exotica/leptonsPlusJets/ExoDiBosonResonances/santanas/EDBR_PATtuple_edbr_zz_20130113_Summer12MC_BulkGravitonsZZ_20130206_194506/santanas/JHU_Bulk1000_ZZ_c1_v2/EDBR_PATtuple_edbr_zz_20130113/a2df48025a27dd8dc244a890c390dec0/JHU_Bulk1000_ZZ_c1_v2__tomei-JHU_Bulk1000_ZZ_c1_STEP3-c8f8ed334db8a7d6f56c62266b1dfa5b__USER_2_1_JCc.root',
'/store/group/phys_exotica/leptonsPlusJets/ExoDiBosonResonances/santanas/EDBR_PATtuple_edbr_zz_20130113_Summer12MC_BulkGravitonsZZ_20130206_194506/santanas/JHU_Bulk1000_ZZ_c1_v2/EDBR_PATtuple_edbr_zz_20130113/a2df48025a27dd8dc244a890c390dec0/JHU_Bulk1000_ZZ_c1_v2__tomei-JHU_Bulk1000_ZZ_c1_STEP3-c8f8ed334db8a7d6f56c62266b1dfa5b__USER_3_1_ItT.root',
'/store/group/phys_exotica/leptonsPlusJets/ExoDiBosonResonances/santanas/EDBR_PATtuple_edbr_zz_20130113_Summer12MC_BulkGravitonsZZ_20130206_194506/santanas/JHU_Bulk1000_ZZ_c1_v2/EDBR_PATtuple_edbr_zz_20130113/a2df48025a27dd8dc244a890c390dec0/JHU_Bulk1000_ZZ_c1_v2__tomei-JHU_Bulk1000_ZZ_c1_STEP3-c8f8ed334db8a7d6f56c62266b1dfa5b__USER_4_1_qIn.root',
'/store/group/phys_exotica/leptonsPlusJets/ExoDiBosonResonances/santanas/EDBR_PATtuple_edbr_zz_20130113_Summer12MC_BulkGravitonsZZ_20130206_194506/santanas/JHU_Bulk1000_ZZ_c1_v2/EDBR_PATtuple_edbr_zz_20130113/a2df48025a27dd8dc244a890c390dec0/JHU_Bulk1000_ZZ_c1_v2__tomei-JHU_Bulk1000_ZZ_c1_STEP3-c8f8ed334db8a7d6f56c62266b1dfa5b__USER_5_1_mpo.root',
'/store/group/phys_exotica/leptonsPlusJets/ExoDiBosonResonances/santanas/EDBR_PATtuple_edbr_zz_20130113_Summer12MC_BulkGravitonsZZ_20130206_194506/santanas/JHU_Bulk1000_ZZ_c1_v2/EDBR_PATtuple_edbr_zz_20130113/a2df48025a27dd8dc244a890c390dec0/JHU_Bulk1000_ZZ_c1_v2__tomei-JHU_Bulk1000_ZZ_c1_STEP3-c8f8ed334db8a7d6f56c62266b1dfa5b__USER_6_1_1NQ.root',
'/store/group/phys_exotica/leptonsPlusJets/ExoDiBosonResonances/santanas/EDBR_PATtuple_edbr_zz_20130113_Summer12MC_BulkGravitonsZZ_20130206_194506/santanas/JHU_Bulk1000_ZZ_c1_v2/EDBR_PATtuple_edbr_zz_20130113/a2df48025a27dd8dc244a890c390dec0/JHU_Bulk1000_ZZ_c1_v2__tomei-JHU_Bulk1000_ZZ_c1_STEP3-c8f8ed334db8a7d6f56c62266b1dfa5b__USER_7_1_x3j.root',
'/store/group/phys_exotica/leptonsPlusJets/ExoDiBosonResonances/santanas/EDBR_PATtuple_edbr_zz_20130113_Summer12MC_BulkGravitonsZZ_20130206_194506/santanas/JHU_Bulk1000_ZZ_c1_v2/EDBR_PATtuple_edbr_zz_20130113/a2df48025a27dd8dc244a890c390dec0/JHU_Bulk1000_ZZ_c1_v2__tomei-JHU_Bulk1000_ZZ_c1_STEP3-c8f8ed334db8a7d6f56c62266b1dfa5b__USER_8_1_5o1.root',
'/store/group/phys_exotica/leptonsPlusJets/ExoDiBosonResonances/santanas/EDBR_PATtuple_edbr_zz_20130113_Summer12MC_BulkGravitonsZZ_20130206_194506/santanas/JHU_Bulk1000_ZZ_c1_v2/EDBR_PATtuple_edbr_zz_20130113/a2df48025a27dd8dc244a890c390dec0/JHU_Bulk1000_ZZ_c1_v2__tomei-JHU_Bulk1000_ZZ_c1_STEP3-c8f8ed334db8a7d6f56c62266b1dfa5b__USER_9_1_uRx.root'
]);
