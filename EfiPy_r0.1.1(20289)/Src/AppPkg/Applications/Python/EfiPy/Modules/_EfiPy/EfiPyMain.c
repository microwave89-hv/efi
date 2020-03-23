/*
 * EfiPyMain.c
 *
 * Copyright (C) 2014 - 2015 efipy.core@gmail.com All rights reserved.
 *
 * EfiPyMain.c is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, version 2 of the License.
 *
 * EfiPy is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along with EfiPy.  If not, see <http://www.gnu.org/licenses/>.
 */


#include <Python.h>
#include "structmember.h"

#include <Base.h>
#include <Library/UefiLib.h>
#include <Library/BaseLib.h>
#include <Library/UefiRuntimeServicesTableLib.h>
#include <Library/UefiBootServicesTableLib.h>

extern EFI_HANDLE pImageHandle;

/*************************************************************************
 * PRIVATE EfiPy_Processor_Init
 *************************************************************************/
int EfiPy_Processor_Init (PyObject *Module)
{
  int       ret;

#define EFIPY_MDE_CPU_IA32    0
#define EFIPY_MDE_CPU_IPF     1
#define EFIPY_MDE_CPU_X64     2
#define EFIPY_MDE_CPU_ARM     3
#define EFIPY_MDE_CPU_AARCH64 4
#define EFIPY_MDE_CPU_EBC     5

  ret = PyModule_AddIntMacro (Module, EFIPY_MDE_CPU_IA32);
  if (ret != 0) {
    return ret;
  }

  ret = PyModule_AddIntMacro (Module, EFIPY_MDE_CPU_IPF);
  if (ret != 0) {
    return ret;
  }

  ret = PyModule_AddIntMacro (Module, EFIPY_MDE_CPU_X64);
  if (ret != 0) {
    return ret;
  }

  ret = PyModule_AddIntMacro (Module, EFIPY_MDE_CPU_ARM);
  if (ret != 0) {
    return ret;
  }

  ret = PyModule_AddIntMacro (Module, EFIPY_MDE_CPU_AARCH64);
  if (ret != 0) {
    return ret;
  }

  ret = PyModule_AddIntMacro (Module, EFIPY_MDE_CPU_EBC);
  if (ret != 0) {
    return ret;
  }

#if defined (MDE_CPU_IA32)
  ret = PyModule_AddIntConstant (Module, "EFIPY_MDE_CPU_TYPE", EFIPY_MDE_CPU_IA32);
#elif defined (MDE_CPU_IPF) 
  ret = PyModule_AddIntConstant (Module, "EFIPY_MDE_CPU_TYPE", EFIPY_MDE_CPU_IPF);
#elif defined (MDE_CPU_X64)
  ret = PyModule_AddIntConstant (Module, "EFIPY_MDE_CPU_TYPE", EFIPY_MDE_CPU_X64);
#elif defined (MDE_CPU_ARM)
  ret = PyModule_AddIntConstant (Module, "EFIPY_MDE_CPU_TYPE", EFIPY_MDE_CPU_ARM);
#elif defined (MDE_CPU_AARCH64)
  ret = PyModule_AddIntConstant (Module, "EFIPY_MDE_CPU_TYPE", EFIPY_MDE_CPU_AARCH64);
#elif defined (MDE_CPU_EBC)
  ret = PyModule_AddIntConstant (Module, "EFIPY_MDE_CPU_TYPE", EFIPY_MDE_CPU_EBC);
#else
#error Unknown Processor Type
#endif

  if (ret != 0) {
    return ret;
  }

  return ret;

} // EfiPy_Processor_Init

/*************************************************************************
 * PRIVATE EfiPy_Constant_Init
 *************************************************************************/
