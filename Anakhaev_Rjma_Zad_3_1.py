import math

number = int(input("Enter number to print: "))

number_list = ["(zero), ноль","(one), один","(two), два","(three), три","(four), четыре","(five), пять","(six), шесть","(seven), семь","(eight), восемь","(nine), девять"]
teen_list = ["(ten), десять","(eleven), одинадцать","(twelve), двенадцать","(thirteen), тринадцать", "(fourteen), четырнадцать","(fifteen), пятнадцать","(sixteen), шестнадцать","(seventeen), семнадцать","(eighteen), восемнадцать","(nineteen) девятнадцать"]
decades_list =["(twenty), двадцать","(thirty), тридцать","forty","(fifty), пятьдесат","(sixty), шестьдясят","(seventy), семдясат","(eighty), восемдясат","(ninety), девяноста"]


if number <= 9:
    print(number_list[number].capitalize())
elif number >= 10 and number <= 19:
    tens = number % 10
    print(teen_list[tens].capitalize())
elif number > 19 and number <= 99:
    ones = math.floor(number/10)
    twos = ones - 2
    tens = number % 10
    if tens == 0:
        print(decades_list[twos].capitalize())
    elif tens != 0:
        print(decades_list[twos].capitalize() + " " + number_list[tens])