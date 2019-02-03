import elasticsearch
from elasticsearch.helpers import bulk


def mapping(index_name):
    es = elasticsearch.Elasticsearch()
    print("MAPPING")
    map = {"mappings": {"_doc": {"properties": {"location": {"type": "geo_point"},
                                                "user_location": {"type": "geo_point"}}}}}
    es.indices.create(index=index_name, body=map)


def insert_elasticsearch(json_list, index_name):
    es = elasticsearch.Elasticsearch()

    actions = [
        {
            "_index": index_name,
            "_type": "_doc",
            "_source": i
        }
        for i in json_list
    ]

    bulk(es, actions, index=index_name)


def override(index_name):
    es = elasticsearch.Elasticsearch()

    es.indices.delete(index=index_name, ignore=[400, 404])
    mapping(index_name)

