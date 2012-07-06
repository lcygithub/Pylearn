#-*- coding:utf8-*-
class signal():
	_instance = 'h'

	@classmethod
	def instance(cls):
		print cls._instance
		if cls._instance == 'h':
			cls._instance = cls()
			cls._instance.start()
		return cls._instance
	def start(self):
		print "start"
