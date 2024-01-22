import base64
import json
import logging
import os
import pathlib
from dataclasses import dataclass
from typing import Optional

from xleap.config import Keys

XLEAP_CREDENTIAL_FILENAME = ".config/xleap-config.json"


logger = logging.getLogger(__name__)


@dataclass
class Auth:
    username: Optional[str] = None
    api_key: Optional[str] = None
    project_id: Optional[str] = None

    secrets_file = pathlib.Path.home() / pathlib.Path(XLEAP_CREDENTIAL_FILENAME)

    @property
    def auth_header(self) -> Optional[str]:
        if not self.username or not self.api_key:
            raise AttributeError("Failed: no authentication header available")

        token = f"{self.username}:{self.api_key}"
        return f"Basic {base64.b64encode(token.encode('ascii')).decode('ascii')}"

    def from_env(self) -> bool:
        """Load credentials from env variable"""
        logger.info("loading credentials from environment variables")

        for key in Keys:
            print(key.suffix, key.value)
            setattr(self, key.suffix, os.getenv(key.value))

        if not self.username:
            logger.warn("username is required")

        if not self.api_key:
            logger.warn("api_key is required")

        if not self.project_id:
            logger.warn("project_id is required")

        return self.auth_header

    def from_file(self) -> bool:
        """Load credentials from disk"""

        if not self.secrets_file.exists():
            logger.info("Credentials file not found.")
            return False

        with self.secrets_file.open() as creds:
            credentials = json.load(creds)
            for key in Keys:
                setattr(self, key.suffix, credentials.get(key.suffix, None))
            return True

    def save(self) -> None:
        """Save credentials to disk."""

        logger.debug("saving credentials")

        self.secrets_file.parent.mkdir(exist_ok=True, parents=True)

        with self.secrets_file.open("w") as creds:
            json.dump(
                {
                    f"{Keys.USERNAME.suffix}": self.username,
                    f"{Keys.API_KEY.suffix}": self.api_key,
                    f"{Keys.PROJECT_ID.suffix}": self.project_id,
                },
                creds,
            )

        logger.info("credentials saved successfully")

    def clean(self) -> None:
        """clean credentials from disk"""

        logger.debug("removing credentials")

        if self.secrets_file.exists():
            self.secrets_file.unlink()

        logger.info("credentials removed")
