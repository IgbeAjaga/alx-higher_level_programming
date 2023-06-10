#include <Python.h>
#include <stdio.h>

/**
 * print_python_string - Prints information about Python strings.
 * @p: A PyObject string object.
 */
void print_python_string(PyObject *p) {
    Py_ssize_t length;
    Py_ssize_t i;
    Py_UNICODE *unicode_str;
    const char *ascii_str;

    printf("[.] string object info\n");

    if (!PyUnicode_Check(p)) {
        printf("  [ERROR] Invalid String Object\n");
        return;
    }

    length = PyUnicode_GET_LENGTH(p);
    unicode_str = PyUnicode_AsUnicode(p);
    ascii_str = PyUnicode_AsUTF8(p);

    printf("  type: %s\n", PyUnicode_IS_COMPACT_ASCII(p) ? "compact ascii" : "compact unicode object");
    printf("  length: %ld\n", length);
    printf("  value: %s\n", PyUnicode_IS_COMPACT_ASCII(p) ? (const char *)ascii_str : (const char *)unicode_str);
}
