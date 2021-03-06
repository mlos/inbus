======
Design
======

The project is a first attempt to explore the thoughts presented in 
Object Thinking, by David West, Microsoft Press, 2004

This section describes the objects in the system, their responsibility, 
collaborators, as well as their methods.

**MessageReceiver**

Responsibilities
  Waits for raw Inbus network messages
  and passes them to the MessageTranslator

Collaborators
  * (System)
  * MessageTranslator

Methods
  * waitForMessage


**IncomingMessageTranslator**

Responsibilities
    Translates raw Inbus messages to either a Subscribe, Unsubscribe or Publish
    method, and invokes those methods on its InbusMethodObserver

Collaborators
    List of InbusMethodObservers

Methods
    translate


**Broadcaster** isA **InbusMethodObserver**

Responsibilities
    Broadcasting Publications to a list of Subscribers

Collaborators
    * Registry
    * OutgoingMessageTranslator
    * MessageSender

Methods
    publish


**Registry** isA **MesssageListener**

Responsibilities
    Manages a list of subscribers.

Collaborators
    None 

Methods
    * subscribe add a subscriber
    * unsubscribe: remove from registry
    * subscribers: returns a list of subscribers 


**OutgoingMessageTranslator**

Responsibilities
    Translate the publish method into a raw Inbus network message

Collaborators
    None

Methods
    translate

**MessageSender**

Responsibilities
    Sends a raw Inbus network message to the network

Collaborators
    (System)

Methods
    send

    


