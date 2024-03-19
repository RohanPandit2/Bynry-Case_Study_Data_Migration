Python 3.6.1 (v3.6.1:69c0db5, Mar 21 2017, 18:41:36) [MSC v.1900 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> #Python Scripts for Automated Mapping
# Data Extraction Script
def extract_data():
# Connect to ABC Utility Company's databases
# Retrieve consumer data
consumer_data = query_consumer_data()
return consumer_data
# Data Mapping Script
def map_data(consumer_data):
mapped_data = []
for consumer in consumer_data:
mapped_consumer = {
'Consumer ID': consumer['Consumer ID'],
'First Name': consumer['Name'].split()[0],
'Last Name': consumer['Name'].split()[1],
'Address Line 1': consumer['Address'].split(',')[0],
'Address Line 2': consumer['Address'].split(',')[1] if len(consumer['Address'].split(',')) > 1 else '',
'City': consumer['Address'].split(',')[2],
'State': consumer['Address'].split(',')[3],
'Zip Code': consumer['Address'].split(',')[4],
'Phone Number': consumer['Contact Number'],
'Email Address': consumer['Email Address']
}
mapped_data.append(mapped_consumer)
return mapped_data
# Transformation and Loading Script
def transform_and_load(mapped_data):
# Transform and load data into SMART360
for consumer in mapped_data:
load_consumer_data(consumer)
# Main Script
if __name__ == "__main__":
consumer_data = extract_data()
mapped_data = map_data(consumer_data)
transform_and_load(mapped_data)
