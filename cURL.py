import argparse
import json
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
parser.add_argument('--get',
                    type=str,
                    help='GET request',
                    )
parser.add_argument('--post',
                    type=str,
                    help='POST request',
                    )
parser.add_argument('--put',
                    type=str,
                    help='PUT request',
                    )
parser.add_argument('--delete',
                    type=str,
                    help='DELETE request',
                    )
parser.add_argument('-d', '--data',
                    type=str,
                    help='Request body data for POST, GET and DELETE',
                    )
parser.add_argument('-u', '--url',
                    type=str,
                    help='Optionally give an URL, else default would be used',
                    )

parser.add_argument('-r', '--repeat',
                    type=str,
                    help='Set the amount of times the request should be sent, defaults to 1.',
                    )


def process_yes_no(text):
    if('y' in text or 'Y' in text):
        return True

    return False


def prompt_edit_now():
    edit_now_option = input(prettify_output(
        '\n Would you like to edit the contents now (Y/N)? \n', True))
    return process_yes_no(edit_now_option)


def format_json(req_body):
    return json.dumps(req_body.replace('\n', ''))


def read_txt_file(txt_file_name):
    file = open(txt_file_name, 'r')
    return file.read().replace('\n', '')


def edit_json(json_file_name):
    os.startfile(json_file_name)
    print('\n')
    os.system('pause')  # Press any key to continue...


def read_json(json_file_name):
    with open(json_file_name) as file:
        return json.load(file)


def prettify_output(output, include_borders=False, border_color='white'):
    if (include_borders):
        return '\n' + colored('--------------------------------------------------------------------', border_color) + '\n' + f'{output}' + '\n' + colored('--------------------------------------------------------------------', border_color) + '\n'

    return f'\n{output}\n'


def execute_shell_command(shell_command):
    os.system(shell_command)


def curl_request_without_body(req_headers):

    execute_shell_command(
        f'curl' + (f' -H {req_headers} ' if req_headers != '' else ' ') + req_url)


def curl_request_with_body(req_url, req_body, req_headers):

    curl_command = '\
    curl' + f' --request {http_request_type.upper()}' + ' -H \"Content-Type: application/json\"' + (f' -H {req_headers}' if req_headers != '' else '')

    if (req_body != None):
        formatted_req_body = format_json(req_body)
        curl_command = f'{curl_command} -d {formatted_req_body}'

    else:
        curl_command = curl_command

    curl_command = f'{curl_command} {req_url}'

    execute_shell_command(curl_command)


def send_request_with_body(req_body_data=None):
    req_body_data = json.dumps(req_body_data, indent=2)

    print(
        prettify_output(
            colored(f'\nSending {http_request_type.upper()} request to ', 'green') + colored(req_url, 'yellow') + colored(f' with body:\n', 'green') + f'{prettify_output(req_body_data)}', True, 'yellow'))

    call_respective_request_function(
        http_request_type, req_url, req_body_data)


def call_respective_request_function(http_request_type, req_url='', req_body_data=None):

    for _ in range(int(req_repeat)):

        req_headers = read_txt_file('req_headers.txt')

        if (http_request_type == 'get'):
            curl_request_without_body(req_headers)

        else:
            # Actually is for any request type besides 'GET' even without body; to refactor to be more clear
            curl_request_with_body(req_url, req_body_data, req_headers)


# vars() to make it iterable
args = vars(parser.parse_args())


url = 'http://localhost:4000' if args['url'] == None else args['url']
req_types = ['get', 'post', 'put', 'delete']
req_repeat = 1 if args['repeat'] == None else args['repeat']

http_request_type = None

for req_type in req_types:
    if args[req_type] == None:
        continue

    else:
        http_request_type = req_type
        req_url = f'{url}{args[req_type]}'


# Request type not specified
# Print the help message
if(http_request_type == None):
    print(prettify_output(colored('\nPlease select a request type\n', 'red'), True))
    os.system('py curl.py -h')
    exit()


# Request type is POST, PUT or DElETE with NO `-d` parameter passed in
if((http_request_type == 'post' or http_request_type == 'put' or http_request_type == 'delete') and args['data'] == None):

    with_req_body_option = input(prettify_output(
        '\n Send with request body data (Y/N)? \n', True))
    with_req_body = process_yes_no(with_req_body_option)

    if(with_req_body):

        if(not os_path.exists('req_body.json')):
            f = open('req_body.json', 'w+')

            edit_json('req_body.json')

        else:
            edit_now = prompt_edit_now()

            if(edit_now):
                edit_json('req_body.json')

        req_body_data = read_json('req_body.json')

        if(req_body_data != ''):
            send_request_with_body(req_body_data)

        else:
            print('Request body is empty')
            exit()

    else:
        call_respective_request_function(http_request_type, req_url)


# Request type is POST, PUT or DElETE with `-d` flag passed in
elif ((http_request_type == 'post' or http_request_type == 'put' or http_request_type == 'delete')):
    try:
        edit_now = prompt_edit_now()

        if(edit_now):
            edit_json(args['data'])

        req_body_data = read_json(args['data'])

        if(req_body_data != ''):
            send_request_with_body(req_body_data)

        else:
            print('Request body is empty')
            exit()

    except:
        print('Please input a valid file location')


# GET request
else:

    # If `-d` flag passed in -> Display error message
    if (args['data'] != None):
        print(prettify_output(
            colored(f'\n\'-d\' flag does not applies for {http_request_type.upper()} request type\n', 'red'), True, 'yellow'))

    call_respective_request_function(http_request_type)
