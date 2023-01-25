

mySentence = 'I love the color'

color_list = ['red','blue','green','pink','teal','black']
# 3 variations below
def color_function():
    #1)print(color_list[0])
    #2)print("{} {}".format(mySentence,color_list[0]))
    for i in color_list:
        print("{} {}".format(mySentence,i))


color_function()



def this_function():
    print("Hi!")

this_function()