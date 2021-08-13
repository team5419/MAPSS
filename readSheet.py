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


@app.route('/delete_container', methods=["GET"])
def delete_container():

    name_of_item = json.loads(request.args.get('name'))

    service = build('sheets', 'v4', credentials=creds)

    # Call the Sheets API
    sheet = service.spreadsheets()

    result = sheet.values().get(spreadsheetId=SPREADSHEET_ID,
                                range="containers", majorDimension="COLUMNS").execute()

    # Get list of lists for sheet values
    values = result.get('values', [])

    rowToRemove = 1000

    for i in range(1, len(values[0])):
        if values[0][i] == name_of_item:
            rowToRemove = i

    request_body = {
        'requests': [
            {
                'deleteDimension': {
                    "range": {
                        "sheetId": 2047041623,
                        "dimension": "ROWS",
                        "startIndex": rowToRemove,
                        "endIndex": rowToRemove+1
                    }
                }
            }
        ]
    }

    service.spreadsheets().batchUpdate(
        spreadsheetId=SPREADSHEET_ID,
        body=request_body
    ).execute()

    return


@app.route('/get_all_containers', methods=["GET"])
def get_all_containers():
    service = build('sheets', 'v4', credentials=creds)

    # Call the Sheets API
    sheet = service.spreadsheets()
    result = sheet.values().get(spreadsheetId=SPREADSHEET_ID,
                                range="containers", majorDimension="COLUMNS").execute()

    # Get list of lists for sheet values
    values = result.get('values', [])

    return jsonify(values)


@app.route('/get_all_data', methods=["GET"])
def get_all_data():
    service = build('sheets', 'v4', credentials=creds)

    # Call the Sheets API
    sheet = service.spreadsheets()
    result = sheet.values().get(spreadsheetId=SPREADSHEET_ID,
                                range="digital_organizer", majorDimension="COLUMNS").execute()

    # Get list of lists for sheet values
    values = result.get('values', [])

    return jsonify(values)


@app.route('/', methods=['GET', 'POST'])
def app_home():
    return render_template("index3.html")

# Lets you pull from the github remote from the web interface


@app.route('/git_pull')
def get_ses():
    g = git.cmd.Git("")
    g.pull()
    return redirect('/', code=302)

# Pass in the tool that we want to locate


@app.route("/get_values", methods=["GET"])
def get_values():
    name_of_item = json.loads(request.args.get('name'))
    values = get_values2(name_of_item)
    return jsonify(values)


@app.route("/set_values_container", methods=["GET"])
def set_values_container():
    name_of_item = json.loads(request.args.get('name'))
    colour_of_item = json.loads(request.args.get('colour'))
    x_coordinate1 = json.loads(request.args.get('lat1'))
    y_coordinate1 = json.loads(request.args.get('lng1'))
    x_coordinate2 = json.loads(request.args.get('lat2'))
    y_coordinate2 = json.loads(request.args.get('lng2'))
    set_values_container_2(name_of_item, colour_of_item,
                           x_coordinate1, y_coordinate1, x_coordinate2, y_coordinate2)
    return 'success'


def set_values_container_2(name_of_item, colour_of_item, x_coordinate1, y_coordinate1, x_coordinate2, y_coordinate2):
    # Create a Credentials object from the service account's credentials and the scopes the application needs access to
    service = build('sheets', 'v4', credentials=creds)

    # Call the Sheets API
    sheet = service.spreadsheets()

    data = [[name_of_item, x_coordinate1, y_coordinate1,
             x_coordinate2, y_coordinate2, colour_of_item]]

    sheet.values().append(spreadsheetId=SPREADSHEET_ID, range="containers!A1:E1",
                          valueInputOption="USER_ENTERED", insertDataOption="INSERT_ROWS", body={"values": data}).execute()


@app.route("/set_values", methods=["GET"])
def set_values():
    name_of_item = json.loads(request.args.get('name'))
    x_coordinate = json.loads(request.args.get('lat'))
    y_coordinate = json.loads(request.args.get('lng'))
    shelf_number = json.loads(request.args.get("info"))
    set_values2(name_of_item, x_coordinate, y_coordinate, shelf_number)
    return


