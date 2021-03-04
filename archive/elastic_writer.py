from elastic_connector import get_connection_from_env
es = get_connection_from_env()
from elasticsearch.helpers import bulk
print(es)

keys = set()
with open("../meta_Clothing_Shoes_and_Jewelry.json") as myfile:
    while next(myfile):
        head = [eval(next(myfile)) for x in range(50000)]
        parsed = [dict(pr, **{"_index": "products"}) for pr in head if pr.get("description")]
        print(bulk(es, parsed))