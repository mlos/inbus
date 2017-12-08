#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright (c) 2017 Maarten Los
# See LICENSE.rst for details.

"""
Tests for the :py:class:`inbus.InbusMethodObserver` class
"""

import pytest

from inbus.server.inbus_method_observer import InbusMethodObserver

def test_inbus_method_observer_ctor():
    with pytest.raises(NotImplementedError):
        InbusMethodObserver()



