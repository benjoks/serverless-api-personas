from utils.aws_resources.dynamo_get_data import get_rut_person
from lib.api_responses import response_bad_request,response_not_found,response_success,response_success_data
from utils.constants import MESSAGE_RES_200, DESCRIPTION_RES_200, MESSAGE_RES_400, MESSAGE_RES_404, DESCRIPTION_RES_404, DESCRIPTION_RES_400_DATE,DESCRIPTION_RES_400_RUT,DESCRIPTION_RES_404_DB
import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

def handler(message, context):
    rut=str(message['pathParameters']['rut'])
    if rut.isdigit()==False:
        return response_bad_request(MESSAGE_RES_400, DESCRIPTION_RES_400_RUT % rut)
    logger.info("Rut is :%s",rut)
    response=get_rut_person(rut)
    logger.info("Response is :%s",response)
    if len(response["Items"])>0:
        response["Items"][0]["rut"] = int(response["Items"][0]["rut"])
        data= response["Items"][0]
        mensaje = response_success_data(MESSAGE_RES_200,DESCRIPTION_RES_200,data)
    else:
        return response_not_found(MESSAGE_RES_404,DESCRIPTION_RES_404_DB)
    return mensaje