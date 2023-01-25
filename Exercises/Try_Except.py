#Error Handling

def getinfo():
    var1 = input("\nPlease provide the first numeric value: ")
    var2 = input("\nPlease provide the second numeric value: ")
    return (var1, var2)


def compute():
    go = True
    while go:
        var1,var2 = getinfo()
        try:
            var3 = int(var1) + int(var2)
            go = False

        except ValueError as e:
            print("{}: \n\nYou did not provide a numeric value ie., 5, 6, 7".format(e))
        except:
            print("\n\nOops, you provided an invalid input, the program will close now!")
    print("{} + {} = {}".format(var1, var2, var3))
    
    
    
    
    
    #finally: 
    # print("Moving on...")



if __name__ == "__main__":
    compute()