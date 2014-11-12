# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.db import models


class TextMessage(models.Model):
    """An outgoing or incoming text message representation.

    .. note::

        messages sent as multipart are still represented by a single
        ``TextMessage`` object.

    ``TextMessage`` objects will be created by other part of the app (e.g the
    ``send_text`` method or incoming messages), so you don't have to create
    them by yourself.

    You can however access ``TextMessage`` objects to have information about
    sent and received messages, such as price, status, date of creation, etc.

    The following attributes are available:

        * `frm`: the sender's phone number
        * `to`: the recipient's phone number
        * `text` : the message's content
        * `direction`: flag to show whether it's an incoming or outgoing
          message. Values are 'incoming' or 'outgoing'.
        * `price (Decimal)`: the price billed by your provider for this message
        * `status`: the message's current status
        * `created_on`: the date / time of the message creation

    Example usage::

        >>> message = send_text(text, frm, to)
        >>> print message.price
        0.015
        >>> print message.direction
        'outgoing'
        >>> print message.status
        'sent'

    """
    pass
