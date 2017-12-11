#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright (c) 2017 Maarten Los
# See LICENSE.rst for details.

"""
Tests for the :py:class:`inbus.server.IncomingMessageTranslator` class
"""
import pytest

import json
from mock import patch
from inbus.shared.opcode import Opcode
from inbus.server.incoming_message_translator import IncomingMessageTranslator
from inbus.server.inbus_method_observer import InbusMethodObserver


def test_incoming_message_translator_without_method_observer_should_raise_error():
    with pytest.raises(AttributeError):
        IncomingMessageTranslator(None)


@patch("inbus.server.inbus_method_observer.InbusMethodObserver")
def test_incoming_message_translator_subscription_should_send_subscribe_message(mock_observer):
    i = IncomingMessageTranslator([mock_observer])
    mock_observer.subscribe
    i.translate(_create_json_message(Opcode.SUBSCRIBE))
    mock_observer.subscribe.assert_called()


@patch("inbus.server.inbus_method_observer.InbusMethodObserver")
def test_incoming_message_translator_cancellation_should_send_unsubscribe_message(mock_observer):
    i = IncomingMessageTranslator([mock_observer])
    mock_observer.unsubscribe
    i.translate(_create_json_message(Opcode.UNSUBSCRIBE))
    mock_observer.unsubscribe.assert_called()


@patch("inbus.server.inbus_method_observer.InbusMethodObserver")
def test_incoming_message_translator_publication_should_send_publish_message(mock_observer):
    i = IncomingMessageTranslator([mock_observer])
    mock_observer.publish
    i.translate(_create_json_message(Opcode.PUBLISH))
    mock_observer.publish.assert_called()

    
def _create_json_message(opcode):
    return json.dumps({'version': 1,
                       'opcode': opcode,
                       'application': ['myapp-key', 0],
                       'address': ['my-address', 0],
                       'payload': 'my-payload'})

