def print_formatted(number):
    if n > 0 and n < 100:
        string = ''
        ascii_number = 65
        string_numbers = ''
        octal_string = ''
        hexa_string = ''
        max = 16
        count = 1
        binary_string = ''
        binary = bin(number)
        for i in range(1, number + 1):
            # Decimal Numbers
            string_numbers = string_numbers + str(i)
            string = string_numbers.rjust(len(binary) - 2, ' ')
            # Octal Numbers
            o = i
            if o < 8:
                octal_string = str(o).rjust(len(binary) - 2, ' ')
                string = string + octal_string.rjust(len(binary) - 1, ' ')
            else:
                while o >= 8:
                    octal_string = octal_string + str(o % 8)
                    o = o // 8
                octal_string = octal_string + str(o % 8)
                string = string + octal_string[::-1].rjust(len(binary) - 1, ' ')
            # Hexadecimal Numbers
            h = i
            if h < 10:
                hexa_string = str(h).rjust(len(binary) - 2, ' ')
                string = string + hexa_string.rjust(len(binary) - 1, ' ')
            elif h >= 10 and h <= 15:
                hexa_string = chr(ascii_number).rjust(len(binary) - 2, ' ')
                string = string + hexa_string.rjust(len(binary) - 1, ' ')
                ascii_number = ascii_number + 1
            elif h >= 16 and h <= 25:
                hexa_string = str(h - 6).rjust(len(binary) - 2, ' ')
                string = string + hexa_string.rjust(len(binary) - 1, ' ')
                ascii_number = 65
            elif h >= 26 and h <= 31:
                hexa_string = '1' + chr(ascii_number)
                hexa_string = hexa_string.rjust(len(binary) - 2, ' ')
                string = string + hexa_string.rjust(len(binary) - 1, ' ')
                ascii_number = ascii_number + 1
            elif h >= 32 and h <= 41:
                hexa_string = str(h - 12).rjust(len(binary) - 2, ' ')
                string = string + hexa_string.rjust(len(binary) - 1, ' ')
                ascii_number = 65
            elif h >= 42 and h <= 47:
                hexa_string = '2' + chr(ascii_number)
                hexa_string = hexa_string.rjust(len(binary) - 2, ' ')
                string = string + hexa_string.rjust(len(binary) - 1, ' ')
                ascii_number = ascii_number + 1
            elif h >= 48 and h <= 57:
                hexa_string = str(h - 18).rjust(len(binary) - 2, ' ')
                string = string + hexa_string.rjust(len(binary) - 1, ' ')
                ascii_number = 65
            elif h >= 58 and h <= 63:
                hexa_string = '3' + chr(ascii_number)
                hexa_string = hexa_string.rjust(len(binary) - 2, ' ')
                string = string + hexa_string.rjust(len(binary) - 1, ' ')
                ascii_number = ascii_number + 1
            elif h >= 64 and h <= 73:
                hexa_string = str(h - 24).rjust(len(binary) - 2, ' ')
                string = string + hexa_string.rjust(len(binary) - 1, ' ')
                ascii_number = 65
            elif h >= 74 and h <= 79:
                hexa_string = '4' + chr(ascii_number)
                hexa_string = hexa_string.rjust(len(binary) - 2, ' ')
                string = string + hexa_string.rjust(len(binary) - 1, ' ')
                ascii_number = ascii_number + 1
            elif h >= 80 and h <= 89:
                hexa_string = str(h - 30).rjust(len(binary) - 2, ' ')
                string = string + hexa_string.rjust(len(binary) - 1, ' ')
                ascii_number = 65
            elif h >= 90 and h <= 95:
                hexa_string = '5' + chr(ascii_number)
                hexa_string = hexa_string.rjust(len(binary) - 2, ' ')
                string = string + hexa_string.rjust(len(binary) - 1, ' ')
                ascii_number = ascii_number + 1
            elif h >= 96 and h <= 99:
                hexa_string = str(h - 36).rjust(len(binary) - 2, ' ')
                string = string + hexa_string.rjust(len(binary) - 1, ' ')
                ascii_number = 65
            # Binary Numbers
            k = i
            if k == 1:
                binary_string = '1'.rjust(len(binary) - 2, ' ')
                string = string + binary_string.rjust(len(binary) - 1, ' ')
            else:
                while k > 1:
                    binary_string = binary_string + str(k % 2)
                    k = k // 2
                binary_string = binary_string + str(k % 2)
                binary_string = binary_string[::-1]
                string = string + binary_string.rjust(len(binary) - 1, ' ')
            print(string)
            string_numbers = ''
            octal_string = ''
            binary_string = ''
            string = ''


if __name__ == '__main__':
    n = int(input())
    print_formatted(n)