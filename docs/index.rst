Welcome to django-simple-sms's documentation!
=============================================

`django-simple-sms` is a Django application to easily send text messages from
your Django application.

Philosophy
----------

The application intends to give you an easy and quick yet reliable way to send
text messages using a third party text message carrier.

Compatibility
-------------

The application is compatible and tested against the two latest Django versions
(1.6 and 1.7) and the two main Python versions (2.7 and 3.4).

Example usage
-------------

.. code:: python

    # -*- coding: utf-8 -*-

    from __future__ import unicode_literals

    from djsms import send_text


    frm = '+33123456789'
    to = '+33987654321'
    text = 'Please remember to pick up the bread before coming'
    send_text(text, frm, to)

Contents
--------

.. toctree::
   :maxdepth: 2

   installation
   sending
   status_report
   incoming
   backends
   api
