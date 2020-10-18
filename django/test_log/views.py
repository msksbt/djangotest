import datetime
from django.http import HttpResponse
from logging import getLogger

logger = getLogger(__name__)


def index(request):
    now = datetime.datetime.now()
    html = "<html><body>It is now %s.</body></html>" % now

    logger.critical('This is critical.')
    logger.error('This is error.')
    logger.warning('This is warning.')
    logger.info('This is info.')
    logger.debug('This is debug.')

    return HttpResponse(html)

