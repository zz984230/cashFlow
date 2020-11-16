import toml
import os
from internal.entity.sqlite_entity import SqliteDb


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
        d = self.__cfg["database"]
        self.__db_cfg = SqliteDb(d["db"],
                                 d["conn_timeout"],
                                 d["table_debts"],
                                 d["table_income"],
                                 d["table_income_payment_flow"],
                                 d["table_investment_flow"],
                                 d["table_investment_info"],
                                 d["table_item_info"],
                                 d["table_payment"],
                                 d["table_property"])

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
