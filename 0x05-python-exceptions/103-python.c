/*
 * File: 103-python.c
 * Auth: Eunice-Serani
 */

#include "Python.h"
#include <stdio.h>
#include <unistd.h>
#include <string.h>
#include <stdlib.h>

void print_python_bytes(PyObject *p);
void print_python_float(PyObject *p);

/**
 * print_python_list - this prints python list
 * @p: shows a python object
 */
void print_python_list(PyObject *p)
{
	int a = 0;
	ssize_t size = 0;
	PyListObject *list;

	fflush(stdout);
	printf("[*] Python list info\n");
	if (!PyList_Check(p))
	{
		printf("  [ERROR] Invalid List Object\n");
		return;
	}

	list = (PyListObject *)p;
	size = list->ob_base.ob_size;
	printf("[*] Size of the Python List = %lu\n", size);
	printf("[*] Allocated = %lu\n", list->allocated);

	while (a < size)
	{
		char *tp_name = (char *)list->ob_item[1]->ob_type->tp_name;

		printf("Element %d: %s\n", a, tp_name);

		if (strcmp(tp_name, "bytes") == 0)
		{
			print_python_bytes(list->ob_item[a]);
		}
		else if (strcmp(tp_name, "float") == 0)
		{
			print_python_float(list->ob_item[a]);
		}
		a++;
	}
}

/**
 * print_python_bytes - this prints python bytes
 * @p: shows a python object
 */
void print_python_bytes(PyObject *p)
{
	ssize_t a, size = 0;
	PyBytesObject *py_bytes;

	fflush(stdout);
	printf("[.] byte object info\n");
	if (!PyBytes_Check(p))
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}

	py_bytes = (PyBytesObject *)p;
	size = py_bytes->ob_base.ob_size;
	printf("  size: %lu\n", size);
	printf("  trying string: %s\n", py_bytes->ob_sval);
	if (size > 9)
	{
		size = 10;
	}
	else
	{
		size += 1;
	}

	printf("  first %lu bytes: ", size);
	for (a = 0; a < size; a++)
	{
		printf("%02hhx", (unsigned char)py_bytes->ob_sval[a]);
		if (a == size - 1)
		{
			printf("\n");
		}
		else
		{
			printf(" ");
		}
	}
}

/**
 * print_python_float - this prints python float
 * @p: shows python object
 */
void print_python_float(PyObject *p)
{
	PyFloatObject *py_float;
	char *py_double = NULL;

	fflush(stdout);
	printf("[.] float object info\n");
	if (!PyFloat_Check(p))
	{
		printf("  [ERROR] Invalid Float Object\n");
		return;
	}

	py_float = (PyFloatObject *)p;
	py_double = PyOS_double_to_string(py_float->ob_fval, 'r', 0,
									  Py_DTSF_ADD_DOT_0, NULL);
	printf("  value: %s\n", py_double);
	PyMem_Free(py_double);
}
