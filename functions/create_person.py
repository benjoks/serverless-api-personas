import logging
import json
from utils.aws_resources.dynamo_write_data import write_in_dynamo_rut
from utils.aws_resources.dynamo_prepare_payload import prepare_payload_rut_dynamo
from utils.gen import validate_date_in, validar_rut
from lib.api_responses import response_bad_request,response_success
from utils.constants import MESSAGE_RES_200, DESCRIPTION_RES_201, MESSAGE_RES_400, DESCRIPTION_RES_400_DATE,DESCRIPTION_RES_400_VARIABLE,DESCRIPTION_RES_400_RUT

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

def handler(event, _):
    logger.info("scope al event: %s", event)
    logger.info("################ BODY ################")
    logger.info(event["body"])
    body = json.loads(event["body"])

    try:
        logger.info("Creando Persona")
        detail = prepare_payload_rut_dynamo(body)
        validate = validate_input(detail)
        if (validate != True):
            return validate
        db_response = write_in_dynamo_rut(detail)
        logger.info("DB: %s",db_response)
        if(db_response["ResponseMetadata"]["HTTPStatusCode"] == 200 or 201):
            return response_success(MESSAGE_RES_200, DESCRIPTION_RES_201)
        return "Que es lo que pasa, chico"

    except ValueError as e:
        return ("Error: ",str(e))
    
def validate_input(body):
    if validate_date_in(body["fecha_nacimiento"])==False:
        return response_bad_request(MESSAGE_RES_400, DESCRIPTION_RES_400_DATE % body["fecha_nacimiento"])
    if (len(body["paterno"])>15):
        return response_bad_request(MESSAGE_RES_400, DESCRIPTION_RES_400_VARIABLE % (body["paterno"],"15"))
    if (len(body["nombres"])>15):
        return response_bad_request(MESSAGE_RES_400, DESCRIPTION_RES_400_VARIABLE % (body["nombres"],"15"))
    if (len(body["nacionalidad"])>15):
        return response_bad_request(MESSAGE_RES_400, DESCRIPTION_RES_400_VARIABLE % (body["nacionalidad"],"10"))
    if (len(body["materno"])>15):
        return response_bad_request(MESSAGE_RES_400, DESCRIPTION_RES_400_VARIABLE % (body["materno"],"15"))
    sexo = ['masculino','m','femenino','f','otro','o']
    if ((body["sexo"].lower() in sexo) == False):
        return response_bad_request(MESSAGE_RES_400, "Variable Sexo no es valida")
    if validar_rut(str(body["rut"]),body["dv"])!=True:
        rut = str(body["rut"])+"-"+body["dv"]
        return response_bad_request(MESSAGE_RES_400, DESCRIPTION_RES_400_RUT % rut)
    return True
         