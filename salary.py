from terminaltables import AsciiTable
from salary_hh import get_salary_hh
from salary_sj import get_salary_sj


def main():
    top_languages_list=('JavaScript', 'Java', 'Python', 'Ruby', 'PHP', 'C++', 'C#', 'C', 'Go', 'Shell', 'Objective-C',
                        'Scala', 'Swift', 'TypeScript')
    func_hh = [list(get_salary_hh(programming_language)) for programming_language in top_languages_list]
    func_sj = [list(get_salary_sj(programming_language)) for programming_language in top_languages_list]
    title_hh = 'HH Moscow'
    title_sj = 'SJ Moscow'
    print(get_table(title_hh, func_hh))
    print(get_table(title_sj, func_sj))


def get_table(title, func):
    indicators_list = ['Язык программирования', 'Средняя зарплата', 'Найдено вакансий', 'Обработано вакансий']
    func.insert(0, indicators_list)
    table = AsciiTable(func, title)
    return table.table

if __name__ == '__main__':
    main()