money_in_mounth = int(input('Сколько вы разарботали в этом месяце?\n'))
procent_of_mortange = int(input('Какой процент уходит на ипотеку?\n'))
procent_of_live = int(input('Какой процент уходит на жизнь?\n'))
all_procent = (procent_of_mortange + procent_of_live)
free_money = money_in_mounth - (all_procent / 100 * money_in_mounth)    #Свободные деньги в месяц
procent_for_mortage = money_in_mounth - (procent_of_mortange/100 * money_in_mounth)
procent_for_mortage_2 = money_in_mounth - procent_for_mortage
print(f'На ипотеку было потраченно: {procent_for_mortage_2 * 12}')
print(f'Было накопленно: {free_money * 12}')

