from django.contrib import admin
from polls.models import Choice, Question

# Register your models here.
# tells the admin that Question objects have an admin interface

class ChoiceInline(admin.TabularInline):
	model = Choice
	extra = 3


class QuestionAdmin(admin.ModelAdmin):
	fieldsets = [
		(None, 			{'fields':['question_text']}),
		('Date Information',	{'fields':['pub_date'], 'classes': ['collapse']}),
	]
	
	inlines = [ChoiceInline]

	list_display = ('question_text', 'pub_date', 'was_published_recently')
	list_filter = ['pub_date']

	search_fields = ['question_text']


admin.site.register(Question, QuestionAdmin)

