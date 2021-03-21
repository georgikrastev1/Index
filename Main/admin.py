from django.contrib import admin
#import export
from import_export.admin import ImportExportModelAdmin
from django.shortcuts import redirect
from django.urls import path

from .models import Companies,FX, Financial_data, Peer_group_lists, Peer_group_Financial_data

# Register your models here.

class CompaniesAdmin(ImportExportModelAdmin):
    list_display = ['name', 'Stock_code', 'Peer_group', 'Fx_company']

class FXAdmin(ImportExportModelAdmin):
    list_display = ['currency', 'exchange_rate']

class Financial_dataAdmin(ImportExportModelAdmin):
    list_display = ['company_id', 'market_capitalization_original',"market_capitalization_euro","share_price_original",
                    "share_price_euro","shares_number","created_at"]

class Peer_group_listsAdmin(ImportExportModelAdmin):
    list_display = ['Group_name', 'Group_description']

class Peer_group_Financial_dataAdmin(ImportExportModelAdmin):
     list_display = ['Peer_group', 'Market_capitalization','Market_capitalization_percent','created_at']

admin.site.register(Companies,CompaniesAdmin)

admin.site.register(FX,FXAdmin)

admin.site.register(Financial_data,Financial_dataAdmin)

admin.site.register(Peer_group_Financial_data,Peer_group_Financial_dataAdmin)

admin.site.register(Peer_group_lists,Peer_group_listsAdmin)