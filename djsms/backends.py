# -*- coding: utf-8 -*-

from __future__ import unicode_literals


class BaseBackend(object):
    """The base class for every backends."""
    pass


class DummyBackend(BaseBackend):
    """As it names says, it's a dummy backend.

    This backend does nothing. It exists because it was easy to write :) Just
    kidding… It can be helpful during development phase, but it's obviously useless
    in production.

    .. code:: python

        DJSMS_BACKEND = 'djsms.backends.DummyBackend'

    """
    pass


class ConsoleBackend(BaseBackend):
    """Sends text messages to the console.

    Outputs sent messages to the console. It can be convenient during development,
    but is not intended for production.

    .. code:: python

        DJSMS_BACKEND = 'djsms.backends.ConsoleBackend'

    """
    pass


class NexmoBackend(BaseBackend):
    """Uses the Nexmo provider.

    The Nexmo Backend uses the `Nexmo provider`_ for
    outgoing messages. Internally, the application uses `libnexmo`_
    to communicate with the `Nexmo API`_

    Did I mention that you need an existing Nexmo account? Isn't it obvious?

    .. code:: python

        NEXMO_API_KEY = 'api_key'
        NEXMO_API_SECRET = 'api_secret'
        DJSMS_BACKEND = 'djsms.backends.NexmoBackend'

    .. _Nexmo provider: https://www.nexmo.com
    .. _libnexmo: http://libnexmo.readthedocs.org/
    .. _Nexmo API: https://docs.nexmo.com/index.php/sms-api/send-message

    """
    pass
