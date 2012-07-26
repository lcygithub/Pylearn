#include <Python.h>
#include<stdio.h>
int iteract_sum(int n) {
	if(n < 1)
		return n;
	else
		return n + iteract_sum(n - 1);
}

static PyObject* Ext_sum(PyObject* self,PyObject* args) {
	int n,result;
	if(!PyArg_ParseTuple(args,"i",&n))
		return NULL;
	result = iteract_sum(n);
	return Py_BuildValue("i",result);
}

static PyMethodDef Methods[] = {
	{"Ext_sum",Ext_sum,METH_VARARGS,"caculate"},
	{NULL,NULL,0,NULL},
};

PyMODINIT_FUNC
initexample(void) {
	// PyObject* m;
	// m = Py_InitModule3("example",Methods,"this is doc");
	// if(m == NULL) return;
	Py_InitModule3("example",Methods,"this is doc");
}