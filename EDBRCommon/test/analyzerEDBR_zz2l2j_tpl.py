import FWCore.ParameterSet.Config as cms
from PhysicsTools.PatAlgos.tools.helpers import *
process = cms.Process("EDBR")
process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1))
process.load("FWCore.MessageLogger.MessageLogger_cfi")
process.MessageLogger.cerr.FwkReport.reportEvery = 1000
process.load("Configuration.Geometry.GeometryIdeal_cff")
process.load("Configuration.StandardSequences.FrontierConditions_GlobalTag_cff")
process.GlobalTag.globaltag = cms.string("START53_V7A::All")
process.load("Configuration.StandardSequences.MagneticField_cff")


### input cmgTuples
process.load("ExoDiBosonResonances.EDBRCommon.datasets.cmgTuple_<SAMPLE>_cff")

## process.source = cms.Source("PoolSource",
##                     noEventSort = cms.untracked.bool(True),
##                     duplicateCheckMode = cms.untracked.string("noDuplicateCheck"),
##                     fileNames = cms.untracked.vstring(
##     '/store/group/phys_exotica/leptonsPlusJets/ExoDiBosonResonances/CMGtuple/productionV1/Summer12/presel/TTBAR/test_0.root')
##                     )



from ExoDiBosonResonances.EDBRCommon.analyzerEDBR_cfi import AnalyzerXZZ
process.ANEDBR = AnalyzerXZZ.clone(
    debug=cms.bool(False),
    outFileName=cms.string("treeEDBR_<SAMPLE>.root"),
    Ngen=cms.uint32(1),
    xsec=cms.double(1.0) ###in pb
    )



### if false, use the default collections
### in ExoDiBosonResonances.EDBRCommon.analyzerEDBR_cfi
### (i.e. all the cands passing pre-selection cuts)
processFullSel=False 

if processFullSel :
    process.ANEDBR.EDBREEJJColl=cms.InputTag("BestSidebandSelectorEle:doubleJet")
    process.ANEDBR.EDBRMMJJColl=cms.InputTag("BestSidebandSelectorMu:doubleJet")
    process.ANEDBR.EDBREEJColl=cms.InputTag("BestSidebandSelectorEle:singleJet")
    process.ANEDBR.EDBRMMJColl=cms.InputTag("BestSidebandSelectorMu:singleJet")



##### set Ngen and xsect values ofr MC samples
if "<SAMPLE>"=="TTBAR" :
    process.ANEDBR.Ngen=cms.uint32(6540800)
    process.ANEDBR.xsec=cms.double(225.197)
elif "<SAMPLE>"=="DYJetsPt50To70" :
    process.ANEDBR.Ngen=cms.uint32(4823000)
    process.ANEDBR.xsec=cms.double(89.0)
    process.ANEDBR.FillGenLevelCode=cms.uint32(1)
elif "<SAMPLE>"=="DYJetsPt70To100" :
    process.ANEDBR.Ngen=cms.uint32(4000000)
    process.ANEDBR.xsec=cms.double(53.0)
    process.ANEDBR.FillGenLevelCode=cms.uint32(1)
elif "<SAMPLE>"=="DYJetsPt100" :
    process.ANEDBR.Ngen=cms.uint32(2500000)
    process.ANEDBR.xsec=cms.double(32.9)
    process.ANEDBR.FillGenLevelCode=cms.uint32(1)
elif "<SAMPLE>"=="WW" :
    process.ANEDBR.Ngen=cms.uint32(3870000)
    process.ANEDBR.xsec=cms.double(57.1097)
elif "<SAMPLE>"=="WZ" :
    process.ANEDBR.Ngen=cms.uint32(1910000)
    process.ANEDBR.xsec=cms.double(22.88)
elif "<SAMPLE>"=="ZZ" :
    process.ANEDBR.Ngen=cms.uint32(485716)
    process.ANEDBR.xsec=cms.double(5.196)
    process.ANEDBR.FillGenLevelCode=cms.uint32(3)
### MC signal
elif "<SAMPLE>"=="BulkG_ZZ_lljj_c1p0_M600" :
    process.ANEDBR.Ngen=cms.uint32(41965)
    process.ANEDBR.xsec=cms.double(652000.0)
    process.ANEDBR.FillGenLevelCode=cms.uint32(7)
