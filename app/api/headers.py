from flask_rest_jsonapi import ResourceDetail, ResourceList, \
    ResourceRelationship

from app.api.helpers.db import safe_query

from app.schema.headers import HeaderSchema
from app.models import db
from app.models.header import Header
from app.models.process import Process


class HeaderList(ResourceList):
    """
    List and create Processes
    """
    def query(self, view_kwargs):
        """
        query method for speakers list class
        :param view_kwargs:
        :return:
        """
        query_ = db.session.query(Header)

        if view_kwargs.get('process_id'):
            process = safe_query(self, Process, 'id',
                                 view_kwargs['process_id'], 'process_id')
            query_ = query_.join(Process).filter(Process.id == process.id)

    schema = HeaderSchema
    data_layer = {'session': db.session,
                  'model': Header}


class HeaderDetail(ResourceDetail):
    """
    Process detail by id
    """
    schema = HeaderSchema
    data_layer = {'session': db.session,
                  'model': Header}


class HeaderRelationship(ResourceRelationship):
    """
    User Relationship
    """
    schema = HeaderSchema
    data_layer = {'session': db.session,
                  'model': Header}
