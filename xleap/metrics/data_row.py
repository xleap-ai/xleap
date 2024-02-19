from dataclasses import dataclass


@dataclass
class DataRow:
    prompt: str
    response: str | None = None

    def get(self, attr_name: str):
        return getattr(self, attr_name)

    def set(self, attr_name: str, value: any):
        return setattr(self, attr_name, value)

    def has(self, attr_name: str):
        return hasattr(self, attr_name)
