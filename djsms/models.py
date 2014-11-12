# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.db import models


class TextMessage(models.Model):
    """A single text message representation.

    Note: messages send as multipart are still represented as a single
    ``TextMessage`` object.

    """
    pass
