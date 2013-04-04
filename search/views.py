from django.db.models import Q
from django.views.generic import FormView
from haystack.query import SearchQuerySet
from employer.models import Job
from forms import SearchForm


def get_search_by_keywords(keywords):
    pk_list = list()
    for keyword in keywords.split(","):
        for search_field in ('name', 'title', 'description', 'essential', 'desireable',):
            pk_list.extend(map(lambda sr: sr.pk, SearchQuerySet().filter(**{search_field: keyword})))
    return Q(pk__in=pk_list)


class SearchView(FormView):
    template_name = "search/search.html"
    form_class = SearchForm

    def form_valid(self, form):
        form_data = form.data
        context = self.get_context_data(form=form)
        query = Q()
        if 'keywords' in form_data and form_data['keywords']:
            query = get_search_by_keywords(form_data['keywords'])
        for field in ('location', 'categories', 'sub_categories',):
            if field in form_data and form_data[field]:
                query &= Q(**{field: form_data[field]})
        context['jobs'] = Job.objects.filter(query).exclude(name=None)
        return  self.render_to_response(context)