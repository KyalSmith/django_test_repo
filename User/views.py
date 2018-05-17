from django.shortcuts import render
from .forms import UserProfileInfoForm,UserForm



def index(request):

    return render(request,'index.html')


# Create your views here.
def login(request):
    pass


def register(request):

    registered = False

    if request.method == "POST":

        userprofile_stuff = UserProfileInfoForm(data=request.POST)
        user_stuff = UserForm(data=request.POST)

        if userprofile_stuff.is_valid() and user_stuff.is_valid():

            user = user_stuff.save()
            user.set_password(user.set_password)
            user.save()

            profile_data =userprofile_stuff.save(commit=False)
            profile_data.user = user

            if 'profile_pic' in request.FILES:

                profile_data.picture = request.FILES('profile_pic')

            profile_data.save()

            registered=True

            return render(request, 'registration.html',
                          {'user_form': user_stuff, 'profile_form': userprofile_stuff, 'registered': registered})

        else:
            print(user_stuff.errors)
            print(userprofile_stuff.errors)

    else:

        user_form = UserForm()
        profile_form = UserProfileInfoForm()


        return render(request,'registration.html',{'user_form':user_form,'profile_form':profile_form,'registered':registered})