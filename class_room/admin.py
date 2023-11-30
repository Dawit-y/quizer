from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(ChoiceQuestion)
admin.site.register(Choice)

admin.site.register(Section)
admin.site.register(TrueFalseQuestion)
admin.site.register(FillInQuestion)
admin.site.register(ClassRoom)

@admin.register(Exam)
class ExamAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'starting_time']
    prepopulated_fields = {'slug' : ('title',)}
