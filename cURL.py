import argparse
import os
import msvcrt

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


# vars() to make it iterable
args = vars(parser.parse_args())


url = 'http://localhost:4000/api/user'
req_types = ['get', 'post', 'put', 'delete']

for req_type in req_types:
    if args[req_type] == None:
        continue

    else:
        http_request_type = req_type
        req_url = f'{url}{args[req_type]}'


print(http_request_type)
print(req_url)

data = {}

input_bytes = msvcrt.getch()
if(input_bytes == b'\x18'):
    send_request = input('Confirm changes to data (Y/N)? ')


def process_input_text(text):
    if(text == str(b'\x18')):
        print(text)


if (http_request_type == 'post'):
    print('{\n')

    input_str = input('')
    process_input_text(input_str)


def execute_shell_command(shell_command):
    os.system(shell_command)


def GET():
    execute_shell_command(f'curl {req_url}')


# To add params functionality
def POST():
    execute_shell_command(f'curl -X POST {req_url}')


# To confirm curl command
def PUT():
    execute_shell_command(f'curl -x PUT {req_url}')


# To confirm curl command
def DELETE():
    execute_shell_command(f'curl -x DELETE {req_url}')
