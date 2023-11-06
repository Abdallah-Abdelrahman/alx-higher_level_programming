#include <stdio.h>
#include <python3.4/Python.h>

/**
 * print_python_list_info - get info about `list` object in python
 * @p: pointer Pyobject (see object.h)
 */
void print_python_list_info(PyObject *p)
{
	int i = 0, size = PyList_Size(p);

	if (PyList_Check(p))
	{
		printf("[*] Size of the Python List = %d\n", size);
		printf("[*] Allocated = %ld\n", ((PyListObject *)p)->allocated);

		for (i = 0; i < size; i++)
		{
			printf("Element %d: %s\n", i, Py_TYPE(PyList_GetItem(p, i))->tp_name);

		}
	}
}
