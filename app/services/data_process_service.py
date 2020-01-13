from flask import jsonify, render_template
from dicttoxml import dicttoxml
from weasyprint import HTML

import json


from app.model_auth.model import db, ReportModel


class DataProcessService(object):

    @staticmethod
    def report_generation(report_id,doctype):

        get_report = db.session.query(ReportModel).get_or_404(report_id)
        data = json.loads(get_report.data)

        if doctype == 'pdf':

            template_rendered = render_template('reporting_template.html', **data)
            pdf_document = HTML(string=template_rendered).write_pdf()

            return pdf_document

        elif doctype == 'xml':

            xml_document = dicttoxml(data, custom_root='report', attr_type=False)

            return xml_document

        else:

            return jsonify(data)







