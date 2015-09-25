color1 = str
color2 = str
accepted_color_list = ['red', 'blue', 'yellow']

def getColor1():
       color1 = str (input ('Please input first color:'))
       while color1 in accepted_color_list:
              print ('Color is:',color1)
              return #exits the function and returns control to main

       #otherwise do this
       print ('Error: You can only select red, blue, or yellow as your primary colors')
       getColor1()


def getColor2():
       color2 = str (input ('Please input second color:'))
       if (color2 != 'red'):
              print ('Error: You can only select red, blue, or yellow as your primary colors')
              getColor2
       else:
              print ('Color is:',color2)
              return color2

def setValidation():
       if color1 == color2:
              print ('Error: Two Primary colors cannot be the same')

       else:
              print ('Selected colors are:',color1, 'and',color2)

def main():
       getColor1()
       getColor2()
       setValidation()

main()
              #if (color1 != 'blue'):
             # print ('Error: You can only select red, blue, or yellow as your primary colors')
       #else:
              #print ('Color is:',color1)

              #elif (color1 != 'blue'):
                     #print ('Error: You can only select red, blue, or yellow as your primary colors')
              #else:
                     #print ('Color is:',color1)
