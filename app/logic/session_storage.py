class SessionStorage:
    storage = {}

    @classmethod
    def set(cls, key: str, value: any):
        cls.storage[key] = value

    @classmethod
    def get(cls, key: str) -> any:
        return cls.storage.get[key]
