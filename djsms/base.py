# -*- coding: utf-8 -*-

from __future__ import unicode_literals


def send_text(text, frm, to, fail_silently=True, status_report=False):
    """A convenient helper to quickly access the application features.

    Required params:

    :param text: the text message body. It's length is not limited, but if it's
        too long, your carrier will probably split it and send in a multipart
        text message, and you will be charged accordingly
    :param frm: the originator phone number. Some carriers accept
        alphanumerical values, but it really depends on mobile networks and
        local laws.
    :param to: the recipient phone number.

    Additionals params:

    :param fail_silently: If True, errors will just be ignored.
        Otherwise raises a :class:`~djsms.exceptions.DjsmsError`. Default to
        True.
    :param status_report: If True, asks the selected carrier to provide
        status report by asynchronously calling an uri. If your carrier does'nt
        provide this option, the parameter value will simply be ignored.

    """
    pass
