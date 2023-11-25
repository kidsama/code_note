from redis import Redis
from redis import ConnectionPool

rds = Redis(connection_pool=ConnectionPool(
    host="127.0.0.1",
    port=20003,
    db=0,
    password="Kcm.2022",
    decode_responses=True,
))
pipeline = rds.pipeline(transaction=False)
pipeline.set("activation_id", "123asd")
pipeline.set("activation_time", "2024-09-09")
pipeline.set("activation_status", "1")
pipeline.set("activation_user", "admin")
pipeline.set("activation_devices", "30000")

pipeline.execute()
