import FWCore.ParameterSet.Config as cms

# do not really on the default cuts implemented here,
# as they are subject to change. 
# you should override these cuts in your analysis.

cmgDiMuonSel = cms.EDFilter(
    "CmgDiMuonSelector",
    src = cms.InputTag( "cmgDiMuon" ),
    cut = cms.string( "getSelection(\"cuts_zmumu\")" )
    )


