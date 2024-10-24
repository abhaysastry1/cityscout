import requests
import json
import urllib.parse

# # DoltHub API endpoint
# # Replace {org} and {repo} with your organization name and repository name
# api_url = "https://www.dolthub.com/api/v1alpha1/Liquidata/fbi-nibrs/branches/main/sql"

# Conversion from string method:
def query(base_url, sql_query):
    """
    Converts a SQL query string into a URL-encoded API URL for DoltHub.
    
    Args:
        base_url (str): The base API URL, e.g., "https://www.dolthub.com/api/v1alpha1/dolthub/fbi-nibrs/main?q="
        sql_query (str): The SQL query string to convert.
    
    Returns:
        str: The complete API URL with the SQL query encoded.
    """
    # URL encode the SQL query
    encoded_query = urllib.parse.quote(sql_query)

    # Construct the full API URL by appending the encoded query to the base URL
    api_url = f"{base_url}{encoded_query}"
    
    return api_url

# Example usage
base_url = "https://www.dolthub.com/api/v1alpha1/dolthub/fbi-nibrs/main?q=" # Don't change
# old_sql_query = "SELECT * FROM `agency_participation` WHERE `STATE_ID` = 40 ORDER BY `DATA_YEAR` ASC, `AGENCY_PARTICIPATION_ID` DESC LIMIT 10;"
sql_query = """SELECT nibrs_victim_offense.VICTIM_ID, nibrs_offense.OFFENSE_ID, nibrs_offense_type.OFFENSE_TYPE_ID, `OFFENSE_NAME`, `age_num`, nibrs_victim.incident_id, nibrs_incident.agency_id, cde_agencies.city_name, cde_agencies.state_abbr, cde_agencies.state_id
                FROM `nibrs_victim_offense` JOIN `nibrs_offense` JOIN `nibrs_offense_type` JOIN `nibrs_victim` JOIN   `nibrs_incident` JOIN `cde_agencies`
                WHERE cde_agencies.state_id = 22
                LIMIT 1000"""



# Convert the SQL query to a URL
new_api_url = query(base_url, sql_query)

# Output the API
print("NEW API URL:", new_api_url)

new_response = response = requests.get(new_api_url)
if new_response.status_code == 200:
    # Parse the JSON response
    data = new_response.json() 

    # Output the data
    print(json.dumps(data, indent=4)) # Output prints to console
else:
    # If there was an error, print the error code and message
    print(f"Error: {new_response.status_code}, {new_response.text}")
