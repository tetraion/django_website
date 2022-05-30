from django.views.generic import TemplateView

class IndexView(TemplateView):
    template_name = "index.html"

    def get_context_data(self):
        ctxt = super().get_context_data()
        ctxt["username"]="taichi"
        return ctxt

class AboutView(TemplateView):
    template_name = "about.html"

    def get_context_data(self):
        ctxt = super().get_context_data()
        ctxt["num_services"]=12345678
        ctxt["skills"]=[
            "python",
            "C++",
            "Javascript",
        ]
        ctxt["licenses"]=[
            "基本情報技術者",
            "Oracle Certified Java Programmer Gold SE 11",
        ]
        return ctxt



from django.views.generic.edit import FormView
from . import forms

class Index(FormView):
    form_class = forms.TextForm
    template_name = "index2.html"

    def form_valid(self, form):
        data = form.cleaned_data
        text = data["text"]
        search = data["search"]
        replace = data["replace"]

        new_text = text.replace(search, replace)

        ctxt = self.get_context_data(new_text=new_text, form=form)
        return self.render_to_response(ctxt)

    def get_url_success(self):

        return "/"