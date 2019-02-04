import elasticsearch
from elasticsearch.helpers import bulk
from lib import static
import json


def mapping(index_name, mapping):
    es = elasticsearch.Elasticsearch()
    map = mapping
    es.indices.create(index=index_name, body=map)


def insert_elasticsearch(json_list, index_name, doc_type):
    es = elasticsearch.Elasticsearch()
    actions = [
        {
            "_index": index_name,
            "_type": doc_type,
            "_source": i
        }
        for i in json_list
    ]
    bulk(es, actions, index=index_name)


def override_user(index_name):
    es = elasticsearch.Elasticsearch()
    es.indices.delete(index=index_name, ignore=[400, 404])
    mapping(index_name, static.MAPPING_USER)


def override_message(index_name):
    es = elasticsearch.Elasticsearch()
    es.indices.delete(index=index_name, ignore=[400, 404])
    mapping(index_name, static.MAPPING_MESSAGE)


# Generate bulk to insert in elasticsearch
def generate_bulk(list_dic, index_name, doc_type):
    bulk_partition = 100000
    total = len(list_dic)
    number_of_bulk = int(total / bulk_partition)
    if total % bulk_partition != 0:
        number_of_bulk = int(total / bulk_partition) + 1
    for i in range(number_of_bulk):
        # Put json bulk in a file
        with open("outputs/{}_{}.json".format(index_name, i), "w") as outfile:
            count = 0
            for i in list_dic:
                outfile.write(json.dumps({"index": {"_index": index_name, "_type": doc_type}}))
                outfile.write("\n")
                outfile.write(json.dumps(i))
                outfile.write("\n")
                count += 1
