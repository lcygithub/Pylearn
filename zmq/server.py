import zmq
context = zmq.Context()
socket = context.socket(zmq.REP)
socket.bind("tcp://127.0.0.1:8080")

while True:
    msg = socket.recv()
    socket.send(msg)
