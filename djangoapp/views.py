from django.shortcuts import render, redirect
from .forms import *
from .models import *
from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from django.contrib import messages
import csv


# Create your views here.
def home(request):
    title = 'CLINICAL MANAGEMENT INFORMATION SYSTEM'
    context = {
        "title": title,
    }
    return render(request, "base.html",context)


def clinical_entry(request):
    title = 'Add Clinical'
    form = ClinicalForm(request.POST or None) 
    if form.is_valid():
        instance = form.save(commit=False)
        instance.employee = str(request.user)
        form.save()
        form.save_m2m()
        messages.success(request, 'Successfully Saved')
        return redirect('/clinical_list')
    context = {
        "title": title,
        "form": form,
     }
    return render(request, "entry.html",context)


def clinical_list(request):
    title = 'List of approved clinical'
    queryset = Clinical.objects.filter(approve_one='approve').filter(approve_two='approve')
    
    queryset1stAppr = Clinical.objects.filter(approve_one=None).filter(approve_two=None)
    countqueryset1stAppr = queryset1stAppr.count()
    
    queryset2ndAppr = Clinical.objects.filter(approve_one='Approve').filter(approve_two=None)
    countqueryset2ndAppr = queryset2ndAppr.count()
    
    form = ClinicalSearchForm(request.POST or None)
    context = {
         "title": title,
         "queryset": queryset,
         "countqueryset1stAppr": countqueryset1stAppr,
         "countqueryset2ndAppr": countqueryset2ndAppr,
         "form": form,
    }
    if request.method == 'POST':
            queryset = Clinical.objects.all().order_by('-timestamp').filter(clinical_name__icontains=form['clinical_name'].value(),users_name__icontains=form['users_name'].value())
            context = {
            "title": title,
            "queryset": queryset,
            "countqueryset1stAppr": countqueryset1stAppr,
            "countqueryset2ndAppr": countqueryset2ndAppr,
            "form": form,
            }
            # if form['export_to_CSV'].value() == True:
            #      response = HttpResponse(content_type='text/csv')
            #      response['Content-Disposition'] = 'attachment; filename="Clinical list.csv"'
            #      writer = csv.writer(response)
            #      writer.writerow(['CLINICAL NAME', 'IP Address', 'MAC ADDRESS', 'OS', 'USERNAME', 'LOCATION', 'PURCHASE DATE', 'TIMESTAMP'])
            #      instance = queryset
            #      for row in instance:
            #          writer.writerow([row.clinical_name, row.IP_address, row.MAC_address, row.operating_system.all(), row.users_name, row.location, row.purchase_date, row.timestamp])
            #      return response
    return render(request, "clinical_list.html",context)


def clinical_edit(request, id=None):    
    instance = get_object_or_404(Clinical, id=id)
    form = ClinicalForm(request.POST or None, instance=instance)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        form.save_m2m()
        messages.success(request, 'Successfully Saved')
        return redirect('/clinical_list')
    context = {
            "title": 'Edit ' + str(instance.clinical_name),
            "instance": instance,
            "form": form,
        }
    return render(request, "entry.html", context)


def clinical_delete(request, id=None):
        instance = get_object_or_404(Clinical, id=id)
        instance.delete()
        return redirect("clinical_list")



def clinical_approve_one_list(request):
    title = 'List of unapproved clinicals'
    queryset = Clinical.objects.filter(approve_one=None).filter(approve_two=None)
    # queryset = Clinical.objects.exclude(approve_one='Approve')
    form = ClinicalSearchForm(request.POST or None)
    context = {
         "title": title,
         "queryset": queryset,
         "form": form,
    }
    if request.method == 'POST':
            queryset = Clinical.objects.all().order_by('-timestamp').filter(clinical_name__icontains=form['clinical_name'].value())
            context = {
            "title": title,
            "queryset": queryset,
            "form": form,
            }
    return render(request, "clinical_approve_list.html",context)


def clinical_approve_one_edit(request, id=None):    
    instance = get_object_or_404(Clinical, id=id)
    form = ClinicalApproveOneForm(request.POST or None, instance=instance)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        form.save_m2m()
        messages.success(request, 'Successfully Saved')
        return redirect('/clinical_approve_one_list')
    context = {
            "title": 'Edit ' ,
            "instance": instance,
            "form": form,
        }
    return render(request, "entry.html", context)


def clinical_approve_two_list(request):
    title = 'List of unapproved clinicals'
    queryset = Clinical.objects.filter(approve_one='Approve').filter(approve_two=None)
    form = ClinicalSearchForm(request.POST or None)
    context = {
         "title": title,
         "queryset": queryset,
         "form": form,
    }
    if request.method == 'POST':
            queryset = Clinical.objects.all().order_by('-timestamp').filter(clinical_name__icontains=form['clinical_name'].value())
            context = {
            "title": title,
            "queryset": queryset,
            "form": form,
            }
    return render(request, "clinical_approve_list.html",context)


def clinical_approve_two_edit(request, id=None):    
    instance = get_object_or_404(Clinical, id=id)
    form = ClinicalApproveTwoForm(request.POST or None, instance=instance)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        form.save_m2m()
        messages.success(request, 'Successfully Saved')
        return redirect('/clinical_approve_two_list')
    context = {
            "title": 'Edit ' ,
            "instance": instance,
            "form": form,
        }
    return render(request, "entry.html", context)


def disease_report_entry(request):
    title = 'Report Disease'
    form = DiseaseForm(request.POST or None) 
    if form.is_valid():
        instance = form.save(commit=False)
        instance.employee = str(request.user)
        form.save()
        form.save_m2m()
        messages.success(request, 'Successfully Saved')
        return redirect('/disease_report_list')
    context = {
        "title": title,
        "form": form,
     }
    return render(request, "entry.html",context)


