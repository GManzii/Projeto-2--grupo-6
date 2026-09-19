from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import ContatoForm

def home(request):
    return render(request, "core/home.html")


def about(request):
    return render(request, "core/about.html")


def contact(request):
    if request.method == 'POST':
        form = ContatoForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Sua mensagem foi enviada com sucesso!')
            return redirect('fale_conosco')
    else:
        form = ContatoForm()

    return render(request, 'contact.html', {'form': form})