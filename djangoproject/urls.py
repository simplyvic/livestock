from django.conf.urls import include, url
from django.contrib import admin
from djangoapp.views import *

urlpatterns = [
    # Examples:
    # url(r'^$', 'djangoproject.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', home, name='home'),
    url(r'^notice_board_entry/$', notice_board_entry, name='notice_board_entry'),
    url(r'^notice_board_list/$', notice_board_list, name='notice_board_list'),
    url(r'^notice_board_list/(?P<id>\d+)/edit$', notice_board_edit, name='notice_board_edit'),
    url(r'^notice_board_list/(?P<id>\d+)/detail$', notice_board_detail, name='notice_board_detail'),

    url(r'^clinical_entry/$', clinical_entry, name='clinical_entry'),
    url(r'^clinical_list/$', clinical_list, name='clinical_list'),
    url(r'^clinical_list/in_progress$', clinical_list_in_progress, name='clinical_list_in_progress'),
    url(r'^clinical_list/(?P<id>\d+)/edit$', clinical_edit, name='clinical_edit'),
    url(r'^clinical_list/(?P<id>\d+)/approve_one$', clinical_approve_one_edit, name='clinical_approve_one_edit'),
    url(r'^clinical_list/(?P<id>\d+)/approve_two$', clinical_approve_two_edit, name='clinical_approve_two_edit'),
    url(r'^clinical_list/(?P<id>\d+)/delete$', clinical_delete, name='clinical_delete'),
    url(r'^clinical_approve_one_list/$', clinical_approve_one_list, name='clinical_approve_one_list'),
    url(r'^clinical_approve_two_list/$', clinical_approve_two_list, name='clinical_approve_two_list'),
    url(r'^clinical_list/(?P<id>\d+)/detail$', clinical_detail, name='clinical_detail'),

    url(r'^disease_report_entry/$', disease_report_entry, name='disease_report_entry'),
    url(r'^disease_report_list/$', disease_report_list, name='disease_report_list'),
    url(r'^disease_report_list/in_progress$', disease_report_list_in_progress, name='disease_report_list_in_progress'),
    url(r'^disease_report_list/(?P<id>\d+)/edit$', disease_report_edit, name='disease_report_edit'),
    url(r'^disease_report_list/(?P<id>\d+)/approve_one$', disease_report_approve_one_edit, name='disease_report_approve_one_edit'),
    url(r'^disease_report_list/(?P<id>\d+)/approve_two$', disease_report_approve_two_edit, name='disease_report_approve_two_edit'),
    url(r'^disease_report_list/(?P<id>\d+)/delete$', disease_report_delete, name='disease_report_delete'),
    url(r'^disease_report_approve_one_list/$', disease_report_approve_one_list, name='disease_report_approve_one_list'),
    url(r'^disease_report_approve_two_list/$', disease_report_approve_two_list, name='disease_report_approve_two_list'),
    url(r'^disease_report/(?P<id>\d+)/detail$', disease_report_detail, name='disease_report_detail'),

    url(r'^lab_entry/$', lab_entry, name='lab_entry'),
    url(r'^lab_list/$', lab_list, name='lab_list'),
    url(r'^lab_list/in_progress$', lab_list_in_progress, name='lab_list_in_progress'),
    url(r'^lab_list/(?P<id>\d+)/edit$', lab_edit, name='lab_edit'),
    url(r'^lab_list/(?P<id>\d+)/approve_one$', lab_approve_one_edit, name='lab_approve_one_edit'),
    url(r'^lab_list/(?P<id>\d+)/approve_two$', lab_approve_two_edit, name='lab_approve_two_edit'),
    url(r'^lab_list/(?P<id>\d+)/delete$', lab_delete, name='lab_delete'),
    url(r'^lab_approve_one_list/$', lab_approve_one_list, name='lab_approve_one_list'),
    url(r'^lab_approve_two_list/$', lab_approve_two_list, name='lab_approve_two_list'),
    url(r'^lab/(?P<id>\d+)/detail$', lab_detail, name='lab_detail'),

    url(r'^abattoir_entry/$', abattoir_entry, name='abattoir_entry'),
    url(r'^abattoir_list/$', abattoir_list, name='abattoir_list'),
    url(r'^abattoir_list/in_progress$', abattoir_list_in_progress, name='abattoir_list_in_progress'),
    url(r'^abattoir_list/(?P<id>\d+)/edit$', abattoir_edit, name='abattoir_edit'),
    url(r'^abattoir_list/(?P<id>\d+)/approve_one$', abattoir_approve_one_edit, name='abattoir_approve_one_edit'),
    url(r'^abattoir_list/(?P<id>\d+)/approve_two$', abattoir_approve_two_edit, name='abattoir_approve_two_edit'),
    url(r'^abattoir_list/(?P<id>\d+)/delete$', abattoir_delete, name='abattoir_delete'),
    url(r'^abattoir_approve_one_list/$', abattoir_approve_one_list, name='abattoir_approve_one_list'),
    url(r'^abattoir_approve_two_list/$', abattoir_approve_two_list, name='abattoir_approve_two_list'),
    url(r'^abattoir/(?P<id>\d+)/detail$', abattoir_detail, name='abattoir_detail'),

    url(r'^locality_entry/$', locality_entry, name='locality_entry'),
    url(r'^locality_list/$', locality_list, name='locality_list'),
    url(r'^locality_list/in_progress$', locality_list_in_progress, name='locality_list_in_progress'),
    url(r'^locality_list/(?P<id>\d+)/edit$', locality_edit, name='locality_edit'),
    url(r'^locality_list/(?P<id>\d+)/approve_one$', locality_approve_one_edit, name='locality_approve_one_edit'),
    url(r'^locality_list/(?P<id>\d+)/approve_two$', locality_approve_two_edit, name='locality_approve_two_edit'),
    url(r'^locality_list/(?P<id>\d+)/delete$', locality_delete, name='locality_delete'),
    url(r'^locality_approve_one_list/$', locality_approve_one_list, name='locality_approve_one_list'),
    url(r'^locality_approve_two_list/$', locality_approve_two_list, name='locality_approve_two_list'),
    url(r'^locality/(?P<id>\d+)/detail$', locality_detail, name='locality_detail'),

    url(r'^vaccination_entry/$', vaccination_entry, name='vaccination_entry'),
    url(r'^vaccination_list/$', vaccination_list, name='vaccination_list'),
    url(r'^vaccination_list/in_progress$', vaccination_list_in_progress, name='vaccination_list_in_progress'),
    url(r'^vaccination_list/(?P<id>\d+)/edit$', vaccination_edit, name='vaccination_edit'),
    url(r'^vaccination_list/(?P<id>\d+)/approve_one$', vaccination_approve_one_edit, name='vaccination_approve_one_edit'),
    url(r'^vaccination_list/(?P<id>\d+)/approve_two$', vaccination_approve_two_edit, name='vaccination_approve_two_edit'),
    url(r'^vaccination_list/(?P<id>\d+)/delete$', vaccination_delete, name='vaccination_delete'),
    url(r'^vaccination_approve_one_list/$', vaccination_approve_one_list, name='vaccination_approve_one_list'),
    url(r'^vaccination_approve_two_list/$', vaccination_approve_two_list, name='vaccination_approve_two_list'),
    url(r'^vaccination/(?P<id>\d+)/detail$', vaccination_detail, name='vaccination_detail'),

    url(r'^vetInfraIndustry_entry/$', vetInfraIndustry_entry, name='vetInfraIndustry_entry'),
    url(r'^vetInfraIndustry_list/$', vetInfraIndustry_list, name='vetInfraIndustry_list'),
    url(r'^vetInfraIndustry_list/in_progress$', vetInfraIndustry_list_in_progress, name='vetInfraIndustry_list_in_progress'),
    url(r'^vetInfraIndustry_list/(?P<id>\d+)/edit$', vetInfraIndustry_edit, name='vetInfraIndustry_edit'),
    url(r'^vetInfraIndustry_list/(?P<id>\d+)/approve_one$', vetInfraIndustry_approve_one_edit, name='vetInfraIndustry_approve_one_edit'),
    url(r'^vetInfraIndustry_list/(?P<id>\d+)/approve_two$', vetInfraIndustry_approve_two_edit, name='vetInfraIndustry_approve_two_edit'),
    url(r'^vetInfraIndustry_list/(?P<id>\d+)/delete$', vetInfraIndustry_delete, name='vetInfraIndustry_delete'),
    url(r'^vetInfraIndustry_approve_one_list/$', vetInfraIndustry_approve_one_list, name='vetInfraIndustry_approve_one_list'),
    url(r'^vetInfraIndustry_approve_two_list/$', vetInfraIndustry_approve_two_list, name='vetInfraIndustry_approve_two_list'),
    url(r'^vetInfraIndustry/(?P<id>\d+)/detail$', vetInfraIndustry_detail, name='vetInfraIndustry_detail'),

    url(r'^permits_entry/$', permits_entry, name='permits_entry'),
    url(r'^permits_list/$', permits_list, name='permits_list'),
    url(r'^permits_list/in_progress$', permits_list_in_progress, name='permits_list_in_progress'),
    url(r'^permits_list/(?P<id>\d+)/edit$', permits_edit, name='permits_edit'),
    url(r'^permits_list/(?P<id>\d+)/approve_one$', permits_approve_one_edit, name='permits_approve_one_edit'),
    url(r'^permits_list/(?P<id>\d+)/approve_two$', permits_approve_two_edit, name='permits_approve_two_edit'),
    url(r'^permits_list/(?P<id>\d+)/delete$', permits_delete, name='permits_delete'),
    url(r'^permits_approve_one_list/$', permits_approve_one_list, name='permits_approve_one_list'),
    url(r'^permits_approve_two_list/$', permits_approve_two_list, name='permits_approve_two_list'),
    url(r'^permits/(?P<id>\d+)/detail$', permits_detail, name='permits_detail'),

    url(r'^transportFleet_entry/$', transportFleet_entry, name='transportFleet_entry'),
    url(r'^transportFleet_list/$', transportFleet_list, name='transportFleet_list'),
    url(r'^transportFleet_list/in_progress$', transportFleet_list_in_progress, name='transportFleet_list_in_progress'),
    url(r'^transportFleet_list/(?P<id>\d+)/edit$', transportFleet_edit, name='transportFleet_edit'),
    url(r'^transportFleet_list/(?P<id>\d+)/approve_one$', transportFleet_approve_one_edit, name='transportFleet_approve_one_edit'),
    url(r'^transportFleet_list/(?P<id>\d+)/approve_two$', transportFleet_approve_two_edit, name='transportFleet_approve_two_edit'),
    url(r'^transportFleet_list/(?P<id>\d+)/delete$', transportFleet_delete, name='transportFleet_delete'),
    url(r'^transportFleet_approve_one_list/$', transportFleet_approve_one_list, name='transportFleet_approve_one_list'),
    url(r'^transportFleet_approve_two_list/$', transportFleet_approve_two_list, name='transportFleet_approve_two_list'),
    url(r'^transportFleet/(?P<id>\d+)/detail$', transportFleet_detail, name='transportFleet_detail'),

    url(r'^production_entry/$', production_entry, name='production_entry'),
    url(r'^production_list/$', production_list, name='production_list'),
    url(r'^production_list/in_progress$', production_list_in_progress, name='production_list_in_progress'),
    url(r'^production_list/(?P<id>\d+)/edit$', production_edit, name='production_edit'),
    url(r'^production_list/(?P<id>\d+)/approve_one$', production_approve_one_edit, name='production_approve_one_edit'),
    url(r'^production_list/(?P<id>\d+)/approve_two$', production_approve_two_edit, name='production_approve_two_edit'),
    url(r'^production_list/(?P<id>\d+)/delete$', production_delete, name='production_delete'),
    url(r'^production_approve_one_list/$', production_approve_one_list, name='production_approve_one_list'),
    url(r'^production_approve_two_list/$', production_approve_two_list, name='production_approve_two_list'),
    url(r'^production/(?P<id>\d+)/detail$', production_detail, name='production_detail'),

    url(r'^accounts/', include('registration.backends.default.urls')),
    url(r'^settings/$', settings, name='settings'),
    url(r'^notice_board/$', notice_board, name='notice_board'),


]