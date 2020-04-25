# -*- coding: utf-8 -*-

import re

def split_syllables_by_hyphen(text):
    def add_hyphen(m):
        ret = m.group(1) + '-' + m.group(2)
        return ret
    
    rus_letters = "[абвгдеёжзийклмнопрстуфхцчшщъыьэюя]"
    rus_vowels = "[аеёиоуыэюя]"
    rus_consonants = "[бвгджзклмнпрстфхцчшщ]"
    rus_aux = "[йъь]"

#    print(f'all letters = {len(rus_letters)-2}')
#    print(f'vowels = {len(rus_vowels)-2}')
#    print(f'consonats = {len(rus_consonants)-2}')
    pattern1 = '('+rus_aux+')('+rus_letters + rus_letters+')'
    pattern2 = "("+rus_vowels+")("+rus_vowels+rus_letters+")"
    pattern3 = "("+rus_vowels+rus_consonants+")("+rus_consonants+rus_vowels+")"
    pattern4 = re.compile("("+rus_consonants+rus_vowels+")("+rus_consonants+rus_vowels+")", flags = re.I)
    pattern5 = "("+rus_vowels+rus_consonants+")("+rus_consonants+rus_consonants+rus_vowels+")"
    pattern6 = "("+rus_vowels+rus_consonants+rus_consonants+")("+rus_consonants+rus_consonants+rus_vowels+")"

    text=re.sub(pattern1, '\g<1>-\g<2>', text, flags=re.I)#re.I == re.IGNORECASE
    text=re.sub(pattern2, add_hyphen , text, flags=re.IGNORECASE)
    text=re.sub(pattern3, '\\1-\\2' , text, flags=re.IGNORECASE)
    text=re.sub(pattern4, r'\1-\2' , text)#sub with compiled process (flags = re.I has already added)
    text=re.sub(pattern5, add_hyphen , text, flags=re.IGNORECASE)
    text=re.sub(pattern6, add_hyphen , text, flags=re.IGNORECASE)
    return text




text = 'Маленький зайчишка достал ружьишко. Пальнул из него в небо, полил дождик где-то.'
print(text)
text = split_syllables_by_hyphen(text)
print(text)