'''code to create a Python function that takes a list of URLs, attempts to download their content, 
and retries up to 3 times if an error occurs. Use appropriate error handling to manage different types 
of exceptions.'''
import requests
from requests.exceptions import HTTPError, Timeout, RequestException

def download_url_content(urls):
    results = {}
    
    for url in urls:
        attempts = 0
        success = False
        
        while attempts < 3 and not success:
            try:
                response = requests.get(url, timeout=5)
                response.raise_for_status() 
                results[url] = response.content
                success = True
            except HTTPError as http_err:
                print(f"HTTP error occurred for {url}: {http_err}")
                results[url] = f"HTTP error: {http_err}"
            except Timeout as timeout_err:
                print(f"Timeout error occurred for {url}: {timeout_err}")
                results[url] = f"Timeout error: {timeout_err}"
            except RequestException as req_err:
                print(f"Request error occurred for {url}: {req_err}")
                results[url] = f"Request error: {req_err}"
            except Exception as err:
                print(f"An error occurred for {url}: {err}")
                results[url] = f"Error: {err}"
            
            attempts += 1
            
            if not success:
                print(f"Retrying {url} ({attempts}/3)")
    
    return results

urls = [
    "https://www.example.com",
    "https://www.nonexistenturl.com", 
    "https://www.google.com"
]

content = download_url_content(urls)
for url, result in content.items():
    if isinstance(result, bytes):
        print(f"Content of {url} downloaded successfully.")
    else:
        print(f"Failed to download content from {url}: {result}")

