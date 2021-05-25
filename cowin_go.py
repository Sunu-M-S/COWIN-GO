#!/usr/bin/python3
import datetime
import requests
import json
import os

print(f" _|_|_|    _|_|    _|          _|  _|_|_|  _|      _|                _|_|_|    _|_|    ")

print(f"_|        _|    _|  _|          _|    _|    _|_|    _|              _|        _|    _|  ")

print(f"_|        _|    _|  _|    _|    _|    _|    _|  _|  _|  _|_|_|_|_|  _|  _|_|  _|    _|  ")

print(f"_|        _|    _|    _|  _|  _|      _|    _|    _|_|              _|    _|  _|    _|  ")

print(f"  _|_|_|    _|_|        _|  _|      _|_|_|  _|      _|                _|_|_|    _|_|    ")
                                                                                        


#headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; rv:78.0) Gecko/20100101 Firefox/78.0"}
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; rv:78.0) Gecko/20100101 Firefox/78.0',
    'Accept': 'application/json, text/plain, */*',
    'Accept-Language': 'en-US,en;q=0.5',
    'Origin': 'https://www.cowin.gov.in',
    'DNT': '1',
    'Connection': 'keep-alive',
    'Referer': 'https://www.cowin.gov.in/',
    'Sec-GPC': '1',
    'TE': 'Trailers',
    'If-None-Match': 'W/"82cc-itufIebzm+UWh8Q12arOUNFbXS4"',
}

def clear(): os.system('clear') #cls


#state
reponse1 = requests.get(f"https://cdn-api.co-vin.in/api/v2/admin/location/states", headers=headers)
raw_data1=reponse1.json()['states']
for data1 in raw_data1:
	print(f"{data1['state_id']}.{data1['state_name']}")
state=input("please select your state_id :")
clear()


#district_id
reponse2 = requests.get(f"https://cdn-api.co-vin.in/api/v2/admin/location/districts/{state}", headers=headers,)
raw_data2=reponse2.json()['districts']
for data2 in raw_data2:
	print(f"{data2['district_id']}.{data2['district_name']}")
id =input("please select your district_id :")
clear()


#id =554

#current_date = datetime.date.today()
#current_date = current_date.strftime("%d-%m-%Y")
#date=5-05-2021
current_date = datetime.date.today()
current_date = current_date.strftime("%d-%m-%Y")
#print(current_date)

params = (
    ('district_id',id),
    ('date',current_date)
)

response =requests.get('https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/calendarByDistrict',headers=headers, params=params)
raw_data=response.json()['centers']
counter =0
for data in raw_data:
	for current_data in data['sessions'] :
		if (current_data['available_capacity'] !=0):
		#print(center_id,name,vaccine,min_age_limit,date,fee_type	available_capacity_dose1 available_capacity_dose2
			print(f"| date :{current_data['date']} | name:{data['name']} | vaccine:{current_data['vaccine']} | dose1:{current_data['available_capacity_dose1']} | dose2:{current_data['available_capacity_dose2']} | total : {current_data['available_capacity']}|fee: {data['fee_type']}" )
			counter=counter+1


if counter==0:
	print(f"=============NO VACCINE AVAILABLE ===========================")
	

















