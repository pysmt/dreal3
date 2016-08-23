/* -*- swig -*- */
/* SWIG interface file to create the Python API for dReal  */

%include "typemaps.i"

/***************************************************************************/

%pythoncode %{

%}

%module drealpy
%{
#include "dreal_c.h"

%}


%include "dreal_c.h"


%{

/* C_STATIC_CODE */

%}


%inline %{

/* C_INLINE_CODE */

%}

/*
%pythoncode %{

## EXTRA_PYTHON_CODE_TAG

%}
*/
