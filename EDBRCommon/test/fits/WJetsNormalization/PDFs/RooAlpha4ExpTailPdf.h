/*****************************************************************************
 * Project: RooFit                                                           *
 *                                                                           *
  * This code was autogenerated by RooClassFactory                            * 
 *****************************************************************************/

#ifndef ROOALPHA4EXPTAILPDF
#define ROOALPHA4EXPTAILPDF

#include "RooAbsPdf.h"
#include "RooRealProxy.h"
#include "RooCategoryProxy.h"
#include "RooAbsReal.h"
#include "RooAbsCategory.h"
 
class RooAlpha4ExpTailPdf : public RooAbsPdf {
public:
  RooAlpha4ExpTailPdf() {} ; 
  RooAlpha4ExpTailPdf(const char *name, const char *title,
	      RooAbsReal& _x,
	      RooAbsReal& _s0,
	      RooAbsReal& _a0,
	      RooAbsReal& _s1,
	      RooAbsReal& _a1);
  RooAlpha4ExpTailPdf(const RooAlpha4ExpTailPdf& other, const char* name=0) ;
  virtual TObject* clone(const char* newname) const { return new RooAlpha4ExpTailPdf(*this,newname); }
  inline virtual ~RooAlpha4ExpTailPdf() { }

protected:

  RooRealProxy x ;
  RooRealProxy s0 ;
  RooRealProxy a0 ;
  RooRealProxy s1 ;
  RooRealProxy a1 ;
  
  Double_t evaluate() const ;

private:

  ClassDef(RooAlpha4ExpTailPdf,1) // Your description goes here...
};
 
#endif
