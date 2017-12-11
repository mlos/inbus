#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright (c) 2017 Maarten Los
# See LICENSE.rst for details.

"""
Tests for the :py:class:`inbus.server.Broadcaster` class
"""
import pytest

from mock import patch, call
from inbus.server.broadcaster import Broadcaster

def test_broadcaster_without_registry_should_raise_error():
    with pytest.raises(AttributeError):
        Broadcaster(None, 1)


def test_broadcaster_without_message_sender():
    with pytest.raises(AttributeError):
        Broadcaster(1, None)


@patch("inbus.server.registry.Registry")
@patch("inbus.server.message_sender.MessageSender")
def test_broadcaster_with_two_subscribers_for_app_should_call_send_twice(mock_registry, mock_sender):
    mock_registry.subscribers.return_value = [ ("address", "app"), ("address-2", "app") ]
    b = Broadcaster(mock_registry, mock_sender)

    b.publish("app", "some-payload")

    mock_sender.send.assert_called()
    assert mock_sender.send.call_count == 2

