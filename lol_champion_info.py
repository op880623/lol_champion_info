
import os
import re

def get_info(source):
    name = "英雄"
    name_eng = "champion"
    stats_hp = '0'
    stats_hpperlevel = '0'
    stats_hpregen = '0'
    stats_hpregenperlevel = '0'
    stats_mp = '0'
    stats_mpperlevel = '0'
    stats_mpregen = '0'
    stats_mpregenperlevel = '0'
    stats_movespeed = '0'
    stats_attackdamage = '0'
    stats_attackdamageperlevel = '0'
    stats_attackspeedoffset = '0'
    stats_attackspeedperlevel = '0'
    stats_attackrange = '0'
    stats_armor = '0'
    stats_armorperlevel = '0'
    stats_spellblock = '0'
    stats_spellblockperlevel = '0'
    info_string = ''
    info_source = open(source , 'r' , encoding = 'utf-8')
    for line in info_source:
        if re.search('champion_name\\"\\>(\S+)\\<' , line):
            name = re.search('champion_name\\"\\>(\S+)\\<' , line).group(1)
            info_string = info_string + name + '\t'
        if re.search('name-en\\"\\>(.*)\\<' , line):
            name_eng = re.search('name-en\\"\\>(.*)\\<' , line).group(1)
            info_string = info_string + name_eng + '\t'
        if re.search('stats_hp\\"\\>(\S+)\\<' , line):
            stats_hp = re.search('stats_hp\\"\\>(\S+)\\<' , line).group(1)
            info_string = info_string + stats_hp + '\t'
        if re.search('stats_hpperlevel\\"\\>(\S+)\\<' , line):
            stats_hpperlevel = re.search('stats_hpperlevel\\"\\>(\S+)\\<' , line).group(1)
            info_string = info_string + stats_hpperlevel + '\t'
        if re.search('stats_hpregen\\"\\>(\S+)\\<' , line):
            stats_hpregen = re.search('stats_hpregen\\"\\>(\S+)\\<' , line).group(1)
            info_string = info_string + stats_hpregen + '\t'
        if re.search('stats_hpregenperlevel\\"\\>(\S+)\\<' , line):
            stats_hpregenperlevel = re.search('stats_hpregenperlevel\\"\\>(\S+)\\<' , line).group(1)
            info_string = info_string + stats_hpregenperlevel + '\t'
        if re.search('stats_mp\\"\\>(\S+)\\<' , line):
            stats_mp = re.search('stats_mp\\"\\>(\S+)\\<' , line).group(1)
            info_string = info_string + stats_mp + '\t'
        if re.search('stats_mpperlevel\\"\\>(\S+)\\<' , line):
            stats_mpperlevel = re.search('stats_mpperlevel\\"\\>(\S+)\\<' , line).group(1)
            info_string = info_string + stats_mpperlevel + '\t'
        if re.search('stats_mpregen\\"\\>(\S+)\\<' , line):
            stats_mpregen = re.search('stats_mpregen\\"\\>(\S+)\\<' , line).group(1)
            info_string = info_string + stats_mpregen + '\t'
        if re.search('stats_mpregenperlevel\\"\\>(\S+)\\<' , line):
            stats_mpregenperlevel = re.search('stats_mpregenperlevel\\"\\>(\S+)\\<' , line).group(1)
            info_string = info_string + stats_mpregenperlevel + '\t'
        if re.search('stats_movespeed\\"\\>(\S+)\\<' , line):
            stats_movespeed = re.search('stats_movespeed\\"\\>(\S+)\\<' , line).group(1)
            info_string = info_string + stats_movespeed + '\t'
        if re.search('stats_attackdamage\\"\\>(\S+)\\<' , line):
            stats_attackdamage = re.search('stats_attackdamage\\"\\>(\S+)\\<' , line).group(1)
            info_string = info_string + stats_attackdamage + '\t'
        if re.search('stats_attackdamageperlevel\\"\\>(\S+)\\<' , line):
            stats_attackdamageperlevel = re.search('stats_attackdamageperlevel\\"\\>(\S+)\\<' , line).group(1)
            info_string = info_string + stats_attackdamageperlevel + '\t'
        if re.search('stats_attackspeedoffset\\"\\>(\S+)\\<' , line):
            stats_attackspeedoffset = re.search('stats_attackspeedoffset\\"\\>(\S+)\\<' , line).group(1)
            info_string = info_string + stats_attackspeedoffset + '\t'
        if re.search('stats_attackspeedperlevel\\"\\>(\S+)\\<' , line):
            stats_attackspeedperlevel = re.search('stats_attackspeedperlevel\\"\\>(\S+)\\<' , line).group(1)
            info_string = info_string + stats_attackspeedperlevel + '\t'
        if re.search('stats_attackrange\\"\\>(\S+)\\<' , line):
            stats_attackrange = re.search('stats_attackrange\\"\\>(\S+)\\<' , line).group(1)
            info_string = info_string + stats_attackrange + '\t'
        if re.search('stats_armor\\"\\>(\S+)\\<' , line):
            stats_armor = re.search('stats_armor\\"\\>(\S+)\\<' , line).group(1)
            info_string = info_string + stats_armor + '\t'
        if re.search('stats_armorperlevel\\"\\>(\S+)\\<' , line):
            stats_armorperlevel = re.search('stats_armorperlevel\\"\\>(\S+)\\<' , line).group(1)
            info_string = info_string + stats_armorperlevel + '\t'
        if re.search('stats_spellblock\\"\\>(\S+)\\<' , line):
            stats_spellblock = re.search('stats_spellblock\\"\\>(\S+)\\<' , line).group(1)
            info_string = info_string + stats_spellblock + '\t'
        if re.search('stats_spellblockperlevel\\"\\>(\S+)\\<' , line):
            stats_spellblockperlevel = re.search('stats_spellblockperlevel\\"\\>(\S+)\\<' , line).group(1)
            info_string = info_string + stats_spellblockperlevel + '\n'
    info_source.close()
    return info_string

##download all champion file
champion_list_source = open('champion.txt' , 'r' , encoding = 'utf8')

content = champion_list_source.read()
pattern = 'https...lol.garena.tw.game.champion.\S+'
urls = re.findall(pattern , content)

for url in urls:
    print(url[:-1])
    os.system("wget " + url[:-1] + " --no-check-certificate --directory-prefix=lolchampion/")

champion_list_source.close()



os.system("cmd /u /c dir /b lolchampion > filelist.txt")
os.system("ConvertZ /i:ULE /o:utf8 filelist.txt filelist.txt")


##filter information
champion_list = open('filelist.txt' , 'r')
champion_info = open('lol_champion_info.txt' , 'w')
champion_info.write('英雄\t名稱\t生命\t生命成長\t生命回復\t生命回復成長\t魔力\t魔力成長\t魔力回復\t魔力回復成長\t移動速度\t物理攻擊\t物理攻擊成長\t攻擊速度\t攻擊速度成長\t攻擊距離\t物理防禦\t物理防禦成長\t魔法防禦\t魔法防禦成長\n')

for line in champion_list:
    champion_name = "lolchampion/" + line.rstrip()
    info = get_info(champion_name)
    champion_info.write(info)


champion_list.close()
champion_info.close()

##remove progessive file
os.system("del filelist.txt")
os.system("rd lolchampion /S /Q")
