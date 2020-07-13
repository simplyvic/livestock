from django.db import models
from datetime import datetime, date

# Create your models here.
class Approver(models.Model):
    name = models.CharField(max_length=30, blank=True) 
    def __unicode__(self):
       return self.name

class Quarter(models.Model):
    name = models.CharField(max_length=30, blank=True) 
    def __unicode__(self):
       return self.name

class Region(models.Model):
    name = models.CharField(max_length=30, blank=True) 
    def __unicode__(self):
       return self.name

class Species(models.Model):
    name = models.CharField(max_length=30, blank=True) 
    def __unicode__(self):
       return self.name

class SpeciesBreed(models.Model):
    name = models.CharField(max_length=30, blank=True) 
    def __unicode__(self):
       return self.name

class Localty(models.Model):
    code = models.CharField(max_length=30, blank=True) 
    short_name = models.CharField(max_length=30, blank=True) 
    full_name = models.CharField(max_length=30, blank=True) 
    def __unicode__(self):
       return self.code + ' ' + self.short_name + ' ' + self.full_name

class PrincipalSign(models.Model):
    name = models.CharField(max_length=30, blank=True) 
    def __unicode__(self):
       return self.name

class ClinicalDiagnosis(models.Model):
    code = models.CharField(max_length=30, blank=True) 
    name = models.CharField(max_length=30, blank=True) 
    def __unicode__(self):
       return self.code + ' ' + self.name

class DiseaseCode(models.Model):
    code = models.CharField(max_length=30, blank=True) 
    name = models.CharField(max_length=30, blank=True) 
    def __unicode__(self):
       return self.code + ' ' + self.name

class ControlMeasures(models.Model):
    name = models.CharField(max_length=30, blank=True) 
    def __unicode__(self):
       return self.name

class VaccinationHistory(models.Model):
    code = models.CharField(max_length=30, blank=True) 
    short_name = models.CharField(max_length=30, blank=True) 
    full_name = models.CharField(max_length=30, blank=True) 
    def __unicode__(self):
       return self.code + ' ' + self.short_name + ' ' + self.full_name

class SampleType(models.Model):
    name = models.CharField(max_length=30, blank=True) 
    def __unicode__(self):
       return self.name

class General(models.Model):
    sex_choice = (
            ('Male', 'Male'),
            ('Female', 'Female'),
        )

    clinical_prognosis_choice = (
            ('Good', 'Good'),
            ('Poor', 'Poor'),
        )

    approval_choice = (
            ('Approve', 'Approve'),
            ('Disapprove', 'Disapprove'),
        )

    notification_frequency_choice = (
            ('Immediate Frequecy', 'Immediate Frequecy'),
            ('Weekly Frequecy', 'Weekly Frequecy'),
            ('Bi-Weekly Frequecy', 'Bi-Weekly Frequecy'),
            ('Monthly Frequecy', 'Monthly Frequecy'),
        )

    sample_type_choice = (
            ('Swabs', 'Swabs'),
            ('LymphNode', 'LymphNode'),
            ('Organ-kidney', 'Organ-Kidney'),
            ('Organ-Lungs', 'Organ-Lungs'),
            ('Organ-Intestine', 'Organ-Intestine'),
            ('Organ-Heart', 'Organ-Heart'),
            ('Organ-Trachea', 'Organ-Trachea'),
            ('Organ-Esophagus', 'Organ-Esophagus'),
            ('Organ-Brain', 'Organ-Brain'),
        )

    lap_test_applied_choice = (
            ('cELISA', 'cELISA'),
            ('PCR', 'PCR'),
            ('Realtime PCR', 'Realtime PCR'),
            ('Cultures', 'Cultures'),
            ('Haematology', 'Haematology'),
            ('Smears', 'Smears'),
            ('Parasitology', 'Parasitology'),
            ('IFAT', 'IFAT'),
        )

    lab_test_results_choice = (
            ('Positive', 'Positive'),
            ('Negative', 'Negative'),
        )

    surveillance_type_choice = (
            ('Active', 'Active'),
            ('Passive', 'Passive'),
        )

