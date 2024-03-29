# python-cURL
Python automation to send REST API requests using `cURL`

# Python Version
- Python 3.10


# Package Installation
- Install neccessary packages
```
pip install termcolor
```

# Usage

To run the script

GET
```bash
py py_curl.py --get /api/route 
```

POST
- Prompt to select or edit request body
```bash
py py_curl.py --post /api/route  
```

PUT
- Prompt to select or edit request body
```bash
py py_curl.py --put /api/route  
```

DELETE
- Prompt to select or edit request body
```bash
py py_curl.py --delete /api/route  
```

## Adding custom path for request body data
- Else defaults to `req_body.txt`
```bash
py py_curl.py --<method> /api/route -d custom_path
py py_curl.py --<method> /api/route --data custom_path
 ```
 
### Format the request body data for the POST, PUT or DELETE requests as follows:
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

## Adding custom url
- Else defaults to `http://localhost:4000`
```bash
py py_curl.py --<method> /api/route -u custom_url
py py_curl.py --<method> /api/route --url custom_url
```

## Adding request repeat amount for a period of time
- Set the amount of time the request should be sent within a period of time; default `1` time only

```bash
py py_curl.py --<method> /api/route -r number_of_times_to_send 
py py_curl.py --<method> /api/route --repeat number_of_times_to_send
```

- The `-r` or `--repeat` field could be used together with the `-t` or `--time` flag too, to set a time period for the request to be sent
- The time `-t` or `--time` defaults to `1 minute`

```bash
py curl.py --<method> /api/route -r number_of_times_to_send -t time_period
py curl.py --<method> /api/route --repeat number_of_times_to_send --time time_period
```


## Adding custom headers
- By default, it would only contain one custom header: `"Content-Type: application/json"`
- Currently only supports adding one extra custom headers; as of now
- Simply enter the header information in the `req_headers.json` file similar to the request body json file:
```json
{
"header_1": "header_1_value",
"header_2": "header_2_value"
}
```


# To Note
- Supports any OS that has the `cURL` executable, that can be ran on a proper bash/terminal/command prompt or any type of command shell. To date, this software has only been tested on Window -- Not tested on other OS yet such as MacOS and Linux. However, it would probably work too as these OS suppports `cURL`.
- Only works with fields containing one layer string; but not nested items such as object or arrays of any sort

# Add-on ideas
- Support for adding multiple request headers in the `req_headers.txt` file
- Support for array and object to be sent in the request body
- Feature to cache the request route URL within a .txt file
- Sending multiple requests for rate limit testing of server routes
