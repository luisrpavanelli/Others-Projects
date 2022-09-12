#Given the following JSON document
import glob
import json
 
# Data to be written
dictionary = {
"claimId": "99999-100000",
"payee": {
"id": 9999,
"role": "Payee"
},
"claimDateTime": 1634860244000,
"invoiceCount": 7, "status": "LoadComplete", "invoiceIds": [
"XXA15839", "XXA25829", "XXA35832", "XXA45830", "XXA55831", "XXA65833", "XXA75834"
],
"jobNumber": 100000,
 
"fileName": "XXXXXX20211021235044.xml",
"fileId": 99999,
"fileDateTime": 1634860244000,
"receivedDateTime": 1634922275533, "process": "TRANSACT", "transmitterId": "XXX", "retailerId": "RETAILERID", "plantName": "XXX1", "totalStoreCount": 2,
"totalOfferCount": 21,
"totalRecordCount": 27,
"totalCouponCount": 166,
"totalFaceValueAmount": 445.58
}

file_dir = Question 5.py #file location
files = glob.glob(file_dir+'*.json')
key = 'payee'
files_with_key = []
for fl in files:
    f = open(fl)
    json_data = json.load(f)
    if key == json_data['payee']:
        files_with_key.append(fl)

print(files_with_key)


# Serializing json
json_object = json.dumps(dictionary, indent=4)
 
# Writing to sample.json
with open("sample.json", "w") as outfile:
    outfile.write(json_object)

# Opening JSON file
with open('sample.json', 'r') as openfile:
 
    # Reading from json file
    json_object = json.load(openfile)
 
print(json_object)
print(type(json_object))