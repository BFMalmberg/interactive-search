def median(lst):
    sortedLst = sorted(lst)
    lstLen = len(lst)
    index = (lstLen - 1) // 2

    if lstLen % 2:
        return sortedLst[index]
    else:
        return (sortedLst[index] + sortedLst[index + 1]) / 2.0


def mean(lst):
    return sum(lst) / len(lst)


def get_price_info(results):
    prices = [hit["_source"]["price"] for hit in results["hits"]["hits"]]
    return median(prices)
