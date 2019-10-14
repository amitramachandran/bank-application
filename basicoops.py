# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import random
class User:
    
    ''' a generic user class'''
    def __init__(self,user_id,name,location,balance):
        '''initialisation for id , name, location'''
        self._user_id = user_id
        self._name = name
        self._location = location
        self._balance = balance
        
    def profile(self):
        return {'ID': self._user_id,'NAME':self._name, 'LOCATION': self._location,'Available balance':self._balance}
   
    def balance(self):
        print ({'NAME':self._name,'Available balance':self._balance})
    
    def _credit(self):
        credit_amount = input('amount to be deposited')
        self._balance += int(credit_amount)
        print ({'NAME':self._name,'Available balance':self._balance})
    
    def _debit(self):
        debit_amount = input('amount to be debited')
        if int(debit_amount) > int(self._balance):
            print("insufficient amount")
            self.balance()
        else:    
            self._balance -= int(debit_amount)
            print({'NAME':self._name,'Available balance':self._balance})
            
def adduser():
    id = int(random.randrange(100,999))
    name = input("what is your name?")
    location = input("where are you from?")
    balance = 0
    user = User(id,name,location,balance)
    return user

def choice():

        print("Banking App")
        print("to create new user - 1")
        print("to deposit amount - 2" )
        print("to withdraw amount - 3")
        print("to exit - 0")
        choice = int(input("enter ur choice"))
        return choice
        
    
def selected_choice():
    while True:
        c = choice()
        if c == 1:
            adduser()
        elif c == 2:
            adduser()._credit()
        elif c == 3:
            adduser()._debit()
        elif c == 0:
            break
        
def main():
    ''' instantiation of a user class'''
    #print(adduser())
    selected_choice()
    '''user1=adduser()
    user2=adduser()
    print(user1.profile())
    print(user2.profile())
    #print(adduser().profile())
    print(adduser()._credit())'''
   

if __name__ == "__main__":
    main()
    