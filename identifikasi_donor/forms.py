from django import forms

class FormIdentifikasiDonor(forms.Form):
    age = forms.IntegerField(label='Usia')
    hemoglobin = forms.FloatField(label='Hemoglobin')
    weight = forms.FloatField(label='Berat Badan')
    systolic = forms.IntegerField(label='Tekanan Darah Sistolik')
    diastolic = forms.IntegerField(label='Tekanan Darah Diastolik')