import logging
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

def prepare_payload_rut_dynamo(detail):
    retorno =  {}
    retorno["rut"] = int(detail["rut"])
    retorno["dv"] = detail["dv"]
    retorno["fecha_nacimiento"] = detail["fecha_nacimiento"]
    retorno["materno"] = detail["materno"]
    retorno["nacionalidad"] =detail["nacionalidad"]
    retorno["nombres"] = detail["nombres"]
    retorno["paterno"] = detail["paterno"]
    retorno["sexo"] = detail["sexo"]
    logger.info(retorno)
    return retorno