"""
/github/objects/label.py

    Copyright (c) 2019-2020 ShineyDev

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

from github import utils
from github.iterator import CollectionIterator
from github.abc import Node
from github.abc import RepositoryNode
from github.abc import Type
from github.abc import UniformResourceLocatable
from .issue import Issue
from .pullrequest import PullRequest


class Label(Node, RepositoryNode, Type, UniformResourceLocatable):
    """
    Represents a label on a :class:`~github.abc.Labelable`.

    Implements:

    * :class:`~github.abc.Node`
    * :class:`~github.abc.RepositoryNode`
    * :class:`~github.abc.Type`
    * :class:`~github.abc.UniformResourceLocatable`
    """

    # https://docs.github.com/en/graphql/reference/objects#label

    __slots__ = ("data", "http")

    def __init__(self, data, http):
        self.data = data
        self.http = http

    @property
    def color(self):
        """
        The color of the label in the GitHub UI.

        :type: :class:`str`
        """

        return self.data["color"]

    colour = color

    @property
    def created_at(self):
        """
        When the label was created.

        :type: :class:`~datetime.datetime`
        """

        created_at = self.data["createdAt"]
        return utils.iso_to_datetime(created_at)

    @property
    def description(self):
        """
        The description of the label.

        :type: :class:`str`
        """

        return self.data["description"] or ""

    @property
    def is_default(self):
        """
        Whether the label is a default label.

        :type: :class:`bool`
        """

        return self.data["isDefault"]

    @property
    def name(self):
        """
        The name of the label.

        :type: :class:`str`
        """

        return self.data["name"]

    @property
    def updated_at(self):
        """
        When the label was last updated.

        :type: :class:`~datetime.datetime`
        """

        updated_at = self.data["updatedAt"]
        return utils.iso_to_datetime(updated_at)

    def fetch_issues(self, **kwargs):
        """
        |aiter|

        Fetches issues with the label.

        Returns
        -------
        :class:`~github.iterator.CollectionIterator`
            An iterator of :class:`~github.Issue`.
        """

        def map_func(data):
            return Issue.from_data(data, self.http)

        return CollectionIterator(self.http.fetch_label_issues, self.id,
                                  map_func=map_func, **kwargs)

    def fetch_pull_requests(self, **kwargs):
        """
        |aiter|

        Fetches pull requests with the label.

        Returns
        -------
        :class:`~github.iterator.CollectionIterator`
            An iterator of :class:`~github.PullRequest`.
        """

        def map_func(data):
            return PullRequest.from_data(data, self.http)

        return CollectionIterator(self.http.fetch_label_pull_requests,
                                  self.id, map_func=map_func, **kwargs)
