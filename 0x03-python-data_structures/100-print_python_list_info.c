#include "/usr/include/python3.8/Python.h"
#include "/usr/include/python3.8/listobject.h"
#include "/usr/include/python3.8"

/**
 * print_python_list_info - Prints basic info about Python lists.
 * @p: A PyObject list.
 */

void print_python_list_info(PyObject *p)
{
	int size, i;
	PyObject *item;
	size = PyList_Size(p);

	printf("[*] Size of the Python List = %d\n", size);
	printf("[*] Allocated = %d\n", ((PyListObject *)p)->allocated);
	for (i = 0; i < size; i++)
	{
		item = PyList_GetItem(p, i);
		printf("Element %d: %s\n", i, Py_TYPE(item)->tp_name);
	}
}