class Clinical(models.Model):
    employee = models.CharField(max_length=30, blank=True)
    date = models.DateField(auto_now_add=False, auto_now=False, blank=True, null=True)
    quarter = models.ForeignKey(Quarter, blank=True, null=True)
    clinical_name = models.CharField(max_length=30, blank=True, null=True)
    region = models.ForeignKey(Region, blank=True, null=True)
    species = models.ForeignKey(Species, blank=True, null=True)
    species_breed = models.ForeignKey(SpeciesBreed, blank=True, null=True)
    specie_sex = models.CharField(max_length=30, blank=True, null=True, choices=General.sex_choice)
    owner_name = models.CharField(max_length=30, blank=True, null=True)
    owner_contact_no = models.CharField(max_length=30, blank=True, null=True)
    owner_gender = models.CharField(max_length=30, blank=True, null=True, choices=General.sex_choice)
    localty = models.ForeignKey(Localty, blank=True, null=True)
    localty_longitude = models.CharField(max_length=30, blank=True)
    localty_latitude = models.CharField(max_length=30, blank=True)
    animal_group_size = models.CharField(max_length=30, blank=True)
    animalID = models.CharField(max_length=30, blank=True)
    pet_name = models.CharField(max_length=30, blank=True)
    animal_live_weight = models.CharField('Animal live weight (KG)', max_length=30, blank=True)
    anamnesis = models.CharField(max_length=30, blank=True)
    principal_signs = models.ForeignKey(PrincipalSign, blank=True, null=True)
    clinical_diagnosis = models.ForeignKey(ClinicalDiagnosis, blank=True, null=True)
    clinical_prognosis = models.CharField(max_length=30, blank=True, null=True, choices=General.clinical_prognosis_choice)
    timestamp = models.DateField(auto_now_add=True, auto_now=False, blank=True)
    approve_one = models.CharField(max_length=30, blank=True, null=True, choices=General.approval_choice)
    approve_two = models.CharField(max_length=30, blank=True, null=True, choices=General.approval_choice)
    export_to_CSV = models.BooleanField(default=False)
    def __unicode__(self):
       return str(self.owner_name) + str(self.species)


class DiseaseReport(models.Model):
    surveillance_type = models.CharField(max_length=30, blank=True, null=True, choices=General.surveillance_type_choice)
    employee = models.CharField(max_length=30, blank=True)
    new_outbreak = models.BooleanField(default=False)
    date = models.DateField(auto_now_add=False, auto_now=False, blank=True, null=True)
    reporter_name = models.CharField(max_length=30, blank=True, null=True)
    start_date = models.DateField(auto_now_add=False, auto_now=False, blank=True, null=True)
    end_date = models.DateField(auto_now_add=False, auto_now=False, blank=True, null=True)
    quarter = models.ForeignKey(Quarter, blank=True, null=True)
    month = models.DateField(auto_now_add=False, auto_now=False, blank=True, null=True)
    year = models.DateField(auto_now_add=False, auto_now=False, blank=True, null=True)
    localty = models.ForeignKey(Localty, blank=True, null=True)
    localty_longitude = models.CharField(max_length=30, blank=True)
    localty_latitude = models.CharField(max_length=30, blank=True)
    owner_name = models.CharField(max_length=30, blank=True, null=True)
    owner_contact_no = models.CharField(max_length=30, blank=True, null=True)
    owner_nin_no = models.CharField(max_length=30, blank=True, null=True)
    owner_gender = models.CharField(max_length=30, blank=True, null=True, choices=General.sex_choice)
    
    species = models.ForeignKey(Species, blank=True, null=True)
    species_breed = models.ForeignKey(SpeciesBreed, blank=True, null=True)
    specie_sex = models.CharField(max_length=30, blank=True, null=True, choices=General.sex_choice)
    specie_age = models.CharField(max_length=30, blank=True)
    animalID = models.CharField(max_length=30, blank=True)
    pet_name = models.CharField(max_length=30, blank=True)
    animal_group_size= models.CharField(max_length=30, blank=True)
    principal_signs = models.ForeignKey(PrincipalSign, blank=True, null=True)
    clinical_diagnosis = models.ForeignKey(ClinicalDiagnosis, blank=True, null=True)
    disease_code = models.ForeignKey(DiseaseCode, blank=True, null=True)
    clinical_prognosis = models.CharField(max_length=30, blank=True, null=True, choices=General.clinical_prognosis_choice)
    vaccination_history = models.ForeignKey(VaccinationHistory, blank=True, null=True)
    notifiable_disease = models.BooleanField(default=False)
    timestamp = models.DateField(auto_now_add=True, auto_now=False, blank=True)
    owner_gender = models.CharField(max_length=30, blank=True, null=True, choices=General.sex_choice)
    notification_frequency = models.CharField(max_length=30, blank=True, null=True, choices=General.notification_frequency_choice)
    zoonosis = models.BooleanField(default=False)
    no_of_cases = models.CharField(max_length=30, blank=True, null=True)
    no_of_deaths = models.CharField(max_length=30, blank=True, null=True)
    no_destroyed = models.CharField(max_length=30, blank=True, null=True)
    incedence_rate= models.CharField(max_length=30, blank=True, null=True)
    motality_rate= models.CharField(max_length=30, blank=True, null=True)
    mobidity_rate= models.CharField(max_length=30, blank=True, null=True)
    lab_sample_collected = models.BooleanField(default=False)
    sample_type = models.CharField(max_length=30, blank=True, null=True, choices=General.sample_type_choice)
    sample_ID= models.CharField(max_length=30, blank=True, null=True)
    lab_test_applied= models.CharField(max_length=30, blank=True, null=True, choices=General.lap_test_applied_choice)
    lab_test_results= models.CharField(max_length=30, blank=True, null=True, choices=General.lab_test_results_choice)
    control_measures= models.ForeignKey(ControlMeasures, blank=True, null=True)
    approve_one = models.CharField(max_length=30, blank=True, null=True, choices=General.approval_choice)
    approve_two = models.CharField(max_length=30, blank=True, null=True, choices=General.approval_choice)

    def __unicode__(self):
       return str(self.owner_name) + ' - ' + str(self.species)




