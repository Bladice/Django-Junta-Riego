from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.db import IntegrityError
from .forms import PersonaForm, CreaPersonaForm
from .models import Personas
from django.contrib.auth.decorators import login_required   #decorador de login requerido de django
from django.utils import timezone
from django.db.models import Q

#from django.http import HttpResponse

# Create your views here.
def home(request):
    return render(request, 'home.html')

def signup(request):
    if request.method == 'GET':
        #print('enviando formulario') #
        return render(request, 'signup.html',{
        'form': UserCreationForm
        })
    else:
        if request.POST['password1'] == request.POST['password2']:
            # registra el usuario
            try:
                user = User.objects.create_user(username = request.POST['username'], password = request.POST['password1'])
                user.save()
                login(request, User)
                return redirect('modulos')
                #return HttpResponse('user create successfully')
            except IntegrityError:
                return render(request, 'signup.html', {
                'form': UserCreationForm,
                "error": 'User already exists'
            }) #return HttpResponse('Username already exists')                
        return render(request, 'signup.html',{
            'form': UserCreationForm,
            "error": 'Password do not match'
        })
        #return HttpResponse('password do not match')

@login_required
def modulos(request):
    return render(request, 'modulos.html')

@login_required
def signout(request):
    logout(request)
    return redirect('home')

def signin(request):
    if request.method == 'GET':
        return render(request, 'signin.html', {
        'form': AuthenticationForm
        })
    else:
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            return render(request, 'signin.html', {
            'form': AuthenticationForm,
            "error": 'Username o Password incorret'
            })
        else:
            login(request, user)
            return redirect('personas')

@login_required        
def personas(request):
    query = request.GET.get('query', '')
    #nombres = request.GET.get('nombres', '')
    personas = Personas.objects.all()
    if query:
        personas = personas.filter(Q(nombres__icontains=query) | Q(cedula__icontains=query))

    #contexto ={'personas': personas}
    return render(request, 'personas.html', {'personas': personas, 'query': query})

@login_required 
def creapersona(request):
    if request.method == 'GET':
        return render(request, 'creapersona.html', {
            'form': CreaPersonaForm
        })
    else:
        try:
            form = CreaPersonaForm(request.POST)
            new_persona = form.save(commit=False)
            #new_persona.user = request.user 
            new_persona.save()
            return redirect('personas') 
                   
        except ValueError:
            return render(request, 'creapersona.html', {
            'form': CreaPersonaForm,
            'error': 'Ingrese valores validos'
        })            

@login_required   
def editpersona(request, personas_id):
    if request.method == 'GET':
        persona = get_object_or_404(Personas, pk=personas_id)
        form = CreaPersonaForm(instance=persona)
        return render(request, 'editpersona.html', {'persona': persona, 'form': form})
    else:        
        try:
            persona = get_object_or_404(Personas, pk=personas_id)
            form = CreaPersonaForm(request.POST, instance=persona)
            form.save()
            return redirect('personas')
        except ValueError:
            return render(request, 'editpersona.html', {'persona':persona, 'form': form, 'error': 'Error al actualizar Datos'})

