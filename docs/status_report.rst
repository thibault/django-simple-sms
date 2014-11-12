Status reports
==============

Some text message providers can asynchronously call one of your api to provide
details about message delivery statuses.

Declaring the callback uri
--------------------------

The application already defines the correct callback uris. All you have to do
is import them in your main's ``urls.py`` file.

.. code:: python

    urlpatterns = patterns('',
        …
        url(r'^djsms', include('djsms.urls')),
        …
    )

Require status reports
----------------------

On most text message carriers, the status report is a per-message option, so we
kept it that way in the application.

.. module:: djsms

To require status updates for a given message, you need to pass the correct
option to :meth:`send_text`:

.. code:: python

    message = send_text(text, frm, to, status_report=True)

Some carriers require that you set the callback uri directly in their
dashboard. Check for your provider documentation. The callback uri will be::

    http://your-site.com/djsms/callback/


Reacting to status updates
--------------------------

.. module:: djsms.models

Internally, the callback view updates the corresponding :class:`TextMessage`
objects. If you need to perform actions on those updates, you can declare
signals in one of your own applicatin. Here is a quick example.


.. code:: python

    # -*- coding: utf-8 -*-

    from __future__ import unicode_literals

    from django.db.models.signals import post_save
    from django.dispatch import receiver
    from djsms.models import TextMessage

    from notifications.models import Notification


    @receiver(post_save, sender=TextMessage, dispatch_uid='message_update_user')
    def update_notification(sender, **kwargs):
        """Update ``Notification`` object when the text message was sent."""
        message = kwargs.get('instance')
        created = kwargs.get('created')

        if not created:
            Notification.object \
                .filter(message=message) \
                .update(status=message.status)
