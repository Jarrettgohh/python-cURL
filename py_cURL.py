import argparse
import subprocess
import json
import sys
import time
import os
import os.path as os_path
from termcolor import colored


os.system('color')

# To make into .exe
# Usage: --<HTTP request type> <request_route>
# Example for GET request
# => --get /api/random

parser = argparse.ArgumentParser(
    description='HTTP GET, POST, PUT and DELETE request using cURL')

parser.add_argument(
    '--get',
    type=str,
    help='GET request',
    nargs='?',
    const=''
)
parser.add_argument(
    '--post',
    type=str,
    help='POST request',
    nargs='?',
    const=''
)
parser.add_argument(
    '--put',
    type=str,
    help='PUT request',
    nargs='?',
    const=''
)
parser.add_argument(
    '--delete',
    type=str,
    help='DELETE request',
    nargs='?',
    const=''
)
parser.add_argument(
    '-d',
    '--data',
    type=str,
    help='Request body data for POST, GET and DELETE',
)
parser.add_argument(
    '-u',
    '--url',
    type=str,
    help='Optionally give an URL, else default would be used',
)

parser.add_argument(
    '-r',
    '--repeat',
    type=int,
    help='Set the amount of times the request should be sent, defaults to 1.',
)

parser.add_argument(
    '-t',
    '--time',
    type=int,
    help='Set the time interval between each request in seconds. (default 1 second)'
)


def generate_request_headers_list(req_headers: dict):
    request_headers_list = []

    for req_header in req_headers:
        req_header_formatted = f'{req_header}: {req_headers[req_header]}'
        request_headers_list.extend(['-H', req_header_formatted])

    return request_headers_list


def format_json(req_body):
    formatted_json = json.dumps(req_body.replace('\n', ''))
    return formatted_json


def process_yes_no(text):
    if ('y' in text or 'Y' in text):
        return True

    return False


def prompt_edit_now():
    edit_now_option = input(
        prettify_output('\n Would you like to edit the contents now (Y/N)? \n',
                        True))
    return process_yes_no(edit_now_option)


def prettify_json(json_str: str):
    return json.dumps(json_str, indent=2)


def read_txt_file(txt_file_name):
    file = open(txt_file_name, 'r')
    return file.read().replace('\n', '')


def edit_txt_file(txt_file_name):
    os.startfile(txt_file_name)
    print('\n')
    os.system('pause')  # Press any key to continue...


def edit_json(json_file_name):
    os.startfile(json_file_name)
    print('\n')
    os.system('pause')  # Press any key to continue...


def read_json(json_file_name):
    with open(json_file_name) as file:

        json_content = json.load(file)

        if not bool(json_content):
            return None

        return json_content


def prettify_output(output, include_borders=False, border_color='white'):
    if (include_borders):
        return '\n' + colored(
            '--------------------------------------------------------------------',
            border_color
        ) + '\n\n' + f'{output}' + '\n\n' + colored(
            '--------------------------------------------------------------------',
            border_color) + '\n'

    return f'\n{output}\n'


def throw_error_and_exit(output: str):
    print('\n')
    print('Error:')
    print(output)
    print('\n')

    sys.exit()


def execute_curl_command(curl_command_list: list[str]):

    PIPE = subprocess.PIPE

    curl_command_list.append('--silent')
    # prevent revocation checks - might cause issues if there is an antivirus with web shield enabled
    curl_command_list.append('--ssl-no-revoke')

    curl_command_display = ' '.join(curl_command_list)
    print(curl_command_display)

    try:
        output = subprocess.run(
            curl_command_list, stdout=PIPE, universal_newlines=True, check=True, shell=False)

        output_stdout = output.stdout

        try:
            output_stdout = json.loads(output_stdout)
            pretty_output = prettify_output(prettify_json(
                output_stdout), include_borders=True, border_color='cyan')

        # Fail to load the json - data type within str is not dict
        except:
            pretty_output = prettify_output(
                output_stdout, include_borders=True, border_color='cyan')

        print(f"\n\n{colored('Response:', 'cyan')}\n{pretty_output}")

        return pretty_output

    except subprocess.CalledProcessError as e:
        print('error')
        print(e)

    except Exception as e:
        print(e.output)
        sys.exit()


# GET cURL request
def GET_curl_request(req_headers):

    curl_command_list = ['curl', req_url]

    default_req_headers = {
        "Content-Type": "application/json"
    }

    if (req_headers is not None):
        req_headers = dict(default_req_headers, **req_headers)

    else:
        req_headers = default_req_headers

    request_headers_list = generate_request_headers_list(req_headers)

    curl_command_list.extend(request_headers_list)

    execute_curl_command(curl_command_list)


# For any request type besides 'GET'
def curl_request_with_request_type(req_url: str, req_body: dict, req_headers: dict):

    curl_command_list = ['curl', '--request',
                         http_request_type.upper(), req_url]

    default_req_headers = {
        "Content-Type": "application/json"
    }

    if (req_headers is not None):
        req_headers = dict(default_req_headers, **req_headers)

    else:
        req_headers = default_req_headers

    request_headers_list = generate_request_headers_list(req_headers)

    curl_command_list.extend(request_headers_list)

    if (req_body is not None):

        formatted_req_body = format_json(req_body)
        curl_command_list.extend(['-d', formatted_req_body])

    execute_curl_command(curl_command_list)


