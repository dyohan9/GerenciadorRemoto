from __future__ import absolute_import, unicode_literals

from celery import shared_task
from twisted.internet import reactor
from apps.controller.socket import MyClientFactory


@shared_task
def sendPacket():
    factory = MyClientFactory('ifconfig')
    reactor.connectTCP('localhost', 9000, factory)
    reactor.run()
    return True


