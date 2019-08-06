from django.db import models


# Create your models here.


class Medic(models.Model):
    medicid = models.BigAutoField(db_column='MedicID', primary_key=True)  # Field name made lowercase.
    numemedic = models.CharField(db_column='NumeMedic', max_length=45, blank=False,
                                 null=False)  # Field name made lowercase.
    prenumemedic = models.CharField(db_column='PrenumeMedic', max_length=45, blank=False,
                                    null=False)  # Field name made lowercase.
    specializare = models.CharField(db_column='Specializare', max_length=45, blank=False,
                                    null=False)  # Field name made lowercase.

    class Meta:
        ordering = ('numemedic', 'prenumemedic')
        managed = False
        db_table = 'medic'

    def __str__(self):
        nume = str(self.numemedic) + ' ' + str(self.prenumemedic) + ', ' + str(self.specializare)
        return nume


class Pacient(models.Model):
    pacientid = models.BigAutoField(db_column='PacientID', primary_key=True)  # Field name made lowercase.
    cnp = models.BigIntegerField(db_column='CNP', blank=False, null=False, unique=True)  # Field name made lowercase.
    numepacient = models.CharField(db_column='NumePacient', max_length=45, blank=False,
                                   null=False)  # Field name made lowercase.
    prenumepacient = models.CharField(db_column='PrenumePacient', max_length=45, blank=False,
                                      null=False)  # Field name made lowercase.
    adresa = models.CharField(db_column='Adresa', max_length=45, blank=False, null=False)  # Field name made lowercase.
    asigurare = models.CharField(db_column='Asigurare', max_length=45, blank=True,
                                 null=True)  # Field name made lowercase.

    class Meta:
        ordering = ('numepacient', 'prenumepacient',)
        managed = False
        db_table = 'pacient'

    def __str__(self):
        nume = str(self.numepacient) + ' ' + str(self.prenumepacient) + ', ' + str(self.cnp)
        return nume


class Medicament(models.Model):
    medicamentid = models.BigAutoField(db_column='MedicamentID', primary_key=True)  # Field name made lowercase.
    denumire = models.TextField(db_column='Denumire', blank=False, null=False)  # Field name made lowercase.

    class Meta:
        ordering = ('denumire',)
        managed = False
        db_table = 'medicament'

    def __str__(self):
        return self.denumire


class Consultatie(models.Model):
    idconsultatie = models.BigAutoField(db_column='IDConsultatie', primary_key=True)  # Field name made lowercase.
    medicid = models.ForeignKey('Medic', models.CASCADE, db_column='MedicID')  # Field name made lowercase.
    pacientid = models.ForeignKey('Pacient', models.CASCADE, db_column='PacientID')  # Field name made lowercase.
    medicamentid = models.ForeignKey('Medicament', models.CASCADE,
                                     db_column='MedicamentID')  # Field name made lowercase.
    data = models.DateField(db_column='Data', blank=False, null=False)  # Field name made lowercase.
    diagnostic = models.CharField(db_column='Diagnostic', max_length=45, blank=False,
                                  null=False)  # Field name made lowercase.
    dozamedicament = models.PositiveIntegerField(db_column='DozaMedicament', blank=True,
                                                 null=True)  # Field name made lowercase.

    class Meta:
        ordering = ('-data',)
        db_table = 'consultatie'


class Medicpacient(models.Model):
    medicid = models.ForeignKey('Medic', models.DO_NOTHING, db_column='MedicID')  # Field name m
    # ade lowercase.
    pacientid = models.ForeignKey('Pacient', models.DO_NOTHING, db_column='PacientID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'medicpacient'
        unique_together = (('medicid', 'pacientid'),)
