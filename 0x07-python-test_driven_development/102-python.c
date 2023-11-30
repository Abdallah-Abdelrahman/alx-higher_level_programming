#include "Python.h"

/**
 * print_python_string - prints Python strings
 * @p: python object
 *
 * Return: Nothing
 */
void print_python_string(PyObject *p)
{
	PyASCIIObject *py_str = (PyASCIIObject *)p;
	char *type = "compact unicode object";

	printf("[.] string object info\n");
	if (!PyUnicode_Check(p))
	{
		printf("  [ERROR] Invalid String Object\n");
		return;
	}
	if (PyUnicode_IS_COMPACT_ASCII(p))
		type = "compact ascii";
	printf("  type: %s\n", type);
	printf("  length: %ld\n", py_str->length);
	printf("  value: %s\n", PyUnicode_AsUTF8(p));
}
