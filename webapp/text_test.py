from re import T
import os



text = "Всем привет на етом сайте вы научитесь собирать кубик рубика"
text2= 'Я умею собирать кубик рубик'
inf_rubik_assamble = 'Я умею собирать кубик рубик'
inf_rubik_assamble2 = 'Прости я не умею собирать кубик рубик'


os.chdir('G:/egor/sait/kubingor.com_copytwo/webapp/text')

text_azbuc = open('text_dvigenii.txt','r',encoding='utf-8')
text_azbucc = text_azbuc.read()
text_azbuc.close()
#print(text_azbucc)
#print(text_azbucс.read())
#print(f)
text_azbuc_r = open('G:/egor/sait/kubingor.com_copytwo/webapp/text/azbuka_r.txt','r',encoding='utf-8')
text_azbuc_rr = text_azbuc_r.read()
text_azbuc_r.close()

text_sostav = open('G:/egor/sait/kubingor.com_copytwo/webapp/text/sostav_cube_detalis.txt','r',encoding='utf-8')
text_sostavv = text_sostav.read()
text_sostav.close()
#print(text_sostavv)

