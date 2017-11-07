#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright (c) 2017 Maarten Los
# See LICENSE.rst for details.

import json

from ..shared.defaults import Defaults
from ..shared.opcode import Opcode


class Publisher(object):

    def __init__(self, application, payload):
        self._application = application
        self._payload = payload

    def application(self):
        return self._application

    def to_outgoing_message(self):
        return json.dumps({'version': Defaults.INBUS_VERSION,
                           'opcode': Opcode.PUBLISH,
                           'application': self._application,
                           'payload': self._payload})
