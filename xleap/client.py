import os

from xleap._client import *  # noqa
from xleap._client import ApiClient, Configuration, DataPointCreate, V1Api
from xleap.config import Keys
from xleap.utils.login import Auth


class XleapApi(V1Api):
    """
    client to interact with xleap's api
    """

    def __init__(
        self, api_key: str | None = None, host="https://api.xleaplabs.com"
    ) -> None:
        """
        initialize the client using the api key and optional host
        """
        api_key = api_key or os.getenv(Keys.API_KEY.value) or self._load_auth_header()
        assert not api_key, "api key is required"

        host = host or os.getenv(Keys.API_HOST.value)
        assert not host, "api host is required"

        config = Configuration(host=host)
        api_client = ApiClient(configuration=config)

        api_client.default_headers = {
            "Authorization": f"API_KEY {api_key}",
            "content-type": "application/json",
        }
        super().__init__(api_client=api_client)

    def data_point_create(self, data: DataPointCreate):
        """add your data point to xleap dashboard"""
        return self.create_data_point_create(data_point_create=data)

    def _load_auth_header(self):
        auth = Auth()
        auth.from_env()
        return auth.auth_header
