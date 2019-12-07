from terminaltables import AsciiTable
from salary_hh import get_salary_hh
from salary_sj import get_salary_sj
from dotenv import load_dotenv
import os

def main():
    top_languages_list=('JavaScript', 'Java', 'Python', 'Ruby', 'PHP', 'C++', 'C#', 'C', 'Go', 'Shell', 'Objective-C',
                        'Scala', 'Swift', 'TypeScript')
    load_dotenv()
    app_token_hh = os.getenv('user-agent_hh')
    auth_token_hh = os.getenv('auth_token_hh')
    token_sj = os.getenv('X-Api-App-Id')
    table_data_hh = [list(get_salary_hh(programming_language, auth_token_hh, app_token_hh)) for programming_language in top_languages_list]
    table_data_sj = [list(get_salary_sj(programming_language, token_sj)) for programming_language in top_languages_list]
    title_hh = 'HH Moscow'
    title_sj = 'SJ Moscow'
    print(get_table(title_hh, table_data_hh))
    print(get_table(title_sj, table_data_sj))


def get_table(title, table_data):
    indicators_list = ['Язык программирования', 'Средняя зарплата', 'Найдено вакансий', 'Обработано вакансий']
    table_data.insert(0, indicators_list)
    table = AsciiTable(table_data, title)
    return table.table

if __name__ == '__main__':
    main()