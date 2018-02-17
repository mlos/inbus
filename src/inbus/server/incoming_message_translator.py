#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright (c) 2017 Maarten Los
# See LICENSE.rst for details.

import json

from ..shared.opcode import Opcode


class IncomingMessageTranslator(object):
    """
    Translates raw Inbus messages to either a Subscribe, Unsubscribe or Publish
    method, and invokes those methods on its InbusMethodObservers

    Forms the bridge between the OO world and the outside world.
    """
    def __init__(self, inbus_method_observers):
        if inbus_method_observers is None:
            raise AttributeError
        self._inbus_method_observers = inbus_method_observers

    def translate(self, data):
        if data is None:
            raise ValueError

        try:
            message = json.loads(data)
        except ValueError:
            raise

        try:
            opcode = message["opcode"]
            application = message["application"]
            address = message["address"]
            payload = message["payload"]
        except KeyError:
            raise ValueError

        for i in self._inbus_method_observers:
            if opcode == Opcode.SUBSCRIBE:
                i.subscribe(address, application)
            elif opcode == Opcode.UNSUBSCRIBE:
                i.unsubscribe(address, application)
            elif opcode == Opcode.PUBLISH:
                i.publish(application, payload)
