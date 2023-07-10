from django.db import models
from django.conf import settings
from .utils import unique_slug_generator
from .validators import validate_file_size


class Exam(models.Model):
    title = models.CharField(max_length=100, null=True, blank=True)
    slug = models.SlugField(unique=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='exams_authored')
    total_mark = models.PositiveSmallIntegerField()
    time_allowed = models.TimeField()
    starting_time = models.TimeField()

    def save(self, *args, **kwargs):
        slug = unique_slug_generator(self)
        self.slug = slug
        super(Exam, self).save(*args, **kwargs)
   

    def __str__(self):
        return self.title


class Section(models.Model):

    TYPE_CHOICES = [
        ('C', 'Choice Questions'),
        ('T', 'True or False Questions'),
        ('F', 'Fill in the Blank')
    ]

    type = models.CharField(max_length=1, choices=TYPE_CHOICES)
    instruction = models.TextField()
    exam = models.ForeignKey(Exam, on_delete=models.CASCADE, related_name='sections')

    def __str__(self):
        return self.type

class ChoiceQuestion(models.Model):  
    number = models.PositiveSmallIntegerField()
    content = models.TextField()
    
    def __str__(self):
        return f'{self.content}'
        
class Choice(models.Model):
    choice_name = models.CharField(max_length=1)
    content = models.TextField()
    is_correct = models.BooleanField(default=False)
    question = models.ForeignKey(ChoiceQuestion, on_delete=models.CASCADE, related_name='answers')

    def __str__(self) -> str:
        return f'{self.choice_name}, {self.content}'

class TrueFalseQuestion(models.Model):

    ANSWER_CHOICES = [
        ('T', 'True'),
        ('F', 'False')
    ]

    number = models.PositiveSmallIntegerField()
    content = models.TextField()
    correct_answer = models.CharField(max_length=5, choices=ANSWER_CHOICES)
    answer = models.CharField(max_length=5, choices=ANSWER_CHOICES)

    def __str__(self) -> str:
        return self.content

class FillInQuestion(models.Model):
    number = models.PositiveSmallIntegerField()
    content = models.TextField()
    correct_answer = models.CharField(max_length=20)
    answer = models.CharField(max_length=20)

    def __str__(self) -> str:
        return self.content


class Student(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='students')
    school_id = models.CharField(max_length=100)
    department = models.CharField(max_length=100)
    section = models.CharField(max_length=100)
    image = models.ImageField(upload_to='students/images/', validators=[validate_file_size])

    def __str__(self):
        return self.user.username


class Teacher(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='teachers')
    school_id = models.CharField(max_length=100)
    department = models.CharField(max_length=100)
    image = models.ImageField(upload_to='teachers/images/', validators=[validate_file_size])
    
    def __str__(self):
        return self.user.username


class ClassRoom(models.Model):
    host = models.ForeignKey(Teacher, on_delete=models.PROTECT, related_name='room')
    name = models.CharField(max_length=50)
    participants = models.ManyToManyField(Student, related_name='class_room')
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)
    created = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name