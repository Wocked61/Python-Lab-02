'''
# Name: Dylan Phan
# Date: 9/4/2024
# File Purpose: putting contacts in a list and making it a program
'''
contacts = [] 
def print_list(contacts = []) :
    #this function prints out every contact in the list contacts
    print('''
================== CONTACT LIST ==================
Index   First Name            Last Name
======  ====================  ====================''')  
    for i in range(len(contacts)) :
        print(f'{str(i):8}{contacts[i][0]:22}{contacts[i][1]:22}')

def add_contact(contacts) :
    #This function adds a contact to the list of contacts
    inp1 = input('Enter first name: ')
    inp2 = input('Enter last name: ')
    contacts.append([inp1,inp2])
    return contacts

def modify_contact(contacts) :
    #this function modifies the contacts list and changes it to the user's request
    inp3 = int(input('\nEnter the index number: '))
    if (inp3 >= len(contacts) or inp3 < 0):
        print('Invalid index number.')
        return contacts
    else :
        inp4 = input('Enter first name: ')
        inp5 = input('Enter last name: ')
        contacts[inp3] = [inp4,inp5]
        return contacts

def delete_contact(contacts) :
    #this function deletes a contact from the contact list
    inp3 = int(input('\nEnter the index number: '))
    if (inp3 >= len(contacts) or inp3 < 0):
        print('Invalid index number.')
        return contacts
    else :
        contacts.remove(contacts[inp3])
        return contacts


