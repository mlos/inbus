#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright (c) 2017 Maarten Los
# See LICENSE.rst for details.

from inbus.client.subscriber import Subscriber

is_running = True

with Subscriber("super-app") as s:
    while is_running:
        try:
            print s.wait_for_published_message()
        except KeyboardInterrupt:
            print "AA"
            is_running = False
