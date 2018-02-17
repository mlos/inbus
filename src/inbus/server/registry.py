#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright (c) 2017 Maarten Los
# See LICENSE.rst for details.

from .inbus_method_observer import InbusMethodObserver


class Registry(InbusMethodObserver):
    """
    Manages a list of subscribers
    """
    def __init__(self):
        self._subscriptions = []

    def subscribe(self, address, application):
        if (address, application) not in self._subscriptions:
            self._subscriptions.append((address, application))

    def unsubscribe(self, address, application):
        self._subscriptions = [
                s for s in self._subscriptions
                if (address != s[0]) and (application != s[1])
                ]

    def publish(self, application, payload):
        pass

    def subscribers(self):
        return self._subscriptions
