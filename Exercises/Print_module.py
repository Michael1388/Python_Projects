#Creates a usable module from "Our_Module.py" file

import Our_Module 
# would need full path if not located in same directory folder

#we can pass numbers hinto this module to get answers returned 
# by the module we created in Our_Module


if __name__ == "__main__":
    results = Our_Module.getNumbers(5,9)
    print(results)
