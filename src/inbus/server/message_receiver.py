#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright (c) 2017 Maarten Los
# See LICENSE.rst for details.

import socket


class MessageReceiver(object):
    """
    Waits for raw Inbus network messages
    and passes them to the MessageTranslator
    """
    def __init__(self, incoming_message_translator, address,
                 buffer_size=65536):
        if incoming_message_translator is None:
            raise AttributeError

        if address is None:
            raise AttributeError

        self._incoming_message_translator = incoming_message_translator
        self._address = address
        self._buffer_size = buffer_size
        self._socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self._socket.bind(address)

    def wait_and_process_message(self):
        data, addr = self._socket.recvfrom(self._buffer_size)
        print data, addr
        self._incoming_message_translator.translate(data)
