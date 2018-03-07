#-*- coding:UTF-8 -*-
#pyversion:python2.7


import logging
from logging.config import fileConfig

fileConfig('logging_config.ini')
logger = logging.getLogger("cse")
#logger.debug('often makes a very good meal of %s', 'visiting tourists')