def disease_report_list(request):
    title = 'List of approved disease_report'
    queryset = DiseaseReport.objects.filter(approve_one='approve').filter(approve_two='approve')

    queryset1stAppr = DiseaseReport.objects.filter(approve_one=None).filter(approve_two=None)
    countqueryset1stAppr = queryset1stAppr.count()
    
    queryset2ndAppr = DiseaseReport.objects.filter(approve_one='Approve').filter(approve_two=None)
    countqueryset2ndAppr = queryset2ndAppr.count()

    form = SearchForm(request.POST or None)
    context = {
         "title": title,
         "countqueryset1stAppr": countqueryset1stAppr,
         "countqueryset2ndAppr": countqueryset2ndAppr,
         "form": form,
    }

    if request.method == 'POST':
            queryset = DiseaseReport.objects.all().order_by('-timestamp').filter(disease_report_name__icontains=form['disease_report_name'].value(),users_name__icontains=form['users_name'].value())
            context = {
            "title": title,
            "queryset": queryset,
            "countqueryset1stAppr": countqueryset1stAppr,
            "countqueryset2ndAppr": countqueryset2ndAppr,
            "form": form,
            }
            # if form['export_to_CSV'].value() == True:
            #      response = HttpResponse(content_type='text/csv')
            #      response['Content-Disposition'] = 'attachment; filename="DiseaseReport list.csv"'
            #      writer = csv.writer(response)
            #      writer.writerow(['CLINICAL NAME', 'IP Address', 'MAC ADDRESS', 'OS', 'USERNAME', 'LOCATION', 'PURCHASE DATE', 'TIMESTAMP'])
            #      instance = queryset
            #      for row in instance:
            #          writer.writerow([row.disease_report_name, row.IP_address, row.MAC_address, row.operating_system.all(), row.users_name, row.location, row.purchase_date, row.timestamp])
            #      return response
    return render(request, "disease_report_list.html",context)


def disease_report_edit(request, id=None):    
    instance = get_object_or_404(DiseaseReport, id=id)
    form = DiseaseReportForm(request.POST or None, instance=instance)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        form.save_m2m()
        messages.success(request, 'Successfully Saved')
        return redirect('/disease_report_list')
    context = {
            "title": 'Edit ',
            "instance": instance,
            "form": form,
        }
    return render(request, "entry.html", context)


def disease_report_delete(request, id=None):
        instance = get_object_or_404(DiseaseReport, id=id)
        instance.delete()
        return redirect("disease_report_list")


def disease_report_approve_one_list(request):
    title = 'List of unapproved disease_reports'
    queryset = DiseaseReport.objects.filter(approve_one=None).filter(approve_two=None)
    form = SearchForm(request.POST or None)
    context = {
         "title": title,
         "queryset": queryset,
         "form": form,
    }
    if request.method == 'POST':
            queryset = DiseaseReport.objects.all().order_by('-timestamp').filter(disease_report_name__icontains=form['disease_report_name'].value())
            context = {
            "title": title,
            "queryset": queryset,
            "form": form,
            }
    return render(request, "disease_report_approve_list.html",context)


def disease_report_approve_one_edit(request, id=None):    
    instance = get_object_or_404(DiseaseReport, id=id)
    form = DiseaseReportapproveOneForm(request.POST or None, instance=instance)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        form.save_m2m()
        messages.success(request, 'Successfully Saved')
        return redirect('/disease_report_approve_one_list')
    context = {
            "title": 'Edit ',
            "instance": instance,
            "form": form,
        }
    return render(request, "entry.html", context)


def disease_report_approve_two_list(request):
    title = 'List of unapproved disease_reports'
    queryset = DiseaseReport.objects.filter(approve_one='Approve').filter(approve_two=None)
    form = SearchForm(request.POST or None)
    context = {
         "title": title,
         "queryset": queryset,
         "form": form,
    }
    if request.method == 'POST':
            queryset = DiseaseReport.objects.all().order_by('-timestamp').filter(disease_report_name__icontains=form['disease_report_name'].value())
            context = {
            "title": title,
            "queryset": queryset,
            "form": form,
            }
    return render(request, "disease_report_approve_list.html",context)


def disease_report_approve_two_edit(request, id=None):    
    instance = get_object_or_404(DiseaseReport, id=id)
    form = DiseaseReportapproveTwoForm(request.POST or None, instance=instance)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        form.save_m2m()
        messages.success(request, 'Successfully Saved')
        return redirect('/disease_report_approve_one_list')
    context = {
            "title": 'Edit ',
            "instance": instance,
            "form": form,
        }
    return render(request, "entry.html", context)



def lab_entry(request):
    title = 'Add Lab'
    form = LabForm(request.POST or None) 
    if form.is_valid():
        instance = form.save(commit=False)
        instance.employee = str(request.user)
        form.save()
        form.save_m2m()
        messages.success(request, 'Successfully Saved')
        return redirect('/lab_list')
    context = {
        "title": title,
        "form": form,
     }
    return render(request, "entry.html",context)


def lab_list(request):
    title = 'List of approved lab'
    queryset = Lab.objects.filter(approve_one='approve').filter(approve_two='approve')

    queryset1stAppr = Lab.objects.filter(approve_one=None).filter(approve_two=None)
    countqueryset1stAppr = queryset1stAppr.count()
    
    queryset2ndAppr = Lab.objects.filter(approve_one='Approve').filter(approve_two=None)
    countqueryset2ndAppr = queryset2ndAppr.count()

    form = SearchForm(request.POST or None)
    context = {
         "title": title,
         "queryset": queryset,
         "countqueryset1stAppr": countqueryset1stAppr,
         "countqueryset2ndAppr": countqueryset2ndAppr,
         "form": form,
    }
    if request.method == 'POST':
            queryset = Lab.objects.all().order_by('-timestamp').filter(lab_name__icontains=form['lab_name'].value(),users_name__icontains=form['users_name'].value())
            context = {
            "title": title,
            "queryset": queryset,
            "countqueryset1stAppr": countqueryset1stAppr,
            "countqueryset2ndAppr": countqueryset2ndAppr,
            "form": form,
            }
            # if form['export_to_CSV'].value() == True:
            #      response = HttpResponse(content_type='text/csv')
            #      response['Content-Disposition'] = 'attachment; filename="Lab list.csv"'
            #      writer = csv.writer(response)
            #      writer.writerow(['CLINICAL NAME', 'IP Address', 'MAC ADDRESS', 'OS', 'USERNAME', 'LOCATION', 'PURCHASE DATE', 'TIMESTAMP'])
            #      instance = queryset
            #      for row in instance:
            #          writer.writerow([row.lab_name, row.IP_address, row.MAC_address, row.operating_system.all(), row.users_name, row.location, row.purchase_date, row.timestamp])
            #      return response
    return render(request, "lab_list.html",context)


