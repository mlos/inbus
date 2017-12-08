#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright (c) 2017 Maarten Los
# See LICENSE.rst for details.

from inbus_method_observer import InbusMethodObserver

class Registry(InbusMethodObserver):

    def __init__(self):
        self._subscriptions = []

    def subscribe(self, address, application):
        print "S", address, application
        self._subscriptions.append((address, application))

    def unsubscribe(self, address, application):
        print "U", address, application
        self._subscriptions = [s for s in self._subscriptions
            if address != subscription[0]]

    def publish(self, address, application, payload):
        pass

    def subscribers(self):
        return self._subscriptions
