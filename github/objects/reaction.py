"""
/github/objects/reaction.py

    Copyright (c) 2019 ShineyDev
    
    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at

        http://www.apache.org/licenses/LICENSE-2.0

    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.
"""

import datetime
import typing

from github import utils
from github.enums import Reaction as reaction_enum


class Reaction():
    """
    Represents a GitHub reaction.

    https://developer.github.com/v4/object/reactiongroup/
    """

    __slots__ = ("data", "http")

    def __init__(self, data: dict, http):
        self.data = data
        self.http = http

    def __repr__(self) -> str:
        return "<{0.__class__.__name__} content='{0.content}'>".format(self)

    @classmethod
    def from_data(data: list, http) -> typing.Iterable["Reaction"]:
        reactions = list()

        for (reaction) in data:
            reactions.append(cls(reaction, http))

        return reactions

    @property
    def created_at(self) -> datetime.datetime:
        """
        The date and time at which this reaction was added.
        """

        created_at = self.data["createdAt"]
        return utils.iso_to_datetime(created_at)

    @property
    def emoji(self) -> str:
        """
        The reaction's emoji.
        """

        content = self.data["content"]
        return reaction_enum._dict[content]

    @property
    def name(self) -> str:
        """
        The reaction's :attr:`.emoji` as a string.
        """

        return self.data["content"]

    @property
    def users(self) -> typing.Iterable["User"]:
        """
        A list of :class:`github.User` who reacted.
        """

        # prevent cyclic imports
        from github.objects import User

        users = self.data["users"]
        return User.from_data(users, self.http)

    @property
    def viewer_has_reacted(self) -> bool:
        """
        Whether or not the authenticated user has reacted.
        """

        return self.data["viewerHasReacted"]