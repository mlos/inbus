#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright (c) 2017 Maarten Los
# See LICENSE.rst for details.

"""
Tests for the :py:class:`inbus.server.InbusMethodObserver` class
"""

import pytest

from inbus.server.inbus_method_observer import InbusMethodObserver

def test_inbus_method_observer_ctor():
    with pytest.raises(NotImplementedError):
        InbusMethodObserver()

def test_inbus_method_observer_methods_are_abstract():
    class Abstract(InbusMethodObserver):
        def __init__(self):
            pass

    a = Abstract()
    with pytest.raises(NotImplementedError):
        a.subscribe(None, None)

    with pytest.raises(NotImplementedError):
        a.unsubscribe(None, None)

    with pytest.raises(NotImplementedError):
        a.publish(None, None)