class Lab(models.Model):
    surveillance_type = models.CharField(max_length=30, blank=True, null=True, choices=General.surveillance_type_choice)
    employee = models.CharField(max_length=30, blank=True)
    new_outbreak = models.BooleanField(default=False)
    date = models.DateField(auto_now_add=False, auto_now=False, blank=True, null=True)
    reporter_name = models.CharField(max_length=30, blank=True, null=True)
    start_date = models.DateField(auto_now_add=False, auto_now=False, blank=True, null=True)
    end_date = models.DateField(auto_now_add=False, auto_now=False, blank=True, null=True)
    quarter = models.ForeignKey(Quarter, blank=True, null=True)
    month = models.DateField(auto_now_add=False, auto_now=False, blank=True, null=True)
    year = models.DateField(auto_now_add=False, auto_now=False, blank=True, null=True)
    localty = models.ForeignKey(Localty, blank=True, null=True)
    localty_longitude = models.CharField(max_length=30, blank=True)
    localty_latitude = models.CharField(max_length=30, blank=True)
    owner_name = models.CharField(max_length=30, blank=True, null=True)
    owner_contact_no = models.CharField(max_length=30, blank=True, null=True)
    owner_nin_no = models.CharField(max_length=30, blank=True, null=True)
    owner_gender = models.CharField(max_length=30, blank=True, null=True, choices=General.sex_choice)
    
    species = models.ForeignKey(Species, blank=True, null=True)
    species_breed = models.ForeignKey(SpeciesBreed, blank=True, null=True)
    specie_sex = models.CharField(max_length=30, blank=True, null=True, choices=General.sex_choice)
    specie_age = models.CharField(max_length=30, blank=True)
    animalID = models.CharField(max_length=30, blank=True)
    pet_name = models.CharField(max_length=30, blank=True)
    animal_group_size= models.CharField(max_length=30, blank=True)
    principal_signs = models.ForeignKey(PrincipalSign, blank=True, null=True)
    clinical_diagnosis = models.ForeignKey(ClinicalDiagnosis, blank=True, null=True)
    disease_code = models.ForeignKey(DiseaseCode, blank=True, null=True)
    clinical_prognosis = models.CharField(max_length=30, blank=True, null=True, choices=General.clinical_prognosis_choice)
    vaccination_history = models.ForeignKey(VaccinationHistory, blank=True, null=True)
    notifiable_disease = models.BooleanField(default=False)
    timestamp = models.DateField(auto_now_add=True, auto_now=False, blank=True)
    owner_gender = models.CharField(max_length=30, blank=True, null=True, choices=General.sex_choice)
    
    incedence_rate= models.CharField(max_length=30, blank=True, null=True)
    analysis_date = models.CharField(max_length=30, blank=True, null=True, choices=General.clinical_prognosis_choice)
    lab_sample_collected = models.BooleanField(default=False)
    sample_type = models.CharField(max_length=30, blank=True, null=True, choices=General.sample_type_choice)
    sample_ID= models.CharField(max_length=30, blank=True, null=True)
    lab_test_applied= models.CharField(max_length=30, blank=True, null=True, choices=General.lap_test_applied_choice)
    lab_test_results= models.CharField(max_length=30, blank=True, null=True, choices=General.lab_test_results_choice)
    approve_one = models.CharField(max_length=30, blank=True, null=True, choices=General.approval_choice)
    approve_two = models.CharField(max_length=30, blank=True, null=True, choices=General.approval_choice)
    
    def __unicode__(self):
       return str(self.owner_name) + ' - ' + str(self.species)