def set_values2(name_of_item, x_coordinate, y_coordinate, shelf_number):
    name_of_container = "Not on Shelf"
    service = build('sheets', 'v4', credentials=creds)

    # Call the Sheets API
    sheet = service.spreadsheets()

    result = sheet.values().get(spreadsheetId=SPREADSHEET_ID,
                                range="digital_organizer", majorDimension="COLUMNS").execute()

    result2 = sheet.values().get(spreadsheetId=SPREADSHEET_ID,
                                 range="containers", majorDimension="COLUMNS").execute()

    # Get list of lists for sheet values
    values = result.get('values', [])
    containers = result2.get('values', [])

    for i in range(1, len(containers[0])):
        if int(containers[1][i]) < int(x_coordinate) and int(containers[3][i]) > int(x_coordinate) and int(containers[2][i]) < int(y_coordinate) and int(containers[4][i]) > int(y_coordinate):
            name_of_container = containers[0][i]
        if int(containers[1][i]) > x_coordinate and int(containers[3][i]) < x_coordinate and int(containers[2][i]) > y_coordinate and int(containers[4][i]) < y_coordinate:
            name_of_container = containers[0][i]

    data = [[name_of_item, x_coordinate, y_coordinate,
             0, 0, shelf_number, name_of_container]]

    request = sheet.values().append(spreadsheetId=SPREADSHEET_ID, range="digital_organizer!A1:G1",
                                    valueInputOption="USER_ENTERED", insertDataOption="INSERT_ROWS", body={"values": data}).execute()


def get_values2(name_of_item):

    # Define list to return
    values_to_return = []
    values_of_item = []
    index = []

    service = build('sheets', 'v4', credentials=creds)

    # Call the Sheets API
    sheet = service.spreadsheets()
    result = sheet.values().get(spreadsheetId=SPREADSHEET_ID,
                                range="digital_organizer", majorDimension="COLUMNS").execute()

    # Get list of lists for sheet values
    values = result.get('values', [])

    # Get row number (index) of item (name_of_item)
    column = values[0]

    for i in range(len(column)):
        if(name_of_item == column[i]):
            index.append(i)

    # loop through rows of spreadsheet to get information
    for index in index:
        values_of_item = []
        for i in range(1, 7):
            values_of_item.append(values[i][index])
        values_to_return.append(values_of_item)

    return values_to_return


@app.route("/find_items_in_container", methods=["GET"])
def findItems():

    container = json.loads(request.args.get('name'))

    # Define list to return
    values_to_return = []

    service = build('sheets', 'v4', credentials=creds)

    # Call the Sheets API
    sheet = service.spreadsheets()
    result = sheet.values().get(spreadsheetId=SPREADSHEET_ID,
                                range="digital_organizer", majorDimension="COLUMNS").execute()

    # Get list of lists for sheet values
    values = result.get('values', [])

    # Get row number (index) of item (name_of_item)
    for i in range(len(values[0])):
        if values[6][i] == container:
            values_to_return.append(values[0][i])

    return jsonify(values_to_return)


@app.route("/remove_values", methods=["GET"])
def remove_values():
    x_coordinate = json.loads(request.args.get('lat'))
    y_coordinate = json.loads(request.args.get('lng'))
    remove_values2(x_coordinate, y_coordinate)


def remove_values2(x_coordinate, y_coordinate):
    service = build('sheets', 'v4', credentials=creds)

    # Call the Sheets API
    sheet = service.spreadsheets()

    result = sheet.values().get(spreadsheetId=SPREADSHEET_ID,
                                range="digital_organizer", majorDimension="COLUMNS").execute()

    # Get list of lists for sheet values
    values = result.get('values', [])

    rowToRemove = 1000

    for i in range(1, len(values[0])):
        if int(float(values[1][i])) == x_coordinate and int(float(values[2][i])) == y_coordinate:
            rowToRemove = i

    request_body = {
        'requests': [
            {
                'deleteDimension': {
                    "range": {
                        "sheetId": 0,
                        "dimension": "ROWS",
                        "startIndex": rowToRemove,
                        "endIndex": rowToRemove+1
                    }
                }
            }
        ]
    }

    service.spreadsheets().batchUpdate(
        spreadsheetId=SPREADSHEET_ID,
        body=request_body
    ).execute()


# print(get_values("Hammer"))
if __name__ == "__main__":
    app.run(debug=True)
