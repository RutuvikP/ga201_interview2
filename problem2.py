employess=[
    {"name":"John","salary":3000,"designation":"developer"},
    {"name":"Emma","salary":4000,"designation":"manager"},
    {"name":"Kelly","salary":3500,"designation":"tester"},
]

def max_salary_employee(emp):
    max=0
    ans={}
    for item in emp:
        if item['salary'] > max:
            max=item['salary']
            ans=item
    print(ans)

max_salary_employee(employess)