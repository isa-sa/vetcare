from django.shortcuts import render, redirect
from .forms import CadastroForm
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import never_cache

def signup(request):
    if request.method == 'POST':
        form = CadastroForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = CadastroForm()
    
    return render(request, 'registration/signup.html', {'form': form})


@login_required
@never_cache
def painel(request):
    return render(request, 'painel.html')

def index(request):
    return render(request, 'index.html')