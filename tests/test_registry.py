#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright (c) 2017 Maarten Los
# See LICENSE.rst for details.

"""
Tests for the :py:class:`inbus.server.Registry` class
"""

import pytest

from inbus.server.registry import Registry


def test_registry_ctor():
    r = Registry()
    assert r.subscribers() == []


def test_registry_registering_one_subscriber_yields_subscriber():
    r = Registry()
    r.subscribe("addr", "myapp")
    subs = r.subscribers()
    assert len(subs) == 1
    assert subs[0] == ("addr", "myapp")


def test_registry_unregistering_only_registered_subscriber_yields_empty_subscribers():
    r = Registry()
    r.subscribe("addr", "myapp")
    r.unsubscribe("addr", "myapp")
    assert r.subscribers() == []


def test_registry_registering_two_same_subscribers_yields_one_subscriber():
    r = Registry()
    r.subscribe("addr", "myapp")
    r.subscribe("addr", "myapp")
    subs = r.subscribers()
    assert len(subs) == 1
    assert subs[0] == ("addr", "myapp")


def test_registry_registering_two_subscribers_differing_in_addr_yields_two_subscribers():
    r = Registry()
    r.subscribe("addr", "myapp")
    r.subscribe("another_addr", "myapp")
    subs = r.subscribers()
    assert len(subs) == 2
    assert subs[0] == ("addr", "myapp")
    assert subs[1] == ("another_addr", "myapp")


def test_registry_registering_two_subscribers_differing_in_app_yields_to_subscribers():
    r = Registry()
    r.subscribe("addr", "myapp")
    r.subscribe("addr", "another_app")
    subs = r.subscribers()
    assert len(subs) == 2
    assert subs[0] == ("addr", "myapp")
    assert subs[1] == ("addr", "another_app")


def test_registry_registering_two_same_and_one_different_subscriber_yields_two_subscribers():
    r = Registry()
    r.subscribe("addr", "myapp")
    r.subscribe("addr", "myapp")
    r.subscribe("xaddr", "myapp")
    subs = r.subscribers()
    assert len(subs) == 2
    assert subs[0] == ("addr", "myapp")
    assert subs[1] == ("xaddr", "myapp")


def test_registry_unsubscribing_non_existing_subscribers_does_not_affeect_subscribers():
    r = Registry()
    r.subscribe("addr0", "myapp")
    r.subscribe("addr1", "myapp")
    r.subscribe("addr2", "myapp")
    r.unsubscribe("bla","bla")
    assert len(r.subscribers()) == 3

def test_registry_publish_method_should_not_raise_error():
    r = Registry()
    r.publish("dummy-app", "dummy-payload")
