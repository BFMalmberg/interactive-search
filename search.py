from elastic_connector import get_connection_from_env

es = get_connection_from_env()


def get_results(
    query, query_fields=("description", "title"), filter_category="T-Shirts"
):
    fields = list(query_fields)
    body = {
        "query": {
            "bool": {
                "must": {"multi_match": {"query": query, "fields": fields}},
                "filter": {"term": {"categories.keyword": filter_category}},
            }
        }
    }
    res = es.search(index="products", body=body)
    print("Got %d Hits:" % res["hits"]["total"]["value"])
    for hit in res["hits"]["hits"]:
        print("%(title)s: %(description)s" % hit["_source"])


get_results("red t-shirt")
