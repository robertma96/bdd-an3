from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('signup', views.signup, name='signup'),
    path('medic', views.medic, name='medic'),
    path('pacienti', views.pacienti, name='pacienti'),
    path('consultatie', views.consultatie, name='consultatie'),
    path('medicament', views.medicament, name='medicament'),
    path('removeMedic', views.removeMedic, name='removeMedic'),
    path('removePacient', views.removePacient, name='removePacient'),
    path('removeConsultatie', views.removeConsultatie, name='removeConsultatie'),
    path('removeMedicament', views.removeMedicament, name='removeMedicament'),
    path('modificaMedic/<int:idModif>', views.modificaMedic, name='modificaMedic'),
    path('modificaPacient/<int:idModif>', views.modificaPacient, name='modificaPacient'),
    path('modificaConsultatie/<int:idModif>', views.modificaConsultatie, name='modificaConsultatie'),
    path('modificaMedicament/<int:idModif>', views.modificaMedicament, name='modificaMedicament'),
]
