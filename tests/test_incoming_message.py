#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright (c) 2017 Maarten Los
# See LICENSE.rst for details.

"""
Tests for the :py:class:`inbus.incoming_message` class 
"""

import pytest
from incoming_message import IncomingMessage
from subscriber  import Subscriber


def test_incoming_message_none():
    with pytest.raises(ValueError):
        IncomingMessage(None)


def test_incoming_message_incorrect():
    with pytest.raises(ValueError):
        IncomingMessage("this is not JSON")


def test_incoming_message_full():
    ic = IncomingMessage('{ "version" : 1'
                        ', "opcode" : 99'
                        ', "application" : [ "app-key", 0 ]'
                        ', "address" : [ "127.0.0.1", 3456 ]'
                        ', "payload" : "ETCETERA" }')
    assert ic._version == 1
    assert ic._opcode == 99
    assert ic._application[0] == "app-key"
    assert ic._application[1] == 0
    assert ic._sender_address[0] == "127.0.0.1"
    assert ic._sender_address[1] == 3456
    assert ic._payload == "ETCETERA"


def test_incoming_message_subscriber():
    ic = IncomingMessage('{ "version" : 1'
                        ', "opcode" : 1'
                        ', "application" : [ "app-key", 0 ]'
                        ', "address" : [ "127.0.0.1", 3456 ]'
                        ', "payload" : "ETCETERA" }')
    assert isinstance(ic.to_subscriber(), Subscriber)
    assert ic.to_publisher() == None
    

