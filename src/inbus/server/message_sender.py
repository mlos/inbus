#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright (c) 2017 Maarten Los
# See LICENSE.rst for details.

import socket


class MessageSender(object):

    def __init__(self, outgoing_message_translator):
        self._outgoing_message_translator = outgoing_message_translator

    def send(self, address, application, payload):
        translated_message = self._outgoing_message_translator.translate(application, payload)
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        try:
            sock.sendto(translated_message, address)
        except socket.error:
            pass  # TODO: logging
