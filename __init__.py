from winreg import (
    CreateKey,
    OpenKey,
    CloseKey,
    SetValueEx,
    QueryValueEx,
    HKEY_CURRENT_USER,
    KEY_READ,
    KEY_WRITE,
    REG_SZ
)

class UserEnv:
    REG_PATH = r'Environment'
    ENV = CreateKey(HKEY_CURRENT_USER, REG_PATH)
    def __init__(self, key):
        self.key = key

    def open_key(self, open_type):
        return OpenKey(HKEY_CURRENT_USER, self.REG_PATH, 0, open_type)

    def set(self, value):
        key = self.open_key(KEY_WRITE)
        SetValueEx(key, self.key, 0, REG_SZ, value)
        CloseKey(key)

    def get(self, default=None):
        key = self.open_key(KEY_READ)
        try:
            value, regtype = QueryValueEx(key, self.key)
        except FileNotFoundError:
            value = default

        CloseKey(key)
        return value
