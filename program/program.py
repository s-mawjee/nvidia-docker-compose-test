import datetime
import socket 

if __name__ == '__main__':
    date = datetime.datetime.now()
    f = open('./data/dockerfile_'+socket.gethostname() + '_' + str(date.date())+'.txt', 'a')
    f.write('Docker Container: ' + socket.gethostname() + ' Date: ' + str(date)+'\n')
    print('Docker Container:',socket.gethostname(),'Date:', str(date.date()))