from rest_framework_nested import routers
from .import views

router = routers.DefaultRouter()
router.register('exams', views.ExamViewSet)
router.register('rooms', views.ClassRoomViewSet)

section_router = routers.NestedDefaultRouter(router, 'exams', lookup='exam' )
section_router.register('sections', views.SectionViewSet, basename='exam-sections')

question_router = routers.NestedDefaultRouter(section_router, 'sections', lookup='section')
question_router.register('questions', views.QuestionModelViewSet, basename='section-questions')

choice_router = routers.NestedDefaultRouter(question_router, 'questions', lookup='question')
choice_router.register('choices', views.ChoiceViewSet, basename='question-choices')



urlpatterns = router.urls + section_router.urls + question_router.urls + choice_router.urls