elif "<SAMPLE>"=="BulkG_ZZ_lljj_c1p0_M1500" :
    process.ANEDBR.Ngen=cms.uint32(40938)
    process.ANEDBR.xsec=cms.double(17700.0)
    process.ANEDBR.FillGenLevelCode=cms.uint32(7)
elif "<SAMPLE>"=="BulkG_ZZ_lljj_c0p2_M1000" :
    process.ANEDBR.Ngen=cms.uint32(40964)
    process.ANEDBR.xsec=cms.double(86200.0)
    process.ANEDBR.FillGenLevelCode=cms.uint32(7)
elif "<SAMPLE>"=="RSG_ZZ_lljj_c0p05_M1000" :
    process.ANEDBR.Ngen=cms.uint32(38022)
    process.ANEDBR.xsec=cms.double(3122.0)
    process.ANEDBR.FillGenLevelCode=cms.uint32(7)
elif "<SAMPLE>"=="RSG_ZZ_lljj_c0p2_M1000" :
    process.ANEDBR.Ngen=cms.uint32(37410)
    process.ANEDBR.xsec=cms.double(48240.0)
    process.ANEDBR.FillGenLevelCode=cms.uint32(7)
elif "<SAMPLE>"=="RSG_ZZ_lljj_c0p2_M1500" :
    process.ANEDBR.Ngen=cms.uint32(24996)
    process.ANEDBR.xsec=cms.double(3877.0)
    process.ANEDBR.FillGenLevelCode=cms.uint32(7)
elif "<SAMPLE>"=="RSG_WW_lvjj_c0p2_M1000" :
    process.ANEDBR.Ngen=cms.uint32(34541)
    process.ANEDBR.xsec=cms.double(402400.0)
    process.ANEDBR.FillGenLevelCode=cms.uint32(7)
### Data Ele
elif "<SAMPLE>"=="Photon_Run2012A_13Jul2012" :
    process.ANEDBR.Ngen=cms.uint32(1)
    process.ANEDBR.xsec=cms.double(1)
    process.ANEDBR.isMC=cms.bool(False)
elif "<SAMPLE>"=="Photon_Run2012A_recover" :
    process.ANEDBR.Ngen=cms.uint32(1)
    process.ANEDBR.xsec=cms.double(1)
    process.ANEDBR.isMC=cms.bool(False)
elif "<SAMPLE>"=="DoublePhotonHighPt_Run2012B_13Jul2012" :
    process.ANEDBR.Ngen=cms.uint32(1)
    process.ANEDBR.xsec=cms.double(1)
    process.ANEDBR.isMC=cms.bool(False)
elif "<SAMPLE>"=="DoublePhotonHighPt_Run2012C_24Aug2012" :
    process.ANEDBR.Ngen=cms.uint32(1)
    process.ANEDBR.xsec=cms.double(1)
    process.ANEDBR.isMC=cms.bool(False)
elif "<SAMPLE>"=="DoublePhotonHighPt_Run2012C_PRv2" :
    process.ANEDBR.Ngen=cms.uint32(1)
    process.ANEDBR.xsec=cms.double(1)
    process.ANEDBR.isMC=cms.bool(False)
elif "<SAMPLE>"=="DoublePhotonHighPt_Run2012D_PRv1" :
    process.ANEDBR.Ngen=cms.uint32(1)
    process.ANEDBR.xsec=cms.double(1)
    process.ANEDBR.isMC=cms.bool(False)
    
else :
    print 'ERROR !!! Sample named <SAMPLE> was not recognized !'

print '---> Ngen=',process.ANEDBR.Ngen,'  Xsect=',process.ANEDBR.xsec



process.filterFinalSelPath = cms.EDFilter("HLTHighLevel",
                                       TriggerResultsTag = cms.InputTag("TriggerResults","","CMG"),
                                       HLTPaths = cms.vstring("cmgEDBRZZEle","cmgEDBRZZMu"),
                                       eventSetupPathsKey = cms.string(''),
                                       andOr = cms.bool(True),  # how to deal with multiple triggers: True (OR) accept if ANY is true, False (AND) accept if ALL are true
                                       throw = cms.bool(True)    # throw exception on unknown path names
                                       )

if processFullSel :
    process.p=cms.Path(process.filterFinalSelPath+process.ANEDBR)
else :
    process.p=cms.Path(process.ANEDBR)
