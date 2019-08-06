from django.shortcuts import render, redirect, HttpResponseRedirect
from .models import *
from .forms import MedicForm, PacientForm, ConsultatieForm, MedicamentForm, SignUpForm
from stdnum.ro import cnp
from stdnum import exceptions
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.contrib.auth.forms import UserCreationForm


# Create your views here.


def signup(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            form = SignUpForm(request.POST)
            if form.is_valid():
                form.save()
                username = form.cleaned_data.get('username')
                raw_password = form.cleaned_data.get('password1')
                user = authenticate(username=username, password=raw_password)
                login(request, user)
                return redirect('/')
        else:
            form = SignUpForm()
        return render(request, 'spital/signup.html', {'form': form})
    else:
        return render(request, 'spital/signup.html', {'message': 'Sunteti deja autentificat'})


def index(request):
    return render(request, 'spital/index.html')


@login_required(login_url='login/')
def medic(request):
    medici_list = Medic.objects.all()
    paginator = Paginator(medici_list, 10)

    page = request.GET.get('page')
    medici = paginator.get_page(page)
    if request.method == 'POST':
        form = MedicForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('medic')
    else:
        form = MedicForm()
    return render(request, 'spital/medic.html', {'medici': medici,
                                                 'form': form})


# Preluam request-ul POST si prelucram obiectul QueryDict intr-o lista
@login_required(login_url='login/')
def removeMedic(request):
    if request.user.is_superuser:
        if request.method == "POST":
            data = request.POST
            listofIDs = dict(data)['listaID[]']
            for ids in listofIDs:
                Medic.objects.filter(medicid=ids).delete()
        return redirect('medic')


@login_required(login_url='login/')
def modificaMedic(request, idModif):
    if request.user.is_superuser:
        medic_selectat = Medic.objects.get(medicid=idModif)
        if request.method == "POST":
            form = MedicForm(request.POST, instance=medic_selectat)
            if form.is_valid():
                form.save()
                return redirect('medic')
        else:
            form = MedicForm(instance=medic_selectat)
        return render(request, 'spital/modificaMedic.html', {'medic_selectat': medic_selectat,
                                                             'form': form})
    else:
        return render(request, 'spital/modificaMedic.html', {'message': 'Acces interzis!'})


@login_required(login_url='login/')
def pacienti(request):
    mesaj_validare = ''
    pacienti_list = Pacient.objects.all()
    paginator = Paginator(pacienti_list, 10)

    page = request.GET.get('page')
    pacientii = paginator.get_page(page)
    if request.method == 'POST':
        form = PacientForm(request.POST)
        if form.is_valid():
            try:
                if cnp.validate(str(form.data['cnp'])) == str(form.data['cnp']):
                    form.save()
                    return HttpResponseRedirect('/pacienti')
            except (exceptions.InvalidLength, exceptions.InvalidFormat, exceptions.InvalidChecksum):
                mesaj_validare = "CNP-ul nu a trecut validarea!"
                pass
    else:
        form = PacientForm()
    return render(request, 'spital/pacient.html', {'pacienti': pacientii,
                                                   'form': form,
                                                   'mesaj_validare': mesaj_validare})


@login_required(login_url='/login/')
def removePacient(request):
    if request.user.is_superuser:
        if request.method == "POST":
            data = request.POST
            listofIDs = dict(data)['listaID[]']
            for ids in listofIDs:
                Pacient.objects.filter(pacientid=ids).delete()
    return redirect('/pacienti')


@login_required(login_url='login/')
def modificaPacient(request, idModif):
    if request.user.is_superuser:
        mesaj_validare = ''
        pacient_selectat = Pacient.objects.get(pacientid=idModif)
        if request.method == "POST":
            form = PacientForm(request.POST, instance=pacient_selectat)
            if form.is_valid():
                try:
                    if cnp.validate(str(form.data['cnp'])) == str(form.data['cnp']):
                        form.save()
                        return redirect('/pacienti')
                except (exceptions.InvalidLength, exceptions.InvalidFormat, exceptions.InvalidChecksum):
                    mesaj_validare = "CNP-ul nu a trecut validarea!"
                    pass
        else:
            form = PacientForm(instance=pacient_selectat, )
        return render(request, 'spital/modificaPacient.html', {'pacient_selectat': pacient_selectat,
                                                               'form': form,
                                                               'mesaj_validare': mesaj_validare})
    else:
        return render(request, 'spital/modificaPacient.html', {'message': 'Acces interzis!'})


@login_required(login_url='login/')
def consultatie(request):
    consultatii_list = Consultatie.objects.all()
    paginator = Paginator(consultatii_list, 10)

    page = request.GET.get('page')
    consultatii = paginator.get_page(page)
    if request.method == 'POST':
        form = ConsultatieForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('consultatie')
    else:
        form = ConsultatieForm()
    return render(request, 'spital/consultatie.html', {'consultatii': consultatii,
                                                       'form': form})


@login_required(login_url='login/')
def removeConsultatie(request):
    if request.user.is_superuser:
        if request.method == "POST":
            data = request.POST
            listofIDs = dict(data)['listaID[]']
            for ids in listofIDs:
                Consultatie.objects.filter(idconsultatie=ids).delete()
    return redirect('consultatie')


@login_required(login_url='login/')
def modificaConsultatie(request, idModif):
    if request.user.is_superuser:
        consultatie_selectata = Consultatie.objects.get(idconsultatie=idModif)
        if request.method == "POST":
            form = ConsultatieForm(request.POST, instance=consultatie_selectata)
            if form.is_valid():
                form.save()
                return redirect('consultatie')
        else:
            form = ConsultatieForm(instance=consultatie_selectata)
        return render(request, 'spital/modificaConsultatie.html', {'consultatie_selectata': consultatie_selectata,
                                                                   'form': form})
    else:
        return render(request, 'spital/modificaConsultatie.html', {'message': 'Acces interzis!'})


@login_required(login_url='login/')
def medicament(request):
    medicamente_list = Medicament.objects.all()
    paginator = Paginator(medicamente_list, 10)

    page = request.GET.get('page')
    medicamente = paginator.get_page(page)
    if request.method == 'POST':
        form = MedicamentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('medicament')
    else:
        form = MedicamentForm()
    return render(request, 'spital/medicament.html', {'medicamente': medicamente,
                                                      'form': form})


@login_required(login_url='login/')
def removeMedicament(request):
    if request.user.is_superuser:
        if request.method == "POST":
            data = request.POST
            listofIDs = dict(data)['listaID[]']
            for ids in listofIDs:
                Medicament.objects.filter(medicamentid=ids).delete()
    return redirect('medicament')


@login_required(login_url='login/')
def modificaMedicament(request, idModif):
    if request.user.is_superuser:
        medicament_selectat = Medicament.objects.get(medicamentid=idModif)
        if request.method == "POST":
            form = MedicamentForm(request.POST, instance=medicament_selectat)
            if form.is_valid():
                form.save()
                return redirect('medicament')
        else:
            form = MedicamentForm(instance=medicament_selectat)
        return render(request, 'spital/modificaMedicament.html', {'medicament_selectat': medicament_selectat,
                                                                  'form': form})
    else:
        return render(request, 'spital/modificaMedicament.html', {'message': 'Acces interzis!'})
