import random # Esta librería va a servir como el motor para que Python escoja una opción aleatoria dentro de su arreglo.

# Este es un programa que representa al juego "Piedra, papel, tijeras".

# Parte 1 - User section
options = ('piedra', 'papel', 'tijeras')
print('Bienvenido, escoge una de las siguientes opciones:', options[0:3])
user_option = input('¿Qué eliges?:')
user_option = user_option.lower()
print('Tu respuesta fue:', user_option)

if not user_option in options:
  print('Esa opción no es válida.')

# Parte 2 - Python's choice
computer_option = random.choice(options) # La función random, con el método choice nos permite aplicar la selección de un elemento al azar de la tupla
print('Elección de Python =>', computer_option)

# Caso: Empate 
if user_option == computer_option:
  print('¡Empate!')
  
# Caso: user option == 'piedra'
#       computer_option == 'tijeras'
elif user_option == 'piedra':
  if computer_option == 'tijeras':
    print('Piedra vence a tijeras')
    print('¡Has ganado!')
  else: #computer_option == 'papel'
    print('Papel gana a piedra.')
    print('Python gana (\(n . n)/)')
    
# Caso: user option == 'papel'
#       computer_option == 'piedra'
elif user_option == 'papel':
  if computer_option == 'piedra':
    print('Papel vence a piedra.')
    print('El usuario gana.')
  else: # computer_option == 'tijeras'
    print('Tijeras vence a papel')
    print('Python gana (\(n . n)/)')
    
# Caso: user option == 'tijeras'
#       computer_option == 'papel'
elif user_option == 'tijeras':
  if computer_option == 'papel':
    print('Tijeras vence a papel.')
    print('El usuario gana.')
  else:                               # computer_option == 'piedra'
    print('Piedra vence a tijeras.')
    print('Python gana (\(n . n)/)')

print('¡Gracias por jugar, hasta luego!')
