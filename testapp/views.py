from django.shortcuts import render
from testapp.forms import FeedbackForm
# Create your views here.
def feedback_view(request):
    submitted=False
    name=''
    if request.method == 'POST':
        form=FeedbackForm(request.POST)
        if form.is_valid():
            print('Form Validation Success and Printing Feedback Information')
            print("*"*50)
            print('Name',form.cleaned_data['full_name'])
            print('Roll_NO',form.cleaned_data['rollno'])
            print('Mail_Id',form.cleaned_data['email'])
            print('Feedback',form.cleaned_data['feedback'])
            submitted=True
            name=form.cleaned_data['full_name']
        else:
            print('Some Field Validations Failed!!!')
    else:
        form=FeedbackForm()
    return render(request,'testapp/index.html',{'form':form,'name':name,'submitted':submitted}) 