from django import forms
from .models import *

class NoticeBoardForm(forms.ModelForm):
	class Meta:
		model = NoticeBoard
		fields = ['message']

	def clean_message(self):
		message = self.cleaned_data.get('message')
		if (message == ""):
			raise forms.ValidationError('Please add a message here')
		return message

class NoticeBoardSearchForm(forms.ModelForm):
    message = forms.CharField(required=False)
    class Meta:
        model = NoticeBoard
        fields = ['sent_by']



class ClinicalForm(forms.ModelForm):
	class Meta:
		model = Clinical
		fields = ['quarter', 'clinical_name', 'region','species', 'species_breed', 'specie_sex',
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
					'comment',
					# 'timestamp',
				]





	def clean_clinical_name(self): # Validates the Clinical Name Field
		clinical_name = self.cleaned_data.get('clinical_name')
		if (clinical_name == None):
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
		fields = ['approve_one', 'comment']
		# fields = '__all__'

	def clean_approve_one(self): # Validates the Clinical Name Field
		approve_one = self.cleaned_data.get('approve_one')
		if (approve_one == None):
			raise forms.ValidationError('Please choose one from the list')

		# for instance in Clinical.objects.all():
		# 	if instance.approve == approve:
		# 		raise forms.ValidationError('There is a clinical with the name ' + approve)
		return approve_one



class ClinicalApproveTwoForm(forms.ModelForm):
	class Meta:
		model = Clinical
		fields = ['approve_one', 'comment']
		# fields = ['approve_two']

	def clean_approve_two(self): # Validates the Clinical Name Field
		approve_two = self.cleaned_data.get('approve_two')
		if (approve_two == None):
			raise forms.ValidationError('Please choose one from the list')

		# for instance in Clinical.objects.all():
		# 	if instance.approve == approve:
		# 		raise forms.ValidationError('There is a clinical with the name ' + approve)
		return approve_two



class ClinicalSearchForm(forms.ModelForm):
    class Meta:
        model = Clinical
        fields = ['clinical_name', 'owner_name', 'export_to_CSV']



class SearchForm(forms.Form): # Customized Form to be to be used to save items in the database
	employee = forms.CharField(required=False)	
	# start_date = forms.DateTimeField(required=False, label=" Start Date and Time")
	# end_date = forms.DateTimeField(required=False, label=" End Date and Time")
	export_to_CSV = forms.BooleanField(required=False, label="Export to CSV")


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
		fields = [	'surveillance_type', 
					'quarter', 
					'species', 
					'species_breed', 
					'specie_sex',
					'owner_name',
					'owner_contact_no',
					'owner_gender',
					'owner_nin_no',
					'localty',
					'localty_longitude',
					'localty_latitude',
					'pet_name',
					'animal_group_size',
					'animalID',
					'new_outbreak',
					'reporter_name',
					'start_date',
					'end_date',
					#'month',
					#'year',
					'specie_age',
					'principal_signs',
					'clinical_diagnosis',
					'disease_code',
					'clinical_prognosis',
					'vaccination_history',
					'notifiable_disease',
					'notification_frequency',
					'zoonosis',
					'no_of_cases',
					'no_of_deaths',
					'no_destroyed',
					'incedence_rate',
					'motality_rate',
					'mobidity_rate',
					'lab_sample_collected',
					'sample_type',
					'sample_ID',
					'lab_test_applied',
					'lab_test_results',
					'control_measures',
					'comment'

				]


	def clean_owner_name(self): # Validates the Clinical Name Field
		owner_name = self.cleaned_data.get('owner_name')
		if (owner_name == ""):
			raise forms.ValidationError('This field cannot be left blank')

		# for instance in Clinical.objects.all():
		# 	if instance.owner_name == owner_name:
		# 		raise forms.ValidationError('There is a clinical with the IP address ' + owner_name)
		return owner_name


