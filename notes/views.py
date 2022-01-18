from django.shortcuts import render , redirect , get_object_or_404 , HttpResponse
from django.contrib.auth.models import *
from .models import *
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.template import *
from django.contrib import auth
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required



# Create your views here.



# view for welcome.html page
def welcome(request):
    return render(request, "welcome.html")






#------------------------------------------------------------------------------------------------------------
# registration view for registration.html
def registration(request):
    if request.method == 'POST':
        # user = registration(request.POST)
        # print(request.POST.get('user_name'))
        # user.save()
        db_user = Registration.objects.all()
        print(request.POST.get('user_name'))
        print(request.POST.get('mobile'))
        print(request.POST.get('email'))
        print(request.POST.get('password'))
        user = Registration(user_name=request.POST['user_name'],mobile=request.POST['mobile'],email=request.POST['email'],password = request.POST['password'])
        print(user)
        user.save()
    return render(request, "registration.html")



#----------------------------------------------------------------------------------------------------------------
#another model for sign_up as simple sign_up
def sign_up(request):
    print("KDFGKDFGK")
    if request.method == 'POST':
        try:
            user = User.objects.get(username = request.POST['mobile'])
            # return HttpResponse(request, 'signup.html')
            return render(request, "login.html", {"msg": "user already exsits!!!"})
        except ObjectDoesNotExist:
            user = User.objects.create_user(username=request.POST['mobile'], password=request.POST['password'])
            user.save()
            return render(request, "login.html")
    else:
        return render(request, "signup.html",{'msg' : 'user already register please login'})
#----------------------------------------------------------------------------------------------------------------




#view for login validation
def login(request):
    if request.method == 'POST':
        user = auth.authenticate(username= request.POST['mobile'], password= request.POST['password'])
        if user is not None:
            auth.login(request,user)
            return render(request, "note.html", {"msg" : "login sucess",'msg1': request.user})
        else:
            return render(request, 'signup.html' , {"warning" : "user not found"})
    else:
        return render(request, "login.html", {"warning" : "please login"})
#------------------------------------------------------------------------------------------------------------------

@login_required(login_url='/login/')
def note(request):
    if request.method == 'POST':
        data = Note(subject = request.POST['subject'] , text = request.POST['text'], user = request.user)
        data.save()
        print(request.user, "LLLLLL")
        note_data = Note.objects.all().values()
        print(note_data)
        notedata = {'note_data': note_data}
        print(notedata)
        for i in range(0,len(note_data)):
            print(note_data[i])

            # print(request.POST.get('subject'))
            # print(request.POST.get('text'))
        return render(request, 'note.html', {"msg1":request.user})

    if request.method == 'GET':
        print('hyyy')
        print(request.user, 'tq')
        #return render(request, 'note.html', {"msg1":request.user})
        return render(request, "note.html", {"msg": "login sucess", 'msg1': request.user})
def logout(request):
    u_name = request.user
    auth.logout(request)
    return render(request, 'login.html' , {'msg_logout': u_name})
def view_notes(request):
    data_notes = Note.objects.all().values()
    return render(request, 'viewnote.html', {'view': data_notes})


def delete(request,pk):
    context= {}
    obj = get_object_or_404(Note,id = pk)
    if request.method == "GET" :
        print('hiii boss')
        obj.delete()
        print('sucess 123')
        data_notes = Note.objects.all().values()
        return render(request , 'viewnote.html' , {'delete' : 'iteam deleted sucess' , 'view' : data_notes , 'id': pk})
    else :

        print('im else')
        return render(request , 'viewnote.html')



def update_view(request , pk):
    obj= get_object_or_404(Note , id = pk)
    if request.method == 'GET' :
        #obj.status = request.POST['updatestatus']
        # note_id = Note.objects.get(id = pk)
        # note_data = note_id.date, note_id.subject , note_id.text
        print(obj.subject)


        return render(request , 'updateview.html', {'data': obj})
    if request.method == "POST" :
        obj.subject = request.POST['subject']
        obj.text = request.POST['text']
        obj.save()
        print('xyz')

        return redirect(view_notes)


def hello(request):
    data='''
    <h1> hello boss</h1>
    

    '''
    return HttpResponse(data)
def log_in(request):
    if request.method == 'POST':
        user = auth.authenticate(username= request.POST['mobile'], password= request.POST['password'])
        if user is not None:
            auth.login(request,user)
            return redirect(note)
            #return render(request, "note.html", {"msg" : "login sucess",'msg1': request.user})
        else:
            return render(request, 'signup.html' , {"warning" : "user not found"})
    # elif request.method == 'GET':
    #     return  render(request, )
    else:
        return render(request, "log_in.html", {"warning" : "please login"})