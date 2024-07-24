from django.urls import path

from knowledge_test.apps import KnowledgeTestConfig
from knowledge_test.views import (
    AnswerCreateApiView,
    AnswerDeleteApiView,
    AnswerDetailApiView,
    AnswerListApiView,
    AnswerUpdateApiView,
    AnswerVerification,
    CourseTestCreateApiView,
    CourseTestDeleteApiView,
    CourseTestDetailApiView,
    CourseTestListApiView,
    CourseTestUpdateApiView,
    GetAnswers,
    GetAnswersCQ,
    GetIsCorrectAnswer,
    GetQuestions,
    QuestionCreateApiView,
    QuestionDeleteApiView,
    QuestionDetailApiView,
    QuestionListApiView,
    QuestionUpdateApiView,
)

app_name = KnowledgeTestConfig.name

urlpatterns = [
    path("course_test/list/", CourseTestListApiView.as_view(), name="course_test_list"),
    path(
        "course_test/detail/<int:pk>/",
        CourseTestDetailApiView.as_view(),
        name="course_test_detail",
    ),
    path(
        "course_test/create/",
        CourseTestCreateApiView.as_view(),
        name="course_test_create",
    ),
    path(
        "course_test/update/<int:pk>/",
        CourseTestUpdateApiView.as_view(),
        name="course_test_update",
    ),
    path(
        "course_test/delete/<int:pk>/",
        CourseTestDeleteApiView.as_view(),
        name="course_test_delete",
    ),
    path("question/list/", QuestionListApiView.as_view(), name="question_list"),
    path(
        "question/detail/<int:pk>/",
        QuestionDetailApiView.as_view(),
        name="question_detail",
    ),
    path("question/create/", QuestionCreateApiView.as_view(), name="question_create"),
    path(
        "question/update/<int:pk>/",
        QuestionUpdateApiView.as_view(),
        name="question_update",
    ),
    path(
        "question/delete/<int:pk>/",
        QuestionDeleteApiView.as_view(),
        name="question_delete",
    ),
    path("answer/list/", AnswerListApiView.as_view(), name="answer_list"),
    path(
        "answer/detail/<int:pk>/", AnswerDetailApiView.as_view(), name="answer_detail"
    ),
    path("answer/create/", AnswerCreateApiView.as_view(), name="answer_create"),
    path(
        "answer/update/<int:pk>/", AnswerUpdateApiView.as_view(), name="answer_update"
    ),
    path(
        "answer/delete/<int:pk>/", AnswerDeleteApiView.as_view(), name="answer_delete"
    ),
    path(
        "get/questions/<int:course_pk>/", GetQuestions.as_view(), name="get_questions"
    ),
    path("get/answers/<int:question_pk>/", GetAnswers.as_view(), name="get_answers"),
    path(
        "get/answers_cq/<int:course_pk>/<int:question_pk>/",
        GetAnswersCQ.as_view(),
        name="get_answers_cq",
    ),
    path(
        "get/is_correct_answer/<int:question_pk>/",
        GetIsCorrectAnswer.as_view(),
        name="get_is_correct_answers",
    ),
    path(
        "answer/verification/<int:question_pk>/<int:answer_pk>/",
        AnswerVerification.as_view(),
        name="answer_verification",
    ),
]
