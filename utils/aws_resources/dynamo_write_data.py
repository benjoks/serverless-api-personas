import logging
import os
import boto3
from boto3 import resource
from boto3.dynamodb.conditions import Key


REGION_NAME_BY_STAGE = os.getenv('REGION_NAME_BY_STAGE')

TABLA_RUT_PERSONAS = os.getenv("TABLA_RUT_PERSONAS")
dynamo_resource = boto3.resource('dynamodb', region_name=REGION_NAME_BY_STAGE)
dynamo_rut_person = resource('dynamodb', use_ssl=True).Table(TABLA_RUT_PERSONAS)

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)


def write_in_dynamo_rut(detail):
    """" Insert or Update Item to Dynamo Table -> TABLA_RUT_PERSONAS """
    try:
        response = dynamo_rut_person.put_item(
            Item = detail
        )
        logger.info("Lead de alta Cargado a dynamo")
        return response
    except Exception as e:
        raise Exception(500, e, 'write_in_dynamo_altas')
