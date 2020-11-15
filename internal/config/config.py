import toml
import os


class Config(object):
    def __init__(self):
        self.__cfg_path = ""
        self.__db_cfg = None
        self.__cfg = {}

    def set_cfg_path(self, cfg_path):
        self.__cfg_path = cfg_path

    def __decode(self):
        if not os.path.exists(self.__cfg_path):
            raise Exception("%s does not exist" % self.__cfg_path)

        with open(self.__cfg_path, "r") as f:
            self.__cfg = toml.load(f)
        self.__db_cfg = self.__cfg["database"]

    def update(self):
        self.__decode()

    @property
    def db_cfg(self):
        return self.__db_cfg

    @db_cfg.setter
    def db_cfg(self, db_cfg):
        self.__db_cfg = db_cfg


if __name__ == "__main__":
    c = Config()
    c.set_cfg_path("./conf.toml")
    c.update()
    print(c.db_cfg)
