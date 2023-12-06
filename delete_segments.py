import csv
import subprocess

csv_file_path = 'your_file.csv'
endpoint = 'https://mylogscaleurl/api/v1/repositories/'

# Open the CSV file and iterate through each row
with open(csv_file_path, 'r') as csvfile:
    reader = csv.DictReader(csvfile)
    
    for row in reader:
        # Extract values from the CSV columns
        repository_name = row['REPOSITORY_NAME']
        datasource_id = row['DATASOURCEID']
        segment_id = row['SEGMENTID']
        
        # Construct the URL
        url = f'{endpoint}{repository_name}/datasources/{datasource_id}/segments/{segment_id}/'
        
        # Use subprocess to make HTTP delete request with curl
        subprocess.run(['curl', '-X', 'DELETE', url])

print('HTTP delete requests completed.')