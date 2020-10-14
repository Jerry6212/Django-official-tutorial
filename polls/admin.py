from django.contrib import admin

from .models import Question, Choice


# This changes around the order of fields on the admin page and allows admin to add question and multiple choices


class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3

# Aligns the choice text and makes the tabular
class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),

    ]
    # Adds fields showing publish dates, if published recently, a filter, and a search bar
    inlines = [ChoiceInline]
    list_display = ('question_text', 'pub_date', 'was_published_recently')
    list_filter = ['pub_date']
    search_fields = ['question_text']
admin.site.register(Question, QuestionAdmin)
