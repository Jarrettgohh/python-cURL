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

Format the request body data for the POST, PUT or DELETE requests as follows:
```json
{
"name": "random_name",
"data": "random_data"
}
```

# To Note
Currently only supports Window -- Not tested on other OS yet such as MacOS and Linux
