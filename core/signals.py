from django.contrib.auth import get_user_model
from django.db.models.signals import post_delete
from django.dispatch import receiver
# from class_room.models import Student, Teacher

User = get_user_model()

# @receiver(post_delete, sender=Student)
# def delete_profile(sender, instance, **kwargs):
#     instance.user.delete()

# @receiver(post_delete, sender=Teacher)
# def delete_profile(sender, instance, **kwargs):
#     instance.user.delete()