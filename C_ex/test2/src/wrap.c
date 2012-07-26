#include <Python.h>
int add(int a,int b) {
	return a+b;
}

static PyObject* wrap_add(PyObject* self,PyObject* args) {
	int a,b;
	if(!PyArg_ParseTuple(args,"ii",&a,&b))
		return NULL;
	int result = add(a,b);
	return (PyObject*)Py_BuildValue("i",result);
}

static PyMethodDef wrap_methods[] = {
	{"add",wrap_add,METH_VARARGS},
	{NULL,NULL}
};

PyMODINIT_FUNC initwrap(void) {
	Py_InitModule("wrap",wrap_methods);
}
