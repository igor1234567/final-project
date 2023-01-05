"""We have an existing dictionary that maps US states to their capitals.
1. Print the state capital of Idaho
2. Print all states.
3. Print all capitals.
4. Create a single string 'Alabama -> Montgomery, Alaska -> Juneau, ...'
5. Ensure the string you created in 4. is alphabetically sorted by state
7. Now we want to add the reverse look up, given the name of a capital what state
is it in?
Implement the function def get_state(capital): below so it returns the state.
GOTCHAS: What happens if two states have the same capital name, how do you
handle that?
"""

STATES_CAPITALS= {
    'Alabama':'Montgomery',
    'Alaska':'Juneau',
    'Arizona':'Phoenix',
    'Arkansas':'Little Rock',
    'California':'Sacramento',
    'Colorado':'Denver',
    'Connecticut':'Hartford',
    'Delaware':'Dover',
    'Florida':'Tallahassee',
    'Georgia':'Atlanta',
    'Hawaii':'Honolulu',
    'Idaho':'Boise',
    'Illinois':'Springfield',
    'Indiana':'Indianapolis',
    'Iowa':'Des Moines',
    'Kansas':'Topeka',
    'Kentucky':'Frankfort',
    'Louisiana':'Baton Rouge',
    'Maine':'Augusta',
    'Maryland':'Annapolis',
    'Massachusetts':'Boston',
    'Michigan':'Lansing',
    'Minnesota':'Saint Paul',
    'Mississippi':'Jackson',
    'Missouri':'Jefferson City',
    'Montana':'Helena',
    'Nebraska':'Lincoln',
    'Nevada':'Carson City',
    'New Hampshire':'Concord',
    'New Jersey':'Trenton',
    'New Mexico':'Santa Fe',
    'New York':'Albany',
    'North Carolina':'Raleigh',
    'North Dakota':'Bismarck',
    'Ohio':'Columbus',
    'Oklahoma':'Oklahoma City',
    'Oregon':'Salem',
    'Pennsylvania':'Harrisburg',
    'Rhode Island':'Providence',
    'South Carolina':'Columbia',
    'South Dakota':'Pierre',
    'Tennessee':'Nashville',
    'Texas':'Austin',
    'Utah':'Salt Lake City',
    'Vermont':'Montpelier',
    'Virginia':'Richmond',
    'Washington':'Olympia',
    'West Virginia':'Charleston',
    'Wisconsin':'Madison',
    'Wyoming':'Cheyenne',
}

#print capital of Idaho
def capital_of_Idaho():
    for key,value in STATES_CAPITALS.items():
        if key == "Idaho":
            print("\n"+str(value)+"\n")

#print all states
def all_states():
    print("states: \n" ,list(dict.fromkeys(STATES_CAPITALS)),"\n")

#print all capital cities
def all_capitals():
    print("capitals: \n" ,list(dict.values(STATES_CAPITALS)),"\n")

#print single string 'Alabama -> Montgomery, Alaska -> Juneau, ... and it is alphabetically sorted (steps 4 and 5 combined)
def states_capitals_string():
    mystr= ""
    for key, value in sorted(STATES_CAPITALS.items()):
        mystr += key + " -> " + value + ", "
    print(mystr+"\n")

#print capital by state input and reverse  look up combined in one function (steps 6 and 7 combined)
def get_state(capital):
    if capital in STATES_CAPITALS.keys():
        print(STATES_CAPITALS[capital]+"\n")
    elif capital in STATES_CAPITALS.values():
        print(list(STATES_CAPITALS.keys())[list(STATES_CAPITALS.values()).index(capital)]+"\n")

#handle two capital cities with same name
#loop thrugh STATES_CAPITALS if input == capital city then append to list
#after loop check len of list to determine if there duplicates in capital cities
def two_states_same_capital():
    capital= input("enter a capital city or country: ")
    mycapital= list(capital)
    mycapital[0]= mycapital[0].upper()
    capital= ''.join(mycapital)
    keys= []
    for key, value in STATES_CAPITALS.items():
        if value == capital:
            keys.append(key)
    if len(keys) > 1:
        print("there are " + str(len(keys)) + " states with the same capital"+"\n")
        print("states: " ,keys,"\n")
    else:
        print("there are no duplicates in capital cities names"+"\n")


capital_of_Idaho()

all_states()

all_capitals()

states_capitals_string()

capital= input("enter a state: ")
mycapital= list(capital)
mycapital[0]= mycapital[0].upper()
capital= ''.join(mycapital)
get_state(capital)

capital= input("enter a capital city: ")
mycapital= list(capital)
mycapital[0]= mycapital[0].upper()
capital= ''.join(mycapital)
get_state(capital)

two_states_same_capital()

