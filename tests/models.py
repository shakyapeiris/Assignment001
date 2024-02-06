from django.db import models

# Create your models here.
class School(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=200)

class Student(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=200)

class Class(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=200)

class AssessmentArea(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=200)

class Answer(models.Model):
    id = models.IntegerField(primary_key=True)
    answer = models.CharField(max_length=200)

class Award(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=200)

class Subject(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=200)
    score = models.IntegerField()

class Summary(models.Model):
    school_id = models.ForeignKey(School, on_delete=models.CASCADE)
    sydney_percentile = models.FloatField()
    assesment_area_id = models.ForeignKey(AssessmentArea, on_delete=models.CASCADE)
    award_id = models.ForeignKey(Award, on_delete=models.CASCADE)
    class_id = models.ForeignKey(Class, on_delete=models.CASCADE)
    correct_answer_percentage_per_class = models.FloatField()
    student_id = models.ForeignKey(Student, on_delete=models.CASCADE)
    participant = models.IntegerField()
    student_score = models.IntegerField()
    subject_id = models.ForeignKey(Subject, on_delete=models.CASCADE)
    year_lvl_name = models.CharField(max_length=20)
    answer = models.CharField(max_length=1)
    correct_answer = models.CharField(max_length=1)
    question = models.IntegerField()


