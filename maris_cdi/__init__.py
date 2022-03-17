""" maris_cdi

.. module:: maris_cdi
    :synopsis: py library to retrieve ODV datasets from the maris CDI service (api)

.. moduleauthor:: Marc Portier <marc.portier@gmail.com>

"""

from .cdi_client import MyModel
import logging

__all__ = ['MyModel']

log = logging.getLogger(__name__)
log.addHandler(logging.NullHandler())
