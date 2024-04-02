from faker import Faker
fake = Faker('pl_PL')

class BaseContact():
    def __init__(self, name, surname, telephone, email):
        self.name = name
        self.surname = surname
        self.telephone = telephone
        self.email = email

        self._label_length = len(self.name) + len(self.surname)
    
    @property
    def label_length(self):
        return self._label_length
                        
    def contact(self):
        return f'Wybieram numer: {self.telephone} i dzwonię do: {self.name} {self.surname}'
    
    def __str__(self):
        return f'{self.name} {self.surname}, {self.telephone}, {self.email}'

class BusinessContact(BaseContact):
    def __init__(self, position, company, work_phone, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.position = position
        self.company = company
        self.work_phone = work_phone
    
    def contact(self):
        return f'Wybieram numer: {self.work_phone} i dzwonię do: {self.name} {self.surname}'
    
    def __str__(self):
        return f'{super().__str__()}, {self.position} {self.company}, {self.work_phone}'
        

def create_contacts(type_b_c, amount_b_c):
    b_c = []
    for i in range(amount_b_c):
        if type_b_c == BaseContact:
            b_c.append(BaseContact(name=fake.first_name(), surname=fake.last_name(), telephone=fake.phone_number(), email=fake.ascii_email()))
        else:
            b_c.append(BusinessContact(name=fake.first_name(), surname=fake.last_name(), telephone=fake.phone_number(), work_phone=fake.phone_number(), company=fake.company(), position=fake.job(), email=fake.ascii_company_email()))
    return b_c

if __name__ == "__main__":
    persona = create_contacts(BusinessContact, 3)

    for person in persona:
        print(person)

