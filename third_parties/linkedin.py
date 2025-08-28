import os
import requests
from dotenv import load_dotenv

load_dotenv()

def scrape_linkedin_profile(linkedin_profile_url: str, mock: bool = False):
    """
    Scrape information from linkedin profiles
    """
    if mock:
        linkedin_profile_url = "https://gist.githubusercontent.com/devashish-roy/1c1a245f33d8a6d95a43117f05aee00e/raw/f9cd86c7bce3af5645967b02616f7120c93455f0/devashish_linkedin.json"
        response = requests.get(linkedin_profile_url, timeout=10)
    else:
        api_endpoint = "https://api.scrapin.io/v1/enrichment/profile"
        params = {
            "apikey" : os.environ["SCRAPIN_API_KEY"],
            "linkedInUrl": linkedin_profile_url
        }
        response = requests.get(api_endpoint, params=params, timeout=10)
    
    data = response.json().get("person")

    #remove items that doesnot have value
    data = {
        k:v 
        for k, v in data.items() if v not in ([], "", None)
    }

    return data



if __name__ == "__main__":
    print(
        scrape_linkedin_profile(linkedin_profile_url="https://www.linkedin.com/in/devashish-singha-roy/")
    )