def send_request_with_body(req_body_data=None):
    req_body_data = json.dumps(req_body_data, indent=2)

    print(
        prettify_output(
            f'\nSending {http_request_type.upper()} request to ' + colored(req_url, 'cyan') +
            f' with body:\n' +
            f'{prettify_output(req_body_data)}', include_borders=True, border_color='cyan'))

    call_respective_request_function(http_request_type, req_url, req_body_data)


def call_respective_request_function(http_request_type,
                                     req_url='',
                                     req_body_data=None):

    edit_req_headers_option = input(
        prettify_output('\n Edit request headers now? (Y/N)? \n', include_borders=True))
    edit_req_headers_now = process_yes_no(edit_req_headers_option)

    # Open the request headers file location to edit the request headers
    if (edit_req_headers_now):
        edit_json(req_headers_json_file_location)

    for i in range(int(req_repeat)):

        req_headers = read_json(req_headers_json_file_location)

        if (http_request_type == 'get'):
            GET_curl_request(req_headers)

        else:
            curl_request_with_request_type(req_url, req_body_data, req_headers)

        # second condition checks that its not the final iteration of the loop
        if time_interval_secs is not None and not (i == (int(req_repeat) - 1)):
            time.sleep(time_interval_secs)


def is_all_items_of_type(item_type: type, items: list):
    for i in items:
        if type(i) is not item_type:
            return False

    return True


url = ''
req_body_json_file_location = ''
req_headers_json_file_location = ''
req_repeat = None
time_interval_secs = None


config_json_data = read_json('config.json')


if config_json_data is None:
    throw_error_and_exit('config.json file must not be empty.')


elif not all(config_json_data.values()):
    throw_error_and_exit('config.json file values must not be empty.')


else:
    url = config_json_data['url_endpoint']
    req_body_json_file_location = config_json_data['req_body_json_file_location']
    req_headers_json_file_location = config_json_data['req_headers_json_file_location']
    req_repeat = config_json_data['req_repeat']
    time_interval_secs = config_json_data['time_interval_secs']

    str_list = [url, req_body_json_file_location,
                req_headers_json_file_location]

    int_list = [req_repeat, time_interval_secs]

    if not is_all_items_of_type(str, str_list) or not is_all_items_of_type(int, int_list):
        throw_error_and_exit(
            'A value in the config.json is not of apprioprate type!')


# vars() to make it iterable
args = vars(parser.parse_args())

#
# Overwrite from input flags
#
if args['url'] is not None:
    url = args['url']

if args['repeat'] is not None:
    req_repeat = args['repeat']

if args['time'] is not None:
    time_interval_secs = args['time']

req_types = ['get', 'post', 'put', 'delete']


http_request_type = None

for req_type in req_types:
    if args[req_type] is None:
        continue

    else:
        http_request_type = req_type
        req_url = f'{url}{args[req_type]}'


def main():
    try:

        # Request type not specified
        # Print the help message
        if (http_request_type is None):
            print(
                prettify_output(
                    colored('\nPlease select a request type\n', 'red'), include_borders=True))
            os.system('py py_curl.py -h')
            exit()

        # Request type is POST, PUT or DElETE with NO `-d` parameter passed in
        if ((http_request_type == 'post' or http_request_type == 'put'
             or http_request_type == 'delete') and args['data'] is None):

            try:

                with_req_body_option = input(
                    prettify_output('\n Send with request body data (Y/N)? \n',
                                    include_borders=True))
                with_req_body = process_yes_no(with_req_body_option)

                # Open req_body.json file to edit the request body
                if (with_req_body):

                    if (not os_path.exists(req_body_json_file_location)):

                        edit_json(req_body_json_file_location)

                    else:
                        edit_now = prompt_edit_now()

                        if (edit_now):
                            edit_json(req_body_json_file_location)

                    req_body_data = read_json(req_body_json_file_location)

                    if (req_body_data != ''):
                        send_request_with_body(req_body_data)

                    else:
                        throw_error_and_exit('Request body is empty.')

                else:
                    call_respective_request_function(
                        http_request_type, req_url)

            except:
                throw_error_and_exit(
                    'Please input a valid file location. The file path given for either the request body or headers json file location could not be found.')

        # Request type is POST, PUT or DElETE with `-d` flag passed in
        elif ((http_request_type == 'post' or http_request_type == 'put'
               or http_request_type == 'delete')):
            try:
                edit_now = prompt_edit_now()

                if (edit_now):
                    edit_json(args['data'])

                req_body_data = read_json(args['data'])

                if (req_body_data != ''):
                    send_request_with_body(req_body_data)

                else:
                    throw_error_and_exit('Request body is empty.')

            except:
                throw_error_and_exit(
                    'Please input a valid file location. The file path given for either the request body or headers json file location could not be found.')

        # GET request
        else:

            # If `-d` flag passed in -> Display error message
            if (args['data'] is not None):
                print(
                    prettify_output(
                        f'\n The \'-d\' flag does not apply for the {http_request_type.upper()} request type\n', include_borders=True, border_color='red'))

                sys.exit()

            call_respective_request_function(http_request_type)

    except KeyboardInterrupt:
        sys.exit()


main()
