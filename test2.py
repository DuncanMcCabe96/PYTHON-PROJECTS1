def gotInfo():
    var1 = input("\nPlease provide the first numeric value: ")
    var2 = input("\nPlease provide the second numeric value: ")
    return(var1, var2)
    

def compute():
    go = True
    while go:
        var1, var2 = gotInfo()
        try:
            var3 = int(var1) + int(var2)
            go = False
        except ValueError as e:
            print("{}: \n\nYOU DIDN'T PROVIDE A NUMBERIC VALUE".format(e))
        except:
            print("\n\nyou provided an invald input, the program will close now")
    print("{} + {} = {}".format(var1, var2, var3))
    

        

if __name__ == "__main__":
    compute()
