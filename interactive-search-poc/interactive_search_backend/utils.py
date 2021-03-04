from typing import List
import json


def get_results(
    es_connection,
    query,
    query_fields=("description", "title"),
    filter_category="T-Shirts",
    min_price=0,
    max_price=500,
    required_field="price",
):
    """ Function to get query results from ElasticSearch.
    """
    response = []
    fields = list(query_fields)
    body = {
        "query": {
            "bool": {
                "must": [
                    {"multi_match": {"query": query, "fields": fields}},
                    {"range": {"price": {"gte": min_price, "lt": max_price}}},
                    {"exists": {"field": required_field}},
                ],
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
