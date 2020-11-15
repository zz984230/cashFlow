from abc import abstractmethod, ABCMeta
import toml
import os


class ConfigHandler(metaclass=ABCMeta):
    @abstractmethod
    def set_cfg_path(self, cfg_path):
        pass

    @abstractmethod
    def update(self):
        pass

    @abstractmethod
    def db_cfg(self):
        pass


class Config(ConfigHandler):
    def __init__(self):
        self.cfg_path = ""
        self.db_cfg = None
        self.cfg = {}

    def set_cfg_path(self, cfg_path):
        self.cfg_path = cfg_path

    def __decode(self):
        if not os.path.exists(self.cfg_path):
            raise Exception("f{self.cfg_path} dose not exist")

        toml.load(self.cfg_path, self.cfg)

    def update(self):
        self.__decode()

    def db_cfg(self):
        return self.db_cfg


if __name__ == "__main__":
    c = ConfigHandler("")