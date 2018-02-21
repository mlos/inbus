Inbus
=====

.. image:: https://travis-ci.org/mlos/inbus.svg?branch=master
   :target: https://travis-ci.org/mlos/inbus

.. image:: https://codecov.io/gh/mlos/inbus/branch/master/graph/badge.svg
  :target: https://codecov.io/gh/mlos/inbus

**inbus** stands for INconnu message BUS and is targeted at small
devices running a limited number of applications exchanging small
messages. It has a single goal: connectionless brokering of messages
between one or more publishers and one or more subscribers.

* Central broker
* Does not try to be all things to all people
* Connectionless (UDP based): No message delivery guaranteed
* No flow control or session management 
* Simple JSON based protocol

