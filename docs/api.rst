API
===

Text message objects
--------------------

Every text message is stored in database.

.. module:: djsms.models

.. autoclass:: TextMessage
    :members:

    .. warning:: Don't mess up with the currency

        The ``price`` attributes contains the price charged by the provider for
        this text message. This price can be expressed in any currency, however,
        depending on your account configuration. Check your provider documentation
        to know more.

    .. data:: STATUSES

        The list of different possible statuses.

            * `created`: the message was just created in the database and was
              not yet submitted to your text message provider
            * `sending`: the message was successfully sent to your provider
            * `sent`: the message was successfully sent to the upstream carrier
            * `delivered`: the message was successfully delivered to the
              destination handset
            * `refused`: the message was refused by your provider
            * `rejected`: the message was refused by the destination carrier

        .. warning:: Don't confuse statuses

            Because a message was received and accepted by your text message
            provider does not mean it will be accepted by the destination
            carrier, nor the destination handset. Be careful not to be confused
            by the different statuses.


Backends
--------

.. module:: djsms.backends

Every text message backend must override :class:`~BaseBackend`.

.. autoclass:: BaseBackend
    :members:


Exceptions
----------

Custom exception classes are defined to handle the different error cases.

.. module:: djsms.exceptions

.. autoexception:: TextMessageError
    :members:
