#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright (c) 2017 Maarten Los
# See LICENSE.rst for details.


class Broadcaster(object):

    def __init__(self, registry, message_sender):
        self._registry = registry
        self._message_sender = message_sender

    def subscribe(self, address, application):
        pass

    def unsubscribe(self, address, application):
        pass

    def publish(self, address, application, payload):
        subscribers = self._registry.subscribers()
        addresses = [tuple(address) for s in subscribers
                     if s.application() == application[0]]
        print application[0]

        for addr in addresses:
            self._message_sender.send(addr, application, payload)
