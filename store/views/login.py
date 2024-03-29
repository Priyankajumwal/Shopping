from django.shortcuts import render , redirect , HttpResponseRedirect
from store.models.customer import Customer
from django.contrib.auth.hashers import make_password, check_password
from django.views import View


print(make_password('1234'))

class Login(View):
    return_url = None
    def get(self , request):    # Handel get request
        Login.return_url = request.GET.get('return_url')
        return render(request, 'login.html')

    def post(self , request): # Handel post request
        email = request.POST.get('Email')
        password = request.POST.get('Password')
        customer = Customer.get_customer_by_email(email)
        error_message = None
        if customer:
            flag = check_password(password, customer.password)
            if flag:
                request.session['customer'] = customer.id

                print('you are : ', request.session.get('email'))

                if Login.return_url:
                    return HttpResponseRedirect(Login.return_url)
                else:
                    Login.return_url = None
                    return redirect('homepage')
            else:
                error_message = 'Email OR Password invalid !!'
        else:
            error_message = 'Email OR Password invalid !!'

        print(email, password)
        return render(request, 'login.html', {'error': error_message})

def logout(request):
    request.session.clear()
    return redirect('login')



