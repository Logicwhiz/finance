from django import forms
from .models import Track

class Form(forms.ModelForm):
    
    class Meta:
        model = Track
        fields = "__all__"  # Include all fields from the Track model
        
    CHOICES = (
        ('', 'Select'),
        ('Income', 'Income'),  # Tuple should contain both value and label
        ('Spend', 'Spend'),    # Tuple should contain both value and label
    )
        
    widgets = {
        'title': forms.TextInput(attrs={'class': 'form-control'}),
        'category': forms.TextInput(attrs={'class': 'form-control'}),
        'type': forms.Select(choices=CHOICES, attrs={'class': 'form-control'}),  # Use forms.Select for ChoiceField
        'amount': forms.NumberInput(attrs={'class': 'form-control'})
    }




