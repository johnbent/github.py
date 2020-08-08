from datetime import datetime
from typing import List, Optional, Union

from github.abc import Lockable
from github.abc import Node
from github.abc import ProjectOwner
from github.abc import Subscribable
from github.abc import Type
from github.abc import UniformResourceLocatable
from github.enums import RepositoryLockReason
from github.enums import RepositoryPermissions
from .codeofconduct import CodeOfConduct
from .issue import Issue
from .language import Language
from .license import License
from .organization import Organization
from .user import User


class Repository(Lockable, Node, ProjectOwner, Subscribable, Type, UniformResourceLocatable):
    @property
    def allows_merge_commit(self) -> bool: ...
    @property
    def allows_rebase_merge(self) -> bool: ...
    @property
    def allows_squash_merge(self) -> bool: ...
    @property
    def code_of_conduct(self) -> Optional[CodeOfConduct]: ...
    @property
    def created_at(self) -> datetime: ...
    @property
    def database_id(self) -> int: ...
    @property
    def default_branch(self) -> str: ...
    @property
    def description(self) -> str: ...
    @property
    def disk_usage(self) -> int: ...
    @property
    def fork_count(self) -> int: ...
    @property
    def has_issues(self) -> bool: ...
    @property
    def has_wiki(self) -> bool: ...
    @property
    def is_archived(self) -> bool: ...
    @property
    def is_disabled(self) -> bool: ...
    @property
    def is_fork(self) -> bool: ...
    @property
    def is_locked(self) -> bool: ...
    @property
    def is_mirror(self) -> bool: ...
    @property
    def is_private(self) -> bool: ...
    @property
    def is_template(self) -> bool: ...
    @property
    def license(self) -> Optional[License]: ...
    @property
    def name(self) -> str: ...
    @property
    def owner(self) -> Union[Organization, User]: ...
    @property
    def primary_language(self) -> Language: ...
    @property
    def pushed_at(self) -> Optional[datetime]: ...
    @property
    def updated_at(self) -> Optional[datetime]: ...
    @property
    def viewer_can_administer(self) -> bool: ...
    @property
    def viewer_can_update_topics(self) -> bool: ...
    @property
    def viewer_permissions(self) -> RepositoryPermissions: ...

    async def fetch_assignable_users(self) -> List[User]: ...
    async def fetch_collaborators(self) -> List[User]: ...
    async def fetch_issue(self, number: int) -> Issue: ...
    async def fetch_issues(self) -> List[Issue]: ...
    async def fetch_parent(self) -> Optional[Repository]: ...
    async def fetch_template(self) -> Optional[Repository]: ...