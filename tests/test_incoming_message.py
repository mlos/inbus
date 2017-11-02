#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright (c) 2017 Maarten Los
# See LICENSE.rst for details.

"""
Tests for the :py:class:`inbus.incoming_message` class 
"""

import pytest
from incoming_message import IncomingMessage
from subscriber import Subscriber

SENDER_ADDRESS = ("127.0.0.1", 12345)

def test_incoming_message_none():
    with pytest.raises(ValueError):
        IncomingMessage(None, SENDER_ADDRESS)


def test_incoming_message_sender_none():
    with pytest.raises(ValueError):
        IncomingMessage("{}", None)


def test_incoming_message_incorrect():
    with pytest.raises(ValueError):
        IncomingMessage("this is not JSON", SENDER_ADDRESS)


def test_incoming_message_full():
    ip = "123.4.1.3"
    port = 1244
    ic = IncomingMessage('{ "version" : 1'
                        ', "opcode" : 99'
                        ', "application" : [ "app-key", 0 ]'
                        ', "address" : [ "127.0.0.1", 3456 ]'
                        ', "payload" : "ETCETERA" }', (ip, port))
    assert ic._version == 1
    assert ic._opcode == 99
    assert ic._application[0] == "app-key"
    assert ic._application[1] == 0
    assert ic._sender_address[0] == ip
    assert ic._sender_address[1] == port
    assert ic._payload == "ETCETERA"


def test_incoming_message_subscriber_subs():
    ic = IncomingMessage('{ "version" : 1'
                        ', "opcode" : 1'
                        ', "application" : [ "app-key", 0 ]'
                        ', "address" : [ "127.0.0.1", 3456 ]'
                        ', "payload" : "ETCETERA" }', SENDER_ADDRESS)
    assert ic.to_publisher() == None
    subs = ic.to_subscriber()
    assert isinstance(subs, Subscriber)
    assert subs.want_to_subscribe() 
    assert not subs.want_to_unsubscribe()


def test_incoming_message_subscriber_unsubs():
    ic = IncomingMessage('{ "version" : 1'
                        ', "opcode" : 2'
                        ', "application" : [ "app-key", 0 ]'
                        ', "address" : [ "127.0.0.1", 3456 ]'
                        ', "payload" : "ETCETERA" }', SENDER_ADDRESS)
    assert ic.to_publisher() == None
    subs = ic.to_subscriber()
    assert isinstance(subs, Subscriber)
    assert not subs.want_to_subscribe() 
    assert subs.want_to_unsubscribe()

