def conv_binary(number):
    binary_string = 0
    binary_list = []
    while number > 0:
        y = number % 10
        number = int(number / 10)
        binary_list.append(y)

    n = 0
    for i in binary_list:

        if i > 0:
            x = pow(2, n)
            binary_string += x
            n = n+1
        else:
            n = n+1

    print(binary_string)


conv_binary(number=int(input("ENTER THE BINARY: ")))
