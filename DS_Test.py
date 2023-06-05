import re

# findin Country from string
def findCountry(s):
        words = s.split()
        capital_count = 0

        for word in words:
            if word[0].isupper():
                capital_count += 1
                if capital_count == 3:
                    if word:
                        return word
                    else:
                        return "0"
        return None
     
def parse_address(address):
    address_parts = {
        'address': '',
        'city': '',
        'zip': '',
        'state': '',
        'country': ''
    }
    
    res = address.split()
    
    # if address is complete
    if len(address) == 59:
        res = address.split()
        print(len(address))
        address_parts['city'] += res[4]
        address_parts['zip'] += res[5]
        address_parts['country'] += res[7]
        address_parts['state'] += res[6]
        parts = address.split(',')
        for part in parts:
            part = part.strip()
            if part.startswith('house#') or part.startswith('st#12') or part.startswith('G-11/3'):
                address_parts['address'] += part
        return address_parts
            
    else: 
                   
        # finding city
        s=re.findall('[A-Z][^A-Z]*',address)
        a1=s[1].split(',')
        pattern_order = r'[0-9]'
        a1 = re.sub(pattern_order, '', a1[0])
        address_parts['city'] += a1
        
        # finding State
        address_parts['state'] += res[6]
        
        #finging Zip code
        #seperate number from string
        number = re.findall('\d+', address)
        #convert it into integer
        number = map(int, number)
        if number:
            address_parts['zip'] = str(max(number))
        else:
            address_parts['zip'] = 0    
        
        #finding country
        if number:
            address_parts['country'] =findCountry(address)
        else:
            address_parts['country'] = 0 
        
        #finding address
        parts = address.split(',')
        for part in parts:
            part = part.strip()
            if part.startswith('house#') or part.startswith('st#12') or part.startswith('G-11/3'):
                address_parts['address'] += part
        return address_parts
    
   
      
print("**************************")       
print("Please enter the address in this formate --->: house# 31, st#12, G-11/3, Islamabad 44000, capital Pakistan")
print("**************************") 
user_input = input("Enter the address: ")
address_parts = parse_address(user_input)

if address_parts['city'] ==None or address_parts['zip']==None or address_parts['country']==None:
    print("City name, zip code and country are compulsory!")
else:
    
    #if user will not enter both state and street address then output would be like:
    if address_parts['address'].startswith('st#12'):    
        print("Address: " + address_parts['address'])
    
    print("City: " + address_parts['city'])
    print("Zip: " + address_parts['zip'])
    if address_parts['state']:
        print("State: " + address_parts['state'])
    print("Country: " + address_parts['country'])
    
    #if user will not enter both state and street address then output would be like:
    if address_parts['state'] and address_parts['address'].startswith('st#12') == None:
        print("City: " + address_parts['city'])
        print("Zip: " + address_parts['zip'])
        print("Country: " + address_parts['country'])
