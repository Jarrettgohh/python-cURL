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


def process_yes_no(text):
    if('y' in text or 'Y' in text):
        return True

    return False


def prompt_edit_now():
    edit_now_option = input(prettify_output(
        '\n Would you like to edit the contents now (Y/N)? \n', True))
    return process_yes_no(edit_now_option)


def open_txt_file(txt_file_name):
    os.startfile(txt_file_name)
    print('\n')
    os.system('pause')  # Press any key to continue...


def read_txt_file(txt_file_name):
    f = open(txt_file_name, 'r')
    return f.read().replace(' ', '')


def prettify_output(output, include_borders=False):
    if (include_borders):
        return f'\n-------------------------------------------------------------------- \n {output} \n--------------------------------------------------------------------\n'

    return f'\n{output}\n'


def format_req_body_json(body):
    return json.dumps(body.replace(' ', '').replace('\n', ''))


def execute_shell_command(shell_command):
    os.system(shell_command)


def GET():
    execute_shell_command(f'curl {req_url}')


def POST(req_url, req_body):

    curl_post_command = '\
    curl\
    --request POST\
    -H \"Content-Type: application/json\"'

    if (req_body != None):
        json_req_body = format_req_body_json(req_body)
        curl_post_command = f'{curl_post_command} -d {json_req_body}'

    else:
        curl_post_command = curl_post_command

    curl_post_command = f'{curl_post_command} {req_url}'
    execute_shell_command(curl_post_command)


# To confirm curl command
def PUT():
    execute_shell_command(f'curl -x PUT {req_url}')


# To confirm curl command
def DELETE():
    execute_shell_command(f'curl -x DELETE {req_url}')


def call_respective_request_function(http_request_type, req_url='', req_body_data=None):

    match_case = http_request_type

    if (match_case == 'get'):
        GET()

    elif (match_case == 'post'):
        POST(req_url, req_body_data)

    else:
        return


# vars() to make it iterable
args = vars(parser.parse_args())


url = 'http://localhost:4000' if args['url'] == None else args['url']
req_types = ['get', 'post', 'put', 'delete']

http_request_type = None

for req_type in req_types:
    if args[req_type] == None:
        continue

    else:
        http_request_type = req_type
        req_url = f'{url}{args[req_type]}'


if(http_request_type == None):
    print(prettify_output(colored('\nPlease select a request type\n', 'red'), True))
    os.system('py curl.py -h')
    exit()


if((http_request_type == 'post' or http_request_type == 'put' or http_request_type == 'delete') and args['data'] == None):

    with_req_body_option = input(prettify_output(
        '\n Send with request body data (Y/N)? \n', True))
    with_req_body = process_yes_no(with_req_body_option)

    if(with_req_body):

        if(not os_path.exists('req_body.txt')):
            f = open('req_body.txt', 'w+')

            open_txt_file('req_body.txt')

        else:
            edit_now = prompt_edit_now()

            if(edit_now):
                open_txt_file('req_body.txt')

        req_body_data = read_txt_file('req_body.txt')

        if(req_body_data != ''):
            print(
                colored(f'\n\nSending {http_request_type.upper()} request to ', 'green') + colored(req_url, 'yellow') + colored(' with body:', 'green'))
            print(prettify_output(req_body_data))

            call_respective_request_function(
                http_request_type, req_url, req_body_data)

        else:
            print('Request body is empty')
            exit()

    else:
        call_respective_request_function(http_request_type, req_url)


elif ((http_request_type == 'post' or http_request_type == 'put' or http_request_type == 'delete')):
    try:
        edit_now = prompt_edit_now()

        if(edit_now):
            open_txt_file(args['data'])

        req_body_data = read_txt_file(args['data'])

        if(req_body_data != ''):
            print(f'\n\nSending {http_request_type} request with body data:')
            print(prettify_output(req_body_data))

            call_respective_request_function(
                http_request_type, req_url, req_body_data)

        else:
            print('Request body is empty')
            exit()

    except:
        print('Please input a valid file location')


else:
    if (args['data'] != None):
        print(prettify_output(
            f'\n\'-d\' flag does not applies for {http_request_type.upper()} request type\n', True))

    call_respective_request_function(http_request_type)


# Experiment where request body is loaded from .txt file
# f = open('req_body.txt', 'r')

# POST(
#     'http://localhost:4000/api/user/curl',
#     f.read(),
# )
