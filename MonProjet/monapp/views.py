from django.shortcuts import render

# Create your views here.
def accueil(request):
    """Page d'accueil"""
    return render(request, 'monapp/accueil.html')

def a_propos(request):
    """Page À propos"""
    return render(request, 'monapp/a_propos.html')

def contact(request):
    """Page Contact"""
    return render(request, 'monapp/contact.html')
