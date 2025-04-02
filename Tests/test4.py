class Solution(object):
    def rotatedDigits(self, n):
        """
        :type n: int
        :rtype: int
        """
        def isGoodNumber(x):
            # Diccionario de rotación de dígitos
            rotation_map = {'0': '0', '1': '1', '8': '8', '2': '5', '5': '2', '6': '9', '9': '6'}
            
            # Convertir el número a cadena para manejar dígitos individualmente
            x_str = str(x)
            
            # Variable para verificar si al menos un dígito cambia
            is_good = False
            
            # Iterar sobre cada dígito del número
            for digit in x_str:
                if digit not in rotation_map:
                    return False  # El dígito no es válido después de la rotación
                if rotation_map[digit] != digit:
                    is_good = True  # Al menos un dígito cambia
            
            return is_good

        count = 0
        # Iterar sobre cada número desde 1 hasta n
        for i in range(1, n + 1):
            if isGoodNumber(i):
                count += 1  # Incrementar el contador si el número es "bueno"
        return count

# Ejemplo de uso
solution = Solution()
print(solution.rotatedDigits(10))  # Salida: 4
print(solution.rotatedDigits(1))   # Salida: 0
print(solution.rotatedDigits(2))   # Salida: 1