class DiseaseReportApproveOneForm(forms.ModelForm):
	class Meta:
		model = DiseaseReport
		fields = ['approve_two', 'comment']
		# fields = '__all__'

	def clean_approve_one(self): # Validates the Clinical Name Field
		approve_one = self.cleaned_data.get('approve_one')
		if (approve_one == None):
			raise forms.ValidationError('Please choose one from the list')

		# for instance in Clinical.objects.all():
		# 	if instance.approve == approve:
		# 		raise forms.ValidationError('There is a clinical with the name ' + approve)
		return approve_one



class DiseaseReportApproveTwoForm(forms.ModelForm):
	class Meta:
		model = DiseaseReport
		fields = ['approve_one', 'comment']
		# fields = ['approve_two']

	def clean_approve_two(self): # Validates the Clinical Name Field
		approve_two = self.cleaned_data.get('approve_two')
		if (approve_two == None):
			raise forms.ValidationError('Please choose one from the list')

		# for instance in Clinical.objects.all():
		# 	if instance.approve == approve:
		# 		raise forms.ValidationError('There is a clinical with the name ' + approve)
		return approve_two



class LabForm(forms.ModelForm):
	class Meta:
		model = Lab
		fields = [	'surveillance_type', 
					'quarter', 
					'species', 
					'species_breed', 
					'specie_sex',
					'owner_name',
					'owner_contact_no',
					'owner_gender',
					'owner_nin_no',
					'localty',
					'localty_longitude',
					'localty_latitude',
					'pet_name',
					'animal_group_size',
					'animalID',
					'new_outbreak',
					'reporter_name',
					'start_date',
					'end_date',
					#'month',
					#'year',
					'specie_age',
					'principal_signs',
					'clinical_diagnosis',
					'disease_code',
					'clinical_prognosis',
					'vaccination_history',
					'notifiable_disease',
					'incedence_rate',
					'analysis_date',
					'lab_sample_collected',
					'sample_type',
					'sample_ID',
					'lab_test_applied',
					'lab_test_results',
					'comment'
				]


	def clean_owner_name(self): # Validates the Clinical Name Field
		owner_name = self.cleaned_data.get('owner_name')
		if (owner_name == ""):
			raise forms.ValidationError('This field cannot be left blank')

		# for instance in Clinical.objects.all():
		# 	if instance.owner_name == owner_name:
		# 		raise forms.ValidationError('There is a clinical with the IP address ' + owner_name)
		return owner_name


class LabApproveOneForm(forms.ModelForm):
	class Meta:
		model = Lab
		fields = ['approve_two', 'comment']
		# fields = '__all__'

	def clean_approve_one(self): # Validates the Clinical Name Field
		approve_one = self.cleaned_data.get('approve_one')
		if (approve_one == None):
			raise forms.ValidationError('Please choose one from the list')

		# for instance in Clinical.objects.all():
		# 	if instance.approve == approve:
		# 		raise forms.ValidationError('There is a clinical with the name ' + approve)
		return approve_one



class LabApproveTwoForm(forms.ModelForm):
	class Meta:
		model = Lab
		fields = ['approve_one', 'comment']
		# fields = ['approve_two']

	def clean_approve_two(self): # Validates the Clinical Name Field
		approve_two = self.cleaned_data.get('approve_two')
		if (approve_two == None):
			raise forms.ValidationError('Please choose one from the list')

		# for instance in Clinical.objects.all():
		# 	if instance.approve == approve:
		# 		raise forms.ValidationError('There is a clinical with the name ' + approve)
		return approve_two



class AbattoirForm(forms.ModelForm):
	class Meta:
		model = Abattoir
		fields = [	'surveillance_type', 
					'quarter', 
					'species', 
					'species_breed', 
					'specie_sex',
					'owner_name',
					'owner_contact_no',
					'owner_gender',
					'owner_nin_no',
					'localty',
					'localty_longitude',
					'localty_latitude',
					'pet_name',
					'animal_group_size',
					'animalID',
					'new_outbreak',
					'reporter_name',
					'start_date',
					'end_date',
					#'month',
					#'year',
					'specie_age',
					'principal_signs',
					'clinical_diagnosis',
					'disease_code',
					'clinical_prognosis',
					'vaccination_history',
					'notifiable_disease',
					'notification_frequency',
					'incedence_rate',
					'motality_rate',
					'mobidity_rate',
					'lab_sample_collected',
					'sample_type',
					'sample_ID',
					'lab_test_applied',
					'lab_test_results',
					'comment'
				]


	def clean_owner_name(self): # Validates the Clinical Name Field
		owner_name = self.cleaned_data.get('owner_name')
		if (owner_name == ""):
			raise forms.ValidationError('This field cannot be left blank')

		# for instance in Clinical.objects.all():
		# 	if instance.owner_name == owner_name:
		# 		raise forms.ValidationError('There is a clinical with the IP address ' + owner_name)
		return owner_name