def lab_edit(request, id=None):    
    instance = get_object_or_404(Lab, id=id)
    form = LabForm(request.POST or None, instance=instance)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        form.save_m2m()
        messages.success(request, 'Successfully Saved')
        return redirect('/lab_list')
    context = {
            "title": 'Edit ',
            "instance": instance,
            "form": form,
        }
    return render(request, "entry.html", context)


def lab_delete(request, id=None):
        instance = get_object_or_404(Lab, id=id)
        instance.delete()
        return redirect("lab_list")



def lab_approve_one_list(request):
    title = 'List of unapproved labs'
    queryset = Lab.objects.filter(approve_one=None).filter(approve_two=None)
    form = SearchForm(request.POST or None)
    context = {
         "title": title,
         "queryset": queryset,
         "form": form,
    }
    if request.method == 'POST':
            queryset = Lab.objects.all().order_by('-timestamp').filter(lab_name__icontains=form['lab_name'].value())
            context = {
            "title": title,
            "queryset": queryset,
            "form": form,
            }
    return render(request, "lab_approve_list.html",context)


def lab_approve_one_edit(request, id=None):    
    instance = get_object_or_404(Lab, id=id)
    form = LabapproveOneForm(request.POST or None, instance=instance)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        form.save_m2m()
        messages.success(request, 'Successfully Saved')
        return redirect('/lab_approve_list')
    context = {
            "title": 'Edit ',
            "instance": instance,
            "form": form,
        }
    return render(request, "entry.html", context)


def lab_approve_two_list(request):
    title = 'List of unapproved labs'
    queryset = Lab.objects.filter(approve_one='Approve').filter(approve_two=None)
    form = SearchForm(request.POST or None)
    context = {
         "title": title,
         "queryset": queryset,
         "form": form,
    }
    if request.method == 'POST':
            queryset = Lab.objects.all().order_by('-timestamp').filter(lab_name__icontains=form['lab_name'].value())
            context = {
            "title": title,
            "queryset": queryset,
            "form": form,
            }
    return render(request, "lab_approve_list.html",context)


def lab_approve_two_edit(request, id=None):    
    instance = get_object_or_404(Lab, id=id)
    form = LabapproveTwoForm(request.POST or None, instance=instance)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        form.save_m2m()
        messages.success(request, 'Successfully Saved')
        return redirect('/lab_approve_list')
    context = {
            "title": 'Edit ',
            "instance": instance,
            "form": form,
        }
    return render(request, "entry.html", context)



def abattoir_entry(request):
    title = 'Add Abattoir'
    form = AbattoirForm(request.POST or None) 
    if form.is_valid():
        instance = form.save(commit=False)
        instance.employee = str(request.user)
        form.save()
        form.save_m2m()
        messages.success(request, 'Successfully Saved')
        return redirect('/abattoir_list')
    context = {
        "title": title,
        "form": form,
     }
    return render(request, "entry.html",context)


def abattoir_list(request):
    title = 'List of approved abattoir'
    queryset = Abattoir.objects.filter(approve_one='approve').filter(approve_two='approve')
    queryset1stAppr = Abattoir.objects.filter(approve_one=None).filter(approve_two=None)
    countqueryset1stAppr = queryset1stAppr.count()
    
    queryset2ndAppr = Abattoir.objects.filter(approve_one='Approve').filter(approve_two=None)
    countqueryset2ndAppr = queryset2ndAppr.count()

    form = SearchForm(request.POST or None)
    context = {
         "title": title,
         "queryset": queryset,
         "countqueryset1stAppr": countqueryset1stAppr,
         "countqueryset2ndAppr": countqueryset2ndAppr,
         "form": form,
    }
    if request.method == 'POST':
            queryset = Abattoir.objects.all().order_by('-timestamp').filter(abattoir_name__icontains=form['abattoir_name'].value(),users_name__icontains=form['users_name'].value())
            context = {
            "title": title,
            "queryset": queryset,
            "countqueryset1stAppr": countqueryset1stAppr,
            "countqueryset2ndAppr": countqueryset2ndAppr,
            "form": form,
            }
            # if form['export_to_CSV'].value() == True:
            #      response = HttpResponse(content_type='text/csv')
            #      response['Content-Disposition'] = 'attachment; filename="Abattoir list.csv"'
            #      writer = csv.writer(response)
            #      writer.writerow(['CLINICAL NAME', 'IP Address', 'MAC ADDRESS', 'OS', 'USERNAME', 'LOCATION', 'PURCHASE DATE', 'TIMESTAMP'])
            #      instance = queryset
            #      for row in instance:
            #          writer.writerow([row.abattoir_name, row.IP_address, row.MAC_address, row.operating_system.all(), row.users_name, row.location, row.purchase_date, row.timestamp])
            #      return response
    return render(request, "abattoir_list.html",context)


def abattoir_edit(request, id=None):    
    instance = get_object_or_404(Abattoir, id=id)
    form = AbattoirForm(request.POST or None, instance=instance)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        form.save_m2m()
        messages.success(request, 'Successfully Saved')
        return redirect('/abattoir_list')
    context = {
            "title": 'Edit ' + str(instance.abattoir_name),
            "instance": instance,
            "form": form,
        }
    return render(request, "entry.html", context)


def abattoir_delete(request, id=None):
        instance = get_object_or_404(Abattoir, id=id)
        instance.delete()
        return redirect("abattoir_list")



def abattoir_approve_one_list(request):
    title = 'List of unapprove_one abattoirs'
    queryset = Abattoir.objects.exclude(approve_one='approve_one')
    form = SearchForm(request.POST or None)
    context = {
         "title": title,
         "queryset": queryset,
         "form": form,
    }
    if request.method == 'POST':
            queryset = Abattoir.objects.all().order_by('-timestamp').filter(abattoir_name__icontains=form['abattoir_name'].value())
            context = {
            "title": title,
            "queryset": queryset,
            "form": form,
            }
    return render(request, "abattoir_approve_list.html",context)


