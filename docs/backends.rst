Text message backends
=====================

.. module:: djsms.backends

The application can be configured to use different backends to send the actual
text messages. Some backends are only used for testing and not intended for
production.

Dummy backend
-------------

.. autoclass:: DummyBackend


Console backend
---------------

.. autoclass:: ConsoleBackend


Nexmo Backend
-------------

.. autoclass:: NexmoBackend


Define your own backend
-----------------------

It's easy to write your own backend. All you have to do is override the
:class:`BaseBackend` class.

.. autoclass:: BaseBackend
    :members:

