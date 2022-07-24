from __future__ import annotations

import logging
import os

from .build import BuildApiMixin
from .info import InfoApiMixin
from ..errors import PyBazelException
from ..models.info import InfoKey

log = logging.getLogger(__name__)


class APIClient(BuildApiMixin, InfoApiMixin):
    def __init__(
        self, bazel_options: list[str] | None = None, workspace: str | None = None
    ) -> None:
        self.bazel_options = bazel_options or []
        self.which_bazel = "bazel"
        self.workspace = workspace  # type: ignore[assignment] # https://github.com/python/mypy/issues/3004

    @property
    def which_bazel(self) -> str:
        return self._which_bazel

    @which_bazel.setter
    def which_bazel(self, value: str) -> str:
        self._which_bazel = value

    @property
    def workspace(self) -> str:
        return self._workspace

    @workspace.setter
    def workspace(self, value: str | None) -> None:
        if not value:
            build_workspace = os.getenv("BUILD_WORKSPACE_DIRECTORY")
            if build_workspace:
                value = build_workspace
            else:
                # Infer the workspace from the current directory.
                self._workspace = os.getcwd()
                # Should this not invoke info() and instead parse the file tree?
                value = self.info(InfoKey.workspace)
                logging
        if not value:
            raise PyBazelException("Unable to infer workspace.")
        self._workspace = value
