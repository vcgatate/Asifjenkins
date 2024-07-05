import requests

def get_jenkins_build_number(job_name, build_id):
    # Replace with your Jenkins URL
    jenkins_url = 'http://13.233.29.101:8080'

    # Jenkins API endpoint to get build information
    api_url = f'{jenkins_url}/job/{job_name}/{build_id}/api/json'

    try:
        # Send GET request to Jenkins API
        response = requests.get(api_url, auth=('username', 'password'))  # Replace with your Jenkins username and password or API token

        # Check if request was successful (status code 200)
        if response.status_code == 200:
            # Parse JSON response
            build_info = response.json()
            # Extract build number from JSON
            build_number = build_info['number']
            return build_number
        else:
            print(f"Failed to retrieve build information. Status code: {response.status_code}")
            return None

    except requests.RequestException as e:
        print(f"Error retrieving build information: {str(e)}")
        return None

# Example usage:
if __name__ == "__main__":
    job_name = 'monitoring'
    build_id = '7'  # This can be 'lastBuild', 'lastCompletedBuild', etc.
    build_number = get_jenkins_build_number(job_name, build_id)
    
    if build_number:
        print(f"Build number of '{job_name}' for build '{build_id}': {build_number}")
    else:
        print("Failed to retrieve build number")
