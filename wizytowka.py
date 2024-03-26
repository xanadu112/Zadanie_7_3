from faker import Faker
fake = Faker('pl_PL')

class BusinessCard:
    
    def __init__(self, name, surname, company, position, email):
        self.name = name
        self.surname = surname
        self.company = company
        self.position = position
        self.email = email

        #Variables
        self._length_name_surname = len(self.name) + len(self.surname) + 1

    def __str__(self):
        return f'{self.name} {self.surname}, {self.email}'
    
    @property
    def length_name_surname(self):
        return self._length_name_surname

class BaseContact(BusinessCard):
    def __init__(self, name, surname, telephone, email):
        self.name = name
        self.surname = surname
        self.telephone = telephone
        self.email = email

        self._length_name_surname = len(self.name) + len(self.surname)
    
    def contact(self):
        return f'Wybieram numer: {self.telephone} i dzwonię do: {self.name} {self.surname}'

class BusinessContact(BusinessCard):
    def __init__(self, name, surname, telephone, work_phone, company, position, email):
        self.name = name
        self.surname = surname
        self.telephone = telephone
        self.work_phone = work_phone
        self.company = company
        self.position = position
        self.email = email

        self._length_name_surname = len(self.name) + len(self.surname)
    
    def contact(self):
        return f'Wybieram numer: {self.work_phone} i dzwonię do: {self.name} {self.surname}'


def create_b_c(type_b_c, amount_b_c):
    if type_b_c == BaseContact:
        for i in range(amount_b_c):
            person = type_b_c(name=fake.first_name(), surname=fake.last_name(), telephone=fake.phone_number(), email=fake.ascii_email())
    else:
        for i in range(amount_b_c):
            person = BusinessContact(name=fake.first_name(), surname=fake.last_name(), telephone=fake.phone_number(), work_phone=fake.phone_number(), company=fake.company(), position=fake.job(), email=fake.ascii_company_email())
    return person


persona = create_b_c(BaseContact, 3)
print(persona)
