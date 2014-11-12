Receiving messages
==================

Some providers will allow for incoming text messages. Upon receiving a message,
they will call an api of yours.

Declaring the incoming uri
--------------------------

For accepting incoming text messages, you must import the application views.

.. code:: python

    urlpatterns = patterns('',
        …
        url(r'^djsms', include('djsms.urls')),
        …
    )

A new uri will be available to accept incoming messages::

    http://your-site.com/djsms/incoming/

Check your text message provider configuration to know how to configure this
uri.


Reacting to incoming messages
-----------------------------

.. module:: djsms.models

When a new text messages is received, a new :class:`TextMessage` will be
created. To react to this, you can `use Django signals
<https://docs.djangoproject.com/en/dev/topics/signals/>`_.

Here is a quick example.

.. code:: python

    # -*- coding: utf-8 -*-

    from __future__ import unicode_literals

    from django.db.models.signals import post_save
    from django.dispatch import receiver
    from djsms.models import TextMessage

    from notifications.models import Notification


    @receiver(post_save, sender=TextMessage, dispatch_uid='message_create_notification')
    def create_notification(sender, **kwargs):
        """Create a new ``Notification`` object when a text message is received."""
        message = kwargs.get('instance')
        created = kwargs.get('created')

        if created:
            Notification.objects.create(text_message=message)
