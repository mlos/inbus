#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright (c) 2017 Maarten Los
# See LICENSE.rst for details.

"""
Tests for the :py:class:`inbus.broadcaster` class 
"""

import pytest
from broadcaster import Broadcaster
from subscriber import Subscriber


def test_broadcaster_ctor():
    bc = Broadcaster()
    assert bc._subscribers == []

def test_broadcaster_manage_subscriber_sub_unsub():
    bc = Broadcaster()
    sub = Subscriber(True, ("127.0.0.1", 1234), "app-key")
    bc.manage_subscriber(sub)
    assert len(bc._subscribers) == 1
    sub = Subscriber(False, ("127.0.0.1", 1234), "app-key")
    bc.manage_subscriber(sub)
    assert bc._subscribers == []

def test_broadcaster_manage_subscriber_sub_all_unsub():
    bc = Broadcaster()
    bc.manage_subscriber(Subscriber(True, ("",0), ""))
    bc.manage_subscriber(Subscriber(True, ("",0), ""))
    bc.manage_subscriber(Subscriber(True, ("",0), ""))
    bc.manage_subscriber(Subscriber(True, ("",0), ""))
    bc.manage_subscriber(Subscriber(True, ("",0), ""))
    bc.manage_subscriber(Subscriber(True, ("",0), ""))
    assert len(bc._subscribers) == 6
    bc.manage_subscriber(Subscriber(False, ("",0), ""))
    assert bc._subscribers == []

def test_broadcaster_manage_subscriber_sub_all_unsub_but_one():
    bc = Broadcaster()
    bc.manage_subscriber(Subscriber(True, ("",0), ""))
    bc.manage_subscriber(Subscriber(True, ("",0), ""))
    bc.manage_subscriber(Subscriber(True, ("",0), ""))
    bc.manage_subscriber(Subscriber(True, ("",11), ""))
    bc.manage_subscriber(Subscriber(True, ("",0), ""))
    bc.manage_subscriber(Subscriber(True, ("",0), ""))
    assert len(bc._subscribers) == 6
    bc.manage_subscriber(Subscriber(False, ("",0), ""))
    assert len(bc._subscribers) == 1
    assert bc._subscribers[0].id() == ("",11)
