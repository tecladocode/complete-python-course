import logging

logging.basicConfig(format='%(asctime)s %(levelname)-8s [%(filename)s:%(lineno)d] %(message)s',
                    datefmt='%d-%m-%Y %H:%M:%S',
                    level=logging.DEBUG,
                    filename='logs.txt')
logger = logging.getLogger(__name__)
logger.info('This will not show up.')
logger.warning('This will.')
logger.debug('This is a debug message.')
logger.critical('A critical error occurred.')
