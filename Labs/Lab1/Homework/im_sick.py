import datetime
from random import choice
from gmail import GMail, Message
now = datetime.datetime.now()
gmail = GMail('hungdz.tk@gmail.com','anhhung1996')
html_template = '''
<i>Chào Sếp !</i>
<p>Hôm nay em bị {{symptom_list}} nên không thể đi làm được.</p>
<p>Sếp cho em nghỉ nhé.</p>
<i><b>Yêu Sếp nhiều hihi !</b></i>
'''
symptom_list = ['ốm', 'đau bụng', 'đau đầu']
while True:
    if now.hour > 7 :
        reason = choice(symptom_list)
        html_content = html_template.replace("{{symptom_list}}", reason)
        msg = Message("Xin Nghỉ Làm Việc Hôm Nay", to="hungdz.tk@gmail.com", html=html_content)
        gmail.send(msg)
        break