class AbattoirApproveOneForm(forms.ModelForm):
	class Meta:
		model = Abattoir
		fields = ['approve_two', 'comment']
		# fields = '__all__'

	def clean_approve_one(self): # Validates the Clinical Name Field
		approve_one = self.cleaned_data.get('approve_one')
		if (approve_one == None):
			raise forms.ValidationError('Please choose one from the list')

		# for instance in Clinical.objects.all():
		# 	if instance.approve == approve:
		# 		raise forms.ValidationError('There is a clinical with the name ' + approve)
		return approve_one



class AbattoirApproveTwoForm(forms.ModelForm):
	class Meta:
		model = Abattoir
		fields = ['approve_one', 'comment']
		# fields = ['approve_two']

	def clean_approve_two(self): # Validates the Clinical Name Field
		approve_two = self.cleaned_data.get('approve_two')
		if (approve_two == None):
			raise forms.ValidationError('Please choose one from the list')

		# for instance in Clinical.objects.all():
		# 	if instance.approve == approve:
		# 		raise forms.ValidationError('There is a clinical with the name ' + approve)
		return approve_two




class LocalityForm(forms.ModelForm):
	class Meta:
		model = Locality
		fields = [	'surveillance_type', 
					'quarter', 
					'species', 
					'species_breed', 
					'specie_sex',
					'owner_name',
					'owner_contact_no',
					'owner_gender',
					'owner_nin_no',
					'localty',
					'localty_longitude',
					'localty_latitude',
					'pet_name',
					'animal_group_size',
					'animalID',
					'new_outbreak',
					'reporter_name',
					'start_date',
					'end_date',
					#'month',
					#'year',
					'specie_age',
					'principal_signs',
					'clinical_diagnosis',
					'disease_code',
					'clinical_prognosis',
					'vaccination_history',
					'notifiable_disease',
					'notification_frequency',
					'incedence_rate',
					'motality_rate',
					'mobidity_rate',
					'lab_sample_collected',
					'sample_type',
					'sample_ID',
					'lab_test_applied',
					'lab_test_results',
					'comment'
				]


	def clean_owner_name(self): # Validates the Clinical Name Field
		owner_name = self.cleaned_data.get('owner_name')
		if (owner_name == ""):
			raise forms.ValidationError('This field cannot be left blank')

		# for instance in Clinical.objects.all():
		# 	if instance.owner_name == owner_name:
		# 		raise forms.ValidationError('There is a clinical with the IP address ' + owner_name)
		return owner_name


class LocalityApproveOneForm(forms.ModelForm):
	class Meta:
		model = Locality
		fields = ['approve_two', 'comment']
		# fields = '__all__'

	def clean_approve_one(self): # Validates the Clinical Name Field
		approve_one = self.cleaned_data.get('approve_one')
		if (approve_one == None):
			raise forms.ValidationError('Please choose one from the list')

		# for instance in Clinical.objects.all():
		# 	if instance.approve == approve:
		# 		raise forms.ValidationError('There is a clinical with the name ' + approve)
		return approve_one



class LocalityApproveTwoForm(forms.ModelForm):
	class Meta:
		model = Locality
		fields = ['approve_one', 'comment']
		# fields = ['approve_two']

	def clean_approve_two(self): # Validates the Clinical Name Field
		approve_two = self.cleaned_data.get('approve_two')
		if (approve_two == None):
			raise forms.ValidationError('Please choose one from the list')

		# for instance in Clinical.objects.all():
		# 	if instance.approve == approve:
		# 		raise forms.ValidationError('There is a clinical with the name ' + approve)
		return approve_two




