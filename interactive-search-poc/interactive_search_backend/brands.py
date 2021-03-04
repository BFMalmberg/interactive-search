"""
Code relevant for the "brands" prompt.
Input: N products from a previous query.
Output: top k brands in these products.

TODO's:
* make sure more articles have "brand" field by extracting from title and/or description
* combine different descriptions of the same brand into a single representation
"""
from typing import List
import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
handler = logging.StreamHandler()
logger.addHandler(handler)


def get_top_k_brands(articles: List[dict], top_k: int = 3):
    """
    Based on list of articles, returns top k brands occurring in articles.
    """
    logger.info(f"Deciding top {top_k} brands for {len(articles)} articles.")
    brand_counts = _count_all_brands(articles)
    sorted_brands = [(k, v) for k, v in sorted(brand_counts.items(), key=lambda x: x[1])]
    return [k for (k, v) in sorted_brands[:top_k] if k != "None"]


def _count_all_brands(articles):
    """
    Based on list of articles, count how often each brand occurs.
    """
    logger.info("Starting counting brands...")
    counts = dict()
    counts["None"] = 0  # Field for counting missing brand-fields.

    for article in articles:
        brand_field_exists = "brand" in article["_source"]
        if not brand_field_exists:
            counts["None"] += 1
        else:
            brand = article["_source"]["brand"]
            if brand not in counts:
                counts[brand] = 0

            counts[brand] += 1
    logger.info(f"Counted {len(counts.keys()) - 1} brands.")
    logger.info(f"{counts['None']} articles did not have a brand.")

    return counts


if __name__ == '__main__':
    test_articles = [
        {'_id': 'FEG8-HcBBjLLZtxn9Uxy',
         '_index': 'products',
         '_score': 1.0,
         '_source': {'asin': 'B000GDAOUC',
                     'brand': 'Sara Lee',
                     'categories': [['Clothing, Shoes & Jewelry',
                                     'Novelty, Costumes & More',
                                     'Shoe Care & Accessories',
                                     'Shoelaces']],
                     'description': 'Kiwi, Pack of 6 pairs, 45", White Athletic Lace, '
                                    'Blister Pack.',
                     'imUrl': 'http://ecx.images-amazon.com/images/I/41ZhKBIsHnL._SY300_.jpg',
                     'price': 5.35,
                     'related': {'also_viewed': ['B003LY5T9O']},
                     'salesRank': {'Home &amp; Kitchen': 865765},
                     'title': 'Pr45&quot; Wht Athletic Lace (pack Of 6 Pairs)'},
         '_type': '_doc'},
        {'_id': 'FkG8-HcBBjLLZtxn9Uxy',
         '_index': 'products',
         '_score': 1.0,
         '_source': {'asin': 'B000GDYK8Y',
                     'categories': [['Clothing, Shoes & Jewelry',
                                     'Women',
                                     'Petite',
                                     'Outerwear & Coats',
                                     'Down & Parkas']],
                     'description': 'Lots of puffy warmth and a waterproof and '
                                    'breathable barrier make the Sub Zero SL Hooded '
                                    'Jacket from Mountain Hardwear just right for '
                                    'frigid, midwinter mountain temps and outdoor '
                                    'activities. Head out onto the mountain on even '
                                    'the coldest days in your own wearable sleeping '
                                    'bag consisting of 650-fill goose down encased '
                                    'within a Conduit SL laminate shell.',
                     'imUrl': 'http://ecx.images-amazon.com/images/I/417RRWimUUL._SY300_.jpg',
                     'salesRank': {'Sports &amp; Outdoors': 685531},
                     'title': "Mountain Hardwear Women's Sub Zero SL Hooded Jacket "
                              'Black X-Small'},
         '_type': '_doc'},
        {'_id': 'EkG8-HcBBjLLZtxn9Uxy',
         '_index': 'products',
         '_score': 1.0,
         '_source': {'asin': 'B000GCQ02O',
                     'brand': 'Chaby',
                     'categories': [['Clothing, Shoes & Jewelry',
                                     'Luggage & Travel Gear',
                                     'Umbrellas']],
                     'description': 'The Deluxe Super Mini Black Umbrella really is '
                                    'deluxe and mini at the same time! It opens to 42 '
                                    'inches and closes small enough to easily fits in '
                                    "purse, briefcase or backpack.It's great for "
                                    'travel anywhere.',
                     'imUrl': 'http://ecx.images-amazon.com/images/I/41H6XPMEysL._SY300_.jpg',
                     'price': 7.61,
                     'related': {'also_viewed': ['B00024QZX0',
                                                 'B00DR67MI2'],
                                 'bought_together': ['B000GCPZKC']},
                     'salesRank': {'Health & Personal Care': 166305},
                     'title': 'Mini Umbrella'},
         '_type': '_doc'}
    ]
    brands = get_top_k_brands(test_articles, top_k=3)
    print("Found brands:")
    print(brands)
