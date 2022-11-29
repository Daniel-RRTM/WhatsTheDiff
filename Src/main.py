
from colorama import init,Fore,Style


init(autoreset=True)


print(Style.BRIGHT+Fore.YELLOW+"enter first text:")
first_text  = input()
print(Style.BRIGHT+Fore.YELLOW+"enter second text:")
second_text = input()

to_itterate = len(first_text) if len(first_text) >= len(second_text) else len(second_text)

first_print  = ""
second_print = ""


for char_nr in range(to_itterate):

    if len(first_text) > char_nr  : first_char  = first_text[char_nr]
    else                          : first_char  = ""
    if len(second_text) > char_nr : second_char  = second_text[char_nr]
    else                          : second_char  = ""
    

    if first_char == second_char :
        first_print  += Style.NORMAL+Fore.WHITE+first_char
        second_print += Style.NORMAL+Fore.WHITE+first_char
    else:
        first_print  += Style.BRIGHT+Fore.YELLOW+first_char
        second_print += Style.BRIGHT+Fore.GREEN+second_char



print()
print(first_print)
print("---------------------")
print(second_print)
print()


