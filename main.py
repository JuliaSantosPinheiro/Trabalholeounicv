class Student:

    def __init__(self, cpf, name, age, course):
        self.cpf = cpf
        self.name = name
        self.age = age
        self.course = course

    def __eq__(self, other):
        return self.cpf == other.cpf and self.name == other.name and self.age == other.age \
               and other.course == self.course


# Update
def update_student(student_number):
    student = students[student_number]

    print()
    print(f'Você está editando: {student.name}')
    print()
    new_name = input(f'Nome: {student.name}\nNovo nome: ')
    if new_name:
        student.name = new_name

    new_cpf = input(f'CPF: {student.cpf}\nNovo CPF: ')
    if new_cpf:
        student.cpf = new_cpf

    new_age = input(f'Idade: {student.age}\nNova idade: ')
    if new_age:
        student.age = int(new_age)

    new_course = input(f'Curso: {student.course}\nNovo curso: ')
    if new_course:
        student.course = new_course

    print(f'CPF: {student.cpf}')
    print(f'Idade: {student.age}')
    print(f'Curso: {student.course}')


def delete_student(student_number):
    students.pop(student_number)


def new_student():
    return Student('', 'Novo estudante', 0, '')


operations_list = [(1, 'Editar', update_student), (2, 'Deletar', delete_student)]

students = [new_student()]


def describe_student(student):
    print()
    print(f'Nome: {student.name}')
    print(f'CPF: {student.cpf}')
    print(f'Idade: {student.age}')
    print(f'Curso: {student.course}')
    print()


def operations(student_number):
    print('Insira 0 para sair')
    describe_student(students[student_number])

    for operation, description, _ in operations_list:
        print(f'{operation} - {description}')

    selected_operation = int(input())

    if selected_operation == 0:
        return

    list(filter(lambda x: x[0] == selected_operation, operations_list))[0][2](student_number)


def menu():
    while True:

        print()
        print('O py-tha-on systems - Insira 0 para sair')
        print()
        for number, student in enumerate(students):
            print(f'{number + 1} - {student.name}')

        student_number = int(input('\nSelecione o aluno: '))

        if student_number == 0:
            break

        if len(students) < student_number:
            print('\nEstudante não encontrado!')
            menu()

        operations(student_number - 1)

        if len(students) < 1 or not students[len(students) - 1].__eq__(new_student()):
            students.append(new_student())


if __name__ == '__main__':
    menu()
