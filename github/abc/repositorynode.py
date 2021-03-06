"""
/github/abc/repositorynode.py

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

class RepositoryNode():
    """
    Represents a node which belongs to a repository.

    Implemented by:

    * :class:`~github.CommitComment`
    * :class:`~github.Issue`
    * :class:`~github.Label`
    * :class:`~github.PullRequest`
    """

    # https://docs.github.com/en/graphql/reference/interfaces#repositorynode

    __slots__ = ()

    async def fetch_repository(self):
        """
        |coro|

        Fetches the repository the repository node belongs to.

        Returns
        -------
        :class:`~github.Repository`
            The repository.
        """

        from github.objects import Repository

        data = await self.http.fetch_repositorynode_repository(self.id)
        return Repository.from_data(data, self.http)
