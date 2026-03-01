from django import forms
class FeedbackForm(forms.Form):
    full_name=forms.CharField(max_length=30)
    rollno=forms.IntegerField()
    email=forms.EmailField()
    feedback=forms.CharField(widget=forms.Textarea)
    
    
    def clean_full_name(self):
        print('Validating Name Field')
        inputname=self.cleaned_data['full_name']
        if len(inputname)>2 and inputname.isalpha() :
            pass
        else:
            raise forms.ValidationError("Minimum Number of Character in the Name Field Should be 3 and Don't Enter Alphanumeric and Numbers.")
        return inputname
    def clean_rollno(self):
        print('Validating Roll_no Field')
        rollno=self.cleaned_data['rollno']
        return rollno
    def clean_email(self):
        print('Validating Email Field')
        inputmail=self.cleaned_data['email']
        if not inputmail.endswith("@gmail.com"):
            raise forms.ValidationError('Enter Valid Email ID')
        return inputmail
    def clean_feedback(self):
        print('Validating Feedback Field')
        feedback=self.cleaned_data['feedback']
        if len(feedback)<10 or len(feedback)>40:
            raise forms.ValidationError('Give Your Feedback Between 10 to 40 Words')
        return feedback
