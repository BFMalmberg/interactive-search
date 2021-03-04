from typing import List
import json


def get_results(es_connection, query, query_fields=("description", "title"), filter_category="T-Shirts"):
    """ Function to get query results from ElasticSearch.
    """
    response = []
    fields = list(query_fields)
    body = {
        "query": {
            "bool": {
                "must": {"multi_match": {"query": query, "fields": fields}},
                "filter": {"term": {"categories.keyword": filter_category}},
            }
        }
    }
    res = es_connection.search(index="products", body=body)

    print("Got %d Hits:" % res["hits"]["total"]["value"])
    for hit in res["hits"]["hits"]:
        print("%(title)s: %(description)s" % hit["_source"])

    if res["hits"]["total"]["value"] != 0:
        for result in res["hits"]["hits"]:
            response.append(result)

    return response




