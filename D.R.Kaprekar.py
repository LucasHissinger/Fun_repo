def nb_is_not_valid(nb):
    if nb == 0:
        return True
    nb = str(nb)
    if len(nb) != 3:
        print("3 numbers i said -_-")
        return True
    elif nb.count(nb[0]) != 1 or nb.count(nb[1]) != 1 or nb.count(nb[2]) != 1:
        print("Each digit must be different...")
        return True
    else:
        return False

def largest_to_smallest(nb):
    list1=[]
    list1[:0]=str(nb)
    list1.sort(reverse=True)
    nb = ''.join(list1)
    return int(nb)

def substract(nb):
    sub = str(nb)
    sub = sub[::-1]
    return int(nb) - int(sub)

choice_nb = 0
count = 0
while (nb_is_not_valid(choice_nb)):
    choice_nb = int(input("Enter number with 3 différents numbers :  "))
while(choice_nb != 495):
    choice_nb = largest_to_smallest(choice_nb)
    choice_nb = substract(choice_nb)
    print(choice_nb)
    count += 1
print("its take " + str(count) + " generations")