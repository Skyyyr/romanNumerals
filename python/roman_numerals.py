def to_roman(num):
    # write your code here!
    numeralMap = {
        'M': 1000,
        'CM': 900,
        'D': 500,
        'CD': 400,
        'C': 100,
        'XC': 90,
        'L': 50,
        'XL': 40,
        'X': 10,
        'V': 5,
        'IV': 4,
        'I': 1,
    }
    output = ''
    for k in numeralMap:
        while num >= numeralMap[k]:
            output += k
            num -= numeralMap[k]
    return output
