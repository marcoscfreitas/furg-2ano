def count(index) :
    if index < 2 :
        count(index+1)
    print(index)

count(0)