import logging


base_logger = logging.getLogger('base')
base_logger.setLevel(logging.DEBUG)
console_handler = logging.StreamHandler()
console_format = logging.Formatter('%(name)s | %(levelname)s | %(message)s')
console_handler.setFormatter(console_format)
base_logger.addHandler(console_handler)
