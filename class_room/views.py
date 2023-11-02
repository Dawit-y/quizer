from django.shortcuts import render
from django.db.models import Count
from rest_framework import status
from rest_framework.viewsets import ModelViewSet, GenericViewSet
from rest_framework.mixins import RetrieveModelMixin
from rest_framework.response import Response
from .models import *
from .serializers import *
# Create your views here.
class ExamViewSet(ModelViewSet):
    queryset = Exam.objects.prefetch_related('sections').all()
    serializer_class = ExamSerializer
    lookup_field = 'slug'

class SectionViewSet(ModelViewSet):
    lookup_field = 'type'
    def get_serializer_class(self):
        if self.request.method == 'POST':
            return AddSectionSerializer
        return SectionSerializer

    def get_queryset(self, **kwargs):
        return Section.objects.filter(exam__slug=self.kwargs['exam_slug'])
    
    def get_serializer_context(self):
        exam = Exam.objects.get(slug=self.kwargs['exam_slug'])
        id = exam.pk
        return {'exam_slug': self.kwargs['exam_slug'], 'exam_id': id}

class QuestionModelViewSet(ModelViewSet):
    def get_queryset(self):
        param = self.kwargs['section_type']
        if param == 'T':
            return TrueFalseQuestion.objects.all()
        elif param == 'C':
            return ChoiceQuestion.objects.all()
        elif param == 'F':
            return FillInQuestion.objects.all()
        else: 
            raise serializers.ValidationError('Something went wrong')
    def get_serializer_class(self):
        param = self.kwargs['section_type']
        if param == 'T':
            return TrueFalseQuestionSerializer
        elif param == 'C':
            return ChoiceQuestionSerializer
        elif param == 'F':
            return FillInQuestionSerializer
        else: 
            raise serializers.ValidationError('Something went wrong')

class ChoiceViewSet(ModelViewSet):
    def get_queryset(self):
        if self.kwargs['section_type'] == 'F':
            return Response({'error': 'The question does not have choices'}, status=status.HTTP_400_BAD_REQUEST)
        question = ChoiceQuestion.objects.get(id=self.kwargs['question_pk'])
        return question.answers.all()       
        
    serializer_class = ChoiceSerializer

    def get_serializer_context(self):
        question_id = self.kwargs['question_pk']
        return {'question_id': question_id}

class StudentViewSet(ModelViewSet):
    queryset = Student.objects.all()
    
    def get_serializer_class(self):
        if self.request.method == 'POST':
            return AddStudentSerializer
        return StudentSerializer
class TeacherViewSet(ModelViewSet):
    queryset = Teacher.objects.all()
    
    def get_serializer_class(self):
        if self.request.method == 'POST':
            return AddTeacherSerializer
        return TeacherSerializer

class ClassRoomViewSet(ModelViewSet):
    queryset = ClassRoom.objects.all()
    serializer_class = ClassRoomSerializer

