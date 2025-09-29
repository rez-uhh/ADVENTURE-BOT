def check_string(str):
    if str.startswith('The'):
        print("Found it!")
    else:
        print ("Nope.")

str1 = 'The'
str2 = 'Thumbs up'
str3 = 'Theatre can be boring'

check_string(str1)
check_string(str2)
check_string(str3)
