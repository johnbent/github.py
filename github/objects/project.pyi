from datetime import datetime
from typing import List

from github.abc import Closable
from github.abc import Node
from github.abc import Type
from github.abc import UniformResourceLocatable
from github.abc import Updatable
from github.enums import ProjectState
from .projectcolumn import ProjectColumn


class Project(Closable, Node, Type, UniformResourceLocatable, Updatable):
    @property
    def body(self) -> str: ...
    @property
    def body_html(self) -> str: ...
    @property
    def created_at(self) -> datetime: ...
    @property
    def database_id(self) -> int: ...
    @property
    def name(self) -> str: ...
    @property
    def number(self) -> int: ...
    @property
    def state(self) -> ProjectState: ...
    @property
    def updated_at(self) -> datetime: ...

    async def fetch_columns(self) -> List[ProjectColumn]: ...
    async def create_column(self, *, name: str) -> ProjectColumn: ...