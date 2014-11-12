Installation
============

Install the application with pip::

    pip install django-simple-sms


Add `djsms` to you ``INSTALLED_APPS``

.. code:: python

    INSTALLED_APPS = (
        …
        'djsms',
        …
    )

Set a text message backend with the ``DJSMS_BACKEND`` ::

    DJSMS_BACKEND = 'djsms.backends.FileBasedBackend'
