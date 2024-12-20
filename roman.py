class RomanNumeralConverter:
    def __init__(self):
        self.roman_values = {
            1000: 'M',
            900: 'CM',
            500: 'D',
            400: 'CD',
            100: 'C',
            90: 'XC',
            50: 'L',
            40: 'XL',
            10: 'X',
            9: 'IX',
            5: 'V',
            4: 'IV',
            1: 'I'
        }

    def to_roman(self, num):
        result = ""
        for value, numeral in self.roman_values.items():
            while num >= value:
                result += numeral
                num -= value
        return result

converter = RomanNumeralConverter()
roman_number = converter.to_roman(int(input("Enter a number")))
print(roman_number)