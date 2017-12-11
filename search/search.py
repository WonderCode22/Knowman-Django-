from elasticsearch_dsl.connections import connections
from elasticsearch_dsl import DocType, Text, Date, Integer
from elasticsearch.helpers import bulk
from elasticsearch import Elasticsearch
from . import models

connections.create_connection()

class TblinstallbaseIndex(DocType):
    prod_family = Text
    prod_model = Text
    alias = Text
    install_start = Integer
    warranty_end = Integer
    ship_date = Integer
    sales_order = Text
    tool_life_stage = Text
    utid = Integer
    legacy_sn = Text
    region_code = Integer
    region = Text
    bu = Text
    fab_code = Integer
    fab = Text
    svr_unit_code = Integer
    svr_unit = Text

    class Meta:
        index = 'TBLInstallBase-Index'
        
def bulk_indexing():
    TblinstallbaseIndex.init()
    es = Elasticsearch()
    bulk(client=es, actions=(b.indexing() for b in models.TBLInstallBase.objects.all().iterator()))