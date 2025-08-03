from django.db.models.signals import (
    post_save,
    post_migrate,
    post_delete
)
from django.dispatch import receiver

from model_signal.models import (
    CourseModel,
    CourseLog
)
import os

@receiver(post_save,sender=CourseModel)
def write_course_file(sender,instance,**kwargs):
    file_name = "Course_data.txt"
    if os.path.exists(file_name):
        with open(file_name,'w',encoding='utf-8') as f:
            f.write(instance.course_name)
            f.write('\n')
            f.write(str(instance.course_number))