//
//  Hello World 服务端
//  绑定一个REP套接字至tcp://*:5555
//  从客户端接收Hello，并应答World
//
#include <zmq.h>
#include <stdio.h>
#include <unistd.h>
#include <string.h>
 
int main (void)
{
    void *context = zmq_init(1);
 
    //  与客户端通信的套接字
    void *responder = zmq_socket(context, ZMQ_REP);
    zmq_bind(responder, "tcp://*:5555");
 
    while (1) {
        //  等待客户端请求
        zmq_msg_t request;
        zmq_msg_init(&request);
        zmq_recv(responder, &request, 0);
        printf("收到 Hello\n");
        zmq_msg_close(&request);
 
        //  做些“处理”
        sleep (1);
 
        //  返回应答
        zmq_msg_t reply;
        zmq_msg_init_size(&reply, 5);
        memcpy(zmq_msg_data(&reply), "World", 5);
        zmq_send(responder, &reply, 0);
        zmq_msg_close(&reply);
    }
    //  程序不会运行到这里，以下只是演示我们应该如何结束
    zmq_close(responder);
    zmq_term(context);
    return 0;
}