class Abattoir(models.Model):
    surveillance_type = models.CharField(max_length=30, blank=True, null=True, choices=General.surveillance_type_choice)
    employee = models.CharField(max_length=30, blank=True)
    new_outbreak = models.BooleanField(default=False)
    date = models.DateField(auto_now_add=False, auto_now=False, blank=True, null=True)
    reporter_name = models.CharField(max_length=30, blank=True, null=True)
    start_date = models.DateField(auto_now_add=False, auto_now=False, blank=True, null=True)
    end_date = models.DateField(auto_now_add=False, auto_now=False, blank=True, null=True)
    quarter = models.ForeignKey(Quarter, blank=True, null=True)
    month = models.DateField(auto_now_add=False, auto_now=False, blank=True, null=True)
    year = models.DateField(auto_now_add=False, auto_now=False, blank=True, null=True)
    localty = models.ForeignKey(Localty, blank=True, null=True)
    localty_longitude = models.CharField(max_length=30, blank=True)
    localty_latitude = models.CharField(max_length=30, blank=True)
    owner_name = models.CharField(max_length=30, blank=True, null=True)
    owner_contact_no = models.CharField(max_length=30, blank=True, null=True)
    owner_nin_no = models.CharField(max_length=30, blank=True, null=True)
    owner_gender = models.CharField(max_length=30, blank=True, null=True, choices=General.sex_choice)
    species = models.ForeignKey(Species, blank=True, null=True)
    species_breed = models.ForeignKey(SpeciesBreed, blank=True, null=True)
    specie_sex = models.CharField(max_length=30, blank=True, null=True, choices=General.sex_choice)
    specie_age = models.CharField(max_length=30, blank=True)
    animalID = models.CharField(max_length=30, blank=True)
    pet_name = models.CharField(max_length=30, blank=True)
    animal_group_size= models.CharField(max_length=30, blank=True)
    principal_signs = models.ForeignKey(PrincipalSign, blank=True, null=True)
    clinical_diagnosis = models.ForeignKey(ClinicalDiagnosis, blank=True, null=True)
    disease_code = models.ForeignKey(DiseaseCode, blank=True, null=True)
    clinical_prognosis = models.CharField(max_length=30, blank=True, null=True, choices=General.clinical_prognosis_choice)
    vaccination_history = models.ForeignKey(VaccinationHistory, blank=True, null=True)
    notifiable_disease = models.BooleanField(default=False)
    timestamp = models.DateField(auto_now_add=True, auto_now=False, blank=True)
    owner_gender = models.CharField(max_length=30, blank=True, null=True, choices=General.sex_choice)
    notification_frequency = models.CharField(max_length=30, blank=True, null=True, choices=General.notification_frequency_choice)
    incedence_rate= models.CharField(max_length=30, blank=True, null=True)
    motality_rate= models.CharField(max_length=30, blank=True, null=True)
    mobidity_rate= models.CharField(max_length=30, blank=True, null=True)
    lab_sample_collected = models.BooleanField(default=False)
    sample_type = models.CharField(max_length=30, blank=True, null=True, choices=General.sample_type_choice)
    sample_ID= models.CharField(max_length=30, blank=True, null=True)
    lab_test_applied= models.CharField(max_length=30, blank=True, null=True, choices=General.lap_test_applied_choice)
    lab_test_results= models.CharField(max_length=30, blank=True, null=True, choices=General.lab_test_results_choice)
    control_measures= models.ForeignKey(ControlMeasures, blank=True, null=True)
    approve_one = models.CharField(max_length=30, blank=True, null=True, choices=General.approval_choice)
    approve_two = models.CharField(max_length=30, blank=True, null=True, choices=General.approval_choice)
    
    def __unicode__(self):
       return str(self.owner_name) + ' - ' + str(self.species)


