from twisted.internet import reactor
import time


def printTime(id):
    print 'Current time is ', id, " ", time.strftime("%H:%M:%S")


def stopReactor():
    print "Stopping reactor"
    reactor.stop()

reactor.callLater(1, printTime, id="1")
reactor.callLater(2, printTime, id="2")
reactor.callLater(3, printTime, id="3")
reactor.callLater(3, printTime, id="4")
reactor.callLater(5, stopReactor)
print 'Running the reactor ...'
reactor.run()
print 'Reactor stopped.'
