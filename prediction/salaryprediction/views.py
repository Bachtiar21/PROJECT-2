from django.shortcuts import render, redirect
import pandas as pd
import pickle

from salaryprediction.forms import PegawaiForm
from salaryprediction.models import Pegawai

# Create your views here.
def index(request):
    context={'a':1}
    return render(request, 'index.html', context)

# our result page view
def result(request):
    print(request)
    tahun = float(request.POST.get('tahun'))

    model = pd.read_pickle('./models/model3.pickle')
    result = model.predict([[tahun]])

    return render(request, 'result.html', {'result':result})

def data(request):
    return render(request, 'data.html')

def visualisasi(request):
    return render(request, 'visualisasi.html')

def pegawai(request):
    if request.method == 'POST':
        form = PegawaiForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('/view')
            except:
                pass
    else:
        form = PegawaiForm()
        return render(request,'tambah.html',{'form':form})