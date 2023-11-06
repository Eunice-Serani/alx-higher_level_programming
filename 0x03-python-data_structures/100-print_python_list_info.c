#include <Python.h>
#include <stdio.h>

/**
 * print_python_list_info -  Function that prints some basic
 * info about Python lists.
 * @p: A PyObject list.
 */
void print_python_list_info(PyObject *p)
{
	int size, alloc, k;
	PyObject *obj;

	size = Py_SIZE(p);
	alloc = ((PyListObject *)p)->allocated;

	printf("[*] Size of Python List = %d\n", size);
	printf("[*] Allocated = %d\n", alloc);

	for (k = 0; k < size; k++)
	{
		printf("Element %d: ", k);

		obj = PyList_GetItem(p, k);
		printf("%s\n", Py_TYPE(obj)->tp_name);
	}
}
