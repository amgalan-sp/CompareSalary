import requests
from dotenv import load_dotenv
import os


def get_salary_sj(programming_language):
    url = 'https://api.superjob.ru/2.0/vacancies/'
    headers = {
    'X-Api-App-Id': os.getenv('X-Api-App-Id')
    }
    payload = {
        'keywords':'Программист {}'.format(programming_language),
        'town': 4,
    }
    vacancies_found = requests.get(url=url, params=payload, headers=headers).json()['total']
    payload['no_agreement'] = 1
    job_request = requests.get(url=url, params=payload, headers=headers).json()
    page = 0
    pages = int(job_request['total'])/20
    vacancies_bank = []
    while page < pages + 1:
        payload['page'] = page
        page += 1
        vc_per_page = [offer for offer in requests.get(url=url, params=payload, headers=headers).json()['objects']]
        vacancies_bank.extend(vc_per_page)
    vacancies_processed = len(vacancies_bank)
    salary_bank = []
    for vacancies in vacancies_bank:
        a = vacancies['payment_from']
        b = vacancies['payment_to']
        if a == 0:
            c = b*0.8
        elif b == 0:
            c = a*1.2
        else:
            c = (a + b)/2
        salary_bank.append(c)
    if vacancies_processed != 0:
        average_salary = int(sum(salary_bank)/vacancies_processed)
    else:
        average_salary = 0
    return programming_language, average_salary, vacancies_found, vacancies_processed

if __name__ == '__main__':
    load_dotenv()
    print(get_salary_sj(''))