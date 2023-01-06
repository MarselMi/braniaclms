from django import forms
from django.utils.translation import gettext_lazy as _
from mainapp import models


class CourseFeedbackForm(forms.ModelForm):
    def __init__(self, *args, course=None, user=None, **kwargs):
        super().__init__(*args, **kwargs)

        if course and user:
            self.fields["course"].initial = course.pk
            self.fields["user"].initial = user.pk

    class Meta:
        model = models.CourseFeedback
        fields = ("course", "user", "feedback", "rating")
        widgets = {
            "course": forms.HiddenInput(),
            "user": forms.HiddenInput(),
            "rating": forms.RadioSelect(),
        }