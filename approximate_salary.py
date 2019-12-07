def predict_rub_salary(salary_from, salary_to):
    if salary_from is None:
        approximate_salary = salary_to*0.8
    elif salary_from == 0:
        approximate_salary = salary_to*0.8
    elif salary_to is None:
        approximate_salary = salary_from*1.2
    elif salary_to == 0:
        approximate_salary = salary_to*1.2    
    else:
        approximate_salary = (salary_from + salary_to)/2
    return approximate_salary


if __name__ == '__main__':
    print(predict_rub_salary(0, 10000))