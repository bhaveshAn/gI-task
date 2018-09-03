from app.api.bootstrap import api
from app.api.processes import ProcessList, ProcessDetail, ProcessRelationship
from app.api.headers import HeaderList, HeaderDetail, HeaderRelationship
from app.api.statistics.process_stats import ProcessStatisticsDetail

# process
api.route(ProcessList, 'process_list', '/process/', '/header/<int:header_id>/processes')
api.route(ProcessDetail, 'process_detail', '/process/<int:id>/')
api.route(ProcessRelationship, 'process_headers', '/process/<int:id>/relationships/headers')

# header
api.route(HeaderList, 'header_list', '/headers/', '/process/<int:process_id>/headers')
api.route(HeaderDetail, 'header_detail', '/header/<int:id>/')
api.route(HeaderRelationship, 'header_processes', '/header/<int:id>/relationships/processes/')

# Process Statistics
api.route(ProcessStatisticsDetail, 'process_statistics_detail', '/stats')
