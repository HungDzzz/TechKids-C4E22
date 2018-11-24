from gmail import GMail,Message
gmail = GMail('hungdz.tk@gmail.com','anhhung1996')
msg = Message('Hello',to='hungdz.tk@gmail.com',text='Say Hello',html="https://pypi.org/project/gmail/")#,attachments=['node_js_JavaScript_hexagon_abstract-1293887.jpg'])
gmail.send(msg)
# html_template = '''
# <p>chao hau</p>
# <h1>an {{food}} khong</h1>
# <i>hihi</i>
# '''
# symptom_list = ['com','chao','my']
# for i in range(len(symptom_list)):
#     html_content = html_template.replace("{{food}}",symptom_list[i])
#     msg = Message("Hello",to='hungdz.tk@gmail.com',html=html_content)
#     gmail.send(msg)
# from random import choice # random
# l = []
# x=choice(l)
# print(x)