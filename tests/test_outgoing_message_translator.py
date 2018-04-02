#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright (c) 2017 Maarten Los
# See LICENSE.rst for details.

"""
Tests for the :py:class:`inbus.server.OutgoingMessageTranslator` class
"""
import pytest

import json
from mock import patch
from inbus.shared.opcode import Opcode
from inbus.server.outgoing_message_translator import OutgoingMessageTranslator
from inbus.server.inbus_method_observer import InbusMethodObserver


def test_outgoing_message_translator_translate_returns_valid_json():
    mt = OutgoingMessageTranslator()
    translated = mt.translate("some-app", "some-payload", 1)
    passed = True
    try:
        message = json.loads(translated)
    except ValueError: # pragma: no cover
       passed = False

    assert passed is True
        



