
import pymysql
from numba.pycc import export
from sqlalchemy import create_engine

HOSTNAME = '127.0.0.1'
DATABASE = 'sakila'
PORT = 3306
USERNAME = 'root'
PASSWORD = '1633476211'
DB_URL = f'mysql+pymysql://{USERNAME}:{PASSWORD}@{HOSTNAME}:{PORT}/{DATABASE}'
engine = create_engine(
    DB_URL,
    max_overflow=0,  # 超过连接池大小外最多创建的连接
    pool_size=5,  # 连接池大小
    pool_timeout=30,  # 池中没有线程最多等待的时间，否则报错
    pool_recycle=-1  # 多久之后对线程池中的线程进行一次连接的回收（重置）
)


