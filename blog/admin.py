from django.contrib import admin

# Register your models here.
from comments.models import Comment
from .models import Topic


class CommentLine(admin.TabularInline):
    model = Comment


class TopicAdmin(admin.ModelAdmin):
    inlines = [
        CommentLine,
    ]


admin.site.register(Topic, TopicAdmin)
