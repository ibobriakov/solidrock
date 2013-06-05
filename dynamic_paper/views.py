import StringIO
from django.http import HttpResponse
from django.template import RequestContext
from django.template.loader import get_template
from django.utils.html import escape
import xhtml2pdf.pisa as pisa


class PdfRenderMixin(object):
    def render_to_response(self, context, **response_kwargs):
        template = get_template(self.template_name)
        html = template.render(RequestContext(self.request, context))
        result = StringIO.StringIO()

        pdf = pisa.pisaDocument(StringIO.StringIO(html.encode("ISO-8859-1")), result)
        if not pdf.err:
            return HttpResponse(result.getvalue(), mimetype='application/pdf')
        return HttpResponse('We had some errors<pre>%s</pre>' % escape(html))