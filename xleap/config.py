from enum import Enum


class Keys(Enum):
    USERNAME = "XLEAP_USERNAME"
    API_KEY = "XLEAP_API_KEY"
    PROJECT_ID = "XLEAP_PROJECT_ID"
    API_ENDPOINT = "XLEAP_API_ENDPOINT"

    @property
    def value(self) -> str:
        return f"XLEAP_{self.name}"

    @property
    def suffix(self):
        return self.name.lower()

    def __eq__(self, __o: object) -> bool:
        return self.value == __o
