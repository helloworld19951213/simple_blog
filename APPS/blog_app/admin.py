from django.contrib import admin
from mdeditor.widgets import MDEditorWidget
from django.db import models

from .models import BlogTag, Blog, UserProfile


# admin.site.unregister(User)


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.TextField: {'widget': MDEditorWidget}
    }
    list_display = [
        'title',
        # 'content',
        'short_content',
        'tag',
        'created_time',
        'modify_time',
        'is_show',
    ]
    readonly_fields = [
        'created_time',
        'modify_time',
        'is_show',
        'author',
    ]
    search_fields = [
        'title',
        'content',
        'tag',
    ]
    list_filter = [
        'tag',
    ]

    def save_model(self, request, obj, form, change):
        user = request.user
        obj.author = user
        obj.save()

    def has_delete_permission(self, request, obj=None):
        if obj is not None and obj.author == request.user:
            return True
        return False

    def short_content(self, obj):
        if obj.content.__len__() > 50:
            return obj.content[:50] + "......"
        return obj.content

    short_content.short_description = '正文内容'


@admin.register(BlogTag)
class BlogTagAdmin(admin.ModelAdmin):
    list_display = [
        'name',
    ]
    readonly_fields = [
        'created_time',
        'modify_time',
        'is_show',
    ]
    list_filter = [
        'name',
    ]
    search_fields = [
        'name',
    ]

    def has_delete_permission(self, request, obj=None):
        if obj is not None and obj.author == request.user:
            return True
        return False


@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = [
        'username',
        'gender',
        'nickname',
        'thumb_head_pic',
    ]
    readonly_fields = [

        'thumb_head_pic',
    ]

    def save_model(self, request, obj, form, change):
        obj.save()
        head_url = obj.thumb_head
        obj.save()
        print(head_url)
