import os
import elasticsearch as es
import logging
import certifi
from dotenv import load_dotenv
load_dotenv()

'''
This file contains a set of helper functions to interact with elasticsearch
'''

_elastic_protocol = os.getenv("ELASTIC_PROTOCOL", "https")
_elastic_host = os.getenv("ELASTIC_HOST", "localhost")
_elastic_port = os.getenv("ELASTIC_PORT", 9200)
_elastic_password = os.getenv("ELASTIC_PASSWORD")


def get_connection(connection_str, use_ssl=False):
    logging.debug(">>>>")
    es_connection = None
    if use_ssl:
        es_connection = es.Elasticsearch(
            connection_str, use_ssl=True, ca_certs=certifi.where()
        )
    else:
        es_connection = es.Elasticsearch(connection_str, use_ssl=False)

    return es_connection


def get_custom_connection(protocol="http", host="elasticsearch", port=9200, password=None):

    connection_str = ""
    if not protocol:
        connection_str = "http://"
    else:
        connection_str = "{}://".format(protocol)

    if password:
        connection_str = "{}elastic:{}@{}:{}".format(connection_str, password, host, port)
    else:
        connection_str = "{}{}:{}".format(connection_str, host, port)

    logging.warning({"connection_str": connection_str})

    use_ssl = False
    if protocol == "https":
        use_ssl = True
    es_connection = get_connection(connection_str=connection_str, use_ssl=use_ssl)

    return es_connection


def get_connection_from_env():
    logging.debug(">>>>")
    logging.info(
        {"protocol": _elastic_protocol, "host": _elastic_host, "port": _elastic_port}
    )
    # Elastic host and port are required
    if not _elastic_host or not _elastic_port:
        logging.info({"status": "failed", "message": "Missing connection data"})
        return None

    return get_custom_connection(
        protocol=_elastic_protocol,
        host=_elastic_host,
        port=_elastic_port,
        password=_elastic_password,
    )


def execute_query(es_connection, query, index, scroll="2s"):
    results = es_connection.search(index=index, scroll=scroll, body=query)

    return results


def create_document(
    es_connection, document_data, index, document_id=None, refresh="wait_for"
):
    logging.debug(">>>>")
    try:
        if document_id:
            logging.debug("document_id specified ")
            result = es_connection.create(
                index=index, id=document_id, body=document_data, refresh=refresh
            )
        else:
            logging.debug("document_id unspecified ")
            result = es_connection.index(index=index, body=document_data, refresh=refresh)

        return result
    except Exception as e:
        logging.exception(e)
        return False


def update_document(
    es_connection, document_data, index, document_id=None, refresh="wait_for"
):
    """
    Note that document_data should have the following format:
    {"doc":{"field": "value"}}
    """
    try:

        result = es_connection.update(
            index=index, id=document_id, body=document_data, refresh=refresh
        )

        return result

    except Exception as e:
        logging.exception(e)
        return False


def delete_document_by_id(es_connection, index, document_id, refresh="wait_for"):
    try:
        return es_connection.delete(index=index, id=document_id, refresh=refresh)
    except Exception as e:
        logging.exception(e)
        return False


def create_index_by_name(es_connection, index):
    try:
        return es_connection.indices.create(index=index)
    except Exception as e:
        logging.exception(e)
        return False


def delete_index_by_name(es_connection, index):
    try:
        return es_connection.indices.delete(index=index, allow_no_indices=True)
    except Exception as e:
        logging.exception(e)
        return False