def abattoir_approve_one_edit(request, id=None):    
    instance = get_object_or_404(Abattoir, id=id)
    form = AbattoirapproveOneForm(request.POST or None, instance=instance)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        form.save_m2m()
        messages.success(request, 'Successfully Saved')
        return redirect('/abattoir_approve_list')
    context = {
            "title": 'Edit ',
            "instance": instance,
            "form": form,
        }
    return render(request, "entry.html", context)



def abattoir_approve_two_list(request):
    title = 'List of unapprove_one abattoirs'
    queryset = Abattoir.objects.filter(approve_one='Approve').filter(approve_two=None)
    form = SearchForm(request.POST or None)
    context = {
         "title": title,
         "queryset": queryset,
         "form": form,
    }
    if request.method == 'POST':
            queryset = Abattoir.objects.all().order_by('-timestamp').filter(abattoir_name__icontains=form['abattoir_name'].value())
            context = {
            "title": title,
            "queryset": queryset,
            "form": form,
            }
    return render(request, "abattoir_approve_list.html",context)


def abattoir_approve_two_edit(request, id=None):    
    instance = get_object_or_404(Abattoir, id=id)
    form = AbattoirapproveTwoForm(request.POST or None, instance=instance)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        form.save_m2m()
        messages.success(request, 'Successfully Saved')
        return redirect('/abattoir_approve_list')
    context = {
            "title": 'Edit ',
            "instance": instance,
            "form": form,
        }
    return render(request, "entry.html", context)



def locality_entry(request):
    title = 'Add Locality'
    form = LocalityForm(request.POST or None) 
    if form.is_valid():
        instance = form.save(commit=False)
        instance.employee = str(request.user)
        form.save()
        form.save_m2m()
        messages.success(request, 'Successfully Saved')
        return redirect('/locality_list')
    context = {
        "title": title,
        "form": form,
     }
    return render(request, "entry.html",context)


def locality_list(request):
    title = 'List of approved localities'
    queryset = Locality.objects.filter(approve_one='approve').filter(approve_two='approve')
    queryset1stAppr = Locality.objects.filter(approve_one=None).filter(approve_two=None)
    countqueryset1stAppr = queryset1stAppr.count()
    
    queryset2ndAppr = Locality.objects.filter(approve_one='Approve').filter(approve_two=None)
    countqueryset2ndAppr = queryset2ndAppr.count()

    form = SearchForm(request.POST or None)
    context = {
         "title": title,
         "queryset": queryset,
         "countqueryset1stAppr": countqueryset1stAppr,
         "countqueryset2ndAppr": countqueryset2ndAppr,
         "form": form,
    }
    if request.method == 'POST':
            queryset = Locality.objects.all().order_by('-timestamp').filter(locality_name__icontains=form['locality_name'].value(),users_name__icontains=form['users_name'].value())
            context = {
            "title": title,
            "queryset": queryset,
            "countqueryset1stAppr": countqueryset1stAppr,
            "countqueryset2ndAppr": countqueryset2ndAppr,
            "form": form,
            }
            # if form['export_to_CSV'].value() == True:
            #      response = HttpResponse(content_type='text/csv')
            #      response['Content-Disposition'] = 'attachment; filename="Locality list.csv"'
            #      writer = csv.writer(response)
            #      writer.writerow(['CLINICAL NAME', 'IP Address', 'MAC ADDRESS', 'OS', 'USERNAME', 'LOCATION', 'PURCHASE DATE', 'TIMESTAMP'])
            #      instance = queryset
            #      for row in instance:
            #          writer.writerow([row.locality_name, row.IP_address, row.MAC_address, row.operating_system.all(), row.users_name, row.location, row.purchase_date, row.timestamp])
            #      return response
    return render(request, "locality_list.html",context)


def locality_edit(request, id=None):    
    instance = get_object_or_404(Locality, id=id)
    form = LocalityForm(request.POST or None, instance=instance)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        form.save_m2m()
        messages.success(request, 'Successfully Saved')
        return redirect('/locality_list')
    context = {
            "title": 'Edit ',
            "instance": instance,
            "form": form,
        }
    return render(request, "entry.html", context)


def locality_delete(request, id=None):
        instance = get_object_or_404(Locality, id=id)
        instance.delete()
        return redirect("locality_list")



def locality_approve_one_list(request):
    title = 'List of unapproved localities'
    queryset = Locality.objects.filter(approve_one=None).filter(approve_two=None)
    form = SearchForm(request.POST or None)
    context = {
         "title": title,
         "queryset": queryset,
         "form": form,
    }
    if request.method == 'POST':
            queryset = Locality.objects.all().order_by('-timestamp').filter(locality_name__icontains=form['locality_name'].value())
            context = {
            "title": title,
            "queryset": queryset,
            "form": form,
            }
    return render(request, "locality_approve_list.html",context)


def locality_approve_one_edit(request, id=None):    
    instance = get_object_or_404(Locality, id=id)
    form = LocalityapproveOneForm(request.POST or None, instance=instance)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        form.save_m2m()
        messages.success(request, 'Successfully Saved')
        return redirect('/locality_approve_list')
    context = {
            "title": 'Edit ',
            "instance": instance,
            "form": form,
        }
    return render(request, "entry.html", context)


def locality_approve_two_list(request):
    title = 'List of unapproved localities'
    queryset = Locality.objects.filter(approve_one='Approve').filter(approve_two=None)
    form = SearchForm(request.POST or None)
    context = {
         "title": title,
         "queryset": queryset,
         "form": form,
    }
    if request.method == 'POST':
            queryset = Locality.objects.all().order_by('-timestamp').filter(locality_name__icontains=form['locality_name'].value())
            context = {
            "title": title,
            "queryset": queryset,
            "form": form,
            }
    return render(request, "locality_approve_list.html",context)


def locality_approve_two_edit(request, id=None):    
    instance = get_object_or_404(Locality, id=id)
    form = LocalityapproveTwoForm(request.POST or None, instance=instance)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        form.save_m2m()
        messages.success(request, 'Successfully Saved')
        return redirect('/locality_approve_list')
    context = {
            "title": 'Edit ',
            "instance": instance,
            "form": form,
        }
    return render(request, "entry.html", context)



def vaccination_entry(request):
    title = 'Add Vaccination'
    form = VaccinationForm(request.POST or None) 
    if form.is_valid():
        instance = form.save(commit=False)
        instance.employee = str(request.user)
        form.save()
        form.save_m2m()
        messages.success(request, 'Successfully Saved')
        return redirect('/vaccination_list')
    context = {
        "title": title,
        "form": form,
     }
    return render(request, "entry.html",context)


