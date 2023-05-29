#ifndef PYTHON_H
#define PYTHON_H

#include <stddef.h>
#include <stdint.h>

/* Define PyObject structure */
typedef struct _object PyObject;

/* Define PyVarObject structure */
typedef struct {
    PyObject ob_base;
    Py_ssize_t ob_size;
} PyVarObject;

/* Define PyListObject structure */
typedef struct {
    PyObject ob_base;
    Py_ssize_t ob_size;
    PyObject **ob_item;
} PyListObject;

/* Define PyBytesObject structure */
typedef struct {
    PyObject ob_base;
    Py_ssize_t ob_size;
    char ob_bytes[1];
} PyBytesObject;

/* Define PyFloatObject structure */
typedef struct {
    PyObject ob_base;
    double ob_fval;
} PyFloatObject;

/* Function prototypes */
PyObject* PyList_GetItem(PyObject *list, Py_ssize_t index);
Py_ssize_t PyList_Size(PyObject *list);
PyObject* PyBytes_AsString(PyObject *bytes);
Py_ssize_t PyBytes_Size(PyObject *bytes);
double PyFloat_AsDouble(PyObject *floatObj);

#endif /* PYTHON_H */
