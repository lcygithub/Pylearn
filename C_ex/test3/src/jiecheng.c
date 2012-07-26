#include <Python.h>
int jie(int c) {
	if(c == 1) {
		return c;
	}
	else 
		return c*jie(c - 1);
}

static PyObject* ex_jie(PyObject* self,PyObject* args) {
	int a;
	if(!PyArg_ParseTuple(args,"i",&a))
		return NULL;
	int result = jie(a);
	return Pylong_FromLong(result);
}

static PyMethodDef JieMethods[] = {
	{"calculate",ex_jie,METH_VARARGS},
	{NULL,NULL}
};

PyMODINIT_FUNC
initjie(void) {
	Py_InitModule("jie",JieMethods);
}