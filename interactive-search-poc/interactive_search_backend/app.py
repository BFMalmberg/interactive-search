from flask import Flask, jsonify, request
from flask_cors import CORS

from elastic_connector import get_connection_from_env
from utils import get_results

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})
es_connection = get_connection_from_env()


@app.route('/query_results', methods=['POST'])
def get_initial_query_results():
    user_query = request.form.get('user_query')
    results = get_results(es_connection, user_query)

    if results:
        return jsonify(status="OK", products=results)
    else:
        return jsonify(status="FAILED",
                       error=404,
                       message="No results found.")


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5050)
