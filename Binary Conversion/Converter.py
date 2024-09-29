import pygame

class Converter:
    def update(self, type1, type2, input):
        # self.type1 = type1
        # self.type2 = type2

        # self.input = None

        # if input is not None: 

        #     try:
        #         self.input = int(input)
        #     except ValueError:
        #         return 

        # if self.input is not None:

        #     if (self.type1 == 1):
        #         self.input = oct(self.input)[2:]
        #     elif (self.type1 == 2):
        #         self.input = hex(self.input)[2:].upper()
        #     elif (self.type1 == 3):
        #         self.input = bin(self.input)[2:]
        #     # elif (self.type1 == 0):
        #     #     self.input = str(self.input)

        #         if self.type1 in {1, 2, 3}:
        #             try:
        #                 # Base map to convert back to integer based on the type1 conversion
        #                 base = {
        #                     1: 8,  # Octal
        #                     2: 16, # Hexadecimal
        #                     3: 2   # Binary
        #                 }[self.type1]
                
        #                 # Convert the string back to an integer using the proper base
        #                 self.input = int(self.input, base)
        #             except ValueError:
        #                 print("Failed to convert back to integer.")
        #                 return None

        #     if (self.type2 == 1):
        #         self.input = oct(self.input)[2:]
        #     elif (self.type2 == 2):
        #         self.input = hex(self.input)[2:].upper()
        #     elif (self.type2 == 3):
        #         self.input = bin(self.input)[2:]
        #     elif (self.type2 == 0):
        #         self.input = str(self.input)
                
        #     return str(self.input)

        if input == None:
            return None


        try:
            if type1 == 0:  # Input is decimal
                decimal_value = int(input)
            elif type1 == 1:  # Input is octal
                decimal_value = int(input, 8)
            elif type1 == 2:  # Input is hexadecimal
                decimal_value = int(input, 16)
            elif type1 == 3:  # Input is binary
                decimal_value = int(input, 2)
            else:
                print("Invalid type1 provided.")
                return None
        except ValueError:
            print("Invalid input for the given type1.")
            return None

        # Convert decimal to the desired output type
        if type2 == 0:  # Convert to decimal
            return str(decimal_value)
        elif type2 == 1:  # Convert to octal
            return oct(decimal_value)[2:]  # Remove '0o' prefix
        elif type2 == 2:  # Convert to hexadecimal
            return hex(decimal_value)[2:].upper()  # Remove '0x' prefix and make uppercase
        elif type2 == 3:  # Convert to binary
            return bin(decimal_value)[2:]  # Remove '0b' prefix
        else:
            print("Invalid type2 provided.")
            return None