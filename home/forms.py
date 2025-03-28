from django import forms

class ContactForm(forms.Form):
    full_name = forms.CharField(max_length=100, required=True, widget=forms.TextInput(attrs={'placeholder': 'Your Full Name'}))
    email = forms.EmailField(required=True, widget=forms.EmailInput(attrs={'placeholder': 'Your Email Address'}))
    subject = forms.CharField(max_length=150, required=True, widget=forms.TextInput(attrs={'placeholder': 'Subject'}))
    message = forms.CharField(required=True, widget=forms.Textarea(attrs={'rows': 6, 'placeholder': 'Your Message'}))

class FeedbackForm(forms.Form):
    full_name = forms.CharField(max_length=100, required=True)
    email = forms.EmailField(required=True)
    message = forms.CharField(required=True, widget=forms.Textarea(attrs={'rows': 5}))

class VolunteerForm(forms.Form):
    first_name = forms.CharField(max_length=50, required=True)
    last_name = forms.CharField(max_length=50, required=True)
    gender = forms.ChoiceField(choices=[('', 'Select Gender'), ('male', 'Male'), ('female', 'Female'), ('other', 'Other'), ('prefer_not_to_say', 'Prefer not to say')], required=True)
    age = forms.IntegerField(min_value=16, required=True) # Example min age
    contact = forms.CharField(max_length=20, required=True, label="Contact Number")
    email = forms.EmailField(required=True)
    message = forms.CharField(required=True, widget=forms.Textarea(attrs={'rows': 5}), label="Why do you want to volunteer?")