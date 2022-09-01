from sys import stderr
from loguru import logger

logger.remove()

#logger.add(
#    './sever/loguru.txt',
#    filter=lambda rec: 'senha' not in rec['message'].lower(),
#    level='INFO'
#)

logger.add(
    sink=stderr,
    format='{time} <r>{level}</r> <g>{message}</g> {file}',
    filter=lambda rec: 'senha' not in rec['message'].lower(),
    #level='INFO'
)
