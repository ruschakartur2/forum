from django.contrib import admin

# Register your models here.
from .models import Topic, Comment


class CommentLine(admin.TabularInline):
    model = Comment


class TopicAdmin(admin.ModelAdmin):
    inlines = [
        CommentLine,
    ]


admin.site.register(Topic, TopicAdmin)
admin.site.register(Comment)
