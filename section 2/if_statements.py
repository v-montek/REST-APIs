
xyz=['abc','xyz']
known_people = ['john','hannah','mary',xyz]
person = input('Enter a name')
if person in known_people:
    print('Yo now {}'.format(person))
else:
    print('Yo do not now {}'.format(person))
print(known_people)
