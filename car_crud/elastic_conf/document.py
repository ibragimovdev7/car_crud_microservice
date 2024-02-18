from elasticsearch import Elasticsearch

ELASTIC_PASSWORD = 'RfstmxP69qIfMVm0VSjI'
ELASTIC_USER = 'elastic'
ELASTIC_PATH = 'http://localhost:9200'
INDEX_NAME = 'cars_list'


def connect_to_elastic() -> Elasticsearch:
    client = Elasticsearch(
        ELASTIC_PATH,
        verify_certs=False,
        basic_auth=(ELASTIC_USER, ELASTIC_PASSWORD)
    )

    return client


mapping = {
    'model': {
        'type': 'text'
    },
    'price': {
        'type': 'float'
    },
    'year': {
        'type': 'date'
    },
    'milage': {
        'type': 'integer'
    }
}


def indexing():
    client = connect_to_elastic()

    client.indices.create(
        index=INDEX_NAME,
        body={
            'mappings': {
                'properties': mapping
            }
        }
    )
