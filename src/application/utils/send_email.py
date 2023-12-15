import os
import uuid
import random

import pandas as pd

import pdfkit

from celery import shared_task

import smtplib

from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication

smtp_server = 'smtp.gmail.com'  # Replace with your SMTP server
smtp_port = 587  # Replace with the appropriate port number for your SMTP server
sender_email = os.environ["EMAIL"] # Replace with your email address
password = os.environ["EMAIL_SECRET_KEY"]  # Replace with your email password

def generate_otp(id = None):
    if id: 
        random.seed(id)
    otp = int(str(int(uuid.uuid1(int(random.random()))))[-6:])
    while (len(str(otp))) != 6:
        otp = int(str(int(uuid.uuid1(int(random.random()))))[-6:])
    return otp

def create_email(recipient, subject, body):
    global sender_email
    message = MIMEMultipart("alternative")
    message['From'] = sender_email
    message['To'] = recipient
    message['Subject'] = subject
    message.attach(body)
    return message;

def signup_template(otp):
    subject = "TicketNow - Signup: Email Verification OTP"
    html_body = """
            <div>
                <p>Hii there,</p>
                <p>Your sign-up - OTP/Verification code is</p>
                <h3>%d</h3>
                <br/>
                <br/>
                <p>If you did not request the verification code, ignore this e-mail.</p>
                <p>Valid for 15 min.</p>
                <p>Do not share this OTP with anyone.</p>

            </div>
        """ % (otp)
    return subject, MIMEText(html_body, 'html')

def password_reset_template(username, otp):
    subject = "TicketNow - Password Reset OTP"
    html_body = """
            <div>
                <p>Hii %s,</p>
                <p>Your password reset OTP/Verification code is</p>
                <h3>%d</h3>
                <br/>
                <br/>
                <p>If you did not request the verification code, ignore this e-mail.</p>
                <p>Valid for 15 min.</p>
                <p>Do not share this OTP with anyone.</p>
            </div>
        """ % (username, otp)
    return subject, MIMEText(html_body, 'html')

def login_template(username, otp):
    subject = "TicketNow - Login OTP"
    html_body = """
            <div>
                <p>Hii %s,</p>
                <p>Your login OTP/Verification code is</p>
                <h3>%d</h3>
                <br/>
                <br/>
                <p>If you did not request the verification code, ignore this e-mail.</p>
                <p>Valid for 15 min.</p>
                <p>Do not share this OTP with anyone.</p>

            </div>
        """ % (username, otp)
    return subject, MIMEText(html_body, 'html')

def ticket_booked_template(username, tdetails):
    subject = "TicketNow - Your Ticket(s) Booked Successfully"
    html_body = """
            <div>
                <p>Hii %s,</p>
                <p>Please find your upcoming show details here:</p>
                <p>Movie Name: <span>%s</span></p> <!-- movie name -->
                <p>Start Time: <span>%s</span></p>
                <p>Number of tickets booked: <span>%d for class %s.</span>
                <p>Price per ticket: &#8377; <span>%d</span>
                <p>Venue: <span>%s</span></p>
                <br/>
                <br/>
                <p>Please strictly follow the health guidelines at the venue.</p>
                <p>Please be environmental friendly and use no plastic or keep the usage minimal.</p>
                <br>
                <br>
                <p>For any queries, kindly write to this email.</p>
            </div>

        """ % (username, *tdetails)
    return subject, MIMEText(html_body, 'html')


def send_email(message, recipient):
    global sender_email
    global smtp_port
    global smtp_server
    global password
    try:
	    # Establish a connection to the SMTP server
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()  # Upgrade the connection to a secure encrypted SSL/TLS connection
        server.login(sender_email, password)  # Login to your email account
	    # Send the email
        server.sendmail(sender_email, recipient, message.as_string())
        print("Email sent successfully!")
        return True
    except Exception as e:
        print("Error: ", str(e))
        return False
    finally:
        server.quit()


@shared_task
def send_password_reset_otp_mail(username, otp, recipient):
    message = create_email(recipient, *password_reset_template(username, otp))
    send_email(message, recipient)

@shared_task
def send_login_otp_mail(username, otp, recipient):
    message = create_email(recipient, *login_template(username, otp))
    return send_email(message, recipient)

@shared_task
def send_signup_otp_mail(otp, recipient):
    message = create_email(recipient, *signup_template(otp))
    return send_email(message, recipient)

@shared_task
def send_ticket_details(username, recipient, tdetails):
    message = create_email(recipient, *ticket_booked_template(username, tdetails))
    return send_email(message, recipient)

########### PDF REPORT SECTION ############

def report_template(username):
    subject = "TicketNow - Report Attachments"
    html_body = """
            <div>
                <p>Hii %s,</p>
                <p>Please find the pdf and csv attachment here:</p>
                <br>
                <br>
                <p>For any queries, kindly write to this email.</p>
            </div>

        """ % (username)
    return subject, MIMEText(html_body, 'html')


def html_to_pdf(html_string, output_path):
    options = {
        'page-size': 'A4',
        'margin-top': '0.75in',
        'margin-right': '0.75in',
        'margin-bottom': '0.75in',
        'margin-left': '0.75in',
    }

    pdfkit.from_string(html_string, output_path, options=options)
    print("PDF generated successfully!")

def generate_pdf(report_data, pdf_name):
    tab_style='style="border-collapse: collapse; width: 100%; border: 1px solid black;"'
    th_style='style="border: 1px solid black; padding: 8px; text-align: left; background-color: #f2f2f2;"'
    td_style = 'style="border: 1px solid black; padding: 8px; text-align: left;"'
    table_html = f"""
    <div>
	<table border="1" {tab_style}>
	    <thead>
	        <tr>
	            <th {th_style}>Booking ID</th>
	            <th {th_style}>Booked At</th>
	            <th {th_style}>Movie Title</th>
	            <th {th_style}>Start Time</th>
	            <th {th_style}>Venue</th>
                <th {th_style}>Class</th>
	            <th {th_style}>No. of Seats</th>
	            <th {th_style}>Price (&#8377;)</th>
	            <th {th_style}>Total (&#8377;)</th>
	        </tr>
	    <thead>
    <tbody>
    """
    for booking in report_data:
        booking["total"] = booking["price"] * booking["no_of_seats"]  # Calculate total
        table_html += """
        <tr>
        """
        for (key, value) in booking.items():
            table_html += f"""
                <td {td_style}>{value}</td>
            """
        table_html += """
            </tr>
        """
    table_html += """
            </tbody>
        </table>
        </div>
    """
    report = html_to_pdf(table_html, pdf_name)
    return report;

@shared_task
def send_report(username, recipient, report_data, pdf_filename="report.pdf"):
    df = pd.DataFrame(report_data)
    csv_filename = "report.csv"
    df.to_csv(csv_filename)
    generate_pdf(report_data, pdf_filename)
    message = create_email(recipient, *report_template(username))

    with open(pdf_filename, "rb") as pdf_file:
        pdf_attachment = MIMEApplication(pdf_file.read(), _subtype="pdf")
        pdf_attachment.add_header("Content-Disposition", f"attachment; filename={pdf_filename}")
        message.attach(pdf_attachment)

    with open(csv_filename, 'rb') as attachment:
        part = MIMEApplication(attachment.read(), Name=csv_filename)
        part['Content-Disposition'] = f'attachment; filename="{csv_filename}"'
        message.attach(part)

    try:
        os.remove(csv_filename)
        os.remove(pdf_filename)
    except OSError as e:
        print(f"Error deleting file '{file_path}':{e}")

    return send_email(message, recipient)
