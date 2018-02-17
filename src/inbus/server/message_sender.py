#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright (c) 2017 Maarten Los
# See LICENSE.rst for details.

import socket


class MessageSender(object):
    """
    Sends a raw Inbus network message to the network
    """
    def __init__(self, outgoing_message_translator, socket):
        if outgoing_message_translator is None:
            raise AttributeError

        if socket is None:
            raise AttributeError

        self._outgoing_message_translator = outgoing_message_translator
        self._socket = socket

    def send(self, address, application, payload):
        translated_message = self._outgoing_message_translator.translate(
                application, payload)
        try:
            self._socket.sendto(translated_message, address)
        except socket.error:
            pass  # TODO: logging