def vaccination_list(request):
    title = 'List of approved vaccination'
    queryset = Vaccination.objects.filter(approve_one='approve').filter(approve_two='approve')
    queryset1stAppr = Vaccination.objects.filter(approve_one=None).filter(approve_two=None)
    countqueryset1stAppr = queryset1stAppr.count()
    
    queryset2ndAppr = Vaccination.objects.filter(approve_one='Approve').filter(approve_two=None)
    countqueryset2ndAppr = queryset2ndAppr.count()
    form = SearchForm(request.POST or None)
    context = {
         "title": title,
         "queryset": queryset,
         "countqueryset1stAppr": countqueryset1stAppr,
         "countqueryset2ndAppr": countqueryset2ndAppr,
         "form": form,
    }
    if request.method == 'POST':
            queryset = Vaccination.objects.all().order_by('-timestamp').filter(vaccination_name__icontains=form['vaccination_name'].value(),users_name__icontains=form['users_name'].value())
            context = {
            "title": title,
            "queryset": queryset,
            "countqueryset1stAppr": countqueryset1stAppr,
            "countqueryset2ndAppr": countqueryset2ndAppr,
            "form": form,
            }
            # if form['export_to_CSV'].value() == True:
            #      response = HttpResponse(content_type='text/csv')
            #      response['Content-Disposition'] = 'attachment; filename="Vaccination list.csv"'
            #      writer = csv.writer(response)
            #      writer.writerow(['CLINICAL NAME', 'IP Address', 'MAC ADDRESS', 'OS', 'USERNAME', 'LOCATION', 'PURCHASE DATE', 'TIMESTAMP'])
            #      instance = queryset
            #      for row in instance:
            #          writer.writerow([row.vaccination_name, row.IP_address, row.MAC_address, row.operating_system.all(), row.users_name, row.location, row.purchase_date, row.timestamp])
            #      return response
    return render(request, "vaccination_list.html",context)


def vaccination_edit(request, id=None):    
    instance = get_object_or_404(Vaccination, id=id)
    form = VaccinationForm(request.POST or None, instance=instance)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        form.save_m2m()
        messages.success(request, 'Successfully Saved')
        return redirect('/vaccination_list')
    context = {
            "title": 'Edit ',
            "instance": instance,
            "form": form,
        }
    return render(request, "entry.html", context)


def vaccination_delete(request, id=None):
        instance = get_object_or_404(Vaccination, id=id)
        instance.delete()
        return redirect("vaccination_list")



def vaccination_approve_one_list(request):
    title = 'List of unapproved vaccinations'
    queryset = Vaccination.objects.filter(approve_one=None).filter(approve_two=None)
    form = SearchForm(request.POST or None)
    context = {
         "title": title,
         "queryset": queryset,
         "form": form,
    }
    if request.method == 'POST':
            queryset = Vaccination.objects.all().order_by('-timestamp').filter(vaccination_name__icontains=form['vaccination_name'].value())
            context = {
            "title": title,
            "queryset": queryset,
            "form": form,
            }
    return render(request, "vaccination_approve_list.html",context)


def vaccination_approve_one_edit(request, id=None):    
    instance = get_object_or_404(Vaccination, id=id)
    form = VaccinationapproveOneForm(request.POST or None, instance=instance)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        form.save_m2m()
        messages.success(request, 'Successfully Saved')
        return redirect('/vaccination_approve_list')
    context = {
            "title": 'Edit ',
            "instance": instance,
            "form": form,
        }
    return render(request, "entry.html", context)


def vaccination_approve_two_list(request):
    title = 'List of unapproved vaccinations'
    queryset = Vaccination.objects.filter(approve_one='Approve').filter(approve_two=None)
    form = SearchForm(request.POST or None)
    context = {
         "title": title,
         "queryset": queryset,
         "form": form,
    }
    if request.method == 'POST':
            queryset = Vaccination.objects.all().order_by('-timestamp').filter(vaccination_name__icontains=form['vaccination_name'].value())
            context = {
            "title": title,
            "queryset": queryset,
            "form": form,
            }
    return render(request, "vaccination_approve_list.html",context)


def vaccination_approve_two_edit(request, id=None):    
    instance = get_object_or_404(Vaccination, id=id)
    form = VaccinationapproveTwoForm(request.POST or None, instance=instance)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        form.save_m2m()
        messages.success(request, 'Successfully Saved')
        return redirect('/vaccination_approve_list')
    context = {
            "title": 'Edit ',
            "instance": instance,
            "form": form,
        }
    return render(request, "entry.html", context)



def vetInfraIndustry_entry(request):
    title = 'Add VetInfraIndustry'
    form = VetInfraIndustryForm(request.POST or None) 
    if form.is_valid():
        instance = form.save(commit=False)
        instance.employee = str(request.user)
        form.save()
        form.save_m2m()
        messages.success(request, 'Successfully Saved')
        return redirect('/vetInfraIndustry_list')
    context = {
        "title": title,
        "form": form,
     }
    return render(request, "entry.html",context)


def vetInfraIndustry_list(request):
    title = 'List of approved vetInfraIndustry'
    queryset = VetInfraIndustry.objects.filter(approve_one='approve').filter(approve_two='approve')
    queryset1stAppr = VetInfraIndustry.objects.filter(approve_one=None).filter(approve_two=None)
    countqueryset1stAppr = queryset1stAppr.count()
    
    queryset2ndAppr = VetInfraIndustry.objects.filter(approve_one='Approve').filter(approve_two=None)
    countqueryset2ndAppr = queryset2ndAppr.count()
    form = SearchForm(request.POST or None)
    context = {
         "title": title,
         "queryset": queryset,
         "countqueryset1stAppr": countqueryset1stAppr,
         "countqueryset2ndAppr": countqueryset2ndAppr,
         "form": form,
    }
    if request.method == 'POST':
            queryset = VetInfraIndustry.objects.all().order_by('-timestamp').filter(vetInfraIndustry_name__icontains=form['vetInfraIndustry_name'].value(),users_name__icontains=form['users_name'].value())
            context = {
            "title": title,
            "queryset": queryset,
            "countqueryset1stAppr": countqueryset1stAppr,
            "countqueryset2ndAppr": countqueryset2ndAppr,
            "form": form,
            }
            # if form['export_to_CSV'].value() == True:
            #      response = HttpResponse(content_type='text/csv')
            #      response['Content-Disposition'] = 'attachment; filename="VetInfraIndustry list.csv"'
            #      writer = csv.writer(response)
            #      writer.writerow(['CLINICAL NAME', 'IP Address', 'MAC ADDRESS', 'OS', 'USERNAME', 'LOCATION', 'PURCHASE DATE', 'TIMESTAMP'])
            #      instance = queryset
            #      for row in instance:
            #          writer.writerow([row.vetInfraIndustry_name, row.IP_address, row.MAC_address, row.operating_system.all(), row.users_name, row.location, row.purchase_date, row.timestamp])
            #      return response
    return render(request, "vetInfraIndustry_list.html",context)


