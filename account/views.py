from django.shortcuts import redirect, render
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from account.models import User_info
from django.contrib.auth.models import User
from .forms import UserSignUpForm, UserInfo, UserFLEname
from shop.models import OrderPlace, Product
from .forms import UserSignUpForm, UserInfo


def user_login(request):
    if not request.user.is_authenticated:
        if request.method == "POST":
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                print('successfully login in')
                return redirect('index')
            else:
                return render(request, 'account/login.html')
        else:
            return render(request, 'account/login.html')
    else:
        return redirect('index')


def signup_view(request):
    if not request.user.is_authenticated:
        form = UserSignUpForm()
        form1 = UserInfo()
        if request.method == "POST":
            form = UserSignUpForm(request.POST)
            form1 = UserInfo(request.POST, request.FILES or None)

            if form.is_valid() and form1.is_valid():
                print(form1.cleaned_data['profile_pic'])
                userform = form.save()
                userinfo = form1.save(commit=False)
                userinfo.user = userform
                userinfo.save()
                return redirect('login')

        return render(request, 'account/signup.html', context={'form': form, 'form1': form1})
    else:
        return redirect('index')


@login_required(login_url='/account/login/')
def user_logout(request):
    if request.user.is_authenticated:
        logout(request)
        if cart := request.session.get('cart'):
            cart = {}
        return redirect('login')
    else:
        return redirect('login')


@login_required(login_url='/account/login/')
def user_profile(request):
    user = request.user
    user_profile = User_info.objects.get(user=user)
    orders = OrderPlace.get_orders_by_customer(user)
    products = Product.objects.filter(user=user)
    context = {
        'user': user,
        'profile': user_profile,
        'orders': orders,
        'products':products,
    }
    return render(request, 'account/dashboard.html', context)


@login_required(login_url='/account/login/')
def editUserInfo(request):
    if request.method == 'POST':
        mydata = User_info.objects.get(user=request.user)
        user = User.objects.get(username=request.user.username)
        form = UserInfo(request.POST, request.FILES or None, instance=mydata)
        form1 = UserFLEname(request.POST, request.FILES or None, instance=user)
        if form.is_valid() and form1.is_valid():
            form.save()
            form1.save()
        return redirect('userprofile')
    else:
        mydata = User_info.objects.get(user=request.user)
        user = User.objects.get(username=request.user.username)
        form = UserInfo(instance=mydata)
        form1 = UserFLEname(instance=user)
    context = {
        'form': form,
        'form1': form1,
        'userinfo': mydata,
    }
    return render(request, 'account/editinfo.html', context)
