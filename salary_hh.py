import requests
from approximate_salary import predict_rub_salary
from dotenv import load_dotenv
import os


def get_salary_hh(programming_language, auth_token_hh, app_token_hh):
    headers = {
    'User-Agent': app_token_hh,
    'Authorization': auth_token_hh
    }
    url = 'https://api.hh.ru/vacancies/'
    payload = {
        'area': '1',
        'text': "Программист {}".format(programming_language),
        'only_with_salary': 'true'
    }
    job_request = requests.get(url=url, params=payload, headers=headers).json()
    page = 0
    pages_number = 1
    vacancies_list = []
    while page < pages_number:
        payload['page'] = page
        pages_number = job_request['pages']
        page += 1
        offer_per_page = [offer['salary'] for offer in job_request['items'] if offer['salary']['currency'] == 'RUR']
        vacancies_list.extend(offer_per_page)
    salaries_list = []
    for offer in vacancies_list:
        if offer:
            salary_from = offer['from']
            salary_to = offer['to']
            salaries_list.append(predict_rub_salary(salary_from, salary_to))
    vacancies_processed = len(salaries_list)
    try:
        average_salary = int(sum(salaries_list)/vacancies_processed)
    except ZeroDivisionError:
        average_salary = 0
    payload['only_with_salary'] = None
    vacancies_found = requests.get(url=url, params=payload, headers=headers).json()['found']
    return programming_language, average_salary, vacancies_found, vacancies_processed


def main():
    load_dotenv()
    print(get_salary_hh('', os.getenv('auth_token_hh'), os.getenv('user-agent_hh')))


if __name__ == '__main__':
    main()