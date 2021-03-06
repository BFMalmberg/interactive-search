from flask import Flask, jsonify, request
from flask_cors import CORS
from prices import get_price_info
from elastic_connector import get_connection_from_env
from utils import get_results
from brands import get_top_k_brands
from weather_api import get_weather_for_latlon

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})
es_connection = get_connection_from_env()


@app.route('/initial_query_results', methods=['POST'])
def get_initial_query_results():
    user_query = request.form.get('user_query')
    results = get_results(es_connection, user_query)
    median_price = get_price_info(results)
    if results:
        return jsonify(status="OK", products=results, median_price=median_price)
    else:
        return jsonify(status="FAILED",
                       error=404,
                       message="No results found.")


@app.route('/price_filtered_results', methods=['POST'])
def get_chosen_price_results():
    user_query = request.form.get('user_query')
    price = request.form.get('median_price')
    higher_lower = request.form.get('price_choice')
    if higher_lower == 'higher':
        results = get_results(es_connection, user_query, min_price=price)
    else:
        results = get_results(es_connection, user_query, max_price=price)

    brand_results = get_top_k_brands(results, top_k=5)
    if results:
        return jsonify(status="OK", products=results, brands=brand_results)
    else:
        return jsonify(status="FAILED",
                       error=404,
                       message="No results found.")


@app.route('/brand_filtered_results', methods=["POST"])
def get_query_results_for_brand():
    """
    :return: new results based on query with user_query and brand_name filter
    as well as price choice from previous prompt.
    """
    user_query = request.form.get('user_query')
    brand = request.form.get('brand_choice')
    price = request.form.get('median_price')
    higher_lower = request.form.get('price_choice')
    if higher_lower == 'higher':
        results = get_results(es_connection, user_query, min_price=price, filter_brand=brand)
    else:
        results = get_results(es_connection, user_query, max_price=price, filter_brand=brand)

    lat = request.form.get('latitude')
    lon = request.form.get('longitude')

    temperature = get_weather_for_latlon(lat, lon)

    if results:
        return jsonify(status="OK", products=results, temperature=temperature)
    else:
        return jsonify(status="FAILED",
                       error=404,
                       message="No results found.")


@app.route('/query_sweater', methods=["POST"])
def get_query_results_for_sweater():
    # TODO: fill in - Siem.
    # If user indeed wants to search for sweaters, give sweater results.

    results = get_results(es_connection, query="jacket", filter_category="Jackets & Coats")

    if results:
        return jsonify(status="OK", products=results)
    else:
        return jsonify(status="FAILED",
                       error=404,
                       message="No results found.")


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5050)
