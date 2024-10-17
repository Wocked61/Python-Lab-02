'''
# Name: Dylan Phan
# Date: 9/4/2024
# File Purpose: contacts program main
'''

from contacts import *

contacts_list = []
while True:
    inp1 = input('''
        *** TUFFY TITAN CONTACT MAIN MENU

1. Print list
2. Add contact
3. Modify contact
4. Delete contact
5. Exit the program 
                 
Enter menu choice: ''')
    if (inp1 == '1') :
        print_list(contacts_list)
    if (inp1 == '2') :
        add_contact(contacts_list)
    if (inp1 == '3'):
        modify_contact(contacts_list)
    if (inp1 == '4') :
        delete_contact(contacts_list)
    if (inp1 == '5') :
        break