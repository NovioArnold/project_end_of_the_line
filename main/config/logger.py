import logging


logging.basicConfig(
    filename='app_debug.log',
    filemode='a',
    encoding='utf-8',
    level=logging.DEBUG,
    format='%(asctime)s %(levelname)s %(name)s %(message)s'
)


logger = logging.getLogger(__name__)