def vetInfraIndustry_edit(request, id=None):    
    instance = get_object_or_404(VetInfraIndustry, id=id)
    form = VetInfraIndustryForm(request.POST or None, instance=instance)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        form.save_m2m()
        messages.success(request, 'Successfully Saved')
        return redirect('/vetInfraIndustry_list')
    context = {
            "title": 'Edit ',
            "instance": instance,
            "form": form,
        }
    return render(request, "entry.html", context)


def vetInfraIndustry_delete(request, id=None):
        instance = get_object_or_404(VetInfraIndustry, id=id)
        instance.delete()
        return redirect("vetInfraIndustry_list")



def vetInfraIndustry_approve_one_list(request):
    title = 'List of unapproved vetInfraIndustrys'
    queryset = VetInfraIndustry.objects.filter(approve_one=None).filter(approve_two=None)
    form = SearchForm(request.POST or None)
    context = {
         "title": title,
         "queryset": queryset,
         "form": form,
    }
    if request.method == 'POST':
            queryset = VetInfraIndustry.objects.all().order_by('-timestamp').filter(vetInfraIndustry_name__icontains=form['vetInfraIndustry_name'].value())
            context = {
            "title": title,
            "queryset": queryset,
            "form": form,
            }
    return render(request, "vetInfraIndustry_approve_list.html",context)


def vetInfraIndustry_approve_one_edit(request, id=None):    
    instance = get_object_or_404(VetInfraIndustry, id=id)
    form = VetInfraIndustryapproveOneForm(request.POST or None, instance=instance)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        form.save_m2m()
        messages.success(request, 'Successfully Saved')
        return redirect('/vetInfraIndustry_approve_list')
    context = {
            "title": 'Edit ',
            "instance": instance,
            "form": form,
        }
    return render(request, "entry.html", context)


def vetInfraIndustry_approve_two_list(request):
    title = 'List of unapproved vetInfraIndustrys'
    queryset = VetInfraIndustry.objects.filter(approve_one='Approve').filter(approve_two=None)
    form = SearchForm(request.POST or None)
    context = {
         "title": title,
         "queryset": queryset,
         "form": form,
    }
    if request.method == 'POST':
            queryset = VetInfraIndustry.objects.all().order_by('-timestamp').filter(vetInfraIndustry_name__icontains=form['vetInfraIndustry_name'].value())
            context = {
            "title": title,
            "queryset": queryset,
            "form": form,
            }
    return render(request, "vetInfraIndustry_approve_list.html",context)


def vetInfraIndustry_approve_two_edit(request, id=None):    
    instance = get_object_or_404(VetInfraIndustry, id=id)
    form = VetInfraIndustryapproveTwoForm(request.POST or None, instance=instance)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        form.save_m2m()
        messages.success(request, 'Successfully Saved')
        return redirect('/vetInfraIndustry_approve_list')
    context = {
            "title": 'Edit ',
            "instance": instance,
            "form": form,
        }
    return render(request, "entry.html", context)



def permits_entry(request):
    title = 'Add Permits'
    form = PermitsForm(request.POST or None) 
    if form.is_valid():
        instance = form.save(commit=False)
        instance.employee = str(request.user)
        form.save()
        form.save_m2m()
        messages.success(request, 'Successfully Saved')
        return redirect('/permits_list')
    context = {
        "title": title,
        "form": form,
     }
    return render(request, "entry.html",context)


def permits_list(request):
    title = 'List of approved permits'
    queryset = Permits.objects.filter(approve_one='approve').filter(approve_two='approve')
    queryset1stAppr = Permits.objects.filter(approve_one=None).filter(approve_two=None)
    countqueryset1stAppr = queryset1stAppr.count()
    
    queryset2ndAppr = Permits.objects.filter(approve_one='Approve').filter(approve_two=None)
    countqueryset2ndAppr = queryset2ndAppr.count()
    form = SearchForm(request.POST or None)
    context = {
         "title": title,
         "queryset": queryset,
         "countqueryset1stAppr": countqueryset1stAppr,
         "countqueryset2ndAppr": countqueryset2ndAppr,
         "form": form,
    }
    if request.method == 'POST':
            queryset = Permits.objects.all().order_by('-timestamp').filter(permits_name__icontains=form['permits_name'].value(),users_name__icontains=form['users_name'].value())
            context = {
            "title": title,
            "queryset": queryset,
            "countqueryset1stAppr": countqueryset1stAppr,
            "countqueryset2ndAppr": countqueryset2ndAppr,
            "form": form,
            }
            # if form['export_to_CSV'].value() == True:
            #      response = HttpResponse(content_type='text/csv')
            #      response['Content-Disposition'] = 'attachment; filename="Permits list.csv"'
            #      writer = csv.writer(response)
            #      writer.writerow(['CLINICAL NAME', 'IP Address', 'MAC ADDRESS', 'OS', 'USERNAME', 'LOCATION', 'PURCHASE DATE', 'TIMESTAMP'])
            #      instance = queryset
            #      for row in instance:
            #          writer.writerow([row.permits_name, row.IP_address, row.MAC_address, row.operating_system.all(), row.users_name, row.location, row.purchase_date, row.timestamp])
            #      return response
    return render(request, "permits_list.html",context)


