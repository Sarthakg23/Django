from django.forms import forms
from django.shortcuts import render
from main import forms
from django.http import HttpResponseRedirect

# Create your views here.
from django.http import HttpResponse

#from main.models import User, Question, Answer
#from . import forms
from main.models import User, Credit, Debit, Transfer


def Homepageview(request):
    return render(request, 'homepage.html')

def signup(request):
    if request.method == 'GET':
        form = forms.UserForm()

    else:
        form = forms.UserForm(request.POST)
        if form.is_valid():
            obj = form.save()
            return HttpResponse("Form Submitted Successfully")
    context = {
        'user_form': form
    }

    return  render(request, 'signup.html', context)

def login(request):
    if request.method == 'GET':
        formlogin = forms.Userloginform()
        context = {
            'user_loginform': formlogin
        }

        return render(request, 'login.html', context)
    else:
        formlogin = forms.Userloginform(request.POST)
        email=formlogin.data["email"]
        password=formlogin.data["password"]
        print(email,password)
        user= User.objects.filter(email=email,password=password)
        print(user)

        if len(user)>0:
            return HttpResponseRedirect('/dashboard/?user_id='+str(user[0].id))
        else:
            context = {
                'user_loginform': formlogin
            }

            return render(request, 'login.html', context)

def dashboard(request):
    user_id = request.GET.get("user_id")
    user = User.objects.filter(id=user_id)
    context= {"user":user[0],
               }
    return render(request, 'dashboard.html',context)


def credit(request):
    if request.method == 'GET':
        user_id = request.GET.get("user_id")
        credit_form = forms.credit_form()
        context = {
        'user_credit_form': credit_form,
        'user_id': user_id
        }
        return render(request, 'credit.html', context)
    else:
        credit_form = forms.credit_form(request.POST)
        if credit_form.is_valid():
            obj = credit_form.save()
            user_id = request.GET.get("user_id")
            credit = credit_form.data["credit"]
            user = User.objects.get(id=user_id)
            balance=user.balance
            print(credit)
            print(balance)
            user.balance = int(balance)+int(credit)
            obj = user.save()
            return HttpResponseRedirect('/dashboard/?user_id='+str(user_id))
        context = {
            'user_credit_form': credit_form
        }

        return render(request, 'credit.html', context)






def debit(request):
    if request.method == 'GET':
        user_id = request.GET.get("user_id")
        debit_form = forms.debit_form()
        context = {
        'user_debit_form': debit_form,
        'user_id': user_id
        }
        return render(request, 'debit.html', context)
    else:
        debit_form = forms.debit_form(request.POST)
        if debit_form.is_valid():
            obj = debit_form.save()
            user_id = request.GET.get("user_id")
            debit = debit_form.data["debit"]
            user = User.objects.get(id=user_id)
            balance=user.balance
            print(credit)
            print(balance)
            user.balance = int(balance)-int(debit)
            obj = user.save()
            return HttpResponseRedirect('/dashboard/?user_id='+str(user_id))
        context = {
            'user_debit_form': debit_form
        }

        return render(request, 'debit.html', context)


def acc_state(request):
    user_id = request.GET.get("user_id")
    user = User.objects.filter(id=user_id)
    credit= Credit.objects.filter(user=user_id)
    debit = Debit.objects.filter(user=user_id)
    transfer = Transfer.objects.filter(user=user_id)
    received=Transfer.objects.filter(receiver=user_id)
    # debit=Debit.objects.all
    context = {"user": user[0],
               "credits":credit,
               "debits":debit,
               "transfers":transfer,
               "receivings":received,

               }
    return render(request, 'acc_state.html', context)



def transfer(request):
    if request.method == 'GET':
        transfer_form = forms.transfer_form()
        context = {
        'user_transfer_form': transfer_form
        }
        return render(request, 'transfer.html', context)
    else:
        transfer_form = forms.transfer_form(request.POST)
        if transfer_form.is_valid():
            obj = transfer_form.save()
            user_id = request.GET.get("user_id")
            print(user_id)
            receiver = transfer_form.data["receiver"]
            debiter = User.objects.get(id=user_id)
            creditor = User.objects.get(id=receiver)
            print(debiter.balance)
            deb_balance = debiter.balance
            cre_balance = creditor.balance
            amount = transfer_form.data["amount"]
            debiter.balance = int(deb_balance)-int(amount)
            creditor.balance = int(cre_balance)+int(amount)
            obj=debiter.save()
            obj=creditor.save()
            return HttpResponseRedirect('/dashboard/?user_id=' + str(user_id))

        context = {
                'user_transfer_form': transfer_form
            }

        return render(request, 'debit.html', context)


#def b_login(request):






