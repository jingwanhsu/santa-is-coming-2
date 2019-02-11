# -*- coding: utf-8 -*-

import sys
import csv
import pprint
from random import shuffle
import smtplib
from email.mime.text import MIMEText
import os.path

input_filename = sys.argv[1]
output_filename = input_filename + '.out'

def read(input_filename):
  participants = []
  with open(input_filename) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    for line_count, row in enumerate(csv_reader):
      if line_count == 0:
        columns = row
        continue
      participant = {}
      for i, column in enumerate(columns):
        participant[column] = row[i]
      participants.append(participant)
    return participants

def write(output_filename, results):
  with open(output_filename, 'w') as csvfile:
      fieldnames = results[0].keys()
      csv_writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
      csv_writer.writeheader()
      for row in results:
        csv_writer.writerow(row)

def send(to_email, data):
  gmail_user = 'yourgmail@gmail.com'
  gmail_password = 'yourgmailpassword'

  sent_from = gmail_user
  subject = 'Christmas gifts exchange'
  body = '''Your should send gift to %s !!!
Their address is %s
receipent: %s
phone number: %s
What they want: %s
''' % (data['name'], 
  data['address'], 
  data['receipent'], 
  data['phone'], 
  data['wants'])

  msg = MIMEText(body)
  msg['Subject'] = subject
  msg['From'] = sent_from
  msg['To'] = to_email
  email_text = msg.as_string()

  try:
    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    server.ehlo()
    server.login(gmail_user, gmail_password)
    server.sendmail(sent_from, [to_email], email_text)
    server.close()
    print('Email sent!')
  except Exception as e:
    print('Something went wrong...')
    print(e)


if (os.path.isfile(output_filename)):
  print('Result exists! resend!')
  participants = read(output_filename)
else:
  participants = read(input_filename)

  pprint.pprint(participants)

  print('Shuffle and write!')
  shuffle(participants)
  write(output_filename, participants)
  # print(list(map(lambda x: x['name'], participants)))

count = len(participants)
for i, person in enumerate(participants):
  sent_to = participants[(i-1) % count]['email']
  send(sent_to, person)
  # print(f'send {person["name"]}\'s data to {sent_to}')
