#include <Python.h>//若有其他头文件，必须在Python.h之后引入 
 
static PyObject * 
spam_system(PyObject *self,PyObject * args) 
{ 
    const char *command; 
    int sts; 
 
    if(!PyArg_ParseTuple(args,"s",&command))//用法类似scanf,把传入python函数的参数转换为C的数据类型，此处为字符串 
        return NULL; 
    sts = system(command);//调用C的system函数 
    if (sts <0){ 
        return NULL; 
    } 
    return PyLong_FromLong(sts);//返回值转换为Python对象 
} 
 
 
//名字绑定至函数，暂且不管METH_VARARGS，更多内容看http://docs.python.org/extending/extending.html 
static PyMethodDef SpamMethods[] = { 
    {"system",spam_system,METH_VARARGS, 
     "Execute a shell command."}, 
    {NULL,NULL,0,NULL} 
}; 
 
//包的初始化方法 
PyMODINIT_FUNC 
initspam(void) 
{ 
    PyObject *m; 
 
    m = Py_InitModule("spam",SpamMethods);//传入函数表 
    if (m = NULL) 
        return; 
} 