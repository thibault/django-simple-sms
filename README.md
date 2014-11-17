django-simple-sms
=================

Easily send text messages from your Django project.

Features
--------

 * Send text messages from any provider (only Nexmo.com is supported right now)
 * Receive text messages status reports
 * Handle incoming text messages

Documentation
-------------

Check it out on [Read the docs](http://django-simple-sms.readthedocs.org/en/latest/).

Compatibility
-------------

This application is tested agains Django 1.6 and 1.7, and Python 2.7 and 3.4.

Installation
------------

Installation is easy with `pip`.

    pip install django-simple-sms

Add `djsms` to you ``INSTALLED_APPS``:

```python
INSTALLED_APPS = (
    …
    'djsms',
    …
)
```

Set a [text message backend](http://django-simple-sms.readthedocs.org/en/latest/backends.html) in your settings::

    DJSMS_BACKEND = 'djsms.backends.FileBasedBackend'

Quick example
-------------

```python
# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from djsms import send_text


frm = '+33123456789'
to = '+33987654321'
text = 'Please remember to pick up the bread before coming'
message = send_text(text, frm, to)
```

Contact / Contributors
----------------------

[See here](http://django-simple-sms.readthedocs.org/en/latest/colophon.html)

License
-------

[See here](https://github.com/thibault/django-simple-sms/blob/master/LICENSE)
