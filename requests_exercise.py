import json
import requests
from requests.exceptions import HTTPError


def show_response(http_response):
    show_headers(http_response)
    show_content(http_response)


def show_content(http_response):
    print(f'Response: {response.url} as bytes: {response.content}')
    print(f'Response: {response.url} as text: {response.text}')
    try:
        print(f'Response: {response.url} as JSON: {response.json()}')
    except json.decoder.JSONDecodeError:
        print(f'Response: {response.url} is not JSON')


def show_headers(http_response):
    print(f'Response headers of {response.url}:')
    for header in response.headers:
        print(f'{header} : {response.headers[header]}')


urls = [#'http://www.aleksanderurbanowicz.com/',
        'https://api.github.com']
params = {'q': 'requests+language:python'}
# Response
if __name__ == '__main__':
    for url in urls:
        try:
            response = requests.get(url, params=params)
            response.raise_for_status()
        except HTTPError as http_error:
            print(f'HTTP error: {http_error}')
        except Exception as other_error:
            print(f'Other error: {other_error}')
        else:
            print(f'Success with status: {response.status_code}')
            show_response(response)

