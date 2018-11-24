from river import River
import mlab

mlab.connect()

river_list = River.objects(continent='Africa')
for r in river_list:
    print(r.name)
    print(r.continent)
    print(r.length)
    print('*'*50)

    

