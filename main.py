def showGame():
  print('''RPG Game
  go[direction]
  get[item]''')

def showStatus():
  print('you are in ' + currentroom)
  print('inventory' + str(inventory))
  if "item" in rooms[currentroom]:
    print('you see a ' + rooms[currentroom]['item'])
    print('______________')

inventory=[]

rooms={'Hall':{'south':'Kitchen',
              'east': 'dining room',
               'item':'key'},
       'dining room':{'west':'Hall',
                    'south':'Garden',
                    'item':'potion'},
       'Kitchen':{'north':'Hall',
                 'east':'Garden',
                 'item':'monster'},
       'Garden':{'north':'dining room',
               'west':'Kitchen'}
      }   

currentroom = 'Hall'


showGame()
while True:
  showStatus()
  
  move = '' 
  while move == '':
    move = input('>')
  move = move.lower().split()

  if move[0] == 'go':
   if move[1] in rooms[currentroom]:
    currentroom = rooms[currentroom][move[1]]
   else:
      print('you cant go that way')
      
  if move[0] == 'get':
    if "item" in rooms[currentroom] and move[1] in rooms[currentroom]['item']:
      inventory += [move[1]]
      print (move[1] + 'got')
      del rooms[currentroom]['item']
    else:
      print('cannot get an item ' + move[1])
      
      
  if "item" in rooms[currentroom] and 'monster' in rooms[currentroom]['item']:
    print('There is a monster game over!')
    break
  
  if currentroom == 'Garden' and 'key' in inventory and 'potion' in inventory:
    print('You are a winner')
      
  
  


