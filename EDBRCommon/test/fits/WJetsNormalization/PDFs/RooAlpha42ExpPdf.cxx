/***************************************************************************** 
 * Project: RooFit                                                           * 
 *                                                                           * 
 * This code was autogenerated by RooClassFactory                            * 
 *****************************************************************************/ 

// Your description goes here... 

#include "Riostream.h" 

#include "RooAlpha42ExpPdf.h" 
#include "RooAbsReal.h" 
#include "RooAbsCategory.h" 
#include <math.h> 
#include "TMath.h" 

ClassImp(RooAlpha42ExpPdf) 

 RooAlpha42ExpPdf::RooAlpha42ExpPdf(const char *name, const char *title, 
                        RooAbsReal& _x,
                        RooAbsReal& _c00,
                        RooAbsReal& _c01,
                        RooAbsReal& _frac0,
                        RooAbsReal& _c10,
                        RooAbsReal& _c11,
                        RooAbsReal& _frac1) :
   RooAbsPdf(name,title), 
   x("x","x",this,_x),
   c00("c00","c00",this,_c00),
   c01("c01","c01",this,_c01),
   frac0("frac0","frac0",this,_frac0),
   c10("c10","c10",this,_c10),
   c11("c11","c11",this,_c11),
   frac1("frac1","frac1",this,_frac1)
 { 
 } 


 RooAlpha42ExpPdf::RooAlpha42ExpPdf(const RooAlpha42ExpPdf& other, const char* name) :  
   RooAbsPdf(other,name), 
   x("x",this,other.x),
   c00("c00",this,other.c00),
   c01("c01",this,other.c01),
   frac0("frac0",this,other.frac0),
   c10("c10",this,other.c10),
   c11("c11",this,other.c11),
   frac1("frac1",this,other.frac1)
 { 
 } 



 Double_t RooAlpha42ExpPdf::evaluate() const 
 { 
   // ENTER EXPRESSION IN TERMS OF VARIABLE ARGUMENTS HERE 
   return 1.0 ; 
 } 


