# python-cURL

Python automation to send HTTP requests using `cURL`. Despite the various other Python tools such as requests, urllib, and PycURL, I have created this just for learning purposes and to implement features that I would like to have that may not be implemented in the others.

# Python Version

- Python 3.10 and above

# Create virtual environment using Python (using Python3.10)

> Using Python3.10

```bash
$ python3.10 -m venv `path/to/venv`
$ path/to/venv/scripts/activate
```

# Package Installation (from within virtual environment)

- Install neccessary packages from `requirements.txt`

```bash
$ pip install -r requirements.txt
```

# Usage

To run the script

> Assume using Python3.10

## Adding custom url

- Else defaults to `http://localhost:4000`

```bash
$ python3.10 py_curl.py --<method> /api/route -u `custom_url`
$ python3.10 py_curl.py --<method> /api/route --url `custom_url`
```

GET

```bash
$ python3.10 py_curl.py --get /api/route
$ python3.10 py_curl.py --get --url `custom_url`
```

POST

```bash
$ python3.10 py_curl.py --post /api/route
$ python3.10 py_curl.py --post --url `custom_url`
```

PUT

```bash
$ python3.10 py_curl.py --put /api/route
$ python3.10 py_curl.py --put --url `custom_url`
```

DELETE

```bash
$ python3.10 py_curl.py --delete /api/route
$ python3.10 py_curl.py --delete --url `custom_url`
```

## Adding custom path for request body data

- Else defaults to `req_body.json` (as specified in the default `config.json`)

```bash
$ python3.10 py_curl.py --<method> /api/route -d `custom_json`.json
$ python3.10 py_curl.py --<method> /api/route --data `custom_json`.json
```

### Format the request body data for the POST, PUT or DELETE requests as follows:

```json
{
  "name": "random_name",
  "data": "random_data"
}
```

## Adding request repeat amount for a period of time

- Set the amount of time the request should be sent within a period of time; default `1` time only (as specified in the default `config.json`)

```bash
$ python3.10 py_curl.py --<method> /api/route -r `number_of_times_to_send`
$ python3.10 py_curl.py --<method> /api/route --repeat `number_of_times_to_send`
```

- The `-r` or `--repeat` field could be used together with the `-t` or `--time` flag too. This flag is to set the time interval between each request in seconds. (default 1 second - as specified in the default `config.json`)

```bash
$ py curl.py --<method> /api/route -r `number_of_times_to_send` -t `time_period`
$ py curl.py --<method> /api/route --repeat `number_of_times_to_send` --time `time_period`
```

## Adding custom headers

- By default, it would only contain one custom header: `"Content-Type: application/json"`
- Simply enter the header information in the `req_headers.json` file similar to the request body json file:

```json
{
  "header_1": "header_1_value",
  "header_2": "header_2_value"
}
```

# config.json

The following `config.json` values can be updated. These values are overwriten by the input flags if provided.

- `url_endpoint`: Custom URL (-u, --url flag)
- `req_body_json_file_location`: Request body data json file location (-d, --d flag)
- `req_headers_json_file_location`: Request headers data json file location (no flag)
- `req_repeat`: Set the amount of time the request should be sent within a period of time (-r , --repeat flag)
- `time_interval_secs`: Set the time interval between each request in seconds (-t, --time flag)

# To Note

- Supports any OS that has the `cURL` executable, that can be ran on a proper bash/terminal/command prompt or any type of command shell. To date, this software has only been tested on Window -- Not tested on other OS yet such as MacOS and Linux. However, it would probably work too as these OS suppports `cURL`.
- Only works with fields containing one layer string; but not nested items such as object or arrays of any sort

# Add-on/improvement ideas

- Use the @ with -d or --data flag instead

```bash
$ curl -X POST -d @req_body.json https://...
```

- Support for array and object to be sent in the request body
- Feature to cache the request route URL within a .txt file
- Sending multiple requests for rate limit testing of server routes
