#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright (c) 2017 Maarten Los
# See LICENSE.rst for details.


class InbusMethodObserver(object):
    """
    Classes implementing this interface should implement
    all methods, providing empty implementations for
    those method they do not support.
    Allows a client to call any inbus message on an observer.
    """
    def __init__(self):
        raise NotImplementedError

    def subscribe(self, address, application):
        raise NotImplementedError

    def unsubscribe(self, address, application):
        raise NotImplementedError

    def publish(self, application, payload):
        raise NotImplementedError
