from cloud_for_alisa_skill import Alisa_skill


def handler(event, context):
    alisa = Alisa_skill(event, context)
    resp = alisa.resp
    return resp
