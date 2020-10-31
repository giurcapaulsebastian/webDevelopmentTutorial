# f = open('simple.txt','r')
# f.write("Test write to simple text!")
# print("HELLO WORLD!")


try:
    f = open('simple.txt','r')
    f.write("Test write to simple text!")
except IOError:
    print("ERROR: COULD NOT FIND FILE OR READ DATA!")
finally:
    print("Happens no matter what!")
    f.close()
