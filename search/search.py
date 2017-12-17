from elasticsearch_dsl.connections import connections
from elasticsearch_dsl import DocType, Text, Date, Integer, Search
from elasticsearch.helpers import bulk
from elasticsearch import Elasticsearch
from . import models

connections.create_connection()

class TblescalationIndex(DocType):
    user = Text()
    entry_date = Date()
    status = Text()
    plc_status = Text()
    poa_close = Integer()
    survey = Integer()
    esc_days = Integer()
    case_id = Integer()
    product_family = Text()
    utid = Integer()
    case_description = Text()
    fab_code = Integer()
    max_escalation_level = Text()
    current_esc_level = Text()
    l1 = Integer()
    l2 = Integer()
    l3 = Integer()
    l4 = Integer()
    escalation = Integer()
    deescalation = Integer()
    tse_owner = Text()
    second_owner = Text()
    first_dispatch_tse = Text()
    first_dispatch_tse_date = Integer()
    problem_statement = Text()
    symptoms = Text()
    fault_id = Integer()
    system = Text()
    subsystem = Text()
    fault = Text()
    fix_rca = Text()
    poa = Text()
    tse_analysis = Text()
    plc_track = Text()
    passdown = Text()
    rca_detail = Text()
    second_tse_dispatch_item = Integer()
    second_tse = Text()
    second_escalation = Integer()
    second_deescalation = Integer()
    third_tse_dispatch_item = Integer()
    third_tse = Text()
    image = Integer()
    poa_1 = Text()
    poa_2 = Text()
    poa_3 = Text()
    poa_4 = Text()
    poa_5 = Text()
    seven_step = Text()
    class Meta:
        index = 'tblescalation-index'

class TblinstallbaseIndex(DocType):
    prod_family = Text()
    prod_model = Text()
    alias = Text()
    install_start = Integer()
    warranty_end = Integer()
    ship_date = Integer()
    sales_order = Text()
    tool_life_stage = Text()
    utid = Integer()
    legacy_sn = Text()
    region_code = Integer()
    region = Text()
    bu = Text()
    fab_code = Integer()
    fab = Text()
    svr_unit_code = Integer()
    svr_unit = Text()
    class Meta:
        index = 'tblinstallbase-index'

def bulk_indexing():
    TblinstallbaseIndex.init()
    TblescalationIndex.init()
    es = Elasticsearch()
    bulk(client=es, actions=(b.indexing() for b in models.Tblinstallbase.objects.all().iterator()))
    bulk(client=es, actions=(b.indexing() for b in models.Tblescalation.objects.all().iterator()))

def search_tblinstallbase_utid(value):
    es = Elasticsearch()
    query = Search(using=es, index="tblinstallbase-index").query("match", utid=value)
    response = query.execute()
    return response

def search_tblescalation_utid(value):
    es = Elasticsearch()
    query = Search(using=es, index="tblescalation-index").query("match", utid=value).sort("case_id")
    response = query.execute()
    return response

def search_tblescalation_symptoms(value):
    es = Elasticsearch()
    query = Search(using=es, index="tblescalation-index").query("match", symptoms=value)
    s = query.highlight_options(order='score')
    response = s.execute()
    return response

def search_tblescalation(utid, symptoms):
    es = Elasticsearch()
    query = Search(using=es, index="tblescalation-index").query("match", utid=utid).query("match", symptoms=symptoms).sort("case_id")
    response = query.execute()
    return response
