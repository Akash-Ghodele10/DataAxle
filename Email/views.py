from datetime import date
from django.core.mail import send_mail
from django.template.loader import render_to_string
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Employee
from .serializers import EmployeeSerializer

class SendBirthdayEmails(APIView):
    def post(self, request, format=None):
        today = date.today()
        employees = Employee.objects.filter(birthday__month=today.month, birthday__day=today.day)

        for employee in employees:
            subject = 'Happy Birthday!'
            message = render_to_string('birthday_email_template.html', {'employee': employee})
            from_email = 'your@example.com'
            recipient_list = [employee.email]

            send_mail(subject, message, from_email, recipient_list)

        return Response({"message": "Birthday emails sent successfully."})
