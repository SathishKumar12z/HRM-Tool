from configs.base_config import BaseConfig

class Configuration(BaseConfig):
    DEBUG = True




    DB_URI = 'mysql+pymysql://root:qwerty@localhost/hrm_tool' 

    # SQLALCHEMY_DATABASE_URL = 'mysql+pymysql://root:@localhost/hotelerp'   89.116.227.168
    ## SQLALCHEMY_DATABASE_URL = "postgresql://user:password@postgresserver/db"