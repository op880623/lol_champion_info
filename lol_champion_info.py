
import os
import re
import requests
from bs4 import BeautifulSoup

def champion_info_from(url):

    def ability_value_of(entry):
        return raw_info.find('span' , class_=entry).string

    url_content = requests.get(url)
    raw_info = BeautifulSoup(url_content.text , 'lxml')
    info_entry = []

    info_entry.append(ability_value_of('champion_name'))
    info_entry.append(ability_value_of('champintro-stats__info-name-en'))
    info_entry.append(ability_value_of('stats_hp'))
    info_entry.append(ability_value_of('stats_hpperlevel'))
    info_entry.append(ability_value_of('stats_hpregen'))
    info_entry.append(ability_value_of('stats_hpregenperlevel'))
    info_entry.append(ability_value_of('stats_mp'))
    info_entry.append(ability_value_of('stats_mpperlevel'))
    info_entry.append(ability_value_of('stats_mpregen'))
    info_entry.append(ability_value_of('stats_mpregenperlevel'))
    info_entry.append(ability_value_of('stats_movespeed'))
    info_entry.append(ability_value_of('stats_attackdamage'))
    info_entry.append(ability_value_of('stats_attackdamageperlevel'))
    info_entry.append(ability_value_of('stats_attackspeedoffset'))
    info_entry.append(ability_value_of('stats_attackspeedperlevel'))
    info_entry.append(ability_value_of('stats_attackrange'))
    info_entry.append(ability_value_of('stats_armor'))
    info_entry.append(ability_value_of('stats_armorperlevel'))
    info_entry.append(ability_value_of('stats_spellblock'))
    info_entry.append(ability_value_of('stats_spellblockperlevel'))

    return '\t'.join(info_entry)+'\n'


with open('champion.txt' , 'r' , encoding = 'utf8') as champion_list_source:
    content = champion_list_source.read()

pattern = 'https...lol.garena.tw.game.champion.\S+'
urls = re.findall(pattern , content)

with open('lol_champion_info.txt' , 'w') as champion_info:
    champion_info.write('英雄\t名稱\t生命\t生命成長\t生命回復\t生命回復成長\t魔力\t魔力成長\t魔力回復\t魔力回復成長\t移動速度\t物理攻擊\t物理攻擊成長\t攻擊速度\t攻擊速度成長\t攻擊距離\t物理防禦\t物理防禦成長\t魔法防禦\t魔法防禦成長\n')
    for url in urls:
        champion_info.write(champion_info_from(url[:-1]))
