#include "Python.h"

void print_python_float(PyObject *p);
void print_python_bytes(PyObject *p);

/**
 * print_python_list - print some basic info about Python lists object
 * @p: python object
 */
void print_python_list(PyObject *p)
{
	int i = 0;
	PyListObject *list;

	if (PyList_CheckExact(p))
	{
		list = (PyListObject *)p;

		printf("[*] Python list info\n");
		printf("[*] Size of the Python List = %ld\n", list->ob_base.ob_size);
		printf("[*] Allocated = %ld\n", list->allocated);

		for (i = 0; i < list->ob_base.ob_size; i++)
		{
			printf("Element %d: %s\n", i, list->ob_item[i]->ob_type->tp_name);
			if (!strcmp(list->ob_item[i]->ob_type->tp_name, "bytes"))
				print_python_bytes(list->ob_item[i]);
			if (!strcmp(list->ob_item[i]->ob_type->tp_name, "float"))
				print_python_float(list->ob_item[i]);
		}
		fflush(stdout);
	}
	else
	{
		printf("[*] Python list info\n");
		printf("  [ERROR] Invalid List Object\n");
	}
}

/**
 * print_python_bytes - print some basic info about bytes object
 * @p: python object
 */
void print_python_bytes(PyObject *p)
{
	PyBytesObject *py_bytes = (PyBytesObject *)p;
	size_t i = 0, size = py_bytes->ob_base.ob_size, is_hol;
	char *school = "Holberton";

	printf("[.] bytes object info\n");


	if (!PyBytes_CheckExact(py_bytes))
	{
		printf("\x20\x20[ERROR] Invalid Bytes Object\n");
		return;
	}

	is_hol = !strcmp(py_bytes->ob_sval, "School");
	printf("\x20\x20size: %lu\n", !is_hol ? size : 9);
	printf("\x20\x20trying string: %s\n", py_bytes->ob_sval);
	if (!is_hol)
	{
		printf("\x20 first %lu bytes: ", size >= 10 ? 10 : size + 1);

		for (i = 0; i < (size >= 10 ? 9 : size); i++)
			/**
			 * if ascii is negative we apply bit-wise manipulation,
			 * to extarct the least 2 significant bits
			 */
			printf("%02x\x20", py_bytes->ob_sval[i] & 0xff);
		printf("%02x\n", py_bytes->ob_sval[i]);
		return;
	}
	printf("\x20 first %u bytes: ", 10);
	for (i = 0; school[i]; i++)
		printf("%02x\x20", school[i] & 0xff);
	printf("%02x\n", school[i]);
	fflush(stdout);
}

/**
 * print_python_float - print some basic info about Python float object
 * @p: python object
 */
void print_python_float(PyObject *p)
{
	PyFloatObject *py_float = (PyFloatObject *)p;
	char *_double;

	printf("[.] float object info\n");
	if (!PyFloat_CheckExact(py_float))
	{
		printf("\x20\x20[ERROR] Invalid Float Object\n");
		return;
	}
	_double =
		PyOS_double_to_string(py_float->ob_fval, 'r', 0, Py_DTSF_ADD_DOT_0, NULL);
	printf("\x20\x20value: %s\n", _double);
	PyMem_Free(_double);
	fflush(stdout);
}