class VaccinationForm(forms.ModelForm):
	class Meta:
		model = Vaccination
		fields = [	'surveillance_type', 
					'quarter', 
					'species', 
					'species_breed', 
					'specie_sex',
					'owner_name',
					'owner_contact_no',
					'owner_gender',
					'owner_nin_no',
					'localty',
					'localty_longitude',
					'localty_latitude',
					'pet_name',
					'animal_group_size',
					'animalID',
					'new_outbreak',
					'reporter_name',
					'start_date',
					'end_date',
					#'month',
					#'year',
					'specie_age',
					'principal_signs',
					'clinical_diagnosis',
					'disease_code',
					'clinical_prognosis',
					'vaccination_history',
					'notifiable_disease',
					'notification_frequency',
					'incedence_rate',
					'motality_rate',
					'mobidity_rate',
					'lab_sample_collected',
					'sample_type',
					'sample_ID',
					'lab_test_applied',
					'lab_test_results',
					'comment'
				]


	def clean_owner_name(self): # Validates the Clinical Name Field
		owner_name = self.cleaned_data.get('owner_name')
		if (owner_name == ""):
			raise forms.ValidationError('This field cannot be left blank')

		# for instance in Clinical.objects.all():
		# 	if instance.owner_name == owner_name:
		# 		raise forms.ValidationError('There is a clinical with the IP address ' + owner_name)
		return owner_name


class VaccinationApproveOneForm(forms.ModelForm):
	class Meta:
		model = Vaccination
		fields = ['approve_two', 'comment']
		# fields = '__all__'

	def clean_approve_one(self): # Validates the Clinical Name Field
		approve_one = self.cleaned_data.get('approve_one')
		if (approve_one == None):
			raise forms.ValidationError('Please choose one from the list')

		# for instance in Clinical.objects.all():
		# 	if instance.approve == approve:
		# 		raise forms.ValidationError('There is a clinical with the name ' + approve)
		return approve_one



class VaccinationApproveTwoForm(forms.ModelForm):
	class Meta:
		model = Vaccination
		fields = ['approve_one', 'comment']
		# fields = ['approve_two']

	def clean_approve_two(self): # Validates the Clinical Name Field
		approve_two = self.cleaned_data.get('approve_two')
		if (approve_two == None):
			raise forms.ValidationError('Please choose one from the list')

		# for instance in Clinical.objects.all():
		# 	if instance.approve == approve:
		# 		raise forms.ValidationError('There is a clinical with the name ' + approve)
		return approve_two




class VetInfraIndustryForm(forms.ModelForm):
	class Meta:
		model = VetInfraIndustry
		fields = [	'quarter', 
					'species', 
					'species_breed', 
					'specie_sex',
					'owner_name',
					'owner_contact_no',
					'owner_gender',
					'owner_nin_no',
					'localty',
					'localty_longitude',
					'localty_latitude',
					'pet_name',
					'animal_group_size',
					'animalID',
					'new_outbreak',
					'reporter_name',
					'start_date',
					'end_date',
					#'month',
					#'year',
					'specie_age',
					'principal_signs',
					'clinical_diagnosis',
					'disease_code',
					'clinical_prognosis',
					'vaccination_history',
					'notifiable_disease',
					'notification_frequency',
					'incedence_rate',
					'motality_rate',
					'mobidity_rate',
					'lab_sample_collected',
					'sample_type',
					'sample_ID',
					'lab_test_applied',
					'lab_test_results',
					'comment'
				]


	def clean_owner_name(self): # Validates the Clinical Name Field
		owner_name = self.cleaned_data.get('owner_name')
		if (owner_name == ""):
			raise forms.ValidationError('This field cannot be left blank')

		# for instance in Clinical.objects.all():
		# 	if instance.owner_name == owner_name:
		# 		raise forms.ValidationError('There is a clinical with the IP address ' + owner_name)
		return owner_name


