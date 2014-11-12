Backends
========

The application can be configured to use different backends to send the actual
text messages. Some backends are only used for testing.

Dummy backend
-------------

This backend does nothing. It exists because it was easy to write :) Just
kidding… It can be helpful during development phase, but it's obviously useless
in production.

.. code:: python

    DJSMS_BACKEND = 'djsms.backends.DummyBackend'


Console backend
---------------

Outputs sent messages to the console. It can be convenient during development,
but is not intended for production.

.. code:: python

    DJSMS_BACKEND = 'djsms.backends.ConsoleBackend'


Nexmo Backend
-------------

The Nexmo Backend uses the `Nexmo provider <https://www.nexmo.com/>`_ for
outgoing messages. Internally, the application uses `libnexmo
<https://github.com/thibault/libnexmo>`_ to communicate with `the Nexmo API
<https://docs.nexmo.com/index.php/sms-api/send-message>`_.

Did I mention that you need an existing Nexmo account? Isn't it obvious?

.. code:: python

    DJSMS_BACKEND = 'djsms.backends.NexmoBackend'
    NEXMO_API_KEY = 'api_key'
    NEXMO_API_SECRET = 'api_secret'
