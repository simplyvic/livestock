from django import forms
from .models import *


class ClinicalForm(forms.ModelForm):
	class Meta:
		model = Clinical
		fields = ['employee', 'quarter', 'date', 'clinical_name', 'region','species', 'species_breed', 'specie_sex',
					'owner_name',
					'owner_contact_no',
					'owner_gender',
					'localty',
					'localty_longitude',
					'localty_latitude',
					'animal_group_size',
					'animalID',
					'pet_name',
					'animal_live_weight',
					'anamnesis',
					'principal_signs',
					'clinical_diagnosis',
					'clinical_prognosis',
					# 'timestamp',
				]





	def clean_clinical_name(self): # Validates the Clinical Name Field
		clinical_name = self.cleaned_data.get('clinical_name')
		if (clinical_name == ""):
			raise forms.ValidationError('This field cannot be left blank')

		# for instance in Clinical.objects.all():
		# 	if instance.clinical_name == clinical_name:
		# 		raise forms.ValidationError('There is a clinical with the name ' + clinical_name)
		return clinical_name

	def clean_owner_name(self): # Validates the Clinical Name Field
		owner_name = self.cleaned_data.get('owner_name')
		if (owner_name == ""):
			raise forms.ValidationError('This field cannot be left blank')

		# for instance in Clinical.objects.all():
		# 	if instance.owner_name == owner_name:
		# 		raise forms.ValidationError('There is a clinical with the IP address ' + owner_name)
		return owner_name


class ClinicalApproveOneForm(forms.ModelForm):
	class Meta:
		model = Clinical
		fields = ['approve_one']

	def clean_approve_one(self): # Validates the Clinical Name Field
		approve_one = self.cleaned_data.get('approve_one')
		if (approve_one == ""):
			raise forms.ValidationError('Please choose one from the list')

		# for instance in Clinical.objects.all():
		# 	if instance.approve == approve:
		# 		raise forms.ValidationError('There is a clinical with the name ' + approve)
		return approve_one



class ClinicalApproveTwoForm(forms.ModelForm):
	class Meta:
		model = Clinical
		fields = ['approve_two']

	def clean_approve_two(self): # Validates the Clinical Name Field
		approve_two = self.cleaned_data.get('approve_two')
		if (approve_two == ""):
			raise forms.ValidationError('Please choose one from the list')

		# for instance in Clinical.objects.all():
		# 	if instance.approve == approve:
		# 		raise forms.ValidationError('There is a clinical with the name ' + approve)
		return approve_two



class ClinicalSearchForm(forms.ModelForm):
    class Meta:
        model = Clinical
        fields = ['clinical_name', 'owner_name', 'export_to_CSV']



class QuarterForm(forms.ModelForm):
    class Meta:
        model =  Quarter
        fields = ['name']


# class ClinicalApproveSearchForm(forms.ModelForm):
#     class Meta:
#         model = Clinical
#         fields = ['clinical_name']



class DiseaseForm(forms.ModelForm):
	class Meta:
		model = DiseaseReport
		fields = ['employee', 'quarter', 'species', 'species_breed', 'specie_sex',
					'owner_name',
					'owner_contact_no',
					'owner_gender',
					'localty',
					'localty_longitude',
					'localty_latitude',
					'animal_group_size',
					'animalID',
				]


	def clean_owner_name(self): # Validates the Clinical Name Field
		owner_name = self.cleaned_data.get('owner_name')
		if (owner_name == ""):
			raise forms.ValidationError('This field cannot be left blank')

		# for instance in Clinical.objects.all():
		# 	if instance.owner_name == owner_name:
		# 		raise forms.ValidationError('There is a clinical with the IP address ' + owner_name)
		return owner_name


class SearchForm(forms.Form): # Customized Form to be to be used to save items in the database
	owner_name = forms.CharField(required=False)	
	start_date = forms.DateTimeField(required=False, label=" Start Date and Time")
	end_date = forms.DateTimeField(required=False, label=" End Date and Time")
	export_to_CSV = forms.BooleanField(required=False, label="Export to CSV")


class LabForm(forms.ModelForm):
	class Meta:
		model = Lab
		fields = ['employee', 'quarter', 'species', 'species_breed', 'specie_sex',
					'owner_name',
					'owner_contact_no',
					'owner_gender',
					'localty',
					'localty_longitude',
					'localty_latitude',
					'animal_group_size',
					'animalID',
				]


	def clean_owner_name(self): # Validates the Clinical Name Field
		owner_name = self.cleaned_data.get('owner_name')
		if (owner_name == ""):
			raise forms.ValidationError('This field cannot be left blank')

		# for instance in Clinical.objects.all():
		# 	if instance.owner_name == owner_name:
		# 		raise forms.ValidationError('There is a clinical with the IP address ' + owner_name)
		return owner_name


