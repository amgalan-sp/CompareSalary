import requests
from approximate_salary import predict_rub_salary
from dotenv import load_dotenv
import os


def get_salary_sj(programming_language, token_sj):
    url = 'https://api.superjob.ru/2.0/vacancies/'
    headers = {
    'X-Api-App-Id': token_sj
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
    vacancies_list = []
    while page < pages + 1:
        payload['page'] = page
        page += 1
        vc_per_page = [offer for offer in requests.get(url=url, params=payload, headers=headers).json()['objects']]
        vacancies_list.extend(vc_per_page)
    vacancies_processed = len(vacancies_list)
    salaries_list = []
    for vacancies in vacancies_list:
        salary_from = vacancies['payment_from']
        salary_to = vacancies['payment_to']
        salaries_list.append(predict_rub_salary(salary_from, salary_to))
    if vacancies_processed != 0:
        average_salary = int(sum(salaries_list)/vacancies_processed)
    else:
        average_salary = 0
    return programming_language, average_salary, vacancies_found, vacancies_processed


def main():
    load_dotenv()
    print(get_salary_sj('', os.getenv('X-Api-App-Id')))


if __name__ == '__main__':
    main()
