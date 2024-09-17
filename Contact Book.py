import sys
def ContactBook():
	rows, cols = int(input("Please enter initial number of contacts: ")), 10
	contact_book = []
	print(contact_book)
	for i in range(rows):
		print("\nEnter contact %d details in the following order (ONLY):" % (i+1))
		print("NOTE: * indicates mandatory fields")
		print("....................................................................")
		temp = []
		for j in range(cols):
			if j == 0:
				temp.append(str(input("Enter name* : ")))
				if temp[j] == '' or temp[j] == ' ':
					sys.exit("Name is a mandatory field. Process exiting due to blank field...")
			if j == 1:
				temp.append(int(input("Enter contact number* : ")))
			if j == 2:
				temp.append(str(input("Enter e-mail : ")))
				if temp[j] == '' or temp[j] == ' ':
					temp[j] = None
					
			if j == 3:
				temp.append(str(input("Enter address : ")))
				if temp[j] == '' or temp[j] == ' ':
					temp[j] = None
					
		contact_book.append(temp)	
	print(contact_book)
	return contact_book

def menu():
	print("********************************************************************")
	print("\t\t\CONTACT BOOK", flush=False)
	print("********************************************************************")
	print("\tYou can now perform the following operations on this phonebook\n")
	print("1. Add a new contact")
	print("2. Remove an existing contact")
	print("3. Search for a contact")
	print("4. Display all contacts")
	print("5. Exit contact book")

	choice = int(input("Please enter your choice: "))
	return choice

def add_contact(cb):
	info = []
	for i in range(len(cb[0])):
		if i == 0:
			info.append(str(input("Enter name: ")))
		if i == 1:
			info.append(int(input("Enter number: ")))
		if i == 2:
			info.append(str(input("Enter e-mail address: ")))
		if i == 3:
			info.append(str(input("Enter date of address: ")))
	cb.append(info)
	return cb

def delete_contact(cb):
	srch = str(input("Please enter the name of the contact you wish to remove: "))
	
	temp = 0	
	for i in range(len(cb)):
		if srch == cb[i][0]:
			temp += 1			
			print(cb.pop(i))
			print("This contact has now been removed")
			return cb
	if temp == 0:
		print("Sorry, you have entered an invalid contact.\
	    Please recheck and try again later.")
		return cb

def search_contact(cb):
	choice = int(input("Enter search criteria\n\n\
	1. Name\n2. Number\n3. Email-id\n4. Address\nPlease enter: "))
	
	temp = []
	check = -1
	
	if choice == 1:
		srch = str(input("Please enter the name of the contact you wish to search: "))
		for i in range(len(cb)):
			if srch == cb[i][0]:
				check = i
				temp.append(cb[i])
				
	elif choice == 2:
		srch = int(input("Please enter the number of the contact you wish to search: "))
		for i in range(len(cb)):
			if srch == cb[i][1]:
				check = i
				temp.append(cb[i])
				
	elif choice == 3:
		srch = str(input("Please enter the e-mail ID of the contact you wish to search: "))
		for i in range(len(cb)):
			if srch == cb[i][2]:
				check = i
				temp.append(cb[i])
				
	elif choice == 4:
		srch = str(input("Please enter the address of the contact you wish to search: "))
		for i in range(len(cb)):
			if srch == cb[i][3]:
				check = i
				temp.append(cb[i])
				
	else:
		print("Invalid search criteria")
		return -1
	if check == -1:
		return -1
	else:
		display_all(temp)
		return check

def display_all(cb):
	if not cb:
		print("List is empty: []")
	else:
		for i in range(len(cb)):
			print(cb[i])

def thanks():
	print("********************************************************************")
	print("Thank you for using our Contact Book System.")
	print("Please visit again!")
	print("********************************************************************")
	sys.exit("Goodbye, have a nice day ahead!")

print("....................................................................")
print("Hello dear user, welcome to our Contact Book system")
print("You may now proceed to explore this contact book")
print("....................................................................")

ch = 1
cb = ContactBook()
while ch in (1, 2, 3, 4, 5):
	ch = menu()
	if ch == 1:
		cb = add_contact(cb)
	elif ch == 2:
		cb = delete_contact(cb)
	elif ch == 3:
		d = search_contact(cb)
		if d == -1:
			print("The contact does not exist. Please try again")
	elif ch == 4:
		display_all(cb)
	else:
		thanks()
