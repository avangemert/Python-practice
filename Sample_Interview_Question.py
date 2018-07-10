# Find which words are anagrams of each other and group them

# Display the groups.  You should end up with something like:
#
# ["badcredit", "debitcard"]
# ["elvis", "lives", "levis"]
# ["silent", "listen"]

# Function to return all anagrams together
def allAnagram(words):
     
    # empty dictionary which holds subsets 
    # of all anagrams together
    dict = {}
 
    # loop through list of strings
    for strVal in words:
         
        # sorted(iterable) method accepts any 
        # iterable and rerturns list of items
        # in ascending order
        key = ''.join(sorted(strVal))
         
        # now check if key exists in dictionary
        # or not. If yes, then simply append the  
        # strVal into the list of it's corresponding 
        # key. If not, then map empty list onto
        # key and then start appending values
        if key in dict.keys():
            dict[key].append(strVal)
        else:
            dict[key] = []
            dict[key].append(strVal)
 
     # loop through dictionary and concatenate values 
     # of keys together
        
        output = ""
    for key,value in dict.items():
        if len(value) > 1:
            output = output +"[" + ' '.join(value) + "]"
    return output

words = ["debitcard", "elvis", "silent", "badcredit", "lives", "freedom", "listen", "levis", "money"]
print (allAnagram(words))
