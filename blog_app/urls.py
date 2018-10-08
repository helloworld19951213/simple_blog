from django.conf.urls import url

from blog_app.views import BlogListView, BlogDetailView

urlpatterns = [
    url(r'^blog_list/$', BlogListView.as_view(), name='blog_list'),
    url(r'^blog/(?P<pk>.+)', BlogDetailView.as_view(), name='blog_detail')

]
