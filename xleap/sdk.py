import logging
import os

import xleap._client
from xleap.config import Keys
from xleap.utils.login import Auth

logger = logging.getLogger(__name__)


class Xleap(xleap._client.V1Api):
    def __init__(
        self, api_key: str = None, host: str = "http://localhost:8000"
    ) -> None:
        self.__api_key = (
            os.getenv(Keys.API_KEY.value) or api_key or self._load_auth_header()
        )
        if not self.__api_key:
            logger.warning("api key not available")

        host = os.getenv(Keys.API_ENDPOINT.value) or host

        config = xleap._client.Configuration(
            host=host,
            api_key={"api": self.__api_key},
            api_key_prefix={"api": "API_KEY"},
        )

        api_client = xleap._client.ApiClient(config)

        if config.api_key:
            api_client.set_default_header(
                "Authorization", config.get_api_key_with_prefix("api")
            )

        super().__init__(api_client)

    def _load_auth_header(self):
        auth = Auth()
        auth.from_env()
        return auth.auth_header
