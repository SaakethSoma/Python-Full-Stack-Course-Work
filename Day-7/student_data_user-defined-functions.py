def student_data(info):
    print(f'name:{info[0]}')
    print(f'course:{info[1]}')
    print(f'grad_year:{info[2]}')
    print('-----END-----')

data=[['saaketh','PFS','2025'],
      ['sathwik','JFS','2025'],
      ['swapnil','DSA','2026'],
      ['sandeep','DS','2025'],]

for i in data:
    student_data(i)