class Locality(models.Model):
    surveillance_type = models.CharField(max_length=30, blank=True, null=True, choices=General.surveillance_type_choice)
    employee = models.CharField(max_length=30, blank=True)
    new_outbreak = models.BooleanField(default=False)
    date = models.DateField(auto_now_add=False, auto_now=False, blank=True, null=True)
    reporter_name = models.CharField(max_length=30, blank=True, null=True)
    start_date = models.DateField(auto_now_add=False, auto_now=False, blank=True, null=True)
    end_date = models.DateField(auto_now_add=False, auto_now=False, blank=True, null=True)
    quarter = models.ForeignKey(Quarter, blank=True, null=True)
    month = models.DateField(auto_now_add=False, auto_now=False, blank=True, null=True)
    year = models.DateField(auto_now_add=False, auto_now=False, blank=True, null=True)
    localty = models.ForeignKey(Localty, blank=True, null=True)
    localty_longitude = models.CharField(max_length=30, blank=True)
    localty_latitude = models.CharField(max_length=30, blank=True)
    owner_name = models.CharField(max_length=30, blank=True, null=True)
    owner_contact_no = models.CharField(max_length=30, blank=True, null=True)
    owner_nin_no = models.CharField(max_length=30, blank=True, null=True)
    owner_gender = models.CharField(max_length=30, blank=True, null=True, choices=General.sex_choice)
    species = models.ForeignKey(Species, blank=True, null=True)
    species_breed = models.ForeignKey(SpeciesBreed, blank=True, null=True)
    specie_sex = models.CharField(max_length=30, blank=True, null=True, choices=General.sex_choice)
    specie_age = models.CharField(max_length=30, blank=True)
    animalID = models.CharField(max_length=30, blank=True)
    pet_name = models.CharField(max_length=30, blank=True)
    animal_group_size= models.CharField(max_length=30, blank=True)
    principal_signs = models.ForeignKey(PrincipalSign, blank=True, null=True)
    clinical_diagnosis = models.ForeignKey(ClinicalDiagnosis, blank=True, null=True)
    disease_code = models.ForeignKey(DiseaseCode, blank=True, null=True)
    clinical_prognosis = models.CharField(max_length=30, blank=True, null=True, choices=General.clinical_prognosis_choice)
    vaccination_history = models.ForeignKey(VaccinationHistory, blank=True, null=True)
    notifiable_disease = models.BooleanField(default=False)
    timestamp = models.DateField(auto_now_add=True, auto_now=False, blank=True)
    owner_gender = models.CharField(max_length=30, blank=True, null=True, choices=General.sex_choice)
    notification_frequency = models.CharField(max_length=30, blank=True, null=True, choices=General.notification_frequency_choice)
    incedence_rate= models.CharField(max_length=30, blank=True, null=True)
    motality_rate= models.CharField(max_length=30, blank=True, null=True)
    mobidity_rate= models.CharField(max_length=30, blank=True, null=True)
    lab_sample_collected = models.BooleanField(default=False)
    sample_type = models.CharField(max_length=30, blank=True, null=True, choices=General.sample_type_choice)
    sample_ID= models.CharField(max_length=30, blank=True, null=True)
    lab_test_applied= models.CharField(max_length=30, blank=True, null=True, choices=General.lap_test_applied_choice)
    lab_test_results= models.CharField(max_length=30, blank=True, null=True, choices=General.lab_test_results_choice)
    control_measures= models.ForeignKey(ControlMeasures, blank=True, null=True)
    approve_one = models.CharField(max_length=30, blank=True, null=True, choices=General.approval_choice)
    approve_two = models.CharField(max_length=30, blank=True, null=True, choices=General.approval_choice)
    
    def __unicode__(self):
       return str(self.owner_name) + ' - ' + str(self.species)



class Vaccination(models.Model):
    surveillance_type = models.CharField(max_length=30, blank=True, null=True, choices=General.surveillance_type_choice)
    employee = models.CharField(max_length=30, blank=True)
    new_outbreak = models.BooleanField(default=False)
    date = models.DateField(auto_now_add=False, auto_now=False, blank=True, null=True)
    reporter_name = models.CharField(max_length=30, blank=True, null=True)
    start_date = models.DateField(auto_now_add=False, auto_now=False, blank=True, null=True)
    end_date = models.DateField(auto_now_add=False, auto_now=False, blank=True, null=True)
    quarter = models.ForeignKey(Quarter, blank=True, null=True)
    month = models.DateField(auto_now_add=False, auto_now=False, blank=True, null=True)
    year = models.DateField(auto_now_add=False, auto_now=False, blank=True, null=True)
    localty = models.ForeignKey(Localty, blank=True, null=True)
    localty_longitude = models.CharField(max_length=30, blank=True)
    localty_latitude = models.CharField(max_length=30, blank=True)
    owner_name = models.CharField(max_length=30, blank=True, null=True)
    owner_contact_no = models.CharField(max_length=30, blank=True, null=True)
    owner_nin_no = models.CharField(max_length=30, blank=True, null=True)
    owner_gender = models.CharField(max_length=30, blank=True, null=True, choices=General.sex_choice)
    species = models.ForeignKey(Species, blank=True, null=True)
    species_breed = models.ForeignKey(SpeciesBreed, blank=True, null=True)
    specie_sex = models.CharField(max_length=30, blank=True, null=True, choices=General.sex_choice)
    specie_age = models.CharField(max_length=30, blank=True)
    animalID = models.CharField(max_length=30, blank=True)
    pet_name = models.CharField(max_length=30, blank=True)
    animal_group_size= models.CharField(max_length=30, blank=True)
    principal_signs = models.ForeignKey(PrincipalSign, blank=True, null=True)
    clinical_diagnosis = models.ForeignKey(ClinicalDiagnosis, blank=True, null=True)
    disease_code = models.ForeignKey(DiseaseCode, blank=True, null=True)
    clinical_prognosis = models.CharField(max_length=30, blank=True, null=True, choices=General.clinical_prognosis_choice)
    vaccination_history = models.ForeignKey(VaccinationHistory, blank=True, null=True)
    notifiable_disease = models.BooleanField(default=False)
    timestamp = models.DateField(auto_now_add=True, auto_now=False, blank=True)
    owner_gender = models.CharField(max_length=30, blank=True, null=True, choices=General.sex_choice)
    notification_frequency = models.CharField(max_length=30, blank=True, null=True, choices=General.notification_frequency_choice)
    incedence_rate= models.CharField(max_length=30, blank=True, null=True)
    motality_rate= models.CharField(max_length=30, blank=True, null=True)
    mobidity_rate= models.CharField(max_length=30, blank=True, null=True)
    lab_sample_collected = models.BooleanField(default=False)
    sample_type = models.CharField(max_length=30, blank=True, null=True, choices=General.sample_type_choice)
    sample_ID= models.CharField(max_length=30, blank=True, null=True)
    lab_test_applied= models.CharField(max_length=30, blank=True, null=True, choices=General.lap_test_applied_choice)
    lab_test_results= models.CharField(max_length=30, blank=True, null=True, choices=General.lab_test_results_choice)
    control_measures= models.ForeignKey(ControlMeasures, blank=True, null=True)
    approve_one = models.CharField(max_length=30, blank=True, null=True, choices=General.approval_choice)
    approve_two = models.CharField(max_length=30, blank=True, null=True, choices=General.approval_choice)
    
    def __unicode__(self):
       return str(self.owner_name) + ' - ' + str(self.species)


