from flask_rest_jsonapi import ResourceDetail, ResourceList, \
    ResourceRelationship
from flask import request

from app.api.helpers.db import safe_query
from app.schema.processes import ProcessSchema
from app.models import db
from app.models.process import Process
from app.models.header import Header


class ProcessList(ResourceList):
    """
    List and create Processes
    """
    def before_post(self, args, kwargs, data):
        """
        before post method to check for required relationship and
        proper permission
        :param args:
        :param kwargs:
        :param data:
        :return:
        """

        data['method'] = request.method
        data['path'] = request.path
        data['query'] = request.args.get('query')
        data['body'] = request.data

    def query(self, view_kwargs):
        """
        query method for speakers list class
        :param view_kwargs:
        :return:
        """
        query_ = db.session.query(Process)

        if view_kwargs.get('header_id'):
            header = safe_query(self, Header, 'id',
                                view_kwargs['process_id'], 'process_id')
            query_ = query_.join(Header).filter(Header.id == header.id)

    view_kwargs = True
    schema = ProcessSchema
    data_layer = {'session': db.session,
                  'model': Process}


class ProcessDetail(ResourceDetail):
    """
    Process detail by id
    """
    schema = ProcessSchema
    data_layer = {'session': db.session,
                  'model': Process}


class ProcessRelationship(ResourceRelationship):
    """
    User Relationship
    """
    schema = ProcessSchema
    data_layer = {'session': db.session,
                  'model': Process}