def permits_edit(request, id=None):    
    instance = get_object_or_404(Permits, id=id)
    form = PermitsForm(request.POST or None, instance=instance)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        form.save_m2m()
        messages.success(request, 'Successfully Saved')
        return redirect('/permits_list')
    context = {
            "title": 'Edit ',
            "instance": instance,
            "form": form,
        }
    return render(request, "entry.html", context)


def permits_delete(request, id=None):
        instance = get_object_or_404(Permits, id=id)
        instance.delete()
        return redirect("permits_list")



def permits_approve_one_list(request):
    title = 'List of unapproved permits'
    queryset = Permits.objects.filter(approve_one=None).filter(approve_two=None)
    form = SearchForm(request.POST or None)
    context = {
         "title": title,
         "queryset": queryset,
         "form": form,
    }
    if request.method == 'POST':
            queryset = Permits.objects.all().order_by('-timestamp').filter(permits_name__icontains=form['permits_name'].value())
            context = {
            "title": title,
            "queryset": queryset,
            "form": form,
            }
    return render(request, "permits_approve_list.html",context)


def permits_approve_one_edit(request, id=None):    
    instance = get_object_or_404(Permits, id=id)
    form = PermitsapproveOneForm(request.POST or None, instance=instance)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        form.save_m2m()
        messages.success(request, 'Successfully Saved')
        return redirect('/permits_approve_list')
    context = {
            "title": 'Edit ',
            "instance": instance,
            "form": form,
        }
    return render(request, "entry.html", context)


def permits_approve_two_list(request):
    title = 'List of unapproved permits'
    queryset = Permits.objects.filter(approve_one='Approve').filter(approve_two=None)
    form = SearchForm(request.POST or None)
    context = {
         "title": title,
         "queryset": queryset,
         "form": form,
    }
    if request.method == 'POST':
            queryset = Permits.objects.all().order_by('-timestamp').filter(permits_name__icontains=form['permits_name'].value())
            context = {
            "title": title,
            "queryset": queryset,
            "form": form,
            }
    return render(request, "permits_approve_list.html",context)


def permits_approve_two_edit(request, id=None):    
    instance = get_object_or_404(Permits, id=id)
    form = PermitsapproveTwoForm(request.POST or None, instance=instance)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        form.save_m2m()
        messages.success(request, 'Successfully Saved')
        return redirect('/permits_approve_list')
    context = {
            "title": 'Edit ',
            "instance": instance,
            "form": form,
        }
    return render(request, "entry.html", context)



def transportFleet_entry(request):
    title = 'Add TransportFleet'
    form = TransportFleetForm(request.POST or None) 
    if form.is_valid():
        instance = form.save(commit=False)
        instance.employee = str(request.user)
        form.save()
        form.save_m2m()
        messages.success(request, 'Successfully Saved')
        return redirect('/transportFleet_list')
    context = {
        "title": title,
        "form": form,
     }
    return render(request, "entry.html",context)



def transportFleet_list(request):
    title = 'List of approved transportFleet'
    queryset = TransportFleet.objects.filter(approve_one='approve').filter(approve_two='approve')
    queryset1stAppr = TransportFleet.objects.filter(approve_one=None).filter(approve_two=None)
    countqueryset1stAppr = queryset1stAppr.count()
    
    queryset2ndAppr = TransportFleet.objects.filter(approve_one='Approve').filter(approve_two=None)
    countqueryset2ndAppr = queryset2ndAppr.count()
    form = SearchForm(request.POST or None)
    context = {
         "title": title,
         "queryset": queryset,
         "countqueryset1stAppr": countqueryset1stAppr,
         "countqueryset2ndAppr": countqueryset2ndAppr,
         "form": form,
    }
    if request.method == 'POST':
            queryset = TransportFleet.objects.all().order_by('-timestamp').filter(transportFleet_name__icontains=form['transportFleet_name'].value(),users_name__icontains=form['users_name'].value())
            context = {
            "title": title,
            "queryset": queryset,
            "countqueryset1stAppr": countqueryset1stAppr,
            "countqueryset2ndAppr": countqueryset2ndAppr,
            "form": form,
            }
            # if form['export_to_CSV'].value() == True:
            #      response = HttpResponse(content_type='text/csv')
            #      response['Content-Disposition'] = 'attachment; filename="TransportFleet list.csv"'
            #      writer = csv.writer(response)
            #      writer.writerow(['CLINICAL NAME', 'IP Address', 'MAC ADDRESS', 'OS', 'USERNAME', 'LOCATION', 'PURCHASE DATE', 'TIMESTAMP'])
            #      instance = queryset
            #      for row in instance:
            #          writer.writerow([row.transportFleet_name, row.IP_address, row.MAC_address, row.operating_system.all(), row.users_name, row.location, row.purchase_date, row.timestamp])
            #      return response
    return render(request, "transportFleet_list.html",context)


def transportFleet_edit(request, id=None):    
    instance = get_object_or_404(TransportFleet, id=id)
    form = TransportFleetForm(request.POST or None, instance=instance)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        form.save_m2m()
        messages.success(request, 'Successfully Saved')
        return redirect('/transportFleet_list')
    context = {
            "title": 'Edit ',
            "instance": instance,
            "form": form,
        }
    return render(request, "entry.html", context)


def transportFleet_delete(request, id=None):
        instance = get_object_or_404(TransportFleet, id=id)
        instance.delete()
        return redirect("transportFleet_list")



def transportFleet_approve_one_list(request):
    title = 'List of unapproved transportFleets'
    queryset = TransportFleet.objects.filter(approve_one=None).filter(approve_two=None)
    form = SearchForm(request.POST or None)
    context = {
         "title": title,
         "queryset": queryset,
         "form": form,
    }
    if request.method == 'POST':
            queryset = TransportFleet.objects.all().order_by('-timestamp').filter(transportFleet_name__icontains=form['transportFleet_name'].value())
            context = {
            "title": title,
            "queryset": queryset,
            "form": form,
            }
    return render(request, "transportFleet_approve_list.html",context)


def transportFleet_approve_one_edit(request, id=None):    
    instance = get_object_or_404(TransportFleet, id=id)
    form = TransportFleetapproveOneForm(request.POST or None, instance=instance)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        form.save_m2m()
        messages.success(request, 'Successfully Saved')
        return redirect('/transportFleet_approve_list')
    context = {
            "title": 'Edit ',
            "instance": instance,
            "form": form,
        }
    return render(request, "entry.html", context)


