# python-cURL
Python automation to send REST API requests using cURL

# Usage

To run the script

GET
```bash
py curl.py --get /api/route 
```

POST
- Prompt to select or edit request body
```bash
py curl.py --post /api/route  
```

PUT
- Prompt to select or edit request body
```bash
py curl.py --put /api/route  
```

DELETE
- Prompt to select or edit request body
```bash
py curl.py --delete /api/route  
```

Adding custom path for request body data
- Else defaults to req_body.txt
```bash
py curl.py --<method> /api/route -d <custom_path>
py curl.py --<method> /api/route --data <custom_path>
 ```
 
Adding custom url
- Else defaults to 'http://localhost:4000'
```bash
py curl.py --<method> /api/route -u <custom_url>
py curl.py --<method> /api/route --url <custom_url>
```


Format the request body data for the POST, PUT or DELETE requests as follows:
```json
{
"name": "random_name",
"data": "random_data"
}
```

Formats that would give an error (To be improved):
- Comma at the end of the last field
```json
{
"name": "random_name",
"data": "random_data",
}
```

# To Note
- Currently only supports Window -- Not tested on other OS yet such as MacOS and Linux
- Only works with fields containing one layer string; but not nested items such as object or arrays of any sort

# Add-on ideas
- Support for array and object to be sent in the request body
- Feature to cache the request route URL within a .txt file
