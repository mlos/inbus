#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright (c) 2017 Maarten Los
# See LICENSE.rst for details.

import json
import socket

from ..shared.opcode import Opcode
from ..shared.defaults import Defaults


class Subscriber(object):

    def __init__(self, app_key, client_address=(Defaults.LOCALHOST, 0),
                 server_address=Defaults.INBUS_ADDRESS, buffer_size=65536):
        self._app_key = app_key
        self._client_address = client_address
        self._server_address = server_address
        self._buffer_size = buffer_size
        self._socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self._socket.bind(self._client_address)

    def __enter__(self):
        # Register
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        sock.sendto(self._to_outgoing_message(Opcode.SUBSCRIBE),
                    self._server_address)
        sock.close()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        # Deregister
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        sock.sendto(self._to_outgoing_message(Opcode.UNSUBSCRIBE),
                    self._server_address)
        sock.close()

    def _to_outgoing_message(self, opcode):
        return json.dumps({'version': 1,
                           'opcode': opcode,
                           'application': [self._app_key, 0],
                           'address': list(self._socket.getsockname())})

    def wait_for_published_message(self):
        data, addr = self._socket.recvfrom(self._buffer_size)
        return data  # TODO extract payload
