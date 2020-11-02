from django.shortcuts import render
from django.views.generic.base import TemplateView

# Create your views here.
from django.views.generic.dates import YearArchiveView

from tej.models import Article#TemplateviewArticle#ArchiveArticledefaultemplate,TemplateviewArticledefaultemplate

class ArticleYearArchiveView(YearArchiveView):
    template_name='yeararchive.html'
    date_field = "pub_date"
    make_object_list = True
    allow_future = True
    queryset= Article.objects.all()

class templateView(TemplateView):

    template_name= 'templateview.html'


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['latest_articles'] =  Article.objects.all()[:5]
        return context


class homepageview(TemplateView):
    template_name="home.html"