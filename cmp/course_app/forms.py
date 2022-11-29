# from django.forms import ModelForm
from django import forms


from .models import Submission, Question


class QuestionForm(forms.Form):
    # user = None

    def __init__(self, homework, *args, **kwargs):
        self.user = kwargs.pop('user')
        answer = kwargs.pop('answer', {})

        super().__init__(*args, **kwargs)
        self.homework = homework

        for question in homework.question_set.all():
            question_id = f"question_{question.id}"

            # print("question", question.type)
            if question.type == "radio":
                choices = list(enumerate(question.options))
                field = forms.MultipleChoiceField(
                    widget=forms.SelectMultiple, choices=choices, 
                )
            elif question.type == "text":
                field = forms.CharField(
                    widget=forms.TextInput
                )
            else:
                field = forms.URLField(
                    widget=forms.URLInput
                )
            
            field.label = question.question
        
            if question_id in answer:
                field.initial = answer[question_id]
    
            self.fields[question_id] = field

    def save(self):
        data = self.cleaned_data.copy()
        # print("DATA====>", data)
        # print("USER", user)

        
        submission = Submission(homework=self.homework, user=self.user)
        submission.answer = data
        print("Submission", submission.user, submission.answer)

        # save self.user 
        submission.save()
