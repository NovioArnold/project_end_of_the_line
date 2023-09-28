import logging
import logging.handlers

logging.basicConfig(
    filename='app_debug.log',
    filemode='a',
    encoding='utf-8',
    level=logging.DEBUG,
    format='%(asctime)s %(levelname)s %(name)s %(message)s'
)

logging.handlers.TimedRotatingFileHandler('midnight.log', when='midnight', interval=1, backupCount=7)

logger = logging.getLogger(__name__)







