from django import forms
from .models import Candidate


class CandidateForm(forms.ModelForm):
    introduction = forms.CharField(label="簡介", widget=forms.Textarea, required=False)

    class Meta:
        model = Candidate
        fields = ["name", "party", "age", "introduction"]
        labels = {
            "name": "姓名",
            "party": "政黨",
            "age": "年齡",
        }
