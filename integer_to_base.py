def base(text, text_base, output_base):
    def romanToInt(s):
        roman = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        total = 0
        prev_value = 0
        for char in reversed(s):
            value = roman[char]
            if value < prev_value:
                total -= value
            else:
                total += value
            prev_value = value
        return total

    def intToRoman(num):
        roman = {1000: 'M', 900: 'CM', 500: 'D', 400: 'CD', 100: 'C', 90: 'XC', 50: 'L', 40: 'XL', 10: 'X', 9: 'IX', 5: 'V', 4: 'IV', 1: 'I'}
        result = ''
        for value in sorted(roman.keys(), reverse=True):
            while num >= value:
                result += roman[value]
                num -= value
        return result

    def intToBase(num, base):
        digits = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        if num == 0:
            return "0"
        result = ""
        while num:
            result = digits[num % base] + result
            num //= base
        return result

    def baseToInt(text, base):
        digits = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        num = 0
        for char in text.upper():
            if char not in digits[:base]:
                raise ValueError(f"Invalid digit '{char}' for base {base}.")
            num = num * base + digits.index(char)
        return num

    def parsePrefix(text):
        if text.startswith('0b'):
            return 2, text[2:]
        elif text.startswith('0o'):
            return 8, text[2:]
        elif text.startswith('0x'):
            return 16, text[2:]
        else:
            return text_base, text

    input_base, clean_text = parsePrefix(text)

    if input_base == 'Roman':
        num = romanToInt(clean_text)
    else:
        num = baseToInt(clean_text, input_base)

    if output_base == 'Roman':
        return intToRoman(num)
    else:
        result = intToBase(num, output_base)
        if output_base == 2:
            return '0b' + result
        elif output_base == 8:
            return '0o' + result
        elif output_base == 16:
            return '0x' + result
        else:
            return result

print(base('0b1010', 2, 16))    
print(base('0x1F', 16, 2))      
print(base('0o123', 8, 10))     
print(base('35', 10, 'Roman'))  
print(base('0Z', 36, 10))       
print(base('0b11011', 2, 10))   
print(base('XXVII', 'Roman', 2)) 

