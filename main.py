'''           Question 1      '''
# Implement a group_by_owners function that:

# Accepts a dictionary containing the file owner name for each file name. Returns a dictionary containing a list of file names for each owner name, in any order. For example, for dictionary {'Input.txt': 'Randy', 'Code.py': 'Stan', 'Output.txt': 'Randy'} the group_by_owners function should return {'Randy': ['Input.txt', 'Output.txt'], 'Stan': ['Code.py']}.


# def group_by_owners(files):

#   ownerdict = {}
  
#   for files, owner in files.items():
#     if owner in ownerdict: #key is owner
#       ownerdict[owner].append(files)
#     else :
#       ownerdict[owner]= [files]
      
#   ownerdict = dict(sorted(ownerdict.items()))    
#   return ownerdict

# if __name__ == "__main__":    
#     files = {
#         'Input.txt': 'Randy',
#         'Code.py': 'Atan',
#         'Output.txt': 'Randy'
#     }   
#     print(group_by_owners(files))

'''Question 2'''

import numpy as np

def find_roots(a, b, c):
    input = [a, b, c]
    answer = tuple(np.roots(input))
    if answer[0] == answer[1]:
      answer = (answer[0],)
     
    return answer

print(find_roots(-1, 2, -1));