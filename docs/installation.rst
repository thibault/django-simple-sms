Installation
============

Install the application with pip::

    pip install django-simple-sms


Add `djsms` to you ``INSTALLED_APPS``::

.. code:: python

    INSTALLED_APPS = (
        …
        'djsms',
        …
    )

Set a :doc:`text message backend </backends>` in your settings::

    DJSMS_BACKEND = 'djsms.backends.FileBasedBackend'