class AbattoirForm(forms.ModelForm):
	class Meta:
		model = Abattoir
		fields = ['employee', 'quarter', 'species', 'species_breed', 'specie_sex',
					'owner_name',
					'owner_contact_no',
					'owner_gender',
					'localty',
					'localty_longitude',
					'localty_latitude',
					'animal_group_size',
					'animalID',
				]


	def clean_owner_name(self): # Validates the Clinical Name Field
		owner_name = self.cleaned_data.get('owner_name')
		if (owner_name == ""):
			raise forms.ValidationError('This field cannot be left blank')

		# for instance in Clinical.objects.all():
		# 	if instance.owner_name == owner_name:
		# 		raise forms.ValidationError('There is a clinical with the IP address ' + owner_name)
		return owner_name

class LocalityForm(forms.ModelForm):
	class Meta:
		model = Locality
		fields = ['employee', 'quarter', 'species', 'species_breed', 'specie_sex',
					'owner_name',
					'owner_contact_no',
					'owner_gender',
					'localty',
					'localty_longitude',
					'localty_latitude',
					'animal_group_size',
					'animalID',
				]


	def clean_owner_name(self): # Validates the Clinical Name Field
		owner_name = self.cleaned_data.get('owner_name')
		if (owner_name == ""):
			raise forms.ValidationError('This field cannot be left blank')

		# for instance in Clinical.objects.all():
		# 	if instance.owner_name == owner_name:
		# 		raise forms.ValidationError('There is a clinical with the IP address ' + owner_name)
		return owner_name

class VaccinationForm(forms.ModelForm):
	class Meta:
		model = Vaccination
		fields = ['employee', 'quarter', 'species', 'species_breed', 'specie_sex',
					'owner_name',
					'owner_contact_no',
					'owner_gender',
					'localty',
					'localty_longitude',
					'localty_latitude',
					'animal_group_size',
					'animalID',
				]


	def clean_owner_name(self): # Validates the Clinical Name Field
		owner_name = self.cleaned_data.get('owner_name')
		if (owner_name == ""):
			raise forms.ValidationError('This field cannot be left blank')

		# for instance in Clinical.objects.all():
		# 	if instance.owner_name == owner_name:
		# 		raise forms.ValidationError('There is a clinical with the IP address ' + owner_name)
		return owner_name

class VetInfraIndustryForm(forms.ModelForm):
	class Meta:
		model = VetInfraIndustry
		fields = ['employee', 'quarter', 'species', 'species_breed', 'specie_sex',
					'owner_name',
					'owner_contact_no',
					'owner_gender',
					'localty',
					'localty_longitude',
					'localty_latitude',
					'animal_group_size',
					'animalID',
				]


	def clean_owner_name(self): # Validates the Clinical Name Field
		owner_name = self.cleaned_data.get('owner_name')
		if (owner_name == ""):
			raise forms.ValidationError('This field cannot be left blank')

		# for instance in Clinical.objects.all():
		# 	if instance.owner_name == owner_name:
		# 		raise forms.ValidationError('There is a clinical with the IP address ' + owner_name)
		return owner_name

class PermitsForm(forms.ModelForm):
	class Meta:
		model = Permits
		fields = ['employee', 'quarter', 'species', 'species_breed', 'specie_sex',
					'owner_name',
					'owner_contact_no',
					'owner_gender',
					'localty',
					'localty_longitude',
					'localty_latitude',
					'animal_group_size',
					'animalID',
				]


	def clean_owner_name(self): # Validates the Clinical Name Field
		owner_name = self.cleaned_data.get('owner_name')
		if (owner_name == ""):
			raise forms.ValidationError('This field cannot be left blank')

		# for instance in Clinical.objects.all():
		# 	if instance.owner_name == owner_name:
		# 		raise forms.ValidationError('There is a clinical with the IP address ' + owner_name)
		return owner_name

class TransportFleetForm(forms.ModelForm):
	class Meta:
		model = TransportFleet
		fields = ['employee', 'quarter', 'species', 'species_breed', 'specie_sex',
					'owner_name',
					'owner_contact_no',
					'owner_gender',
					'localty',
					'localty_longitude',
					'localty_latitude',
					'animal_group_size',
					'animalID',
				]


	def clean_owner_name(self): # Validates the Clinical Name Field
		owner_name = self.cleaned_data.get('owner_name')
		if (owner_name == ""):
			raise forms.ValidationError('This field cannot be left blank')

		# for instance in Clinical.objects.all():
		# 	if instance.owner_name == owner_name:
		# 		raise forms.ValidationError('There is a clinical with the IP address ' + owner_name)
		return owner_name

class ProductionForm(forms.ModelForm):
	class Meta:
		model = Production
		fields = ['employee', 'quarter', 'species', 'species_breed',
					'owner_name',
					'owner_contact_no',
					'owner_gender',
					'localty',
					'localty_longitude',
					'localty_latitude',
					'animal_group_size',
					'animalID',
				]


	def clean_owner_name(self): # Validates the Clinical Name Field
		owner_name = self.cleaned_data.get('owner_name')
		if (owner_name == ""):
			raise forms.ValidationError('This field cannot be left blank')

		# for instance in Clinical.objects.all():
		# 	if instance.owner_name == owner_name:
		# 		raise forms.ValidationError('There is a clinical with the IP address ' + owner_name)
		return owner_name