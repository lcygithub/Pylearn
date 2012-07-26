#include <Python.h>
#include <stdio.h>

int comp(int a,int b) {
	return a>b?a:b;
}

static PyObject*
ex_comp(PyObject *self,PyObject *args) {
	int a,b;
	int result;
	if(!PyArg_ParseTuple(args,"ii",&a,&b))
		return NULL;
	result = comp(a,b);
	return (PyObject*)PyLong_FromLong(result);
}

static PyMethodDef ComMethods[] = {
	{"comp",ex_comp,METH_VARARGS,"compare two numbers"},
	{NULL,NULL,0,NULL}
};

PyMODINIT_FUNC
initcompare(void) {
	PyObject* m;
	m = Py_InitModule("compare",ComMethods);
	if(m == NULL)
		return;
}