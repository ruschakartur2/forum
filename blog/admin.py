from django.contrib import admin

# Register your models here.
from comments.models import Comment
from .models import Topic, Membership


class CommentLine(admin.TabularInline):
    model = Comment


class MembershipLine(admin.StackedInline):
    model = Membership


class TopicAdmin(admin.ModelAdmin):
    inlines = [
        CommentLine,
        MembershipLine
    ]


admin.site.register(Topic, TopicAdmin)
admin.site.register(Membership)
