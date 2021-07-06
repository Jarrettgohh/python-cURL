import argparse
import os
import os
from termcolor import colored

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
                    help='DELETE request',
                    )


def process_yes_no(text):
    if('y' in text or 'Y' in text):
        return True

    return False


# vars() to make it iterable
args = vars(parser.parse_args())

url = 'http://localhost:4000/api/user'
req_types = ['get', 'post', 'put', 'delete']

http_request_type = None

for req_type in req_types:
    if args[req_type] == None:
        continue

    else:
        http_request_type = req_type
        req_url = f'{url}{args[req_type]}'

print(args)

if(http_request_type == None):
    # select_req_type = colored('Please select a request type\n', 'red')
    print('Please select a request type\n')
    os.system('py curl.py -h')
    exit()

if(http_request_type == 'post' and args['data'] == None):
    yes_no = input('Send with request body data (Y/N)? \n')
    with_req_body = process_yes_no(yes_no)

    if(with_req_body):
        f = open("req_body.txt", "w+")
        os.startfile(f.name)

else:
    try:
        os.startfile(args['data'])

    except:
        print('Please input a valid file location')


# print(http_request_type)
# print(req_url)

data = {}


# if (http_request_type == 'post'):
#     print('-----------------------------------------------------')
#     print('\nPress ctrl + X to exit the data editor')
#     print('In the exit stage, press enter to send the request\n')
#     print('-----------------------------------------------------')

#     print('{\n')

#     while 1:

#         input_bytes = msvcrt.getch()
#         if(input_bytes == b'\x18'):
#             print('}')
#             send_request = input('Confirm changes to data (Y/N)? ')

#             if('y' in send_request or 'Y' in send_request):
#                 break
#             else:
#                 continue

#         input_str = input('')
#         process_input_text(input_str)

#     input('\nEdit data (Y/N)? -- If no, the request would be sent with the current data \n')


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
