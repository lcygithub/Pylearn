#-*- coding:utf8-*-
import Queue

def worker():
	while True:
		item = q.get()
		do_work(item)
		q.task_done()
q = Queue
for i in range(num_worker_threads):
	t = Thread(target = worker)
	t.setDaemon(True)
	t.start()

for item in source():
	q.put(item)

q.join()