
import os
import re
from bs4 import BeautifulSoup

def get_info(source):

    def get_single_info(entry):
        return raw_info.find('span' , class_=entry).string

    info_entry = []
    info_source = open(source , 'r' , encoding = 'utf-8')
    raw_info = BeautifulSoup(info_source.read() , 'lxml')

    info_entry.append(get_single_info('champion_name'))
    info_entry.append(get_single_info('champintro-stats__info-name-en'))
    info_entry.append(get_single_info('stats_hp'))
    info_entry.append(get_single_info('stats_hpperlevel'))
    info_entry.append(get_single_info('stats_hpregen'))
    info_entry.append(get_single_info('stats_hpregenperlevel'))
    info_entry.append(get_single_info('stats_mp'))
    info_entry.append(get_single_info('stats_mpperlevel'))
    info_entry.append(get_single_info('stats_mpregen'))
    info_entry.append(get_single_info('stats_mpregenperlevel'))
    info_entry.append(get_single_info('stats_movespeed'))
    info_entry.append(get_single_info('stats_attackdamage'))
    info_entry.append(get_single_info('stats_attackdamageperlevel'))
    info_entry.append(get_single_info('stats_attackspeedoffset'))
    info_entry.append(get_single_info('stats_attackspeedperlevel'))
    info_entry.append(get_single_info('stats_attackrange'))
    info_entry.append(get_single_info('stats_armor'))
    info_entry.append(get_single_info('stats_armorperlevel'))
    info_entry.append(get_single_info('stats_spellblock'))
    info_entry.append(get_single_info('stats_spellblockperlevel'))

    info_source.close()
    return '\t'.join(info_entry)+'\n'


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
