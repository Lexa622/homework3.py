my_string = input('введите произвольный текст: ')
print('длинна символов ', len(my_string), '\nстрока в верхнем регистре ', my_string.upper(),\
      '\nстрока в нижнем регистре ', my_string.lower(), '\nстрока без пробелов ',my_string.replace(' ',''),\
      '\nпервый символ строки ',my_string[0], '\nпоследний символ строки', my_string[len(my_string) - 1])