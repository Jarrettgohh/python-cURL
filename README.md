# python-cURL
Python automation to send REST API requests using cURL

# Usage

To run the script

GET
```bash
py curl.py --get /api/route 
```

POST
- Would be prompted to select or edit request body
```bash
py curl.py --post /api/route  
```

PUT
- Would be prompted to select or edit request body
```bash
py curl.py --put /api/route  
```

DELETE
- Would be prompted to select or edit request body
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

# To Note
Currently only supports Window -- Not tested on other OS yet such as MacOS and Linux
