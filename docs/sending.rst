Sending text messages
=====================

So, how do me actually send text messages?

Quick example
-------------

.. code:: python

    # -*- coding: utf-8 -*-

    from __future__ import unicode_literals

    from djsms import send_text


    frm = '+33123456789'
    to = '+33987654321'
    text = 'Please remember to pick up the bread before coming'
    send_text(text, frm, to)

The ``send_text`` method
------------------------

The easiest way to send text messages is to use the ``send_text`` utility
method. It's a convenient helper to quickly access the application features.

.. automodule:: djsms
    :members: send_text


.. note:: Formatting phone numbers

    Phone numbers must be formatted in international format, with the country
    code at the beginning and a leading "+".