class VetInfraIndustry(models.Model):
    employee = models.CharField(max_length=30, blank=True)
    new_outbreak = models.BooleanField(default=False)
    date = models.DateField(auto_now_add=False, auto_now=False, blank=True, null=True)
    reporter_name = models.CharField(max_length=30, blank=True, null=True)
    start_date = models.DateField(auto_now_add=False, auto_now=False, blank=True, null=True)
    end_date = models.DateField(auto_now_add=False, auto_now=False, blank=True, null=True)
    quarter = models.ForeignKey(Quarter, blank=True, null=True)
    month = models.DateField(auto_now_add=False, auto_now=False, blank=True, null=True)
    year = models.DateField(auto_now_add=False, auto_now=False, blank=True, null=True)
    localty = models.ForeignKey(Localty, blank=True, null=True)
    localty_longitude = models.CharField(max_length=30, blank=True)
    localty_latitude = models.CharField(max_length=30, blank=True)
    owner_name = models.CharField(max_length=30, blank=True, null=True)
    owner_contact_no = models.CharField(max_length=30, blank=True, null=True)
    owner_nin_no = models.CharField(max_length=30, blank=True, null=True)
    owner_gender = models.CharField(max_length=30, blank=True, null=True, choices=General.sex_choice)
    species = models.ForeignKey(Species, blank=True, null=True)
    species_breed = models.ForeignKey(SpeciesBreed, blank=True, null=True)
    specie_sex = models.CharField(max_length=30, blank=True, null=True, choices=General.sex_choice)
    specie_age = models.CharField(max_length=30, blank=True)
    animalID = models.CharField(max_length=30, blank=True)
    pet_name = models.CharField(max_length=30, blank=True)
    animal_group_size= models.CharField(max_length=30, blank=True)
    principal_signs = models.ForeignKey(PrincipalSign, blank=True, null=True)
    clinical_diagnosis = models.ForeignKey(ClinicalDiagnosis, blank=True, null=True)
    disease_code = models.ForeignKey(DiseaseCode, blank=True, null=True)
    clinical_prognosis = models.CharField(max_length=30, blank=True, null=True, choices=General.clinical_prognosis_choice)
    vaccination_history = models.ForeignKey(VaccinationHistory, blank=True, null=True)
    notifiable_disease = models.BooleanField(default=False)
    timestamp = models.DateField(auto_now_add=True, auto_now=False, blank=True)
    owner_gender = models.CharField(max_length=30, blank=True, null=True, choices=General.sex_choice)
    notification_frequency = models.CharField(max_length=30, blank=True, null=True, choices=General.notification_frequency_choice)
    incedence_rate= models.CharField(max_length=30, blank=True, null=True)
    motality_rate= models.CharField(max_length=30, blank=True, null=True)
    mobidity_rate= models.CharField(max_length=30, blank=True, null=True)
    lab_sample_collected = models.BooleanField(default=False)
    sample_type = models.CharField(max_length=30, blank=True, null=True, choices=General.sample_type_choice)
    sample_ID= models.CharField(max_length=30, blank=True, null=True)
    lab_test_applied= models.CharField(max_length=30, blank=True, null=True, choices=General.lap_test_applied_choice)
    lab_test_results= models.CharField(max_length=30, blank=True, null=True, choices=General.lab_test_results_choice)
    control_measures= models.ForeignKey(ControlMeasures, blank=True, null=True)
    approve_one = models.CharField(max_length=30, blank=True, null=True, choices=General.approval_choice)
    approve_two = models.CharField(max_length=30, blank=True, null=True, choices=General.approval_choice)
    
    def __unicode__(self):
       return str(self.owner_name) + ' - ' + str(self.species)


