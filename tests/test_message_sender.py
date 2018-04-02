#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright (c) 2018 Maarten Los
# See LICENSE.rst for details.

"""
Tests for the :py:class:`inbus.server.MessageSender` class
"""
import pytest
import socket

from mock import patch, call
from inbus.server.message_sender import MessageSender
from inbus.server.outgoing_message_translator import OutgoingMessageTranslator

@patch("socket.socket")
def test_message_sender_without_outgoing_message_translator_should_raise_error(mock_socket):
    with pytest.raises(AttributeError):
        MessageSender(None, mock_socket)

@patch("inbus.server.outgoing_message_translator.OutgoingMessageTranslator")
def test_message_sender_without_socket_should_raise_error(mock_outgoing_message_translator):
    with pytest.raises(AttributeError):
        MessageSender(mock_outgoing_message_translator, None)


@patch("inbus.server.outgoing_message_translator.OutgoingMessageTranslator")
@patch("socket.socket")
def test_message_sender_send_should_call_translate_and_socket_send(mock_outgoing_message_translator, mock_socket):
    ms = MessageSender(mock_outgoing_message_translator, mock_socket)
    ms.send("some-address", "some-app", "some-payload", 2)
    mock_outgoing_message_translator.translate.assert_called()
    mock_socket.sendto.assert_called()


@patch("inbus.server.outgoing_message_translator.OutgoingMessageTranslator")
@patch("socket.socket")
def test_message_sender_send_should_hide_socket_send_error(mock_outgoing_message_translator, mock_socket):
    ms = MessageSender(mock_outgoing_message_translator, mock_socket)
    mock_socket.sendto.side_effect = socket.error
    ms.send("some-address", "some-app", "some-payload", 2)

