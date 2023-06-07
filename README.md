# marketing-subscriber-informer
 
A marketing script that sends mail to the subscribers about your newly published blog posts, information messages or announcements. 

## Requirements 
- smtplib 
- json
- boto3
- MIMEMultipart
- MIMEText 

And additionally a stable running cloud environment, which we use AWS here. 

## Usage 
1. The repo includes two scripts for now. First one (getsubscriber) collects the subscriber info from the user. And the second one (informsubscriber) sends emails to them about your little updates. Besides these, a csv file needs to be located in an Amazon S3 bucket with the necessary bucket permissions. 
2. Both scripts should be deployed on serverless app, like AWS Lambda. 
3. The user updates the csv file with the related subscriber info periodically or manually - by using getsubcriber.py, all data is stored in the csv file. 
4. The user can send all kinds of update messages to the subscribers whenever needed - by using informsubscriber.py, the message is sent to people via an SMTP server. 

## Additional Notes 
- The code might need to be refactored according to the current Lambda environment or SMTP server status. 