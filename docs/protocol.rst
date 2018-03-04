========
Protocol
========

**NOTE** Use of the words, must, should, could, etc. adheres to the best practice
suggested in RFC2119 (https://www.ietf.org/rfc/rfc2119.txt)

-----------
Description
-----------

Protocol messages MUST be specified in the following JSON format:

.. code-block:: console

    {   
        "version" : <inbus-version>,
        "opcode" : <opcode>, 
        "application" :[ <app-key>, <app-type> ], 
        "address" : [ <ip-number>, <port> ], 
        "payload" : <payload>
    }

All messages MUST contain all elements, even if they are not used.

Elements that do not apply to a particular type of message (as
defined by its ``<opcode>``), SHOULD be an empty string or zero,
depending on the data type.

``<inbus-version>``
    Integer specifying the Inbus protocol version.
    MUST be 1.

``<opcode>`` 
    Integer specifying the type of message

    * 0: reserved
    * 1: subscribe
    * 2: unsubscribe
    * 3: publish
    * 4-999: reserved

``<app-key>``
    String identifying the application to which
    the message applies. 

    The values ``*`` and ``_inbus`` are reserved for future use.

``<app-type>``
    Integer, specifying an application defined 
    value. Can be used to distinguish multiple messages
    related to the same application.

    The element only applies to *publish* messages.

``<ip-number>``
    String containing an IP number part of the
    subscriber address. In case of a publish message,
    the element does not apply.


``<port>``
    Integer containing the port number of the subscriber
    address. In case of a *publish* message, the element 
    does NOT apply.

    The subscriber address, together with the ``app-key``
    uniquely identifies a subscription.


``<payload>``
    String specifying a user defined payload.
    This implies that binary data must be string-encoded.
    The element only applies to *publish* messages.

--------------
Infrastructure
--------------
The protocol SHOULD use port 7222

----------------
Example messages
----------------

^^^^^^^^^
Subscribe
^^^^^^^^^

.. code-block:: console

    {   "version" : 1 ,
        "opcode" : 1, 
        "application" : [ "upnp", 0 ],
        "address" : [ "127.0.0.1", 3456 ],
        "payload" : ""
    }

Subscription message indicating that the subscriber wants to receive messages from an application that publishes
messages under the "upnp" app-key.

^^^^^^^^^^^
Unsubscribe
^^^^^^^^^^^

.. code-block:: console

    {   "version" : 1 ,
        "opcode" : 2,
        "application" : [ "upnp", 0 ],
        "address" : [ "127.0.0.1", 3456 ],
        "payload" : "" 
    }

Message indicating that the subscriber no longer wants to receive messages from the application that publishes
messages under the "upnp" app-key.

^^^^^^^
Publish
^^^^^^^

.. code-block:: console

    {   "version" : 1 ,
        "opcode" : 3,
        "application" : [ "upnp", 17 ],
        "address" : [ "", 0 ],
        "payload" : "Omega - Gammapolis I. - 0:45" 
    }

Message sent by the application using the app-key "upnp", using app-type 17. 