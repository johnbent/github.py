"""
/github/abc/sponsorable.py

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

class Sponsorable():
    """
    Represents an object which can be sponsored.

    https://developer.github.com/v4/interface/sponsorable/

    Implemented by:

    * :class:`~github.AuthenticatedUser`
    * :class:`~github.Organization`
    * :class:`~github.User`
    """

    __slots__ = ()

    async def fetch_sponsor_listing(self):
        """
        |coro|

        Fetches the sponsorable's sponsor listing.

        Returns
        -------
        Optional[:class:`~github.objects.SponsorListing`]
            The sponsorable's sponsor listing.
        """

        # prevent cyclic imports
        from github.objects import SponsorListing

        data = await self.http.fetch_sponsorable_sponsor_listing(self.id)
        return SponsorListing.from_data(data, self.http)