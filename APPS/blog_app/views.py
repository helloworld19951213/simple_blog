from django.core.paginator import PageNotAnInteger
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.views.generic import View
from pure_pagination import Paginator

from blog_app.models import Blog, UserProfile


class BlogListView(View):
    def get(self, request):
        blog_obj = Blog.objects.all().order_by('-created_time')
        try:
            page = request.GET.get('page', 1)
        except PageNotAnInteger:
            page = 1
        p = Paginator(blog_obj, 4, request=request)
        if int(page) not in list(p.page_range):
            return HttpResponseRedirect('/')
        orgs = p.page(page)
        index = orgs.number - 1
        max_index = len(p.page_range)
        start_index = index - 3 if index >= 3 else 0
        end_index = index + 3 if index <= max_index - 3 else max_index
        page_range = list(p.page_range)[start_index:end_index]
        return render(self.request, 'index.html', {'all_blog': orgs,
                                                   'page_range': page_range,
                                                   'max_index': max_index,
                                                   })


class BlogDetailView(View):
    def get(self, request, pk):
        context = get_object_or_404(Blog, pk=pk)
        # form = MDEditorForm(context)
        return render(self.request, 'detail.html', {'detail': context,
                                                    'content': context.content})


def base_context(request):
    """
    全局字段
    :param request:
    :return:
    """
    return {"base_user": UserProfile.objects.first()}


