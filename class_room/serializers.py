from rest_framework import serializers
from rest_framework.response import Response
from django.utils.text import slugify
from core.serializers import UserCreateSerializer, UserSerializer
from django.contrib.auth import get_user_model
from .models import *

class ExamSerializer(serializers.ModelSerializer):
    slug = serializers.SlugField(read_only=True)
    class Meta:
        model = Exam
        fields = ['id','title','slug', 'author', 'total_mark', 'time_allowed', 'starting_time']
        lookup_field = 'slug'
        extra_kwargs = {
            'url': {'lookup_field': 'slug'}
        }

class SimpleExamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Exam
        fields = ['title']

class SectionSerializer(serializers.ModelSerializer):
    lookup_field = 'type'
    extra_kwargs = {
            'url': {'lookup_field': 'type'}
        }
    exam = SimpleExamSerializer()
    class Meta:
        model = Section
        fields = ['id', 'type', 'instruction', 'exam']
    
class AddSectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Section
        fields = ['id', 'type', 'instruction']
    def create(self, validated_data):
        type = validated_data['type']
        exam_id = self.context['exam_id']
        if Section.objects.filter(type=type).exists():
            raise serializers.ValidationError('There is already that type of section')
        return Section.objects.create(exam_id = exam_id, **validated_data)

class TrueFalseQuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = TrueFalseQuestion
        fields = ['id', 'number', 'content','correct_answer' ,'answer']

class FillInQuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = FillInQuestion
        fields = ['id', 'number', 'content','correct_answer' ,'answer']

class ChoiceQuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChoiceQuestion
        fields = ['id', 'number', 'content']

class ChoiceSerializer(serializers.ModelSerializer):
    question = ChoiceQuestionSerializer(read_only=True)
    class Meta:
        model = Choice
        fields = ['id', 'choice_name', 'content', 'is_correct', 'question']

    def create(self, validated_data):
        question_id = self.context['question_id']
        question = ChoiceQuestion.objects.get(id = question_id)
        return Choice.objects.create(question=question, **validated_data)

class StudentSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    class Meta:
        model = Student
        fields = ['id','user', 'school_id', 'image']

class AddStudentSerializer(serializers.ModelSerializer):
    user = UserCreateSerializer()
    class Meta:
        model = Student
        fields = ['id','user', 'school_id', 'image']
    
    def create(self, validated_data):
        user = dict(validated_data.pop('user'))
        instance = get_user_model().objects.create(**user, user_type='S')      
        return Student.objects.create(user=instance, **validated_data)
    

class TeacherSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    class Meta:
        model = Teacher
        fields = ['id','user', 'school_id','image']

class AddTeacherSerializer(serializers.ModelSerializer):
    user = UserCreateSerializer()
    class Meta:
        model = Teacher
        fields = ['id','user', 'school_id', 'image']
    
    def create(self, validated_data):
        user = dict(validated_data.pop('user'))
        instance = get_user_model().objects.create(**user, user_type='T')      
        return Teacher.objects.create(user=instance, **validated_data)

class ClassRoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClassRoom
        fields = ['id', 'host', 'name', 'participants']
        