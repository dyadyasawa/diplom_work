
from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView, UpdateAPIView, DestroyAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from knowledge_test.models import CourseTest, Question, Answer

from knowledge_test.serializers import CourseTestSerializer, QuestionSerializer, AnswerSerializer
from rest_framework.permissions import IsAdminUser


class CourseTestListApiView(ListAPIView):
    serializer_class = CourseTestSerializer
    queryset = CourseTest.objects.all()
    permission_classes = (IsAdminUser,)


class CourseTestDetailApiView(RetrieveAPIView):
    serializer_class = CourseTestSerializer
    queryset = CourseTest.objects.all()
    permission_classes = (IsAdminUser,)


class CourseTestCreateApiView(CreateAPIView):
    serializer_class = CourseTestSerializer
    queryset = CourseTest.objects.all()
    permission_classes = (IsAdminUser,)


class CourseTestUpdateApiView(UpdateAPIView):
    serializer_class = CourseTestSerializer
    queryset = CourseTest.objects.all()
    permission_classes = (IsAdminUser,)


class CourseTestDeleteApiView(DestroyAPIView):
    serializer_class = CourseTestSerializer
    queryset = CourseTest.objects.all()
    permission_classes = (IsAdminUser,)


class QuestionListApiView(ListAPIView):
    serializer_class = QuestionSerializer
    queryset = Question.objects.all()
    permission_classes = (IsAdminUser,)


class QuestionDetailApiView(RetrieveAPIView):
    serializer_class = QuestionSerializer
    queryset = Question.objects.all()
    permission_classes = (IsAdminUser,)


class QuestionCreateApiView(CreateAPIView):
    serializer_class = QuestionSerializer
    queryset = Question.objects.all()
    permission_classes = (IsAdminUser,)


class QuestionUpdateApiView(UpdateAPIView):
    serializer_class = QuestionSerializer
    queryset = CourseTest.objects.all()
    permission_classes = (IsAdminUser,)


class QuestionDeleteApiView(DestroyAPIView):
    serializer_class = QuestionSerializer
    queryset = CourseTest.objects.all()
    permission_classes = (IsAdminUser,)


class AnswerListApiView(ListAPIView):
    serializer_class = AnswerSerializer
    queryset = Answer.objects.all()
    permission_classes = (IsAdminUser,)


class AnswerDetailApiView(RetrieveAPIView):
    serializer_class = AnswerSerializer
    queryset = Answer.objects.all()
    permission_classes = (IsAdminUser,)


class AnswerCreateApiView(CreateAPIView):
    serializer_class = AnswerSerializer
    queryset = Answer.objects.all()
    permission_classes = (IsAdminUser,)


class AnswerUpdateApiView(UpdateAPIView):
    serializer_class = AnswerSerializer
    queryset = Answer.objects.all()
    permission_classes = (IsAdminUser,)


class AnswerDeleteApiView(DestroyAPIView):
    serializer_class = AnswerSerializer
    queryset = Answer.objects.all()
    permission_classes = (IsAdminUser,)


class GetQuestions(APIView):
    def get(self, request, *args, **kwargs):
        """ Получение вопросов для теста по заданному курсу. """

        course_test = CourseTest.objects.get(pk=kwargs["course_pk"])
        questions_lst = course_test.question_set.all().values()
        return Response({"Вопросы": list(questions_lst)})


class GetAnswers(APIView):
    """ Получение ответов для теста по заданному вопросу. """

    def get(self, request, *args, **kwargs):
        question = Question.objects.get(pk=kwargs["question_pk"])
        answers_lst = question.answer_set.all().values()
        return Response({"Варианты ответа": list(answers_lst)})


class AnswerVerification(APIView):
    """ Проверка правильности ответа. """

    def get(self, request, *args, **kwargs):
        question = Question.objects.get(pk=kwargs["question_pk"])
        answers_lst = question.answer_set.filter(is_correct=True).values()
        return Response({"Варианты ответа": list(answers_lst)})