def transportFleet_approve_two_list(request):
    title = 'List of unapproved transportFleets'
    queryset = TransportFleet.objects.filter(approve_one='Approve').filter(approve_two=None)
    form = SearchForm(request.POST or None)
    context = {
         "title": title,
         "queryset": queryset,
         "form": form,
    }
    if request.method == 'POST':
            queryset = TransportFleet.objects.all().order_by('-timestamp').filter(transportFleet_name__icontains=form['transportFleet_name'].value())
            context = {
            "title": title,
            "queryset": queryset,
            "form": form,
            }
    return render(request, "transportFleet_approve_list.html",context)


def transportFleet_approve_two_edit(request, id=None):    
    instance = get_object_or_404(TransportFleet, id=id)
    form = TransportFleetapproveTwoForm(request.POST or None, instance=instance)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        form.save_m2m()
        messages.success(request, 'Successfully Saved')
        return redirect('/transportFleet_approve_list')
    context = {
            "title": 'Edit ',
            "instance": instance,
            "form": form,
        }
    return render(request, "entry.html", context)



def production_entry(request):
    title = 'Add Production'
    form = ProductionForm(request.POST or None) 
    if form.is_valid():
        instance = form.save(commit=False)
        instance.employee = str(request.user)
        form.save()
        form.save_m2m()
        messages.success(request, 'Successfully Saved')
        return redirect('/production_list')
    context = {
        "title": title,
        "form": form,
     }
    return render(request, "entry.html",context)



def production_list(request):
    title = 'List of approved production'
    queryset = Production.objects.filter(approve_one='approve').filter(approve_two='approve')
    queryset1stAppr = Lab.objects.filter(approve_one=None).filter(approve_two=None)
    countqueryset1stAppr = queryset1stAppr.count()
    
    queryset2ndAppr = Lab.objects.filter(approve_one='Approve').filter(approve_two=None)
    countqueryset2ndAppr = queryset2ndAppr.count()
    form = SearchForm(request.POST or None)
    context = {
         "title": title,
         "queryset": queryset,
         "countqueryset1stAppr": countqueryset1stAppr,
         "countqueryset2ndAppr": countqueryset2ndAppr,
         "form": form,
    }
    if request.method == 'POST':
            queryset = Production.objects.all().order_by('-timestamp').filter(production_name__icontains=form['production_name'].value(),users_name__icontains=form['users_name'].value())
            context = {
            "title": title,
            "queryset": queryset,
            "countqueryset1stAppr": countqueryset1stAppr,
            "countqueryset2ndAppr": countqueryset2ndAppr,
            "form": form,
            }
            # if form['export_to_CSV'].value() == True:
            #      response = HttpResponse(content_type='text/csv')
            #      response['Content-Disposition'] = 'attachment; filename="Production list.csv"'
            #      writer = csv.writer(response)
            #      writer.writerow(['CLINICAL NAME', 'IP Address', 'MAC ADDRESS', 'OS', 'USERNAME', 'LOCATION', 'PURCHASE DATE', 'TIMESTAMP'])
            #      instance = queryset
            #      for row in instance:
            #          writer.writerow([row.production_name, row.IP_address, row.MAC_address, row.operating_system.all(), row.users_name, row.location, row.purchase_date, row.timestamp])
            #      return response
    return render(request, "production_list.html",context)


def production_edit(request, id=None):    
    instance = get_object_or_404(Production, id=id)
    form = ProductionForm(request.POST or None, instance=instance)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        form.save_m2m()
        messages.success(request, 'Successfully Saved')
        return redirect('/production_list')
    context = {
            "title": 'Edit ' + str(instance.production_name),
            "instance": instance,
            "form": form,
        }
    return render(request, "entry.html", context)


def production_delete(request, id=None):
        instance = get_object_or_404(Production, id=id)
        instance.delete()
        return redirect("production_list")



def production_approve_one_list(request):
    title = 'List of unapproved productions'
    queryset = Production.objects.filter(approve_one=None).filter(approve_two=None)
    form = SearchForm(request.POST or None)
    context = {
         "title": title,
         "queryset": queryset,
         "form": form,
    }
    if request.method == 'POST':
            queryset = Production.objects.all().order_by('-timestamp').filter(production_name__icontains=form['production_name'].value())
            context = {
            "title": title,
            "queryset": queryset,
            "form": form,
            }
    return render(request, "production_approve_list.html",context)


def production_approve_one_edit(request, id=None):    
    instance = get_object_or_404(Production, id=id)
    form = ProductionapproveOneForm(request.POST or None, instance=instance)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        form.save_m2m()
        messages.success(request, 'Successfully Saved')
        return redirect('/production_approve_list')
    context = {
            "title": 'Edit ' ,
            "instance": instance,
            "form": form,
        }
    return render(request, "entry.html", context)


def production_approve_two_list(request):
    title = 'List of unapproved productions'
    queryset = Production.objects.filter(approve_one='Approve').filter(approve_two=None)
    form = SearchForm(request.POST or None)
    context = {
         "title": title,
         "queryset": queryset,
         "form": form,
    }
    if request.method == 'POST':
            queryset = Production.objects.all().order_by('-timestamp').filter(production_name__icontains=form['production_name'].value())
            context = {
            "title": title,
            "queryset": queryset,
            "form": form,
            }
    return render(request, "production_approve_list.html",context)


def production_approve_two_edit(request, id=None):    
    instance = get_object_or_404(Production, id=id)
    form = ProductionapproveTwoForm(request.POST or None, instance=instance)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        form.save_m2m()
        messages.success(request, 'Successfully Saved')
        return redirect('/production_approve_list')
    context = {
            "title": 'Edit ' ,
            "instance": instance,
            "form": form,
        }
    return render(request, "entry.html", context)




def settings(request):
    title = 'Add quarter'
    form = QuarterForm(request.POST or None)
    if form.is_valid():
        form.save()
        messages.success(request, 'Successfully Saved')
        return redirect('/disease_report_list')
    context = {
        "title": title,
        "form": form,
    }       
    return render(request, "settings.html",context)





























        # form.save_m2m()