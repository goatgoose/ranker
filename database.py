import mysql.connector
import json

with open("config.json") as json_data_file:
    configs = json.load(json_data_file)

cnx = mysql.connector.connect(user=configs['mysql']['user'], password=configs['mysql']['passwd'],
                              host=configs['mysql']['host'],
                              database=configs['mysql']['db'])
cnx.close()