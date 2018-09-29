from django.shortcuts import render, get_object_or_404
from django.views.generic import View

from blog_app.models import Blog, UserProfile


# from blog_app.forms import MDEditorForm


class BlogListView(View):
    def get(self, request):
        blog_obj = Blog.objects.all()
        return render(self.request, 'index.html', {'all_blog': blog_obj.order_by('-created_time')})


class BlogDetailView(View):
    def get(self, request, pk):
        context = get_object_or_404(Blog, pk=pk)
        # form = MDEditorForm(context)
        return render(self.request, 'detail.html', {'detail': context,
                                                    'content': context.content})

    # markdown.markdown(context.content,
    #                   extensions=[
    #                       'markdown.extensions.extra',
    #                       'markdown.extensions.codehilite',
    #                       'markdown.extensions.toc',
    #                   ])


def base_context(request):
    return {"base_user": UserProfile.objects.first()}
