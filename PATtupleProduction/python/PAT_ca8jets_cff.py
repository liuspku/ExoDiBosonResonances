import FWCore.ParameterSet.Config as cms

# JETS  CA8 ----------------------------

from RecoJets.JetProducers.ak5PFJets_cfi import ak5PFJets
ca8PFJetsCHS = ak5PFJets.clone(
    src = 'pfNoPileUp',
    jetPtMin = cms.double(10.0),
    doAreaFastjet = cms.bool(True),
    rParam = cms.double(0.8),
    jetAlgorithm = cms.string("CambridgeAachen"),
    )

jetSource = 'ca8PFJetsCHS'

# corrections 
from PhysicsTools.PatAlgos.recoLayer0.jetCorrFactors_cfi import *
patJetCorrFactorsCA8CHS = patJetCorrFactors.clone()
patJetCorrFactorsCA8CHS.src = jetSource
# will need to add L2L3 corrections in the cfg
patJetCorrFactorsCA8CHS.levels = ['L1FastJet', 'L2Relative', 'L3Absolute']
patJetCorrFactorsCA8CHS.payload = 'AK7PFchs'
patJetCorrFactorsCA8CHS.useRho = True

# parton and gen jet matching

from PhysicsTools.PatAlgos.mcMatchLayer0.jetMatch_cfi import *
patJetPartonMatchCA8CHS = patJetPartonMatch.clone()
patJetPartonMatchCA8CHS.src = jetSource
patJetGenJetMatchCA8CHS = patJetGenJetMatch.clone()
patJetGenJetMatchCA8CHS.src = jetSource
patJetGenJetMatchCA8CHS.matched = 'ca8GenJetsNoNu'

from PhysicsTools.PatAlgos.mcMatchLayer0.jetFlavourId_cff import *
patJetPartonAssociationCA8CHS = patJetPartonAssociation.clone()
patJetPartonAssociationCA8CHS.jets = jetSource

# pat jets

from PhysicsTools.PatAlgos.producersLayer1.jetProducer_cfi import *
patJetsCA8CHS = patJets.clone()
patJetsCA8CHS.jetSource = jetSource
patJetsCA8CHS.addJetCharge = False
patJetsCA8CHS.embedCaloTowers = False
patJetsCA8CHS.embedPFCandidates = False
patJetsCA8CHS.addAssociatedTracks = False
patJetsCA8CHS.addBTagInfo = False
patJetsCA8CHS.addDiscriminators = False
patJetsCA8CHS.getJetMCFlavour = False
patJetsCA8CHS.jetCorrFactorsSource = cms.VInputTag(cms.InputTag('patJetCorrFactorsCA8CHS'))
patJetsCA8CHS.genPartonMatch = cms.InputTag('patJetPartonMatchCA8CHS')
patJetsCA8CHS.genJetMatch = cms.InputTag('patJetGenJetMatchCA8CHS')

from PhysicsTools.PatAlgos.selectionLayer1.jetSelector_cfi import *
selectedPatJetsCA8CHS = selectedPatJets.clone()
selectedPatJetsCA8CHS.src = 'patJetsCA8CHS'
selectedPatJetsCA8CHS.cut = 'pt()>20'

from RecoJets.Configuration.RecoGenJets_cff import ak7GenJetsNoNu
ca8GenJetsNoNu = ak7GenJetsNoNu.clone()
ca8GenJetsNoNu.rParam = 0.8
ca8GenJetsNoNu.jetAlgorithm = "CambridgeAachen"

from RecoJets.Configuration.GenJetParticles_cff import genParticlesForJetsNoNu
jetMCSequenceCA8CHS = cms.Sequence(
    patJetPartonMatchCA8CHS +
    genParticlesForJetsNoNu +
    ca8GenJetsNoNu +
    patJetGenJetMatchCA8CHS
    )

PATCMGJetSequenceCA8CHS = cms.Sequence(
    ca8PFJetsCHS +
    jetMCSequenceCA8CHS +
    patJetCorrFactorsCA8CHS +
    patJetsCA8CHS +
    selectedPatJetsCA8CHS
    )

# JETS PRUNED CA8 ----------------------------

from RecoJets.JetProducers.ak5PFJetsPruned_cfi import ak5PFJetsPruned
ca8PFJetsCHSpruned = ak5PFJetsPruned.clone(
    src = 'pfNoPileUp',
    jetPtMin = cms.double(10.0),
    doAreaFastjet = cms.bool(True),
    rParam = cms.double(0.8),
    jetAlgorithm = cms.string("CambridgeAachen"),
    )

