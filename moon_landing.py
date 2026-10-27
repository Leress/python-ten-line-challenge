stats ={'height':500, 'velocity': 50, 'fuel':120 }
while(stats['fuel'] > 0):
    print(f"height: {stats['height']},velocity: {stats['velocity']},fuel: {stats['fuel']}")
    burn = int(input(f'How much fuel to use? (0-30):'))
    if burn < 0: burn == 0
    if burn >30: burn == 30
    if burn > stats['fuel']: burn == stats['fuel']
    v1 = stats['velocity'] - burn + 5
    stats['fuel'] = stats['fuel'] - burn
    if ((v1 + stats['velocity']/2) >= stats['height']):
        break
    stats['height'] = stats['height'] - (v1 + stats['velocity'])/2
    stats['velocity'] = v1
v1 = stats['velocity'] + (5- burn) * stats['height']/stats['velocity']
if v1 >5: print('you crashed all have died')
if v1 >1 and v1<=5: print('ok but some injuries')
if v1 <=1: print('safe landing')