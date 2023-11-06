from utils.aws_resources.dynamo_get_data import get_rut_person
from utils.gen import validate_date_in
from lib.api_responses import response_bad_request,response_not_found,response_success
from utils.constants import MESSAGE_RES_200, DESCRIPTION_RES_200, MESSAGE_RES_400, MESSAGE_RES_404, DESCRIPTION_RES_404, DESCRIPTION_RES_400_DATE,DESCRIPTION_RES_400_RUT,DESCRIPTION_RES_404_DB
import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

def handler(message, context):
    date_in= str(message['pathParameters']['fecha'])
    logger.info("Date is :%s",date_in)
    if validate_date_in(date_in)==False:
        return response_bad_request(MESSAGE_RES_400, DESCRIPTION_RES_400_DATE % date_in)
    rut=str(message['pathParameters']['rut'])
    if rut.isdigit()==False:
        return response_bad_request(MESSAGE_RES_400, DESCRIPTION_RES_400_RUT % rut)
    logger.info("Rut is :%s",rut)
    response=get_rut_person(rut)
    logger.info("Response is :%s",response)
    if len(response["Items"])>0:
        is_date=is_born_date(date_in,response["Items"])
    else:
        return response_not_found(MESSAGE_RES_404,DESCRIPTION_RES_404_DB)
    if is_date:
        mensaje=response_success(MESSAGE_RES_200, DESCRIPTION_RES_200)
    else:
        mensaje=response_not_found(MESSAGE_RES_404,DESCRIPTION_RES_404)
    return mensaje

def is_born_date(date_in,persons):
    is_born = False
    for person in persons:
        logger.info("Fecha -> %s",person["fecha_nacimiento"])
        if str(person["fecha_nacimiento"])==str(date_in):
            is_born=True
    return is_born
