#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright (c) 2017 Maarten Los
# See LICENSE.rst for details.

from publisher import Publisher

p = Publisher(("127.0.0.1", 7222), "my-key")
p.publish("Hallo")
