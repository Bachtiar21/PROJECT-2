from django.shortcuts import render, redirect
import pandas as pd
import pickle
from prediksi.forms import PegawaiForm
from prediksi.forms import Pegawai
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
    context = {'a': 1}
    return render(request, 'index.html', context)

# our result page view


def result(request):
    print(request)
    Age = float(request.POST.get('Age'))
    JobLevel = int(request.POST.get('JobLevel'))
    TotalWorkingYears = int(request.POST.get('TotalWorkingYears'))
    YearsAtCompany = int(request.POST.get('YearsAtCompany'))

    model = pd.read_pickle('./models/model3.pickle')
    result = model.predict([[Age,JobLevel,TotalWorkingYears,YearsAtCompany]])

    return render(request, 'result.html', {'result': result})


def predict(request):
    context={'a':1}
    return render(request, 'predict.html', context)

def data(request):
    return render(request, 'data.html')


def visualisasi(request):
    return render(request, 'visualisasi.html')


def pgw(request):
    if request.method == "POST":
        form = PegawaiForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('/view')
            except:
                pass
    else:
        form = PegawaiForm()
    return render(request, 'haltambah.html', {'form': form})


def view(request):
    pegawai = Pegawai.objects.all()
    return render(request, "view.html", {'pegawai': pegawai})


def delete(request, id):
    pegawai = Pegawai.objects.get(id=id)
    pegawai.delete()
    return redirect("/view")


def edit(request, id):
    pegawai = Pegawai.objects.get(id=id)
    return render(request, 'edit.html', {'pegawai': pegawai})


def update(request, id):
    pegawai = Pegawai.objects.get(id=id)
    form = PegawaiForm(instance=pegawai)

    if request.method == 'POST':
        form = PegawaiForm(request.POST, instance=pegawai)
        if form.is_valid():
            form.save()
            return redirect('/view')

    return render(request, 'view.html', {'form': form})


def indexView(request):
    return render(request, 'index.html')


@login_required
def dashboardView(request):
    return render(request, 'dashboard.html')


def registerView(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login_url')
    else:
        form = UserCreationForm()

    return render(request, 'registration/register.html', {'form': form})
