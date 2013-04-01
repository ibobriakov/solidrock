from django.views.generic import FormView
from forms import SearchForm


class SearchView(FormView):
    template_name = "search/search.html"
    form_class = SearchForm

    def form_valid(self, form):
        return self.render_to_response(self.get_context_data(form=form))
