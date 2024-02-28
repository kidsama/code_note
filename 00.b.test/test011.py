from sqlalchemy import (create_engine, Table, Column, MetaData, Unicode,
                        Float, LargeBinary)

tablename = "auto_create1"
tableschema = None
engine_options = None


DIALECT = "mysql"
DRIVER = "mysqldb"
USERNAME = "root"

PASSWORD = "lwx984502"
HOST = "127.0.0.1"
PORT = "3306"
DATABASE = "liu"

url = "{}+{}://{}:{}@{}:{}/{}?charset=utf8".format(
    DIALECT, DRIVER, USERNAME, PASSWORD, HOST, PORT, DATABASE
)
engine = create_engine(url, **(engine_options or {}))


xxx = Table(
    tablename, MetaData(),
    Column('id', Unicode(191), primary_key=True),
    Column('next_run_time', Float(25), index=True),
    Column('job_state', LargeBinary(16777215), nullable=False),
    schema=tableschema
)

xxx.create(engine, True)
