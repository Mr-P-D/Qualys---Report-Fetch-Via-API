# Qualys Report Fetching Via TemplateID
<br> Simple Python Script To Download Vulnerability Scan Results Via QualysAPI With The Help Of TemplateID.
<br> It is expected that you have already created a report template in Qualys Platform and know the TemplateID.

# Usage
python Qualys-Data-Fetch-Via-API-With-Template-ID.py


# Things to modify before execution
Global Variables modify as per your requirements:
<br> domain = " "        # Replace with your Qualys Qualys Platform
<br> template_id = " "   # Replace with your Report Template ID
<br> report_title = " "  # Replace with your Report Title / Name


<br> Basic authorization is used in the script:
<br> *dXNlcm5hbWU6cGFzc3dvcmQ=* is a placeholder, replace this with your qualys cloud platform credentials in username:password base64 encoded format.


Once above changes are done, You should be able to get CSV output of the TemplateID as expected.
