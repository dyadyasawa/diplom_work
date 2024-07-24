from django.contrib import admin

from knowledge_test.models import Answer, CourseTest, Question


@admin.register(CourseTest)
class CourseTestAdmin(admin.ModelAdmin):
    list_display = ("name",)
    list_filter = ("name",)
    search_fields = ("name",)


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ("question_text",)
    list_filter = ("question_text",)
    search_fields = ("question_text",)


@admin.register(Answer)
class AnswerAdmin(admin.ModelAdmin):
    list_display = ("answer_text",)
    list_filter = ("answer_text",)
    search_fields = ("answer_text",)
