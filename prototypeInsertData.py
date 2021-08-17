from Insert_NewUser import insert_data
class Account:
    def __init__(self, name, password) -> None:
        self.name = name
        self.password = password
        
    def account(self):
        insert_data(self.name, self.password)

account = Account('Amber Jewels', 'Renault')
print(account.account())