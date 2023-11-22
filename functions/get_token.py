import logging
import json
from utils.authorize import get_token
from lib.api_responses import response_success_data
from utils.constants import MESSAGE_RES_200, DESCRIPTION_RES_200,DESCRIPTION_RES_500,MESSAGE_RES_500

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

def handler(event, _):
    try:
        logger.info("Creando Persona")
        res = get_token()
        return response_success_data(MESSAGE_RES_200,DESCRIPTION_RES_200,res)

    except ValueError as e:
        return ("Error: ",str(e))
         