from elastic_connector import get_connection_from_env
from prices import get_price_info

es = get_connection_from_env()


def get_results(
    query,
    query_fields=("description", "title"),
    filter_category="T-Shirts",
    min_price=0,
    max_price=500,
):
    fields = list(query_fields)
    body = {
        "query": {
            "bool": {
                "must": [
                    {"multi_match": {"query": query, "fields": fields}},
                    {"range": {"price": {"gte": min_price, "lt": max_price}}},
                    {"exists": {"field": "brand"}},
                ],
                "filter": {"term": {"categories.keyword": filter_category}},
            }
        }
    }
    res = es.search(index="products", body=body, size=100)
    print("Got %d Hits:" % res["hits"]["total"]["value"])
    for hit in res["hits"]["hits"]:
        print("%(title)s, %(price)s, %(brand)s: %(description)s" % hit["_source"])
    return res


res = get_results("red t-shirt")
pr = get_price_info(res)