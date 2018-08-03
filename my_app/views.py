from django.shortcuts import render
from django.template.context_processors import csrf
from .forms import ApplicantInfoForm


# Create your views here.
def index(request):
    return render(request, 'index.html')


#


def apply(request):
    applied = False
    form = ApplicantInfoForm()
    #
    # c = {}
    # c.update(csrf(request))
    # applied = False
    if request.method == "POST":
        form = ApplicantInfoForm(request.POST)
        if form.is_valid():

            application = form.save(commit=False)
            if 'resume'and 'cover_letter' in request.FILES:
                print('FOUND A FILE SUBMITTED')
                # FILES contains a dict of media dirs
            application.resume = request.FILES['resume']
            application.cover_letter = request.FILES['cover_letter']
            application.save()
            applied = True
        else:
            print(form.errors)

    return render(request, 'form.html', {'applied': applied,'form':form})
