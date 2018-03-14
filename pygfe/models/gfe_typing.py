# coding: utf-8

from __future__ import absolute_import
from pygfe.models.feature import Feature
from .base_model_ import Model
from datetime import date, datetime
from typing import List, Dict
from ..util import deserialize_model


class GfeTyping(Model):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, gfe: str=None, features_shared: int=None, shares: List[Feature]=None):
        """
        GfeTyping - a model defined in Swagger

        :param gfe: The gfe of this GfeTyping.
        :type gfe: str
        :param features_shared: The features_shared of this GfeTyping.
        :type features_shared: int
        :param shares: The shares of this GfeTyping.
        :type shares: List[Feature]
        """
        self.swagger_types = {
            'gfe': str,
            'features_shared': int,
            'shares': List[Feature]
        }

        self.attribute_map = {
            'gfe': 'gfe',
            'features_shared': 'features_shared',
            'shares': 'shares'
        }

        self._gfe = gfe
        self._features_shared = features_shared
        self._shares = shares

    @classmethod
    def from_dict(cls, dikt) -> 'GfeTyping':
        """
        Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The GfeTyping of this GfeTyping.
        :rtype: GfeTyping
        """
        return deserialize_model(dikt, cls)

    @property
    def gfe(self) -> str:
        """
        Gets the gfe of this GfeTyping.

        :return: The gfe of this GfeTyping.
        :rtype: str
        """
        return self._gfe

    @gfe.setter
    def gfe(self, gfe: str):
        """
        Sets the gfe of this GfeTyping.

        :param gfe: The gfe of this GfeTyping.
        :type gfe: str
        """

        self._gfe = gfe

    @property
    def features_shared(self) -> int:
        """
        Gets the features_shared of this GfeTyping.

        :return: The features_shared of this GfeTyping.
        :rtype: int
        """
        return self._features_shared

    @features_shared.setter
    def features_shared(self, features_shared: int):
        """
        Sets the features_shared of this GfeTyping.

        :param features_shared: The features_shared of this GfeTyping.
        :type features_shared: int
        """

        self._features_shared = features_shared

    @property
    def shares(self) -> List[Feature]:
        """
        Gets the shares of this GfeTyping.

        :return: The shares of this GfeTyping.
        :rtype: List[Feature]
        """
        return self._shares

    @shares.setter
    def shares(self, shares: List[Feature]):
        """
        Sets the shares of this GfeTyping.

        :param shares: The shares of this GfeTyping.
        :type shares: List[Feature]
        """

        self._shares = shares

