from faker import Faker
fake = Faker('pl_PL')

class BaseContact():
    def __init__(self, name, surname, telephone, email):
        self.name = name
        self.surname = surname
        self.telephone = telephone
        self.email = email

        self._length_name_surname = len(self.name) + len(self.surname)
    
    @property
    def length_name_surname(self):
        return self._length_name_surname
                        
    def contact(self):
        return f'Wybieram numer: {self.telephone} i dzwonię do: {self.name} {self.surname}'

class BusinessContact(BaseContact):
    def __init__(self, position, company, work_phone, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.position = position
        self.company = company
        self.work_phone = work_phone
    
    def contact(self):
        return f'Wybieram numer: {self.work_phone} i dzwonię do: {self.name} {self.surname}'


def create_b_c(type_b_c, amount_b_c):
    b_c = []
    if type_b_c == BaseContact:
        for i in range(amount_b_c):
            b_c.append(type_b_c(name=fake.first_name(), surname=fake.last_name(), telephone=fake.phone_number(), email=fake.ascii_email()))
    else:
        for i in range(amount_b_c):
            b_c.append(BusinessContact(name=fake.first_name(), surname=fake.last_name(), telephone=fake.phone_number(), work_phone=fake.phone_number(), company=fake.company(), position=fake.job(), email=fake.ascii_company_email()))
    return b_c


persona = create_b_c(BusinessContact, 3)
print(persona)
