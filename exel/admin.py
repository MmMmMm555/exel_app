import os
import json
import pandas as pd
from datetime import datetime
from django.conf import settings
from django.http import HttpResponseRedirect
from django.contrib import admin
from django.urls import path, reverse
from django.utils.html import format_html
from .models import ReportsModel
from .authenticate import send_data


@admin.action(description='Send')
def send_report_action(modeladmin, request, queryset):
    if queryset.count() != 1:
        modeladmin.message_user(request, "Please select exactly one report.", level='error')
        return HttpResponseRedirect(request.get_full_path())
    
    report = queryset.first()
    
    if not report.file:
        modeladmin.message_user(request, "No file found in the selected report.", level='error')
        return HttpResponseRedirect(request.get_full_path())
    
    file_path = report.file.path
    
    try:
        df = pd.read_excel(file_path)
        json_data = df.to_json(orient='records')
        results_path = os.path.join(settings.MEDIA_ROOT, 'results')
        os.makedirs(results_path, exist_ok=True)
        
        json_file_path = os.path.join(results_path, f"{str(report.id)}-{report.title or 'report'}.json")
        with open(json_file_path, 'w') as json_file:
            json_file.write(json_data)
        
        modeladmin.message_user(request, f"JSON file created at {json_file_path}", level='success')
    except Exception as e:
        modeladmin.message_user(request, f"Error converting file: {e}", level='error')
    return HttpResponseRedirect(request.get_full_path())


class ReportsModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'creator', 'created_at', 'updated_at', 'sent_at', 'send_report', 'import_id')
    actions = [send_report_action]

    def send_report(self, obj):
        url = reverse('admin:send_report_action', args=[obj.id])
        return format_html(
            '<a class="button" href="{}">Send</a>',
            url
        )
    send_report.short_description = 'Send Report'
    send_report.allow_tags = True

    def get_urls(self):
        urls = super().get_urls()
        custom_urls = [
            path(
                'send_report_action/<int:report_id>/',
                self.admin_site.admin_view(self.send_report_view),
                name='send_report_action',
            ),
        ]
        return custom_urls + urls

    def send_report_view(self, request, report_id):
        report = self.get_object(request, report_id)
        if not report:
            self.message_user(request, "Report not found.", level='error')
            return HttpResponseRedirect('../')
        if not report.file:
            self.message_user(request, "No file found in the selected report.", level='error')
            return HttpResponseRedirect('../')
        file_path = report.file.path
        try:
            df = pd.read_excel(file_path)
            json_data = df.to_json(orient='records')
            code, response = send_data(data=json_data)
            if code == 0:
                results_path = os.path.join(settings.MEDIA_ROOT, 'results')
                os.makedirs(results_path, exist_ok=True)
                json_file_path = os.path.join(results_path, f'{str(report.id)}-{report.title or "report"}.json')
                with open(json_file_path, 'w') as json_file:
                    json_file.write(json_data)
                report.sent_at = datetime.now()
                report.import_id = response
                report.save()
                self.message_user(request, f"JSON file created at {json_file_path}", level='success')
            else:
                self.message_user(request, f"Error sending report: xxx {response} xxx", level='error')
        except Exception as e:
            self.message_user(request, f"Error converting file: {e}", level='error')
        return HttpResponseRedirect('/admin/exel/reportsmodel/')


admin.site.register(ReportsModel, ReportsModelAdmin)
