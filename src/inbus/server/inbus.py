#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright (c) 2017 Maarten Los
# See LICENSE.rst for details.

import socket
from registry import Registry
from message_receiver import MessageReceiver
from incoming_message_translator import IncomingMessageTranslator
from broadcaster import Broadcaster
from message_sender import MessageSender
from outgoing_message_translator import OutgoingMessageTranslator


class Inbus(object):

    def __init__(self, address=("127.0.0.1", 7222), buffer_size=65536):
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        registry = Registry()
        self._message_receiver = MessageReceiver(
            IncomingMessageTranslator(
                [registry,
                 Broadcaster(registry,
                             MessageSender(OutgoingMessageTranslator(), sock))
                 ]), address, buffer_size)

    def run(self):
        while True:
            self._message_receiver.wait_and_process_message()
