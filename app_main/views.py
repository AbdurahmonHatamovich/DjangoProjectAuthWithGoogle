from django.shortcuts import redirect,render
from django.urls import reverse

def home(request):
    if not request.user.is_authenticated:
        return redirect("login")

    return render(request, "app_main/home.html")




def google_login(request):
    return redirect(reverse('social:begin', args=['google-oauth2']))
