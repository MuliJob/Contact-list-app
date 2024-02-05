import pyperclip


class Contact:
    '''
    Class that generates new instances of the contact list
    '''
    contact_list = []
    
    
    def save_contact(self):
        '''
        save_contact method saves contact objects into contact_list
        '''

        Contact.contact_list.append(self)
    
    @classmethod
    def find_by_number(cls,number):
        '''
        Method that takes in a number and returns a contact that matches that number.

        Args:
            number: Phone number to search for
        Returns :
            Contact of person that matches the number.
        '''

        for contact in cls.contact_list:
            if contact.phone_number == number:
                return contact
            
    def delete_contact(self):

        '''
        delete_contact method deletes a saved contact from the contact_list
        '''

        Contact.contact_list.remove(self)
    
    @classmethod
    def display_contacts(cls):
        '''
        method that returns the contact list
        '''
        return cls.contact_list
    
    @classmethod
    def copy_email(cls,number):
        contact_found = Contact.find_by_number(number)
        pyperclip.copy(contact_found.email)
        
    
        
    def __init__(self,first_name,last_name,number,email) -> None:
        
        
        self.first_name = first_name
        self.last_name = last_name
        self.phone_number = number
        self.email = email
        
        pass
    
    @classmethod
    def contact_exist(cls,number):
        '''
        Method that checks if a contact exists from the contact list.
        Args:
            number: Phone number to search if it exists
        Returns :
            Boolean: True or false depending if the contact exists
        '''
        for contact in cls.contact_list:
            if contact.phone_number == number:
                    return True

        return False
    
    
def create_contact(fname,lname,phone,email):
    '''
    Function to create a new contact
    '''
    new_contact = Contact(fname,lname,phone,email)
    return new_contact

def save_contacts(contact):
    '''
    Function to save contact
    '''
    contact.save_contact()
    
def del_contact(contact):
    '''
    Function to delete a contact
    '''
    contact.delete_contact()
    
def find_contact(number):
    '''
    Function that finds a contact by number and returns the contact
    '''
    return Contact.find_by_number(number)

def check_existing_contacts(number):
    '''
    Function that check if a contact exists with that number and return a Boolean
    '''
    return Contact.contact_exist(number)

def display_contacts():
    '''
    Function that returns all the saved contacts
    '''
    return Contact.display_contacts()

def copy_email(self):
        """
        Copies the email address to the clipboard.
        """
        try:
            pyperclip.copy(self.email)
            print(f"Email '{self.email}' copied to clipboard successfully!")
        except Exception as e:
            print(f"Error copying email to clipboard: {e}")

def main():
    print("Hello Welcome to your contact list. What is your name?")
    user_name = input()

    print(f"Hello {user_name}. what would you like to do?")
    print('\n')

    while True:
        print("Use these short codes : cc - create a new contact, dc - display contacts, fc -find a contact, cp -copy a contact, del -delete a contact, ex -exit the contact list ")

        short_code = input().lower()

        if short_code == 'cc':
            print("New Contact")
            print("-"*10)

            print ("First name ....")
            f_name = input()

            print("Last name ...")
            l_name = input()

            print("Phone number ...")
            p_number = input()

            print("Email address ...")
            e_address = input()


            save_contacts(create_contact(f_name,l_name,p_number,e_address)) # create and save new contact.
            print ('\n')
            print(f"New Contact {f_name} {l_name} created")
            print ('\n')

        elif short_code == 'dc':

            if display_contacts():
                print("Here is a list of all your contacts")
                print('\n')

                for contact in display_contacts():
                    print(f"{contact.first_name} {contact.last_name} .....{contact.phone_number}")

                    print('\n')
            else:
                print('\n')
                print(r"You don't seem to have any contacts saved yet")
                print('\n')

        elif short_code == 'fc':

            print("Enter the number you want to search for")

            search_number = input()
            if check_existing_contacts(search_number):
                    search_contact = find_contact(search_number)
                    print(f"{search_contact.first_name} {search_contact.last_name}")
                    print('-' * 20)

                    print(f"Phone number.......{search_contact.phone_number}")
                    print(f"Email address.......{search_contact.email}")
            else:
                    print("That contact does not exist")
        elif short_code == 'cp':
            copy_email(p_number)
            
        elif short_code == 'del':
            print("Enter contact number you want to delete")
            
            search_number = input()
            
            if del_contact(search_number):
                search_contact = Contact.contact_list.remove(search_number)
                print("Number has been deleted successfully")
            else:
                print("Unable to delete contact")
                
            
        elif short_code == "ex":
            print("Bye .......")
            break
        else:
            print("I really didn't get that. Please use the short codes")
            print("/n")
            
if __name__ == '__main__':

    main()