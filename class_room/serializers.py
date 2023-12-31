from rest_framework import serializers
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
    
class ClassRoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClassRoom
        fields = ['id', 'host', 'name', 'participants']
        