class VetInfraIndustryApproveOneForm(forms.ModelForm):
	class Meta:
		model = VetInfraIndustry
		fields = ['approve_two', 'comment']
		# fields = '__all__'

	def clean_approve_one(self): # Validates the Clinical Name Field
		approve_one = self.cleaned_data.get('approve_one')
		if (approve_one == None):
			raise forms.ValidationError('Please choose one from the list')

		# for instance in Clinical.objects.all():
		# 	if instance.approve == approve:
		# 		raise forms.ValidationError('There is a clinical with the name ' + approve)
		return approve_one



class VetInfraIndustryApproveTwoForm(forms.ModelForm):
	class Meta:
		model = VetInfraIndustry
		fields = ['approve_one', 'comment']
		# fields = ['approve_two']

	def clean_approve_two(self): # Validates the Clinical Name Field
		approve_two = self.cleaned_data.get('approve_two')
		if (approve_two == None):
			raise forms.ValidationError('Please choose one from the list')

		# for instance in Clinical.objects.all():
		# 	if instance.approve == approve:
		# 		raise forms.ValidationError('There is a clinical with the name ' + approve)
		return approve_two




class PermitsForm(forms.ModelForm):
	class Meta:
		model = Permits
		fields = [	'quarter', 
					'species', 
					'species_breed', 
					'specie_sex',
					'owner_name',
					'owner_contact_no',
					'owner_gender',
					'owner_nin_no',
					'localty',
					'localty_longitude',
					'localty_latitude',
					'pet_name',
					'animal_group_size',
					'animalID',
					'new_outbreak',
					'reporter_name',
					'start_date',
					'end_date',
					#'month',
					#'year',
					'specie_age',
					'principal_signs',
					'clinical_diagnosis',
					'disease_code',
					'clinical_prognosis',
					'vaccination_history',
					'notifiable_disease',
					'notification_frequency',
					'incedence_rate',
					'motality_rate',
					'mobidity_rate',
					'lab_sample_collected',
					'sample_type',
					'sample_ID',
					'lab_test_applied',
					'lab_test_results',
					'comment'
				]


	def clean_owner_name(self): # Validates the Clinical Name Field
		owner_name = self.cleaned_data.get('owner_name')
		if (owner_name == ""):
			raise forms.ValidationError('This field cannot be left blank')

		# for instance in Clinical.objects.all():
		# 	if instance.owner_name == owner_name:
		# 		raise forms.ValidationError('There is a clinical with the IP address ' + owner_name)
		return owner_name


class PermitsApproveOneForm(forms.ModelForm):
	class Meta:
		model = Permits
		fields = ['approve_two', 'comment']
		# fields = '__all__'

	def clean_approve_one(self): # Validates the Clinical Name Field
		approve_one = self.cleaned_data.get('approve_one')
		if (approve_one == None):
			raise forms.ValidationError('Please choose one from the list')

		# for instance in Clinical.objects.all():
		# 	if instance.approve == approve:
		# 		raise forms.ValidationError('There is a clinical with the name ' + approve)
		return approve_one



class PermitsApproveTwoForm(forms.ModelForm):
	class Meta:
		model = Permits
		fields = ['approve_one', 'comment']
		# fields = ['approve_two']

	def clean_approve_two(self): # Validates the Clinical Name Field
		approve_two = self.cleaned_data.get('approve_two')
		if (approve_two == None):
			raise forms.ValidationError('Please choose one from the list')

		# for instance in Clinical.objects.all():
		# 	if instance.approve == approve:
		# 		raise forms.ValidationError('There is a clinical with the name ' + approve)
		return approve_two




