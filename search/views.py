from django.views.generic import FormView
from forms import SearchForm

def search_view(request):
    return
class SearchView(FormView):
    template_name = "search/search.html"
    form_class = SearchForm

    def form_valid(self, form):
        return self.form_invalid(form)