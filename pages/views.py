from django.views.generic import TemplateView   # Template view has alot going on.


class HomePageView(TemplateView):               # inherating template view.
    template_name = "pages/home.html"           # overriding the template name.

class AboutPageView(TemplateView):               # inherating template view.
    template_name = "pages/about.html"           # overriding the template name.