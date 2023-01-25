mySentence = 'loves the color'

color_list = ['red','blue','green','pink','teal','black']
#  variations below
def color_function(name):
    lst = []
    #1)print(color_list[0])
    #2)print("{} {}".format(mySentence,color_list[0]))
    for i in color_list:
        msg = "{} {} {}".format(name,mySentence,i)
        lst.append(msg)
    return lst 
    #return msg   # returns either red or black depending on the 
    # indentation but not all 6 
                   
        #3) print("{} {} {}".format(name,mySentence,i))
 
# color_function('Daniel')
lst = (color_function('Sally'))
for i in lst:
    print(i)



def get_name():
    name = input('What is your name?' )
    lst = color_function(name)
    for i in lst:
        print(i)

get_name


text1 = "My name is {}, I'm {}".format("Michael", "amazing!")
print(text1) 

