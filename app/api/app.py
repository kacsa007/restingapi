from flask import request, make_response

from app.api import api

from app.services.data_process_service import DataProcessService


@api.route('/reports/<int:report_id>', methods=['GET'])
def report_generation(report_id):

    doctype = request.args.get('format', '')
    response_doc = DataProcessService().report_generation(report_id, doctype)

    if doctype == 'pdf':

        get_response = make_response(response_doc)
        get_response.headers['Content-Type'] = 'application/pdf'
        get_response.headers['Content-Disposition'] = 'inline'

        return get_response

    elif doctype == 'xml':

        get_response = make_response(response_doc)
        get_response.headers['Content-Type'] = 'application/xml'

        return get_response

    else:

        return response_doc
        




