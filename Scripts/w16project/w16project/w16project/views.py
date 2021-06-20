from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    if 'user' not in request.COOKIES: # (For first time user)
        
        response = render(request=request, 
                          template_name='template.htm', 
                          context={'message':'Please REFRESH...'})
        response.set_cookie(key='user', value='user1')
        return response
    else: # (For login again)
        
        return render(request=request, 
                      template_name='index.html', 
                      context={'message': 'Welcome back,'+ request.COOKIES['user']})
