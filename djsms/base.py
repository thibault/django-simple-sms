# -*- coding: utf-8 -*-

from __future__ import unicode_literals


def send_text(text, frm, to):
    """A convenient helper to quickly access the application features.

    :param text: the text message body. It's length is not limited, but if it's
        too long, your carrier will probably split it and send in a multipart
        text message, and you will be charged accordingly
    :param frm: the originator phone number. Some carriers accept
        alphanumerical values, but it really depends on mobile networks and
        local laws.
    :param to: the recipient phone number.

    """
    pass
