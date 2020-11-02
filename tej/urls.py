from django.urls import path

from tej.views import ArticleYearArchiveView, templateView,homepageview


urlpatterns = [ path('tempview/', templateView.as_view(), name='templateview'),
    path('<int:year>/',
         ArticleYearArchiveView.as_view(),
         name="yeararchive"),
    path('',homepageview.as_view(), name='home')
]