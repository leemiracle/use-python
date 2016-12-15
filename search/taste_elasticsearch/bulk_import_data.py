import time

import sys
from sqlalchemy.testing import db

from elasticsearch_dsl.connections import connections
from elasticsearch_dsl.document import DOC_META_FIELDS
from elasticsearch import helpers


def bulk_update_elastic_search(actions, cls):
    es = connections.get_connection()
    obj = cls()
    # log.info(str(body))
    helpers.bulk(es, actions, index=obj._get_index(None), doc_type=obj._doc_type.name)


def convert_obj_to_dict(obj, cls):

    message_doc = cls(meta={"id": str(obj.id)})
    message_doc.create_time = obj.create_time
    message_doc.write_time = obj.write_time
    for index_key, sql_key in cls.FIELD_MAP.items():
        value = get_value(obj, sql_key.split('.'))
        if value is not None:
            setattr(message_doc, index_key, value)
    cls._set_values(message_doc, obj)

    # 更新meta字段
    doc_meta = dict(
        ("_"+k, message_doc.meta[k])
        for k in DOC_META_FIELDS
        if k in message_doc.meta
    )
    # log.info(str(message_doc.to_dict()))
    # log.info(str(doc_meta))
    result = message_doc.to_dict()
    result.update(doc_meta)
    return result


def get_value(obj, key_list):
    if len(key_list) == 1:
        return getattr(obj, key_list[0])
    else:
        if getattr(obj, key_list[0]):
            return get_value(getattr(obj, key_list[0]), key_list[1:])
        else:
            return None


def elastic_refresh():
    start_time = time.time()
    if index.exists():
        index.delete()
    index.create()
    # Modle为数据库的类
    query = db.session.query(Modle).filter(Modle.state in ['1','2'])
    length = query.count()
    actions = []
    for i, message in enumerate(query.yield_per(100).enable_eagerloads(False)):
        sys.stdout.write('\b' * 100)
        sys.stdout.write('{}/{}'.format(i, length))
        sys.stdout.flush()
        # ModleDoc为elastic_search的DocType类
        actions.append(convert_obj_to_dict(message, ModleDoc))
        if i and i % 1000 == 0:
            bulk_update_elastic_search(actions, ModleDoc)
            actions = []
    else:
        if actions:
            bulk_update_elastic_search(actions, ModleDoc)
    sys.stdout.write('\n')
    print("--- %s seconds ---" % (time.time() - start_time))






