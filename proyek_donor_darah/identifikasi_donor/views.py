from django.shortcuts import render
from django.http import JsonResponse
from .forms import FormIdentifikasiDonor
import joblib
import numpy as np

def beranda(request):
    return render(request, 'identifikasi_donor/beranda.html')

def tentang(request):
    return render(request, 'identifikasi_donor/tentang.html')

def identifikasi(request):
    if request.method == 'POST':
        form = FormIdentifikasiDonor(request.POST)
        if form.is_valid():
            # Load model dan scaler
            model = joblib.load('best_model.pkl')
            scaler = joblib.load('scaler.pkl')
            
            # Siapkan data input
            input_data = np.array([[
                form.cleaned_data['age'],
                form.cleaned_data['hemoglobin'],
                form.cleaned_data['weight'],
                form.cleaned_data['systolic'],
                form.cleaned_data['diastolic']
            ]])
            
            # Normalisasi input data
            input_scaled = scaler.transform(input_data)
            
            # Buat prediksi
            prediksi = model.predict(input_scaled)[0]
            hasil_prediksi = "Layak" if prediksi == 1 else "Tidak Layak"
            icon = "success" if prediksi == 1 else "warning"
            
            if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
                return JsonResponse({
                    'prediksi': hasil_prediksi,
                    'icon': icon
                })
            else:
                return render(request, 'identifikasi_donor/identifikasi.html', {
                    'form': form,
                    'prediksi': hasil_prediksi
                })
    else:
        form = FormIdentifikasiDonor()
    return render(request, 'identifikasi_donor/identifikasi.html', {'form': form})