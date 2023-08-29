#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    newList = [0] * list_length
    i = 0
    for i in range(list_length):
        try:
            division = my_list_1[i] / my_list_2[i]
            newList[i] = division
        except ZeroDivisionError:
            print("division by 0")
        except TypeError:
            print("wrong type")
        except IndexError:
            print("out of range")
        finally:
            pass
    return newList
