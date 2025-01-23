from django.shortcuts import render


def home(request):
    return render(request, 'blog/home.html')
def about(request):
    return render(request, 'blog/about.html')
def privacy_policy(request):
    return render(request, 'blog/privacy_policy.html')

# Terms of Service Page View
def terms_of_service(request):
    return render(request, 'blog/terms_of_service.html')

def register(request):
    return render(request, 'blog/register.html')