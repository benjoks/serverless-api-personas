# -*- coding: utf-8 -*-
import re

MESSAGE_RES_200 = "Success"
MESSAGE_RES_400 = "Bad request"
MESSAGE_RES_404 = "Not found"
MESSAGE_RES_500 = "Internal server error"


DESCRIPTION_RES_200 = "Se encontro registros"
DESCRIPTION_RES_400 = "Los parametros no son correctos"
DESCRIPTION_RES_404 = "No hay registros que coincidan"
DESCRIPTION_RES_500 = "Ha ocurrido un error, revisar logs"

DESCRIPTION_RES_404_DB = "El rut no se encuentra en la Base de Datos"
DESCRIPTION_RES_400_DATE = "La fecha %s tiene otro formato o no es valida. Prueba con YYYY-MM-DD o una fecha valida"
DESCRIPTION_RES_400_RUT = "El rut %s no es valido"

