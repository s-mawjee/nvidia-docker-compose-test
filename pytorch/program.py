import datetime
import socket 
import torch

if __name__ == '__main__':
    date = datetime.datetime.now()
    f = open('./data/dockerfile_'+socket.gethostname() + '_' + str(date.date())+'.txt', 'a')
    f.write('Docker Container: ' + socket.gethostname() + ' Date: ' + str(date)+'\n')
    if torch.cuda.is_available():
        f.write('List of GPUs:'+'\n')
        print('List of GPUs:'+'\n')
        number_of_gpu = torch.cuda.device_count()
        for i in range(number_of_gpu):
            f.write('('+str(i)+') '+torch.cuda.get_device_name(i)+'\n')
            print('('+str(i)+') '+torch.cuda.get_device_name(i)+'\n')
    else:
        f.write('GPU is Not available'+'\n')
        print('GPU is Not available'+'\n')
    print('Docker Container:',socket.gethostname(),'Date:', str(date.date()))