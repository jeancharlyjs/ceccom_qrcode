from apps.serializers.UserSerializer import LoginSerializer
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from rest_framework.views import APIView

class Login(APIView):
    def userLogin(request):
        if request.method == "POST":
            form = LoginSerializer(request.POST)
            if form.is_valid():
                cd = form.cleaned_data
                user = authenticate(request,
                                     username=cd['username']
                                     password=cd['passowrd'])
                if user is not None:
                    if user.is_active:
                        login(request, LoginSerializer)
                        return HttpResponse("Acceso correcto")
                    else:
                        return  HttpResponse("Acceso denegado")
        else:
            form = LoginSerializer()
            
