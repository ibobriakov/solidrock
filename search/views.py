from django.db.models import Q
from django.views.generic import FormView
from django.views.generic.list import MultipleObjectMixin
from haystack.query import SearchQuerySet
from employer.models import Job
from forms import SearchForm


def get_search_by_keywords(keywords):
    pk_list = list()
    for keyword in keywords.split(","):
        for search_field in ('name', 'title', 'description', 'essential', 'desireable',):
            pk_list.extend(map(lambda sr: sr.pk, SearchQuerySet().filter(**{search_field: keyword})))
    return Q(pk__in=pk_list)


class SearchView(FormView, MultipleObjectMixin):
    template_name = "search/search.html"
    form_class = SearchForm
    context_object_name = 'jobs'
    paginate_by = 3

    def get_context_data(self, **kwargs):
        if 'object_list' not in kwargs:
            kwargs['object_list'] = Job.objects.none()
        context = super(SearchView, self).get_context_data(**kwargs)
        context['full_search_form'] = True
        context['query_dict'] = self.request.GET.urlencode()
        return context

    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)

    def get_form_kwargs(self):
        """
        Returns the keyword arguments for instantiating the form.
        """
        kwargs = {'initial': self.get_initial()}
        if self.request.method in ('POST', 'PUT'):
            kwargs.update({
                'data': self.request.POST,
                'files': self.request.FILES,
            })
        if self.request.method == 'GET':
            kwargs['data'] = self.request.GET
        return kwargs

    def form_valid(self, form):
        form_data = form.data
        query = Q()
        if 'keywords' in form_data and form_data['keywords']:
            query = get_search_by_keywords(form_data['keywords'])
        for field in ('location', 'categories', 'sub_categories', 'hours', 'employment_type'):
            if field in form_data and form_data[field]:
                query &= Q(**{field: form_data[field]})
        if 'featured' in form_data:
            query &= Q(featured_job=True)
        if 'salary_min' in form_data and form_data['salary_min'] != '':
            query &= Q(salary_range_min__gte=form_data['salary_min'])
        if 'salary_max' in form_data and form_data['salary_max'] != '':
            query &= Q(salary_range_max__lte=form_data['salary_max'])
        jobs = Job.objects.filter(query).exclude(name=None)
        if 'executive_positions' in form_data:
            jobs = jobs.exclude(executive_positions=None)
        jobs = jobs.exclude(approved=False)
        context = self.get_context_data(form=form, object_list=jobs)
        return  self.render_to_response(context)