class TransportFleetForm(forms.ModelForm):
	class Meta:
		model = TransportFleet
		fields = [	'quarter', 
					'species', 
					'species_breed', 
					'specie_sex',
					'owner_name',
					'owner_contact_no',
					'owner_gender',
					'owner_nin_no',
					'localty',
					'localty_longitude',
					'localty_latitude',
					'pet_name',
					'animal_group_size',
					'animalID',
					'new_outbreak',
					'reporter_name',
					'start_date',
					'end_date',
					#'month',
					#'year',
					'specie_age',
					'principal_signs',
					'clinical_diagnosis',
					'disease_code',
					'clinical_prognosis',
					'vaccination_history',
					'notifiable_disease',
					'notification_frequency',
					'incedence_rate',
					'motality_rate',
					'mobidity_rate',
					'lab_sample_collected',
					'sample_type',
					'sample_ID',
					'lab_test_applied',
					'lab_test_results',
					'comment'
				]


	def clean_owner_name(self): # Validates the Clinical Name Field
		owner_name = self.cleaned_data.get('owner_name')
		if (owner_name == ""):
			raise forms.ValidationError('This field cannot be left blank')

		# for instance in Clinical.objects.all():
		# 	if instance.owner_name == owner_name:
		# 		raise forms.ValidationError('There is a clinical with the IP address ' + owner_name)
		return owner_name


class TransportFleetApproveOneForm(forms.ModelForm):
	class Meta:
		model = TransportFleet
		fields = ['approve_two', 'comment']
		# fields = '__all__'

	def clean_approve_one(self): # Validates the Clinical Name Field
		approve_one = self.cleaned_data.get('approve_one')
		if (approve_one == None):
			raise forms.ValidationError('Please choose one from the list')

		# for instance in Clinical.objects.all():
		# 	if instance.approve == approve:
		# 		raise forms.ValidationError('There is a clinical with the name ' + approve)
		return approve_one



class TransportFleetApproveTwoForm(forms.ModelForm):
	class Meta:
		model = TransportFleet
		fields = ['approve_one', 'comment']
		# fields = ['approve_two']

	def clean_approve_two(self): # Validates the Clinical Name Field
		approve_two = self.cleaned_data.get('approve_two')
		if (approve_two == None):
			raise forms.ValidationError('Please choose one from the list')

		# for instance in Clinical.objects.all():
		# 	if instance.approve == approve:
		# 		raise forms.ValidationError('There is a clinical with the name ' + approve)
		return approve_two




class ProductionForm(forms.ModelForm):
	class Meta:
		model = Production
		fields = [	
					'new_outbreak',
					'reporter_name',
					'start_date',
					'end_date',
					'quarter', 
					# 'month',
					'localty',
					'localty_longitude',
					'localty_latitude',
					'production_system',
					'production_type',
					'species', 
					'species_breed',
					'animal_group_size',
					'no_animal_producer',
					'no_of_borns',
					'no_of_deaths',
					'animalID',
					'no_of_milkltres',
					'no_of_eggs',
					'owner_name',
					'owner_contact_no',
					'owner_gender',
					'owner_nin_no',
					'cost_produced_per_milk_ltres',
					'cost_produced_eggs',
					'comment'
				]


	def clean_owner_name(self): # Validates the Clinical Name Field
		owner_name = self.cleaned_data.get('owner_name')
		if (owner_name == ""):
			raise forms.ValidationError('This field cannot be left blank')

		# for instance in Clinical.objects.all():
		# 	if instance.owner_name == owner_name:
		# 		raise forms.ValidationError('There is a clinical with the IP address ' + owner_name)
		return owner_name


class ProductionApproveOneForm(forms.ModelForm):
	class Meta:
		model = Production
		fields = ['approve_two', 'comment']
		# fields = '__all__'

	def clean_approve_one(self): # Validates the Clinical Name Field
		approve_one = self.cleaned_data.get('approve_one')
		if (approve_one == None):
			raise forms.ValidationError('Please choose one from the list')

		# for instance in Clinical.objects.all():
		# 	if instance.approve == approve:
		# 		raise forms.ValidationError('There is a clinical with the name ' + approve)
		return approve_one



class ProductionApproveTwoForm(forms.ModelForm):
	class Meta:
		model = Production
		fields = ['approve_one', 'comment']
		# fields = ['approve_two']

	def clean_approve_two(self): # Validates the Clinical Name Field
		approve_two = self.cleaned_data.get('approve_two')
		if (approve_two == None):
			raise forms.ValidationError('Please choose one from the list')

		# for instance in Clinical.objects.all():
		# 	if instance.approve == approve:
		# 		raise forms.ValidationError('There is a clinical with the name ' + approve)
		return approve_two

