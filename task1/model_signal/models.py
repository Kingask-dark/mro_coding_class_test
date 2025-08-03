from django.db import models

# Create your models here.
class CourseModel(models.Model):
    course_name = models.CharField(max_length=50)
    course_number = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name = "Course"
        verbose_name_plural = "Course's"

    def __str__(self):
        return self.course_name

class CourseLog(models.Model):
    course = models.ForeignKey(CourseModel,on_delete=models.PROTECT,related_name="course")
    details = models.CharField(max_length=100)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    
    class Meta:
        verbose_name = "Course Log"
        verbose_name_plural = "Course Logs"

    def __str__(self):
        return self.course