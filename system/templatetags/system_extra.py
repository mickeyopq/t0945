#coding: utf-8 -*-
from django import template
from django.utils.translation import ugettext as _
from atexit import register

register = template.Library()
@register.filter(name='transto')
def transto(value):
    #print(value)
    return _(value)

@register.filter(name='phone')
def phone(value):
	if value != '':
		phone = '(%s) %s%s' %(value[0:2],value[2:5],value[5:10])
		return phone
	else:
		return ''

@register.filter(name='money_format')
def money_format(value):
    if value != '':        
        return format(value,',')
    else:
        return 0
@register.filter(name='chinese_money_format')
def chinese_money_format(money):    
    if money != '':
        numc = [u"零",u"壹",u"貳",u"參",u"肆",u"伍",u"陸",u"柒",u"捌",u"玖"]
        unic = [u"元",u"拾",u"佰",u"仟",u"萬",u"拾萬",u"佰萬",u"仟萬",u"億",u"拾億",u"佰億",u"仟億"]        
        unit = []
        TW_money = ''
        count_tmp = 1
        lens = len(str(money))    
        str_money = str(money)        
        for k in range(lens,1,-1):
            count_tmp = count_tmp * 10
            unit.append(count_tmp)
        unit.append(1)
        unit.sort(reverse = True)
        unic_ct_one = 0
        unic_ct_two = 1
        for k in unit:        
            ct = str_money[unic_ct_one:unic_ct_two]
            if TW_money == '':
                TW_money = "%s" %(numc[int(ct)])    
                TW_money = "%s %s" %(TW_money,unic[len(str(k))-1])
                unic_ct_one = unic_ct_one+1
                unic_ct_two = unic_ct_two+1
            else:
                TW_money = "%s %s" %(TW_money,numc[int(ct)])
                if len(str(k))-1 != 0:
                    TW_money = "%s %s" %(TW_money,unic[len(str(k))-1])
                unic_ct_one = unic_ct_one+1
                unic_ct_two = unic_ct_two+1             
        return TW_money       
    else:
        return 0