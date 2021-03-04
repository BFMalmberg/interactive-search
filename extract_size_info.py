from elastic_connector import execute_query, get_connection_from_env

INDEX = "products"



query = {
    "query": {
        "exists": {
            "field": "title"
        }
    }
}


size_mapping = {
    "XXXS": {"XXXS", "3X-small"},
    "XXS": {"XXS", "2X-small"},
    "XS": {"XS", "extra small", "X-small"},
    "S": {"S", "small"},
    "M": {"M", "medium"},
    "L": {"L", "large"},
    "XL": {"XL", "extra large", "X-large"},
    "XXL": {"XXL", "2X-large"},
    "XXXL": {"XXXL", "3x-large"}
}


es = get_connection_from_env()

for i in range(5):
    print("---------")
    results = execute_query(es_connection=es,
                            query=query,
                            index=INDEX)

    print(len(results))
    for result in results["hits"]["hits"]:
        print(result["_source"]["title"])
