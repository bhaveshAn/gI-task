from marshmallow_jsonapi import fields
from marshmallow_jsonapi.flask import Relationship, Schema

from app.api.helpers.utils import dasherize


class HeaderSchema(Schema):

    class Meta:
        """
        Meta class for Process Api Schema
        """
        type_ = 'header'
        self_view = 'v1.header_detail'
        self_view_kwargs = {'id': '<id>'}
        inflect = dasherize

    id = fields.Str(dump_only=True)
    name = fields.Str(allow_none=False, required=True)
    processes = Relationship(
        attribute='processes',
        self_view='v1.header_processes',
        self_view_kwargs={'id': '<id>'},
        related_view='v1.process_list',
        related_view_kwargs={'header_id': '<id>'},
        schema='ProcessSchema',
        many=True,
        type_='process')
