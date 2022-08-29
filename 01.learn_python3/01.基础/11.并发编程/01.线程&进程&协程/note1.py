import gevent
from gevent.pool import Pool
from gevent import monkey
monkey.patch_all(ssl=False)