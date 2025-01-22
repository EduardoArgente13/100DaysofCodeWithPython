class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        val = [
            1000, 900, 500, 400,
            100, 90, 50, 40,
            10, 9, 5, 4,
            1
        ]
        syms = [
            "M", "CM", "D", "CD",
            "C", "XC", "L", "XL",
            "X", "IX", "V", "IV",
            "I"
        ]
        roman_numeral = ""
        for i in range(len(val)):
            while num >= val[i]:
                roman_numeral += syms[i]
                num -= val[i]
        return roman_numeral

# Ejemplo de uso:
solution = Solution()
print(solution.intToRoman(3))      # Salida: "III"
print(solution.intToRoman(4))      # Salida: "IV"
print(solution.intToRoman(9))      # Salida: "IX"
print(solution.intToRoman(58))     # Salida: "LVIII"
print(solution.intToRoman(1994))   # Salida: "MCMXCIV"
