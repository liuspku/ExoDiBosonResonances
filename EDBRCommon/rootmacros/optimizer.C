#include <Riostream.h>
#include <vector>
#include <string>
#include <sstream>

#include "TROOT.h"
#include "TError.h"
#include "TFile.h"
#include "TCollection.h"
#include "TKey.h"
#include "TGraph.h"
#include "TF1.h"
#include "OptimizationMaker.h"
#include "CMSTDRStyle.h"

double optimizer(){

	gErrorIgnoreLevel=kFatal;//suppresses all info messages
	setTDRStyle();//TDR style

	/// Boolean flags to steer the histogram making
	bool wantElectrons = true; // Will make histograms for electrons
	bool wantMuons     = true; // Will make histograms for muons
	bool wantSideband  = false; // Will make histograms for sideband region
	bool wantSignal    = true; // Will make histograms for signal region
	int  wantNXJets    = 1; // Will make histograms for 1 or 2 jet topology
	bool isZZchannel   = false; 
	int  flavour = 0; 
	if(wantElectrons) flavour=11; if(wantMuons) flavour=13;

	/// Luminosity value in pb^-1
	//double lumiValue = 19477.6;
	double lumiValue = 19538.85;// for SingleMu2012

	/// Path to wherever the files with the trees are. 
	//std::string pathToTrees="/afs/cern.ch/user/t/tomei/work/public/EXOVV_2012/analyzer_trees/productionv4/fullsigCA8/";
	//std::string pathToTrees="/afs/cern.ch/user/b/bonato/work/PhysAnalysis/EXOVV_2012/analyzer_trees/productionv1d/fullsig/";
	std::string pathToTrees="/afs/cern.ch/work/s/shuai/public/diboson/trees/productionv8/fullallrange/";

	//do not change this name (it has to be modified in various parts in this file and in ROCcurves.C)
	system("rm -rf optimization_tau21");	
	system("mkdir  optimization_tau21");
	
	/*
       /// Setup names of data files for trees.
       const int nDATA=0;
       std::vector<std::string> fData;
       fData.clear();
	*/

	/// Setup names of MC files for trees.

	//ZZ
	/*
  const int nMC=7;//set to zero if you don't want to plot
  std::string mcLabels[nMC]={
                 "TTBARpowheg",
                 "WW",
                 "WZ",
                 "ZZ",
                 "DYJetsPt50To70",
                 "DYJetsPt70To100",
                 "DYJetsPt100",
                 //"WJetsPt50To70",
                 //"WJetsPt70To100",
		 // "WJetsPt100",
		 //"WJetsPt180",
                 };
	*/
	//WW
  const int nMC=5;//set to zero if you don't want to plot
  std::string mcLabels[nMC]={//"TTBAR_xww",
                               "TTBARpowheg_xww",
			     //"SingleTopBarTWchannel_xww",
			     //"SingleTopTWchannel_xww",
			     //"SingleTopBarSchannel_xww", 
			     //"SingleTopSchannel_xww",
			     //"SingleTopBarTchannel_xww",
			     //"SingleTopTchannel_xww",
				"SingleTop_xww",
			     //"WW_xww",
			     //"WZ_xww",
			     //"ZZ_xww",
				"VV_xww",
			     //"DYJetsPt50To70_xww",
			     //"DYJetsPt70To100_xww",
			     //"DYJetsPt100_xww",
				"DYJets_xww",
			     //"WJetsPt50To70_xww",
			     //"WJetsPt70To100_xww",
			     "WJetsPt180_xww",
			       //   "WJetsPt100_xww",
			     };


	std::vector<std::string> fMC;
	for(int ii=0;ii<nMC;ii++){
		fMC.push_back(pathToTrees+"treeEDBR_"+mcLabels[ii]+".root");
	}


	char buffer[256];
	printf("All strings set\n");

	/// ----------------------------------------------------------------
	/// This first part is the loop over trees to create histogram files 
	/// ----------------------------------------------------------------

	/// The EDBRHistoMaker, for reference
	///
	///EDBRHistoMaker::EDBRHistoMaker(TTree* tree, 
	///		       bool wantElectrons,
	///		       bool wantMuons,
	///		       bool wantSideband,
	///		       bool wantSignal,
	///		       int wantNXJets)


	//loop over MC files and make histograms individually for each of them
	for(int i=0;i<nMC;i++){
		std::cout<<"\n-------\nRunning over "<<mcLabels[i].c_str()<<std::endl;
		std::cout<<"The file is " <<fMC.at(i)<<std::endl;    
		sprintf(buffer,"optimization_tau21/background_%s.root",mcLabels[i].c_str());


		TFile *fileMC = TFile::Open(fMC.at(i).c_str());
		TTree *treeMC = (TTree*)fileMC->Get("SelectedCandidates");
		OptimizationMaker* maker = new OptimizationMaker(treeMC, 
				wantElectrons, 
				wantMuons, 
				wantSideband, 
				wantSignal, 
				wantNXJets,
				isZZchannel);
		maker->setUnitaryWeights(false);
		maker->setLumi(lumiValue);
		maker->Loop(buffer,1000,0.15);
		//delete maker; // This class is badly written and deleting it isn't safe!
		fileMC->Close();

	}//end loop on MC files

	// The signal:
	std::vector<int> massPoints;
	/*
	massPoints.push_back(600); 
	massPoints.push_back(700); 
	massPoints.push_back(800);
	massPoints.push_back(900); 
	massPoints.push_back(1000); 
	massPoints.push_back(1100); 
	massPoints.push_back(1300); 
	massPoints.push_back(1400); 
	massPoints.push_back(1500); 
	massPoints.push_back(1700); 
	massPoints.push_back(1800); 
	massPoints.push_back(1900);
	*/

	massPoints.push_back(600); 
	massPoints.push_back(700); 
	massPoints.push_back(800);
	massPoints.push_back(900); 
	massPoints.push_back(1000); 
	massPoints.push_back(1100); 
	massPoints.push_back(1200); 
	massPoints.push_back(1300); 
	massPoints.push_back(1400); 
	massPoints.push_back(1500); 
	massPoints.push_back(1600); 
	massPoints.push_back(1700); 
	massPoints.push_back(1800); 
	massPoints.push_back(1900);
	massPoints.push_back(2000);
	massPoints.push_back(2100);
	massPoints.push_back(2200);
	massPoints.push_back(2300);
	massPoints.push_back(2400);
	massPoints.push_back(2500);

	for(size_t i=0; i!=massPoints.size(); ++i)
	{
		std::stringstream pathToSignal;
		//pathToSignal << pathToTrees << "treeEDBR_BulkG_ZZ_lljj_c0p2_M"
		pathToSignal << pathToTrees << "treeEDBR_BulkG_WW_lvjj_c0p2_M"
			     << massPoints.at(i) << "_xww.root";
				//<< massPoints.at(i) << ".root";
		printf("Running over %s\n",pathToSignal.str().c_str());
		sprintf(buffer,"optimization_tau21/signal_%i.root",massPoints.at(i));

		TFile *fileMC = TFile::Open(pathToSignal.str().c_str());
		TTree *treeMC = (TTree*)fileMC->Get("SelectedCandidates");    
		OptimizationMaker* maker = new OptimizationMaker(treeMC, 
				wantElectrons, 
				wantMuons, 
				wantSideband, 
				wantSignal, 
				wantNXJets,
				isZZchannel);
		maker->setUnitaryWeights(false);
		maker->setLumi(lumiValue);
		maker->Loop(buffer,1000,0.15);
	}

	system("hadd -f optimization_tau21/allBackgrounds.root optimization_tau21/background_*");
	return 0.0;
}//end main
