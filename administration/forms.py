from django import forms


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

class MultipleFileInput(forms.ClearableFileInput):
    allow_multiple_selected = True

class MultipleFileField(forms.FileField):
    def __init__(self, *args, **kwargs):
        kwargs.setdefault("widget", MultipleFileInput())
        super().__init__(*args, **kwargs)

    def clean(self, data, initial=None):
        single_file_clean = super().clean
        if isinstance(data, (list, tuple)):
            result = [single_file_clean(d, initial) for d in data]
        else:
            result = [single_file_clean(data, initial)]
        return result

class UploadFileForm(forms.Form):
    title = forms.CharField(max_length = 200)
    description = forms.CharField(max_length = 500)
    file = MultipleFileField()
    school = forms.ChoiceField(choices=SCHOOL_CHOICES)
    grade = forms.ChoiceField(choices=GRADE_CHOICES)
    subject = forms.ChoiceField(choices=SUBJECT_CHOICES)
