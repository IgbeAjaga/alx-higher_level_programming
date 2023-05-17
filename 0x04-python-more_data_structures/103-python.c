#include <Python.h>

void print_python_list(PyObject *p)
{
	Py_ssize_t size, i;
	PyObject *item;
	if (!PyList_Check(p))
	{
		printf("[ERROR] Invalid Python list object\n");
		return;
	}
	size = PyList_Size(p);
	printf("[*] Size of the Python List = %zd\n", size);
	for (i = 0; i < size; i++)
	{
		item = PyList_GetItem(p, i);
		printf("Element %zd: %s\n", i, Py_TYPE(item)->tp_name);
	}
}

void print_python_bytes(PyObject *p)
{
	Py_ssize_t size, i;
	char *data;
	if (!PyBytes_Check(p))
	{
		printf("[ERROR] Invalid Python bytes object\n");
		return;
	}
	size = PyBytes_Size(p);
	data = PyBytes_AsString(p);
	printf("[.] bytes object info\n");
	printf("  - Length: %zd\n", size);
	printf("  - Bytes: ");
	if (size > 10)
	{
		for (i = 0; i < 10; i++)
		{
			printf("%02x ", (unsigned char)data[i]);
		}
		printf("\n       first 10 bytes\n");
	}
	else
	{
		for (i = 0; i < size; i++)
		{
			printf("%02x ", (unsigned char)data[i]);
		}
		printf("\n");
	}
}
