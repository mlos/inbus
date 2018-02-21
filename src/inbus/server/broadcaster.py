#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright (c) 2017 Maarten Los
# See LICENSE.rst for details.

from .inbus_method_observer import InbusMethodObserver


class Broadcaster(InbusMethodObserver):
    """
    Broadcasts Publications to a list of Subscribers
    """
    def __init__(self, registry, message_sender):
        if registry is None:
            raise AttributeError

        if message_sender is None:
            raise AttributeError

        self._registry = registry
        self._message_sender = message_sender

    def subscribe(self, address, application):
        pass

    def unsubscribe(self, address, application):
        pass

    def publish(self, application, payload):
        subscribers = self._registry.subscribers()
        addresses = [tuple(s[0]) for s in subscribers if s[1][0] == application[0]]

        for addr in addresses:
            self._message_sender.send(addr, application, payload)
