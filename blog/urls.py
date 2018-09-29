"""blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Import the include() function: from django.conf.urls import url, include
    3. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf import settings
from django.conf.urls import url, include
from django.conf.urls.static import static
from django.contrib import admin
from blog_app.catch_request_error import handler404, handler500
from blog_app.views import BlogListView

urlpatterns = [
                  url(r'^admin/', admin.site.urls),
                  url(r'^blog/', include('blog_app.urls')),
                  url(r'^$', BlogListView.as_view()),
                  url(r'mdeditor/', include('mdeditor.urls'))

              ] + static(settings.MEDIA_URL,
                         document_root=settings.MEDIA_ROOT) + static(settings.STATIC_URL,
                                                                     document_root=settings.STATIC_ROOT)
handler404 = handler404
handler500 = handler500
