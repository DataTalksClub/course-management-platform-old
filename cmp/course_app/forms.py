# from django.forms import ModelForm
from django import forms


from .models import Submission, Question


class QuestionForm(forms.Form):
    email = forms.EmailField()

    def __init__(self, homework, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.homework = homework

        for question in homework.question_set.all():
            # print("question", question.type)
            if question.type == "radio":
                choices = list(enumerate(question.options))
                self.fields[f"question_{question.id}"] = forms.MultipleChoiceField(
                    widget=forms.SelectMultiple, choices=choices
                )
                self.fields[f"question_{question.id}"].label = question.question
            elif question.type == "text":
                self.fields[f"question_{question.id}"] = forms.CharField(
                    widget=forms.TextInput
                )
                self.fields[f"question_{question.id}"].label = question.question
            else:
                self.fields[f"question_{question.id}"] = forms.URLField(
                    widget=forms.URLInput
                )
                self.fields[f"question_{question.id}"].label = question.question

    def save(self):
        data = self.cleaned_data.copy()
        print("DATA====>", data)

        email = data.pop("email")
        submission = Submission(homework=self.homework, participant_email=email)
        submission.answer = data
        submission.save()
