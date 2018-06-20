import json
import argparse

def json_csv(json_string):
    try:
        json_obj = json.loads(json_string)
    except:
        return "Error! Incorrect JSON format."

    if (type(json_obj) == dict):
        csv = dict_func(json_obj)

    if (type(json_obj) == list):
        csv = list_func(json_obj)

    return csv

def dict_func(d):
    csv_string = ''
    keys = list(d.keys())

    for i in range(len(keys)):
        if i == len(keys)-1:
            csv_string = csv_string+keys[i]+'\n'
        else:
            csv_string = csv_string+keys[i]+', '

    for i in range(len(keys)):
        if i == len(keys)-1:
            csv_string = csv_string + str(d[keys[i]]) + '\n'
        else:
            csv_string = csv_string + str(d[keys[i]]) + ', '

    return csv_string

def unique_append(e, l):
    if e not in l:
        e.append(l)

def list_func(l):
    all_keys = []
    csv_string = ''
    for i in range(len(l)):
        entry = l[i]
        entry_keys = entry.keys()
        for key in entry_keys:
            if key not in all_keys:
                all_keys.append(key)

    for i in range(len(all_keys)):
        if i == len(all_keys)-1:
            csv_string = csv_string+all_keys[i]+'\n'
        else:
            csv_string = csv_string+all_keys[i]+', '

    for i in range(len(l)):
        for j in range(len(all_keys)):
            try:
                if j == len(all_keys)-1:
                    csv_string = csv_string + str(l[i][all_keys[j]]) + '\n'
                else:
                    csv_string = csv_string + str(l[i][all_keys[j]]) + ', '
            except KeyError:
                if j == len(all_keys)-1:
                    csv_string = csv_string + 'na'+'\n'
                else:
                    csv_string = csv_string + 'na'+', '
                
    return csv_string

def json_csv_file():
    try:
        with open('file.json') as f:
            json_obj = json.load(f)
    except:
        return 'Error! Incorrect JSON format.'

    if (type(json_obj) == dict):
        csv = dict_func(json_obj)

    if (type(json_obj) == list):
        csv = list_func(json_obj)

    file = open("file.csv", "wb") #ab+ to read and append to file
    file.write(bytes(csv, 'UTF-8'))
    file.close()

    return None

def handle_uploaded_file(f):
    with open('file.json', 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)
    return json_csv_file()