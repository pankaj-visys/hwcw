'''Tutorial1 Models'''

from django.db import models
from django.contrib.auth import get_user_model
from taggit.managers import TaggableManager
from django.core.validators import FileExtensionValidator 
import datetime

SCHOOL_OPTIONS = (
    ('lmc','LMC'),
    ('sfc', 'SFC'),
    ('cms','CMS'),
    ('mbic','MBIC'),
)

GRADE_OPTIONS = (
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

SUBJECT_OPTIONS = (
    ('English','Eng'),
    ('Hindi','Hin'),
    ('Mathematics','Maths'),
    ('Computer','Comp'),
)

TYPE_OPTIONS = (
    ('Classwork','CW'),
    ('Homework','HW'),
)

class Work(models.Model):
    
    title = models.CharField(max_length=45)
    
    description = models.CharField(max_length=250)

    created = models.DateTimeField(auto_now_add=True)

    workfile = models.FileField(upload_to='work/')

    submitter = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    school = models.CharField(max_length=6, choices=SCHOOL_OPTIONS, default='CMS')
    grade = models.CharField(max_length=4, choices=GRADE_OPTIONS, default='1')
    subject = models.CharField(max_length=20, choices=SUBJECT_OPTIONS, default='English')
    type = models.CharField(max_length=10, choices=TYPE_OPTIONS, default='HW')
    dateOfAssignment = models.DateField(default=datetime.date.today)

    tags = TaggableManager() 

    def __str__(self):
        return self.title