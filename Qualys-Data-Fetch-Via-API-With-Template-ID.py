import requests
import re
import time
import pandas as pd
import io
 
# Global variables
domain = "https://qualysapi.qg1.apps.qualys.ae"  # Replace with your Qualys domain
template_id = "459498"  # Replace with your template ID
report_title = "Prasad_Test_Report"  # Replace with your report title
 
# Launch the report in Qualys
def launch_report():
    url = f'{domain}/api/2.0/fo/report/?'
    headers = {
        'Authorization': 'Basic pastebase64here',
        'X-Requested-With': 'Power BI'
    }
    data = {
        'action': 'launch',
        'template_id': template_id,
        'report_title': report_title,
        'output_format': 'csv',
        'hide_header': 1
    }
    response = requests.post(url, data=data, headers=headers)
 
    # Match the report ID from the response
    match = re.search(r'<VALUE>(\d+)</VALUE>', response.text)
    if match:
        report_id = match.group(1)
        return report_id
    else:
        raise ValueError("Failed to get report ID from the API response. Please check the response and API call.")
 
# Download the report using the report ID
def download_report(report_id):
    url = f'{domain}/api/2.0/fo/report/?action=fetch&id={report_id}'
    headers = {
        'Authorization': 'Basic dXNlcm5hbWU6cGFzc3dvcmQ=', // add your credentials with this format (username:password) in base64 format 
        'X-Requested-With': 'Power BI'
    }
 
    while True:
        response = requests.post(url, headers=headers)
        # Check if the report is still being generated
        if '<CODE>1001</CODE>' in response.text:
            time.sleep(60)  # Wait if report is still generating
            continue
        elif '<CODE>500</CODE>' in response.text:
            raise ValueError("An error occurred. Please check the report ID or status.")
        elif '<CODE>7001</CODE>' in response.text:
            time.sleep(60)  # Wait if report is not ready yet
            continue
        # Return the content if the report is ready
        return response.text
 
# Save the report content as CSV
def save_report_to_csv(report_content):
    # Save the CSV content directly to a file
    csv_filename = f"{template_id}.csv"
    with open(csv_filename, 'w', newline='', encoding='utf-8') as file:
        file.write(report_content)
 
# Main function to launch, download, and save the report
def main():
    try:
        report_id = launch_report()
        report_content = download_report(report_id)
        save_report_to_csv(report_content)
    except Exception as e:
        # If you want to log errors, consider writing to a log file instead of printing
        with open('error_log.txt', 'a') as log_file:
            log_file.write(f"Error occurred: {e}\n")
 
if __name__ == "__main__":
    main()