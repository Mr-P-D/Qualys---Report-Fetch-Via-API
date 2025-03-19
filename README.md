# Qualys-Report-Fetch-Via-API
Python Script to download the vulnerability scan results from QualysAPI


# Usage
python Qualys-Data-Fetch-Via-API-With-Template-ID.py


# Things to modify before execution
Global Variables modify as per your requirements:
<br> domain = " "        # Replace with your Qualys domain
<br> template_id = " "   # Replace with your template ID
<br> report_title = " "  # Replace with your report title


<br> Basic authorization is used in the script:
<br> *dXNlcm5hbWU6cGFzc3dvcmQ=* is a placeholder, replace this with your qualys cloud platform credentials in username:password base64 encoded format.


Once above changes are done, You should be able to get CSV output of the TemplateID as expected.
