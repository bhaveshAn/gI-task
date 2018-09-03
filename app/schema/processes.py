from marshmallow_jsonapi import fields
from marshmallow_jsonapi.flask import Relationship, Schema

from app.api.helpers.utils import dasherize


class ProcessSchema(Schema):

    class Meta:
        """
        Meta class for Process Api Schema
        """
        type_ = 'process'
        self_view = 'v1.process_detail'
        self_view_kwargs = {'id': '<id>'}
        inflect = dasherize

    id = fields.Str(dump_only=True)
    time = fields.DateTime(dump_only=True)
    method = fields.Str(dump_only=True)
    path = fields.Str(allow_none=True)
    body = fields.Str(allow_none=True)
    query = fields.Str(allow_none=True)
    headers = Relationship(
        attribute='headers',
        self_view='v1.process_headers',
        self_view_kwargs={'id': '<id>'},
        related_view='v1.header_list',
        related_view_kwargs={'process_id': '<id>'},
        schema='HeaderSchema',
        many=True,
        type_='header')
    duration = fields.Str(allow_none=True)
