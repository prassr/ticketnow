from celery import shared_task

from datetime import datetime
from datetime import timedelta
from flask import jsonify
from application.dao import BookingDAO, AdminDAO
from application.utils import send_report, filter_bookings_by_date_range

class AdminReport():
    @classmethod
    def get(cls, start_date, end_date, sm):
        report_data = BookingDAO.generate_report()
        user = AdminDAO.get_admin()

        if start_date and end_date:
            report_data = filter_bookings_by_date_range(report_data, start_date, end_date)
        if sm == "1":
            report = send_report.delay(user.first_name +" "+user.last_name, user.email, report_data)
        return jsonify(report_data)



@shared_task
def generate_report(report_type, start_date=None, end_date=None):
    current_time = datetime.now()
    
    if report_type == 'monthly':
        breakpoint()
        start_date = datetime.now().replace(day=1)
        end_date = datetime.now()
        

    if report_type == 'weekly':
        start_date = datetime.now() - timedelta(days=7)
        end_date = datetime.now()

    if report_type == 'daily':
        start_date = datetime.now()
        end_date = datetime.now()

    query_string = {
        "start_date": start_date.strftime('%Y-%m-%d'),
        "end_date": end_date.strftime('%Y-%m-%d'),
        "sm": "1"
    }
    report = AdminReport.get(**query_string)
    print(report)

@shared_task
def sum(a=10, b=10):
    print("sum is "+ str(a + b))
    return a + b
