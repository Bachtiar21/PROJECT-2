from django.shortcuts import render, redirect
from prediksi.forms import PegawaiForm
from prediksi.forms import Pegawai


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
    return render(request, 'index.html', {'form': form})


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
