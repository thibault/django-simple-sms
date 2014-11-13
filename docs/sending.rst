Sending text messages
=====================

To send text messages, you can use a high-level helper api or use the low level
api.

Quick example
-------------

.. code:: python

    # -*- coding: utf-8 -*-

    from __future__ import unicode_literals

    from djsms import send_text


    frm = '+33123456789'
    to = '+33987654321'
    text = 'Please remember to pick up the bread before coming'
    message = send_text(text, frm, to)

The ``send_text`` method
------------------------

.. note::

    Phone numbers must be formatted in international format, with the country
    code at the beginning and a leading "+".

The easiest way to send text messages is to use the ``send_text`` utility
method. It's a convenient helper to quickly access the application features.

.. automodule:: djsms
    :members: send_text

.. warning::

    Most backends will work using a REST Api. ``send_text`` will result in a
    blocking HTTP request which can generate a noticeable delay if called
    during a client's request processing.

    You might want to delegate the actual call to the method in a Celery task.


The ``TextMessage`` class
-------------------------

.. autoclass:: djsms.models.TextMessage
    :members:

    .. warning::

        The ``price`` attributes contains the price charged by the provider for
        this text message. This price can be expressed in any currency, however,
        depending on your account configuration. Check your provider documentation
        to know more.

    .. data:: STATUSES

        The list of different possible statuses.

            * `created`: the message was just created in the database and was
              not yet submitted to your text message provider
            * `sending`: the message was successfully sent to your provider
            * `sent`: the message was successfully sent to the upstream carrier
            * `delivered`: the message was successfully delivered to the
              destination handset
            * `refused`: the message was refused by your provider
            * `rejected`: the message was refused by the destination carrier

        .. warning::

            Because a message was received and accepted by your text message
            provider does not mean it will be accepted by the destination
            carrier, nor the destination handset. Be careful not to be confused
            by the different statuses.


