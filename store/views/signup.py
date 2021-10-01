from django.shortcuts import render, redirect
from store.models.customer import Customer
from django.views import View
from django.contrib.auth.hashers import make_password , check_password

print(make_password('1234'))


class Signup(View):
    def get(self, request):
        return render(request, 'signup.html')

    def post(self, request):
        postData = request.POST
        first_name = postData.get('first_name')
        last_name = postData.get('last_name')
        email = postData.get('email')
        phone = postData.get('phone')
        password = postData.get('password')

        # validation

        value = {
            'first_name': first_name,
            'last_name': last_name,
            'phone': phone,
            'email': email,

        }
        error_message = None

        customer = Customer(first_name=first_name,
                            last_name=last_name,
                            email=email,
                            phone=phone,
                            password=password)

        error_message = self.validateCustomer(customer)

        # saving_values

        if not error_message:
            print(first_name,last_name,phone,email,password)
            customer.password = make_password(customer.password)
            customer.register()
            return redirect('homepage')
        else:
            data = {
                'error': error_message,
                'values': value
            }
            return render(request, 'signup.html', data)

    def validateCustomer(self, customer):

        error_message = None;
        if not customer.first_name:
            error_message = 'First Name is Required!!'
        elif len(customer.first_name) < 4:
            error_message = 'First Name should not be less than 4 characters!!'

        elif not customer.last_name:
            error_message = 'Last Name is Required!!'
        elif len(customer.last_name) < 4:
            error_message = 'Last Name should not be less than 4 characters!!'

        elif not customer.email:
            error_message = 'Email is Required!!'
        elif len(customer.email) < 4:
            error_message = 'E-mail should not be less than 4 characters!!'

        elif not customer.password:
            error_message = 'Password is Required!!'
        elif len(customer.password) < 6 :
            error_message = 'Password should not be less than 8 characters!!'

        elif not customer.phone:
            error_message = 'Phone Number is Required!!'
        elif len(customer.phone) < 10:
            error_message = 'Phone Number should not be less than 10 characters!!'


        elif customer.isExists():
            error_message = 'Email already Registered..'

        return error_message


