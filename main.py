from morse import codes

def morseCode():
  morseList = []
  stringToTranslate = input("What text would you like to translate? ").lower()
  for char in stringToTranslate:
    if char in codes:
      morseList += codes[char] + ' '
    else:
      return print(f'No morse characters available for {char}')
  return print(''.join(morseList))


x = True
while x:
  y = input('Do you want to translate a phrase to morse code? (y/n) ')
  if y.lower() == 'y' or y.lower() == 'yes':
    morseCode()
  elif y.lower() == 'n' or y.lower() == 'no':
    x = False
  else:
    print('Please enter y or n')
