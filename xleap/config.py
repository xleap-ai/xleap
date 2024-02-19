from enum import Enum


class Keys(Enum):
    API_KEY = "XLEAP_API_KEY"
    API_HOST = "XLEAP_API_HOST"
    USERNAME = "XLEAP_USERNAME"
    PROJECT_ID = "XLEAP_PROJECT_ID"

    @property
    def value(self) -> str:
        return f"XLEAP_{self.name}"

    @property
    def suffix(self):
        return self.name.lower()

    def __eq__(self, __o: object) -> bool:
        return self.value == __o