class Permits(models.Model):
    employee = models.CharField(max_length=30, blank=True)
    new_outbreak = models.BooleanField(default=False)
    date = models.DateField(auto_now_add=False, auto_now=False, blank=True, null=True)
    reporter_name = models.CharField(max_length=30, blank=True, null=True)
    start_date = models.DateField(auto_now_add=False, auto_now=False, blank=True, null=True)
    end_date = models.DateField(auto_now_add=False, auto_now=False, blank=True, null=True)
    quarter = models.ForeignKey(Quarter, blank=True, null=True)
    month = models.DateField(auto_now_add=False, auto_now=False, blank=True, null=True)
    year = models.DateField(auto_now_add=False, auto_now=False, blank=True, null=True)
    localty = models.ForeignKey(Localty, blank=True, null=True)
    localty_longitude = models.CharField(max_length=30, blank=True)
    localty_latitude = models.CharField(max_length=30, blank=True)
    owner_name = models.CharField(max_length=30, blank=True, null=True)
    owner_contact_no = models.CharField(max_length=30, blank=True, null=True)
    owner_nin_no = models.CharField(max_length=30, blank=True, null=True)
    owner_gender = models.CharField(max_length=30, blank=True, null=True, choices=General.sex_choice)
    species = models.ForeignKey(Species, blank=True, null=True)
    species_breed = models.ForeignKey(SpeciesBreed, blank=True, null=True)
    specie_sex = models.CharField(max_length=30, blank=True, null=True, choices=General.sex_choice)
    specie_age = models.CharField(max_length=30, blank=True)
    animalID = models.CharField(max_length=30, blank=True)
    pet_name = models.CharField(max_length=30, blank=True)
    animal_group_size= models.CharField(max_length=30, blank=True)
    principal_signs = models.ForeignKey(PrincipalSign, blank=True, null=True)
    clinical_diagnosis = models.ForeignKey(ClinicalDiagnosis, blank=True, null=True)
    disease_code = models.ForeignKey(DiseaseCode, blank=True, null=True)
    clinical_prognosis = models.CharField(max_length=30, blank=True, null=True, choices=General.clinical_prognosis_choice)
    vaccination_history = models.ForeignKey(VaccinationHistory, blank=True, null=True)
    notifiable_disease = models.BooleanField(default=False)
    timestamp = models.DateField(auto_now_add=True, auto_now=False, blank=True)
    owner_gender = models.CharField(max_length=30, blank=True, null=True, choices=General.sex_choice)
    notification_frequency = models.CharField(max_length=30, blank=True, null=True, choices=General.notification_frequency_choice)
    incedence_rate= models.CharField(max_length=30, blank=True, null=True)
    motality_rate= models.CharField(max_length=30, blank=True, null=True)
    mobidity_rate= models.CharField(max_length=30, blank=True, null=True)
    lab_sample_collected = models.BooleanField(default=False)
    sample_type = models.CharField(max_length=30, blank=True, null=True, choices=General.sample_type_choice)
    sample_ID= models.CharField(max_length=30, blank=True, null=True)
    lab_test_applied= models.CharField(max_length=30, blank=True, null=True, choices=General.lap_test_applied_choice)
    lab_test_results= models.CharField(max_length=30, blank=True, null=True, choices=General.lab_test_results_choice)
    control_measures= models.ForeignKey(ControlMeasures, blank=True, null=True)
    approve_one = models.CharField(max_length=30, blank=True, null=True, choices=General.approval_choice)
    approve_two = models.CharField(max_length=30, blank=True, null=True, choices=General.approval_choice)
    
    def __unicode__(self):
       return str(self.owner_name) + ' - ' + str(self.species)



