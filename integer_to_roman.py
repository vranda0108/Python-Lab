def intToRoman(text, textbase=10):
    # Convert the input text to an integer based on the specified base (2 to 36)
    num = int(text, textbase)

    # Roman numeral conversion dictionary
    roman = {1000: 'M', 900: 'CM', 500: 'D', 400: 'CD', 100: 'C', 
             90: 'XC', 50: 'L', 40: 'XL', 10: 'X', 9: 'IX', 
             5: 'V', 4: 'IV', 1: 'I'}

    result = ''
    for value in sorted(roman.keys(), reverse=True):
        while num >= value:
            result += roman[value]
            num -= value

    return result

# Example usage:
print(intToRoman('11', 2))  
print(intToRoman('07', 8))  
print(intToRoman('73', 10)) 
print(intToRoman('1F', 16))  

