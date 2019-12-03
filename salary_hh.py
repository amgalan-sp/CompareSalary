import requests
from dotenv import load_dotenv
import os


def get_salary_hh(programming_language):
    headers = {
    'User-Agent': os.getenv('user-agent_hh'),
    'Authorization': os.getenv('auth_token_hh')
    }
    url = 'https://api.hh.ru/vacancies/'
    payload = {
        'area': '1',
        'text': "программист {}".format(programming_language),
        'only_with_salary': 'true'
    }
    job_request = requests.get(url=url, params=payload, headers=headers).json()
    page = 0
    pages_number = 1
    vacancies_bank = []
    while page < pages_number:
        payload['page'] = page
        pages_number = job_request['pages']
        page += 1
        offer_per_page = [offer['salary'] for offer in job_request['items'] if offer['salary']['currency'] == 'RUR']
        vacancies_bank.extend(offer_per_page)
    salary_list = []
    for offer in vacancies_bank:
        if offer:
            a = offer['from']
            b = offer['to']
            if a is None:
                c = b*0.8
            elif b is None:
                c = a*1.2
            else:
                c = (a + b)/2
            salary_list.append(c)
    vacancies_processed = len(salary_list)
    average_salary = int(sum(salary_list)/vacancies_processed)
    payload['only_with_salary'] = None
    vacancies_found = requests.get(url=url, params=payload, headers=headers).json()['found']
    return programming_language, average_salary, vacancies_found, vacancies_processed

if __name__ == '__main__':
    load_dotenv()
    print(get_salary_hh(''))