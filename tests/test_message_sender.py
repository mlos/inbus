#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright (c) 2018 Maarten Los
# See LICENSE.rst for details.

"""
Tests for the :py:class:`inbus.server.MessageSender` class
"""
import pytest

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
    ms.send("some-address", "some-app", "some-payload")
    mock_outgoing_message_translator.translate.assert_called()
    mock_socket.sendto.assert_called()

'''
@patch("inbus.server.registry.Registry")
def test_message_sender_with_two_subscribers_for_app_should_call_send_twice(mock_registry, mock_sender):
    mock_registry.subscribers.return_value = [ ("address", "app"), ("address-2", "app") ]
    b = Broadcaster(mock_registry, mock_sender)

    b.publish("app", "some-payload")

    mock_sender.send.assert_called()
    assert mock_sender.send.call_count == 2


@patch("inbus.server.registry.Registry")
@patch("inbus.server.message_sender.MessageSender")
def test_message_sender_subscribe_method_should_not_raise_error(mock_registry, mock_sender):
    b = Broadcaster(mock_registry, mock_sender)
    b.subscribe("dummy-address", "dummy-app")


@patch("inbus.server.registry.Registry")
@patch("inbus.server.message_sender.MessageSender")
def test_message_sender_unsubscribe_method_should_not_raise_error(mock_registry, mock_sender):
    b = Broadcaster(mock_registry, mock_sender)
    b.unsubscribe("dummy-address", "dummy-app")
'''
