#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    result = []
    for i in range(list_length):
        try:
            num1 = my_list_1[i]
            num2 = my_list_2[i]
            if not (isinstance(num1, (int, float)) and isinstance(num2, (int, float))):
                print("wrong type")
                result.append(0)
            else:
                try:
                    division = num1 / num2
                    result.append(division)
                except ZeroDivisionError:
                    print("division by 0")
                    result.append(0)
        except IndexError:
            print("out of range")
            result.append(0)
        finally:
            pass  # Required to satisfy the "finally" constraint
    return result
