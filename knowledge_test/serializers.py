from rest_framework import serializers

from knowledge_test.models import Answer, CourseTest, Question


class CourseTestSerializer(serializers.ModelSerializer):
    class Meta:
        model = CourseTest
        fields = "__all__"


class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = "__all__"


class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = "__all__"
