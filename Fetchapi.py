import requests
import pandas as pd

# Get the page number from the user
page = input("Enter page number: ")

url = f"URL:api"

headers = {
    'Host': 'v1.example.com',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/115.0',
    'Accept': 'application/json, text/plain, */*',
    'Accept-Language': 'en-US,en;q=0.5',
    'Accept-Encoding': 'gzip, deflate',
    'Origin': 'example.com',
    'Referer': 'example.com',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-site',
    'Te': 'trailers',
}

response = requests.get(url, headers=headers)

# Check for successful response
if response.status_code == 200:
    data = response.json()
    # Print the entire JSON response for inspection
    print(data)
    # Extract email and name from the response data
    if 'user' in data:
        emails_and_names = [(d['user']['email'], d['user']['name']) for d in data['user']]
        # Create a DataFrame
        df = pd.DataFrame(emails_and_names, columns=['Email', 'Name'])
        # Save the DataFrame to a text file
        df.to_csv('output.txt', index=False, sep='\t')
        print("Output saved to output.txt")
    else:
        print("No 'user' data found in the JSON response.")
else:
    print(f"Failed to retrieve data. Status code: {response.status_code}")
