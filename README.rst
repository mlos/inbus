inbus **|** 

Inbus
=========

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

License
-------
BSD 2-Clause License

Copyright (c) 2017 Maarten Los
All rights reserved.

Redistribution and use in source and binary forms, with or without modification,
are permitted provided that the following conditions are met:

* Redistributions of source code must retain the above copyright notice, this
  list of conditions and the following disclaimer.

* Redistributions in binary form must reproduce the above copyright notice,
  this list of conditions and the following disclaimer in the documentation and/or
  other materials provided with the distribution.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND
ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED.
IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT,
INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT
NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR
PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY,
WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE)
ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
POSSIBILITY OF SUCH DAMAGE.
