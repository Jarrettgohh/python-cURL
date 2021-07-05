import argparse
import os

# To make into .exe

parser = argparse.ArgumentParser(
    description='HTTP GET, POST, PUT and DELETE request using cURL')
parser.add_argument('integers', metavar='N', type=int, nargs='+',
                    help='an integer for the accumulator')
parser.add_argument('--sum', dest='accumulate',
                    action='store_const',
                    const=sum, default=max,
                    help='sum the integers (default: find the max)')


args = parser.parse_args()
print(args.accumulate(args.integers))

# print('\n\n--------------------------------------')
# print('cURL executable written in Python\n')
# print('Usage guide: \n \'get\' \'post\' \'put\' \'delete\' followed by request route\n')
# print('Example usage: \n get /api/test\n')

# req_route = input('')
req_url = f'http://localhost:4000/api/user{req_route}'


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


def GET_TEST():
    execute_shell_command(f'curl https://google.com')


if('get' in req_route):
    print(GET_TEST())
