"""
This script extracts information from the title and description fields and uses it to fill other/new fields.
For instance:
* scan title and description for brand names and add them to empty brand fields;
* scan title and description for sizes and add them to a new field size.

TODO: note work in progress
"""

from elastic_connector import execute_query, get_connection_from_env, update_document, delete_index_by_name
from elasticsearch.helpers import bulk
from pprint import pprint

INDEX = "products_diede"

query = {
    "query": {
        "exists": {
            "field": "old_brand"
        }
    }
}


def _preprocess_product(product_json):

    return product_json


def ingest_to_index():
    """
    Ingests all products into the index. Does some preprocessing before hand.
    :return:
    """
    es = get_connection_from_env()

    with open("../../meta_Clothing_Shoes_and_Jewelry.json") as myfile:
        while next(myfile):
            head = [eval(next(myfile)) for x in range(50000)]
            parsed = [dict(_preprocess_product(pr), **{"_index": INDEX}) for pr in head if pr.get("description")]
            print(bulk(es, parsed))


if __name__ == '__main__':
    es = get_connection_from_env()
    delete_index_by_name(es_connection=es, index=INDEX)
    ingest_to_index()
    print("Done")


# def store_old_brand_value():
#     """
#     Creates a new field for all articles named "old_brand" containing the old value of the "brand" field.
#     """
#     es = get_connection_from_env()
#     n_results = 1
#
#     while n_results > 0:
#         results = execute_query(es_connection=es,
#                                 query=query,
#                                 index=INDEX)
#
#         n_results = len(results["hits"]["hits"])
#         for result in results["hits"]["hits"]:
#             doc_id = result["_id"]
#             doc_data = result["_source"]
#             if "brand" in doc_data:
#                 old_brand = doc_data["brand"]
#             else:
#                 old_brand = None
#
#             doc_data["old_brand"] = old_brand
#             update_document(es_connection=es,
#                             document_id=doc_id,
#                             document_data={"doc": {"old_brand": old_brand}},
#                             index=INDEX)