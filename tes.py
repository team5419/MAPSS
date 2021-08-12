from googleapiclient.discovery import build
from google.oauth2.credentials import Credentials
from pprint import pprint
from googleapiclient import discovery
from google.oauth2 import service_account
from flask import Flask, jsonify, render_template, request, redirect
import json
import git
import configparser

app = Flask(__name__)

config = configparser.ConfigParser()
config.read('auth.ini')
SPREADSHEET_ID = config.get('auth', 'SPREADSHEET_ID')

# Create a Credentials object from the service account's credentials and the scopes the application needs access to
SERVICE_ACCOUNT_FILE = 'keys.json'
SCOPES = ['https://www.googleapis.com/auth/spreadsheets']

creds = None
creds = service_account.Credentials.from_service_account_file(
    SERVICE_ACCOUNT_FILE, scopes=SCOPES)

def move_container(row, x1, x2, y1, y2):

    service = build('sheets', 'v4', credentials=creds)

    # Call the Sheets API
    sheet = service.spreadsheets()

    values = [[x1, y1, x2, y2]]
    body = {'values': values}

    service.spreadsheets().values().update(
        spreadsheetId=SPREADSHEET_ID, range="containers!B"+str(row)+":E"+str(row),
        valueInputOption="USER_ENTERED", body=body).execute()

    return

move_container(8, 0, 0, 50, 50)