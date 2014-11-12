Errors and exceptions
=====================

.. module:: djsms.exceptions

Sending text messages is a tricky job. Your python code will issue an http
request to a text message provider, that will dispatch your message to a
carrier that will dispatch it to the end user handheld. A lot of things could
go wrong.

Hence we define different error classes to handle errors as accurately as
possible.

However, remember that you can never be 100% sure that a given message was
actually read by it's intented recipient.

Exceptions
----------

.. autoexception:: TextMessageError
    :members:
