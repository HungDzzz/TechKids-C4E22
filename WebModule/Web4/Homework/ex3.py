from river import River
import mlab

mlab.connect()

river_list = River.objects(continent = 'S. America', length__lt = 1000)
for r in river_list:
    print(r.name)
    print(r.continent)
    print(r.length)
    print('*'*50)