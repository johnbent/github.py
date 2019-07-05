"""
/github/objects/abc/actor.py

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


"""
https://developer.github.com/v4/interface/actor/

... implemented by ...
User

... not implemented ...
resourcePath
"""
class Actor():
    """
    Represents an object which can take actions on GitHub.
    """

    @property
    def avatar_url(self) -> str:
        """
        A URL pointing to the actor's public avatar.
        """

        return self.data.get("avatarUrl")

    @property
    def login(self) -> str:
        """
        The username of the actor.
        """

        return self.data.get("login")

    @property
    def url(self) -> str:
        """
        The HTTP URL for this actor.
        """

        return self.data.get("url")

    async def fetch_avatar_url(self, size: int=None) -> str:
        """

        """

        ...