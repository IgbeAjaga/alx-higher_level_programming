#include <Python.h>
#include <stdio.h>

void print_python_string(PyObject *p) {
    if (PyUnicode_Check(p)) {
        Py_ssize_t length = PyUnicode_GET_LENGTH(p);
        int is_unicode = PyUnicode_IS_UNICODE(p);
        const char *value = PyUnicode_AsUTF8(p);

        printf("[.] string object info\n");
        printf("  type: %s\n", is_unicode ? "compact unicode object" : "compact ascii");
        printf("  length: %zd\n", length);
        printf("  value: %s\n", value);
    } else {
        printf("[.] string object info\n");
        printf("  [ERROR] Invalid String Object\n");
    }
}

int main(void) {
    Py_Initialize();

    // Test cases
    PyObject *s = PyUnicode_FromString("The spoon does not exist");
    print_python_string(s);

    s = PyUnicode_FromString("ложка не существует");
    print_python_string(s);

    s = PyUnicode_FromString("La cuillère n'existe pas");
    print_python_string(s);

    s = PyUnicode_FromString("勺子不存在");
    print_python_string(s);

    s = PyUnicode_FromString("숟가락은 존재하지 않는다.");
    print_python_string(s);

    s = PyUnicode_FromString("スプーンは存在しない");
    print_python_string(s);

    s = PyBytes_FromString("The spoon does not exist");
    print_python_string(s);

    Py_Finalize();
    return 0;
}

