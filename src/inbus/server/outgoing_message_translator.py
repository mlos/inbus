#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright (c) 2017 Maarten Los
# See LICENSE.rst for details.

import json

from ..shared.defaults import Defaults
from ..shared.opcode import Opcode


class OutgoingMessageTranslator(object):
    """
    Translate the publish method into a raw Inbus network message
    """
    def __init__(self):
        pass

    def translate(self, application, payload):
        return json.dumps({'version': Defaults.INBUS_VERSION,
                           'opcode': Opcode.PUBLISH,
                           'application': application,
                           'payload': payload})
