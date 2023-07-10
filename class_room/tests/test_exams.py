from rest_framework.test import APIClient
from rest_framework import status
import pytest

@pytest.mark.django_db
class TestCreateExam:  # creating is one scenario in dealing with exams endpoint

    @pytest.mark.skip
    def test_if_user_is_anonymous_return_401(self):
    # Arrange Act Assert 
        client = APIClient()
        response = client.post('/exams/', {'title' : 'a'})
        assert response.status_code == status.HTTP_401_UNAUTHORIZED
# {
#         "id": 3,
#         "title": "civics and ethical education grade 9",
#         "slug": "civics-and-ethical-education-grade-9",
#         "author": 13,
#         "total_mark": 80,
#         "time_allowed": "08:08:39",
#         "starting_time": "21:30:44"}