class TransportFleet(models.Model):
    date = models.DateField(auto_now_add=False, auto_now=False, blank=True)
    employee = models.CharField(max_length=30, blank=True)
    new_outbreak = models.BooleanField(default=False)
    date = models.DateField(auto_now_add=False, auto_now=False, blank=True, null=True)
    reporter_name = models.CharField(max_length=30, blank=True, null=True)
    start_date = models.DateField(auto_now_add=False, auto_now=False, blank=True, null=True)
    end_date = models.DateField(auto_now_add=False, auto_now=False, blank=True, null=True)
    quarter = models.ForeignKey(Quarter, blank=True, null=True)
    month = models.DateField(auto_now_add=False, auto_now=False, blank=True, null=True)
    year = models.DateField(auto_now_add=False, auto_now=False, blank=True, null=True)
    localty = models.ForeignKey(Localty, blank=True, null=True)
    localty_longitude = models.CharField(max_length=30, blank=True)
    localty_latitude = models.CharField(max_length=30, blank=True)
    owner_name = models.CharField(max_length=30, blank=True, null=True)
    owner_contact_no = models.CharField(max_length=30, blank=True, null=True)
    owner_nin_no = models.CharField(max_length=30, blank=True, null=True)
    owner_gender = models.CharField(max_length=30, blank=True, null=True, choices=General.sex_choice)
    species = models.ForeignKey(Species, blank=True, null=True)
    species_breed = models.ForeignKey(SpeciesBreed, blank=True, null=True)
    specie_sex = models.CharField(max_length=30, blank=True, null=True, choices=General.sex_choice)
    specie_age = models.CharField(max_length=30, blank=True)
    animalID = models.CharField(max_length=30, blank=True)
    pet_name = models.CharField(max_length=30, blank=True)
    animal_group_size= models.CharField(max_length=30, blank=True)
    principal_signs = models.ForeignKey(PrincipalSign, blank=True, null=True)
    clinical_diagnosis = models.ForeignKey(ClinicalDiagnosis, blank=True, null=True)
    disease_code = models.ForeignKey(DiseaseCode, blank=True, null=True)
    clinical_prognosis = models.CharField(max_length=30, blank=True, null=True, choices=General.clinical_prognosis_choice)
    vaccination_history = models.ForeignKey(VaccinationHistory, blank=True, null=True)
    notifiable_disease = models.BooleanField(default=False)
    timestamp = models.DateField(auto_now_add=True, auto_now=False, blank=True)
    owner_gender = models.CharField(max_length=30, blank=True, null=True, choices=General.sex_choice)
    notification_frequency = models.CharField(max_length=30, blank=True, null=True, choices=General.notification_frequency_choice)
    incedence_rate= models.CharField(max_length=30, blank=True, null=True)
    motality_rate= models.CharField(max_length=30, blank=True, null=True)
    mobidity_rate= models.CharField(max_length=30, blank=True, null=True)
    lab_sample_collected = models.BooleanField(default=False)
    sample_type = models.CharField(max_length=30, blank=True, null=True, choices=General.sample_type_choice)
    sample_ID= models.CharField(max_length=30, blank=True, null=True)
    lab_test_applied= models.CharField(max_length=30, blank=True, null=True, choices=General.lap_test_applied_choice)
    lab_test_results= models.CharField(max_length=30, blank=True, null=True, choices=General.lab_test_results_choice)
    control_measures= models.ForeignKey(ControlMeasures, blank=True, null=True)
    approve_one = models.CharField(max_length=30, blank=True, null=True, choices=General.approval_choice)
    approve_two = models.CharField(max_length=30, blank=True, null=True, choices=General.approval_choice)
    
    def __unicode__(self):
       return str(self.owner_name) + ' - ' + str(self.species)


class Production(models.Model):
    employee = models.CharField(max_length=30, blank=True)
    new_outbreak = models.BooleanField(default=False)
    date = models.DateField(auto_now_add=False, auto_now=False, blank=True, null=True)
    reporter_name = models.CharField(max_length=30, blank=True, null=True)
    start_date = models.DateField(auto_now_add=False, auto_now=False, blank=True, null=True)
    end_date = models.DateField(auto_now_add=False, auto_now=False, blank=True, null=True)
    quarter = models.ForeignKey(Quarter, blank=True, null=True)
    month = models.DateField(auto_now_add=False, auto_now=False, blank=True)
    
    localty = models.ForeignKey(Localty, blank=True, null=True)
    localty_longitude = models.CharField(max_length=30, blank=True)
    localty_latitude = models.CharField(max_length=30, blank=True)
    
    production_system = models.CharField(max_length=30, blank=True, null=True, choices=General.clinical_prognosis_choice)
    production_type = models.CharField(max_length=30, blank=True, null=True, choices=General.clinical_prognosis_choice)
    species = models.ForeignKey(Species, blank=True, null=True)
    species_breed = models.ForeignKey(SpeciesBreed, blank=True, null=True)
    animal_group_size= models.CharField(max_length=30, blank=True)
    No_animal_producer= models.CharField(max_length=30, blank=True)
    No_of_borns= models.CharField(max_length=30, blank=True)
    no_of_deaths = models.CharField(max_length=30, blank=True, null=True)
    animalID = models.CharField(max_length=30, blank=True)
    no_of_milkltres = models.CharField(max_length=30, blank=True, null=True)
    no_of_eggs = models.CharField(max_length=30, blank=True, null=True)
    
    owner_name = models.CharField(max_length=30, blank=True, null=True)
    owner_contact_no = models.CharField(max_length=30, blank=True, null=True)
    owner_nin_no = models.CharField(max_length=30, blank=True, null=True)
    owner_gender = models.CharField(max_length=30, blank=True, null=True, choices=General.sex_choice)
    cost_produced_per_milk_ltres = models.CharField(max_length=30, blank=True, null=True)
    cost_produced_eggs = models.CharField(max_length=30, blank=True, null=True)
    approve_one = models.CharField(max_length=30, blank=True, null=True, choices=General.approval_choice)
    approve_two = models.CharField(max_length=30, blank=True, null=True, choices=General.approval_choice)
    
    def __unicode__(self):
       return str(self.owner_name) + ' - ' + str(self.species)



