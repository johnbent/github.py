"""
/github/objects/pullrequest.py

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

from github.abc import Assignable
from github.abc import Closable
from github.abc import Comment
from github.abc import Commentable
from github.abc import Labelable
from github.abc import Lockable
from github.abc import Node
from github.abc import Participable
from github.abc import Reactable
from github.abc import RepositoryNode
from github.abc import Subscribable
from github.abc import Type
from github.abc import UniformResourceLocatable
from github.abc import Updatable
from github.enums import PullRequestState


class PullRequest(Assignable, Closable, Comment, Commentable, Labelable, Lockable, Node,
                  Participable, Reactable, RepositoryNode, Subscribable, Type,
                  UniformResourceLocatable, Updatable):
    """
    Represents a pull request on a :class:`~github.Repository`.

    https://developer.github.com/v4/object/pullrequest/

    Implements:

    * :class:`~github.abc.Assignable`
    * :class:`~github.abc.Closable`
    * :class:`~github.abc.Comment`
    * :class:`~github.abc.Commentable`
    * :class:`~github.abc.Labelable`
    * :class:`~github.abc.Lockable`
    * :class:`~github.abc.Node`
    * :class:`~github.abc.Participable`
    * :class:`~github.abc.Reactable`
    * :class:`~github.abc.RepositoryNode`
    * :class:`~github.abc.Subscribable`
    * :class:`~github.abc.Type`
    * :class:`~github.abc.UniformResourceLocatable`
    * :class:`~github.abc.Updatable`
    """

    __slots__ = ("data", "http")

    def __init__(self, data, http):
        self.data = data
        self.http = http

    @classmethod
    def from_data(cls, data, http):
        if isinstance(data, dict):
            return cls(data, http)
        elif isinstance(data, list):
            return [cls(pull, http) for pull in data]

    @property
    def additions(self) -> int:
        """
        The number of additions in the pull request.
        """

        return self.data["additions"]

    @property
    def database_id(self) -> int:
        """
        The primary key for the pull request from the database.
        """

        return self.data["databaseId"]

    @property
    def deletions(self) -> int:
        """
        The number of deletions in the pull request.
        """

        return self.data["deletions"]

    @property
    def number(self) -> int:
        """
        The pull request number.
        """

        return self.data["number"]

    @property
    def state(self) -> PullRequestState:
        """
        The pull request state.
        """

        state = self.data["state"]
        return PullRequestState.from_data(state)

    @property
    def title(self) -> int:
        """
        The pull request title.
        """

        return self.data["title"]