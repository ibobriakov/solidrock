from django.db.models import Q
from django.views.generic import FormView
from employer.models import Job
from forms import SearchForm


class SearchView(FormView):
    template_name = "search/search.html"
    form_class = SearchForm

    def form_valid(self, form):
        form_data = form.data
        context = self.get_context_data(form=form)
        query = Q()
        for field in ('location', 'categories', 'sub_categories',):
            if field in form_data and form_data[field]:
                query &= Q(**{field: form_data[field]})
        context['jobs'] = Job.objects.filter(query)
        return  self.render_to_response(context)