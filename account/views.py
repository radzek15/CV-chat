from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .forms import UserRegistrationForm


@login_required
def dashboard(request):
    return render(request, 'chat/index.html', {})


def register(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            new_user = user_form.save(commit=False)  # Tworzy uzytkownika, nie zapisuje
            new_user.set_password(user_form.cleaned_data['password'])  # Ustala haslo
            new_user.save()  # zapisuje tutaj
            return render(request, 'account/register_done.html', {'new_user': new_user})
    else:
        user_form = UserRegistrationForm()
    return render(request, 'account/register.html', {'user_form': user_form})
