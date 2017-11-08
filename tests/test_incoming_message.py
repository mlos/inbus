#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright (c) 2017 Maarten Los
# See LICENSE.rst for details.

"""
Tests for the :py:class:`inbus.incoming_message` class
"""

import pytest
from inbus.server.incoming_message import IncomingMessage
from inbus.server.subscriber import Subscriber


def test_incoming_message_none():
    with pytest.raises(ValueError):
        IncomingMessage(None)


def test_incoming_message_incorrect():
    with pytest.raises(ValueError):
        IncomingMessage("this is not JSON")


def test_incoming_message_full():
    ip = "123.4.1.3"
    port = 1244
    ic = IncomingMessage('{ "version" : 1'
                         ', "opcode" : 99'
                         ', "application" : [ "app-key", 0 ] }')
    assert ic._version == 1
    assert ic._opcode == 99
    assert ic._application[0] == "app-key"
    assert ic._application[1] == 0


def test_incoming_message_subscriber_subs():
    ic = IncomingMessage('{ "version" : 1'
                         ', "opcode" : 1'
                         ', "application" : [ "app-key", 0 ]'
                         ', "address" : [ "127.0.0.1", 3456 ]'
                         ', "payload" : "ETCETERA" }')
    assert ic.to_publisher() is None
    subs = ic.to_subscriber()
    assert isinstance(subs, Subscriber)
    assert subs.want_to_subscribe()
    assert not subs.want_to_unsubscribe()


def test_incoming_message_subscriber_unsubs():
    ic = IncomingMessage('{ "version" : 1'
                         ', "opcode" : 2'
                         ', "application" : [ "app-key", 0 ]'
                         ', "address" : [ "127.0.0.1", 3456 ]'
                         ', "payload" : "ETCETERA" }')
    assert ic.to_publisher() is None
    subs = ic.to_subscriber()
    assert isinstance(subs, Subscriber)
    assert not subs.want_to_subscribe()
    assert subs.want_to_unsubscribe()