jetSource = 'ca8PFJetsCHSpruned'

# corrections 
from PhysicsTools.PatAlgos.recoLayer0.jetCorrFactors_cfi import *
patJetCorrFactorsCA8CHSpruned = patJetCorrFactors.clone()
patJetCorrFactorsCA8CHSpruned.src = jetSource
# will need to add L2L3 corrections in the cfg
patJetCorrFactorsCA8CHSpruned.levels = ['L1FastJet', 'L2Relative', 'L3Absolute']
patJetCorrFactorsCA8CHSpruned.payload = 'AK7PFchs'
patJetCorrFactorsCA8CHSpruned.useRho = True

# parton and gen jet matching

from PhysicsTools.PatAlgos.mcMatchLayer0.jetMatch_cfi import *
patJetPartonMatchCA8CHSpruned = patJetPartonMatch.clone()
patJetPartonMatchCA8CHSpruned.src = jetSource
patJetGenJetMatchCA8CHSpruned = patJetGenJetMatch.clone()
patJetGenJetMatchCA8CHSpruned.src = jetSource
patJetGenJetMatchCA8CHSpruned.matched = 'ca8GenJetsNoNu'

from PhysicsTools.PatAlgos.mcMatchLayer0.jetFlavourId_cff import *
patJetPartonAssociationCA8CHSpruned = patJetPartonAssociation.clone()
patJetPartonAssociationCA8CHSpruned.jets = jetSource

# pat jets

from PhysicsTools.PatAlgos.producersLayer1.jetProducer_cfi import *
patJetsCA8CHSpruned = patJets.clone()
patJetsCA8CHSpruned.jetSource = jetSource
patJetsCA8CHSpruned.addJetCharge = False
patJetsCA8CHSpruned.embedCaloTowers = False
patJetsCA8CHSpruned.embedPFCandidates = False
patJetsCA8CHSpruned.addAssociatedTracks = False
patJetsCA8CHSpruned.addBTagInfo = False
patJetsCA8CHSpruned.addDiscriminators = False
patJetsCA8CHSpruned.getJetMCFlavour = False
patJetsCA8CHSpruned.jetCorrFactorsSource = cms.VInputTag(cms.InputTag('patJetCorrFactorsCA8CHSpruned'))
patJetsCA8CHSpruned.genPartonMatch = cms.InputTag('patJetPartonMatchCA8CHSpruned')
patJetsCA8CHSpruned.genJetMatch = cms.InputTag('patJetGenJetMatchCA8CHSpruned')

from PhysicsTools.PatAlgos.selectionLayer1.jetSelector_cfi import *
selectedPatJetsCA8CHSpruned = selectedPatJets.clone()
selectedPatJetsCA8CHSpruned.src = 'patJetsCA8CHSpruned'
selectedPatJetsCA8CHSpruned.cut = 'pt()>20'

jetMCSequenceCA8CHSpruned = cms.Sequence(
    patJetPartonMatchCA8CHSpruned +
    patJetGenJetMatchCA8CHSpruned
    )

PATCMGJetSequenceCA8CHSpruned = cms.Sequence(
    ca8PFJetsCHSpruned +
    jetMCSequenceCA8CHSpruned +
    patJetCorrFactorsCA8CHSpruned +
    patJetsCA8CHSpruned +
    selectedPatJetsCA8CHSpruned
    )


#### Adding Nsubjetiness

selectedPatJetsCA8CHSwithNsub = cms.EDProducer("NjettinessAdder",
                              src=cms.InputTag("selectedPatJetsCA8CHS"),
                              cone=cms.double(0.8)
                              )

#### Adding QJets

selectedPatJetsCA8CHSwithQjets = cms.EDProducer("QjetsAdder",
                               src=cms.InputTag("selectedPatJetsCA8CHSwithNsub"),
                               zcut=cms.double(0.1),
                               dcutfctr=cms.double(0.5),
                               expmin=cms.double(0.0),
                               expmax=cms.double(0.0),
                               rigidity=cms.double(0.1),
                               ntrial = cms.int32(50),
                               cutoff=cms.double(100.0),
                               jetRad= cms.double(0.8),
                               jetAlgo=cms.string("CA"),
                               preclustering = cms.int32(50),
                              )

ca8Jets = cms.Sequence( PATCMGJetSequenceCA8CHS + PATCMGJetSequenceCA8CHSpruned + selectedPatJetsCA8CHSwithNsub + selectedPatJetsCA8CHSwithQjets )
