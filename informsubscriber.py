# This script gets a list of subscribers, and send a mail including the post URL with a stylish mail body. 
# It works on AWS Lambda with the integration of Amazon S3. 

import smtplib, sys, json
import boto3
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from datetime import datetime

def lambda_handler(event, context):
    #TODO implement 
    parser()
    return {
        'statusCode': 200, 
        'body': json.dumps('[INFO] The script has been worked successfully.')
    }

def parser():
    # PART 1. 
    # Set the bucket and csv file name. These values should be just names, not arn or url. 
    myBucket = "S3_BUCKET_NAME"
    myFile = "subscriber-list.csv" 

    # Read the object file from the bucket. 
    s3 = boto3.client("s3")
    response = s3.get_object(Bucket=myBucket, Key=myFile)
    file_content = response["Body"].read().decode("utf-8")

    # Parse the file content to extract the email addresses. 
    email_addresses = []
    lines = file_content.split("\n")
    for line in lines:
        columns = line.split(",")
        if len(columns) >= 2:
            email_addresses.append(columns[1])

    # Print the email addresses
    for email_address in email_addresses: 
        print(email_address)
    
    # PART 2. 
    # SMTP server setup. 
    mailserver = smtplib.SMTP("smtp.gmail.com", 587)
    mailserver.ehlo()
    mailserver.starttls()
    mailserver.login("SENDER_MAIL_ADDRESS", "SENDER_MAIL_PASS")
    
    sender = 'SENDER_MAIL_ADDRESS'
    recipients = [email_addresses]
    
    now = datetime.now()
    sentDate = now.strftime("%d/%m/%Y %H+3:%M")
 
    msg = MIMEMultipart()
    msg["From"] = sender
    msg["To"] = ", ".join(recipients)
    msg["Subject"] = str(input("\n\nSubject: ")) + str(" " + sentDate)
 
    body = str(input("Your message: "))
 
    body_text = MIMEText(body, "plain")
    msg.attach(body_text)
 
    mailserver.sendmail(msg["From"], recipients, msg.as_string())
    print("[INFO] The mail has been sent from AWS Lambda.")
    mailserver.close()