#! /bin/bash

SampleName=( BulkG_ZZ_lljj_c1p0_M600 BulkG_ZZ_lljj_c1p0_M1500 RSG_WW_lvjj_c0p2_M1000 BulkG_ZZ_lljj_c0p2_M1000 RSG_ZZ_lljj_c0p05_M1000 RSG_ZZ_lljj_c0p2_M1000 RSG_ZZ_lljj_c0p2_M1500  TTBAR DYJetsPt50To70 DYJetsPt70To100 DYJetsPt100 WW WZ ZZ DoubleMu_Run2012A_13Jul2012 DoubleMu_Run2012A_recover DoubleMu_Run2012B_13Jul2012 DoubleMu_Run2012C_24Aug2012 DoubleMu_Run2012C_PRv2 DoubleMu_Run2012D_PRv1 DoublePhotonHighPt_Run2012B_13Jul2012  DoublePhotonHighPt_Run2012C_24Aug2012 DoublePhotonHighPt_Run2012C_PRv2 DoublePhotonHighPt_Run2012D_PRv1 Photon_Run2012A_13Jul2012 Photon_Run2012A_recover )

for sample in  "${SampleName[@]}"
do
echo "Submitting $sample"
bsub -q 8nh -J "treeEDBR_${sample}" run_AnalyzerEDBR.sh $sample
echo
done

#${CMSSW_BASE}/ExoDiBosonResonances/EDBRCommon/test/
