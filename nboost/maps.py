
# class => module
MODULE_MAP = {
    'QAModel': 'models.qa',
    'ShuffleModel': 'models.shuffle',
    'PtBertModel': 'models.pt_models.bert',
    'TfBertModel': 'models.tf_models.bert',
    'TfAlbertModel': 'models.tf_models.albert',
    'PtDistilBertQAModel': 'models.pt_models.distilbert_qa',
}

CLASS_MAP = {
    "tf-bert-base-uncased-msmarco": "TfBertModel",
    "tf-albert-tiny-uncased-msmarco": "TfAlbertModel",
    "tf-biobert-base-uncased-msmarco": "TfBertModel",
    "pt-tinybert-msmarco": "PtBertModel",
    "pt-bert-base-uncased-msmarco": "PtBertModel",
    "pt-tinybert-mrpc": "PtBertModel"
}

URL_MAP = {
    "tf-bert-base-uncased-msmarco": "https://storage.googleapis.com/koursaros/tf-bert-base-uncased-msmarco.tar.gz",
    "tf-albert-tiny-uncased-msmarco": "https://storage.googleapis.com/koursaros/albert-tiny-uncased-msmarco.tar.gz",
    "tf-biobert-base-uncased-msmarco": "https://storage.googleapis.com/koursaros/biobert-base-uncased-msmarco.tar.gz",
    "pt-tinybert-msmarco": "https://storage.googleapis.com/koursaros/pt-tinybert-msmarco.tar.gz",
    "pt-bert-base-uncased-msmarco":  "https://storage.googleapis.com/koursaros/pt-bert-base-uncased-msmarco.tar.gz",
    "pt-tinybert-mrpc" : "https://storage.googleapis.com/koursaros/pt-tinybert-mrpc.tar.gz",
}

# backwards compatibility (before we added tf/pt)
CLASS_MAP["bert-base-uncased-msmarco"] = CLASS_MAP["tf-bert-base-uncased-msmarco"]
CLASS_MAP["albert-tiny-uncased-msmarco"] = CLASS_MAP["tf-albert-tiny-uncased-msmarco"]
CLASS_MAP["biobert-base-uncased-msmarco"] = CLASS_MAP["tf-biobert-base-uncased-msmarco"]
URL_MAP["bert-base-uncased-msmarco"] = URL_MAP["tf-bert-base-uncased-msmarco"]
URL_MAP["albert-tiny-uncased-msmarco"] = URL_MAP["tf-albert-tiny-uncased-msmarco"]
URL_MAP["biobert-base-uncased-msmarco"] = URL_MAP["tf-biobert-base-uncased-msmarco"]

# image => directory
IMAGE_MAP = {
    'alpine': '../Dockerfiles/alpine',
    'tf': '../Dockerfiles/tf',
    'pt': '../Dockerfiles/pt'
}

CONFIG_MAP = {
    'elasticsearch': {
        'query_path': '(body.query.match) | (body.query.term.*) | (url.query.q)',
        'topk_path': '(body.size) | (url.query.size)',
        'choices_path': 'body.hits.hits',
        'cvalues_path': '_source.*',
        'cids_path': '_id',
        'search_path': '/.*/_search',
        'default_topk': 10
    }
}
