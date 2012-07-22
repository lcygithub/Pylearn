#-*- coding:utf8-*-
import threading
import random
import time
from Queue import Queue

class Producer(threading.Thread):
	def __init__(self,threadname,queue):
		threading.Thread.__init__(self,name = threadname)
		self.sharedata = queue

	def run(self):
		for i in range(10):
			print self.getName(),'adding',i,'to queue'
			self.sharedata.put(id)
			print "producer succed"
			time.sleep(1)
		print self.getName(),'Finished'

class Consumer(threading.Thread):
	def __init__(self,threadname,queue):
		threading.Thread.__init__(self,name = threadname)
		self.sharedata = queue

	def run(self):
		for i in range(20):
			print self.getName(),'got a value',self.sharedata.get()
			time.sleep(1)
		print self.getName(),'Finished'
def main():
	queue = Queue()
	producer = Producer('Producer',queue)
	consumer = Consumer('Consumer',queue)
	print "Starting threads..."
	consumer.start()
	producer.start()
	consumer.join()
	producer.join()
	
	print "All threads have terminated."
if __name__ == "__main__":
	main()