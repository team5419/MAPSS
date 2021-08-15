# to do:
# - make it so it can return multiple locations if an item is in multiple locations
# - add number out variable

from googleapiclient.discovery import build
from google.oauth2.credentials import Credentials
from pprint import pprint
from googleapiclient import discovery
from google.oauth2 import service_account
from flask import Flask, jsonify, render_template, request, redirect
import json
import git
import configparser

config = configparser.ConfigParser()
config.read('auth.ini')
SPREADSHEET_ID = config.get('auth', 'SPREADSHEET_ID')

# Create a Credentials object from the service account's credentials and the scopes the application needs access to
SERVICE_ACCOUNT_FILE = 'keys.json'
SCOPES = ['https://www.googleapis.com/auth/spreadsheets']

creds = None
creds = service_account.Credentials.from_service_account_file(
    SERVICE_ACCOUNT_FILE, scopes=SCOPES)

app = Flask(__name__)

@app.route('/pick_container', methods=["GET"])
def pick_container(container):

    service = build('sheets', 'v4', credentials=creds)

    # Call the Sheets API
    sheet = service.spreadsheets()

    value = [[container]]
    body = {'values': value}

    #get items to change
    result1 = sheet.values().get(spreadsheetId=SPREADSHEET_ID, range="digital_organizer", majorDimension="COLUMNS").execute()
    values = result1.get('values', [])

    # update container
    service.spreadsheets().values().update(
        spreadsheetId=SPREADSHEET_ID, range="digital_organizer!G"+str(len(values[0])),
        valueInputOption="USER_ENTERED", body=body).execute()

pick_container("pi")