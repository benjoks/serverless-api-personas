import os
import boto3
from boto3 import resource
from boto3.dynamodb.conditions import Key

REGION_NAME_BY_STAGE = os.getenv('REGION_NAME_BY_STAGE')

TABLA_RUT_PERSONAS = os.getenv("TABLA_RUT_PERSONAS")
dynamo_resource = boto3.resource('dynamodb', region_name=REGION_NAME_BY_STAGE)
dynamo_rut_person = resource('dynamodb', use_ssl=True).Table(TABLA_RUT_PERSONAS)

def get_rut_person(rut_ask):
    try:
        response = dynamo_rut_person.query(
            KeyConditionExpression=
                Key('rut').eq(int(rut_ask))
        )
        return response
    except Exception as e:
        raise Exception(500, e, "poliza: {}".format(rut_ask), 'get_rut_person')