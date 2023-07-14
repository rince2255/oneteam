class Password_manager:
    def _init_(self):
        self.old_passwords = []

    def get_password(self):
        return self.old_passwords[-1]

    def set_password(self, new_password):
        if new_password not in self.old_passwords:
            self.old_passwords.append(new_password)
            print("Good password selection!, Registered sucessfully")
        else:
            print("Try another password")

    def is_correct(self, password):
        if password == self.get_password():
            return True
        else:
            return False


obj1 = Password_manager()
obj1.old_passwords = ['thor', 'asgard', 'godofthunder']
obj1.set_password('kollam')
print(obj1.is_correct('oneteam'))
print(obj1.is_correct('kollam'))

print(obj1.old_passwords)
