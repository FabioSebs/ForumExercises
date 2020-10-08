#Exercise 4

def calc_new_height():
    w,h,dw = int(input("Enter the current width: ")) , int(input("Enter the current height: ")), int(input("Enter the desired width: "))
    x , y = ratio(w,h)
    dh = y*dw/x
    print("The corresponding height is: ", dh)

def ratio(width, height):
    while width % 2 == 0 and height % 2 == 0:
        ratio(width//2,height//2)
        break
    return(width,height)
 
calc_new_height()
        

