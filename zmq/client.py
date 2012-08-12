import zmq
context = zmq.Context()
socket = context.socket(zmq.REQ)
socket.connect("tcp://127.0.0.1:8080")
msg_send = "lcyang"
socket.send(msg_send)
print "Send:", msg_send
msg_recv = socket.recv()
print "Receive:", msg_recv
