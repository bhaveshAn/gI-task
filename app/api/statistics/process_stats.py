from flask_rest_jsonapi import ResourceDetail
from marshmallow_jsonapi.flask import Schema
from marshmallow_jsonapi import fields
from datetime import datetime, timedelta
import pytz

from app.api.helpers.utils import dasherize
from app.models import db
from app.models.process import Process
from app.api.data_layers.NoModelLayer import NoModelLayer
from app.api.helpers.db import get_count


class ProcessStatisticsSchema(Schema):
    """
    Api schema
    """
    class Meta:
        """
        Meta class
        """
        type_ = 'process-statistics'
        self_view = 'v1.process_statistics_detail'
        inflect = dasherize

    id = fields.String()
    total_requests = fields.Method("total_requests")
    active_get_requests = fields.Method("active_get_requests")
    active_post_requests = fields.Method("active_post_requests")
    active_put_requests = fields.Method("active_put_requests")
    total_requests_past_hour = fields.Method("total_requests_past_hour")
    total_requests_past_minute = fields.Method("total_requests_past_minute")
    avg_response_time_past_minute = fields.Method(
        "avg_response_time_past_minute")
    avg_response_time_past_hour = fields.Method(
        "avg_response_time_past_hour")

    def total_requests(self, obj):
        return get_count(Process.query.all())

    def active_get_requests(self, obj):
        return get_count(Process.query.filter_by(method="GET"))

    def active_post_requests(self, obj):
        return get_count(Process.query.filter_by(method="POST"))

    def active_put_requests(self, obj):
        return get_count(Process.query.filter_by(method="PUT"))

    def total_requests_past_hour(self, obj):
        all_processes = get_count(Process.query.filter_by(
            time=datetime.now(pytz.utc)))
        processes_till_last_1_hour = get_count(Process.query.filter(
            Process.time <= datetime.now(pytz.utc) - timedelta(hours=1)))
        return all_processes - processes_till_last_1_hour

    def total_requests_past_minute(self, obj):
        all_processes = get_count(Process.query.filter_by(
            time=datetime.now(pytz.utc)))
        processes_till_last_1_min = get_count(Process.query.filter(
            Process.time <= datetime.now(pytz.utc) - timedelta(minutes=1)))
        return all_processes - processes_till_last_1_min

    def avg_response_time_past_minute(self, obj):
        requests = self.total_requests_past_minute()
        total_time = 0
        for process in Process.query.order_by(
                Process.id.desc()).limit(requests):
            total_time += process.duration
        return total_time // requests

    def avg_response_time_past_hour(self, obj):
        requests = self.total_requests_past_hour()
        total_time = 0
        for process in Process.query.order_by(
                Process.id.desc()).limit(requests):
            total_time += process.duration
        return total_time // requests


class ProcessStatisticsDetail(ResourceDetail):
    """
    Detail by id
    """
    methods = ['GET']
    schema = ProcessStatisticsSchema
    data_layer = {
        'class': NoModelLayer,
        'session': db.session
    }
