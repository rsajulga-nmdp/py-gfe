# coding: utf-8

from __future__ import absolute_import
from .base_model_ import Model
from datetime import date, datetime
from typing import List, Dict
from ..util import deserialize_model


class Feature(Model):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, accession: int=None, rank: int=None, sequence: str=None, term: str=None):
        """
        Feature - a model defined in Swagger

        :param accession: The accession of this Feature.
        :type accession: int
        :param rank: The rank of this Feature.
        :type rank: int
        :param sequence: The sequence of this Feature.
        :type sequence: str
        :param term: The term of this Feature.
        :type term: str
        """
        self.swagger_types = {
            'accession': int,
            'rank': int,
            'sequence': str,
            'term': str
        }

        self.attribute_map = {
            'accession': 'accession',
            'rank': 'rank',
            'sequence': 'sequence',
            'term': 'term'
        }

        self._accession = accession
        self._rank = rank
        self._sequence = sequence
        self._term = term

    @classmethod
    def from_dict(cls, dikt) -> 'Feature':
        """
        Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The Feature of this Feature.
        :rtype: Feature
        """
        return deserialize_model(dikt, cls)

    @property
    def accession(self) -> int:
        """
        Gets the accession of this Feature.

        :return: The accession of this Feature.
        :rtype: int
        """
        return self._accession

    @accession.setter
    def accession(self, accession: int):
        """
        Sets the accession of this Feature.

        :param accession: The accession of this Feature.
        :type accession: int
        """

        self._accession = accession

    @property
    def rank(self) -> int:
        """
        Gets the rank of this Feature.

        :return: The rank of this Feature.
        :rtype: int
        """
        return self._rank

    @rank.setter
    def rank(self, rank: int):
        """
        Sets the rank of this Feature.

        :param rank: The rank of this Feature.
        :type rank: int
        """

        self._rank = rank

    @property
    def sequence(self) -> str:
        """
        Gets the sequence of this Feature.

        :return: The sequence of this Feature.
        :rtype: str
        """
        return self._sequence

    @sequence.setter
    def sequence(self, sequence: str):
        """
        Sets the sequence of this Feature.

        :param sequence: The sequence of this Feature.
        :type sequence: str
        """

        self._sequence = sequence

    @property
    def term(self) -> str:
        """
        Gets the term of this Feature.

        :return: The term of this Feature.
        :rtype: str
        """
        return self._term

    @term.setter
    def term(self, term: str):
        """
        Sets the term of this Feature.

        :param term: The term of this Feature.
        :type term: str
        """

        self._term = term