int EfiPy_Constant_Init (PyObject *Module)
{

  int       ret;
  PyObject *PyObject_MAX_BIT;
  PyObject *PyObject_MAX_2_BITS;
  PyObject *PyObject_MAX_ADDRESS;
  PyObject *PyObject_CPU_STACK_ALIGNMENT;
  PyObject *PyObject_gImageHandle;
  PyObject *PyObject_pImageHandle;
  PyObject *PyObject_gST;
  PyObject *PyObject_gRT;
  PyObject *PyObject_gBS;

  //
  // ProcessorBind
  //

  PyObject_MAX_BIT              = PyLong_FromUnsignedLongLong (MAX_BIT);
  Py_INCREF (PyObject_MAX_BIT);
  ret = PyModule_AddObject (Module, "MAX_BIT", PyObject_MAX_BIT);
  if (ret != 0) {
    return ret;
  }

  PyObject_MAX_2_BITS           = PyLong_FromUnsignedLongLong (MAX_2_BITS);
  Py_INCREF (PyObject_MAX_2_BITS);
  ret = PyModule_AddObject (Module, "MAX_2_BITS", PyObject_MAX_2_BITS);
  if (ret != 0) {
    return ret;
  }

  PyObject_MAX_ADDRESS          = PyLong_FromUnsignedLongLong (MAX_ADDRESS);
  Py_INCREF (PyObject_MAX_ADDRESS);
  ret = PyModule_AddObject (Module, "MAX_ADDRESS", PyObject_MAX_ADDRESS);
  if (ret != 0) {
    return ret;
  }

  PyObject_CPU_STACK_ALIGNMENT  = PyLong_FromUnsignedLongLong (CPU_STACK_ALIGNMENT);
  Py_INCREF (PyObject_CPU_STACK_ALIGNMENT);
  ret = PyModule_AddObject (Module, "CPU_STACK_ALIGNMENT", PyObject_CPU_STACK_ALIGNMENT);
  if (ret != 0) {
    return ret;
  }

  //
  // Process Handles
  //

  PyObject_gImageHandle         = PyLong_FromVoidPtr(&gImageHandle);
  Py_INCREF (PyObject_gImageHandle);
  ret = PyModule_AddObject (Module, "gImageHandle", PyObject_gImageHandle);
  if (ret != 0) {
    return ret;
  }

  PyObject_pImageHandle         = PyLong_FromVoidPtr(&pImageHandle);
  Py_INCREF (PyObject_pImageHandle);
  ret = PyModule_AddObject (Module, "pImageHandle", PyObject_pImageHandle);
  if (ret != 0) {
    return ret;
  }

  //
  // Table address
  //

  PyObject_gST                  = PyLong_FromVoidPtr(gST);
  Py_INCREF (PyObject_gST);
  ret = PyModule_AddObject (Module, "EfiPygStAddr", PyObject_gST);
  if (ret != 0) {
    return ret;
  }

  PyObject_gRT                  = PyLong_FromVoidPtr(gRT);
  Py_INCREF (PyObject_gRT);
  ret = PyModule_AddObject (Module, "EfiPygRtAddr", PyObject_gRT);
  if (ret != 0) {
    return ret;
  }

  PyObject_gBS                  = PyLong_FromVoidPtr(gBS);
  Py_INCREF (PyObject_gBS);
  ret = PyModule_AddObject (Module, "EfiPygBsAddr", PyObject_gBS);
  if (ret != 0) {
    return ret;
  }

  return ret;

} // EfiPy_Constant_Init

/*************************************************************************
 * PUBLIC EfiPy Module initialize
 *************************************************************************/
#ifndef PyMODINIT_FUNC  /* declarations for DLL import/export */
#define PyMODINIT_FUNC void
#endif
PyMODINIT_FUNC
init_EfiPy(void)
{
  PyObject *EfiPyModule = NULL;

  EfiPyModule = Py_InitModule3("_EfiPy", NULL,
                               "Library for python to contact EFI interface.");

  if (EfiPyModule == NULL) {
    return;
  }

  if (0 != EfiPy_Constant_Init(EfiPyModule)) {
    Py_DECREF (EfiPyModule);
    return;
  }

  if (0 != EfiPy_Processor_Init(EfiPyModule)) {
    Py_DECREF (EfiPyModule);
    return;
  }

} // init_EfiPy
