from django.db import models
from django.contrib.auth import get_user_model
from taggit.managers import TaggableManager
from django.core.validators import FileExtensionValidator 
import datetime

SCHOOL_CHOICES = (
    ('lmc','LMC'),
    ('sfc', 'SFC'),
    ('cms','CMS'),
    ('mbic','MBIC'),
)

GRADE_CHOICES = (
    ('1','1'),
    ('2','2'),
    ('3','3'),
    ('4','4'),
    ('5','5'),
    ('6','6'),
    ('7','7'),
    ('8','8'),
    ('9','9'),
    ('10','10'),
    ('11','11'),
    ('12','12'),
)

SUBJECT_CHOICES = (
    ('English','Eng'),
    ('Hindi','Hin'),
    ('Mathematics','Maths'),
    ('Computer','Comp'),
)

TYPE_CHOICES = (
    ('Classwork','CW'),
    ('Homework','HW'),
)

class Myfiles(models.Model):
    
    title = models.CharField(max_length=45)
    
    description = models.CharField(max_length=250)

    created = models.DateTimeField(auto_now_add=True)

    fileName = models.FileField(upload_to='raw/')
    batch = models.CharField(max_length=250, null=True)

    submitter = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, null=True)
    school = models.CharField(max_length=6, choices=SCHOOL_CHOICES, default='CMS')
    grade = models.CharField(max_length=4, choices=GRADE_CHOICES, default='1')
    subject = models.CharField(max_length=20, choices=SUBJECT_CHOICES, default='English')
    type = models.CharField(max_length=10, choices=TYPE_CHOICES, default='HW')
    dateOfAssignment = models.DateField(default=datetime.date.today)

    tags = TaggableManager()

    def __str__(self):
        return self.title
 