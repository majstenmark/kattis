short = {'thou': 'th', 'inch': 'in', 'foot': 'ft', 'yard':'yd', 'chain': 'ch', 'furlong': 'fur', 'mile':'mi', 'league':'lea'}
trans = {'in': (1000, 'th'), 'ft': (12, 'in'), 'yd': (3, 'ft'), 'ch': (22, 'yd'), 'fur': (10, 'ch'), 'mi': (8, 'fur'), 'lea': (3, 'mi')}
allinth = {'th': 1}
for unit, mapping in trans.items():
    translation, smaller_unit = mapping
    nbr_of_ths = translation * allinth[smaller_unit]
    allinth[unit] = nbr_of_ths
line = raw_input().split()
v= int(line[0])
unit1 = line[1]
if unit1 in short:
    unit1 = short[unit1]
unit2 = line[-1]
if unit2 in short:
    unit2 = short[unit2]
tot_th = v * allinth[unit1]
res = tot_th * 1.0/allinth[unit2]
print(res)
