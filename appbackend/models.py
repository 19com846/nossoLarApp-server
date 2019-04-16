from django.db import models
from appbackend.enums import Role, Cycle


class User(models.Model):
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    phone = models.CharField(max_length=20)
    role = Role


class Course(models.Model):
    name = models.CharField(max_length=50)
    cycle = Cycle


class ClassGroup(models.Model):
    course = models.ForeignKey(Course, related_name="course", on_delete=models.CASCADE)
    students = models.ManyToManyField(User)
    leader = models.ForeignKey(User, related_name="class leader", on_delete=models.CASCADE)


class Lesson(models.Model):
    name = models.CharField(max_length=50)
    class_group = models.ForeignKey(ClassGroup, related_name="class", on_delete=models.CASCADE)
    date = models.DateTimeField()

# Relationship between User/Student and ClassGroup
class Enrollment(models.Model):
    students = models.ManyToManyField(User)
    class_group = models.ForeignKey(ClassGroup, related_name="class", on_delete=models.CASCADE)


# Relationship between User/Student and Lesson
class Attendance(models.Model):
    students = models.ManyToManyField(User)
    lesson = models.ForeignKey(Lesson, related_name="lesson", on_delete=models.CASCADE)