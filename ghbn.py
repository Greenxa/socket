import socket
from colorama import Fore, init

import sys
import time
import os

init(convert=True)


class SocketOption (object):
    def __init__(self,hostName=''):
        self.hostName = hostName
        


    def get_by_host_name(self):
        ipAddress = socket.gethostbyname(self.hostName)
        print("IP address of the host name {} is: {}".format(self.hostName, ipAddress))
        
    def get_by_host_name_ex(self):
        ipAddress = socket.gethostbyname_ex(self.hostName)
        print("IP address of the host name {} is: {}".format(self.hostName, ipAddress))
        time.sleep(2)
    def get_by_host_addr(self,ipAddress=''):
        hostName = socket.gethostbyaddr(ipAddress)
        print("Host Name for the IP address {} is {}".format(ipAddress, hostName))
        time.sleep(2)
    def get_service_by_name(self,servicename = ''):
        if servicename == '':
            serviceList = ["daytime","ftp","gopher","http","https","imap", "kerberos-adm","mysql-im","pop3","qotd","ssh","snmp","smtp"]
            print('the app services and port')
            for service in serviceList:
                try:
                    portnum = socket.getservbyname(service, servicename)
                    print("The service {} uses port number {} ".format(service, portnum))
                except socket.error:
                    print('Cant find {} sorry'.format(service))
                    continue
        else:
                
              
            print('the app services and port')
            
            try:
                portnum = socket.getservbyname(servicename)
                print("The service {} uses port number {} ".format(servicename, portnum))
            except socket.error:
                print('Cant find {} sorry'.format(service))
        time.sleep(2)        

    def get_serv_by_port(self ,services):
        
        portnumber = [13, 21, 70, 80, 443, 143, 749, 110, 17, 22, 25]
        for port in portnumber:
            servicename = socket.getservbyport(port , services)
            print("The service name is {} uses port number {} ".format(servicename,port))     
        time.sleep(2)    
    def connectex(self,HOST,PORT):
        conn = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        error = conn.connect_ex((HOST,PORT))
        if error == 0:
            print('On HOST {} And Port {} Connected '.format(HOST,PORT))
        time.sleep(2)
while True:
    try:
        
        print('Please enter the number to use this options'+'\n'+
        Fore.WHITE+'the number'+Fore.LIGHTGREEN_EX +' 1'+Fore.LIGHTMAGENTA_EX +' is'+ Fore.RED+' get host by name'+'\n'
        +Fore.WHITE+'the number'+Fore.LIGHTGREEN_EX +' 2'+Fore.LIGHTMAGENTA_EX +' is'+ Fore.RED+' get host by name ex'+'\n'
        +Fore.WHITE+'the number'+Fore.LIGHTGREEN_EX +' 3'+Fore.LIGHTMAGENTA_EX +' is'+ Fore.RED+' get by host ip address'+'\n'
        +Fore.WHITE+'the number'+Fore.LIGHTGREEN_EX +' 4'+Fore.LIGHTMAGENTA_EX +' is'+ Fore.RED+' get service by name(this shows port lets try)'+'\n'
        +Fore.WHITE+'the number'+Fore.LIGHTGREEN_EX +' 5'+Fore.LIGHTMAGENTA_EX +' is'+ Fore.RED+' get serv by port'+'\n'
        +Fore.WHITE+'the number'+Fore.LIGHTGREEN_EX+ ' 6'+Fore.LIGHTMAGENTA_EX +' is'+ Fore.RED+' connect ex' +'\n'+Fore.WHITE)

        number = int(input('\n'+'\n'+'YOUR NUMBER ? >'))

        if number <= 6:

            if number == 1:
                hostName = input('Please enter your hostName ')
                if '.' in hostName:
                    p1 = SocketOption(hostName)
                    p1.get_by_host_name()

            elif number == 2:
                hostName = input('Please enter your hostName ')
                if '.' in hostName:
                    p2 = SocketOption(hostName)
                    p2.get_by_host_name_ex()

            elif number == 3:
                ip_address = input('Please enter your ip address ')
                p3 = SocketOption()
                p3.get_by_host_addr(ip_address)

            elif number == 4:
                app_services = input('Do you have name app if you have write it and if not just enter its show all ')
                p4 = SocketOption()
                p4.get_service_by_name(app_services)

            elif number == 5:
                protocol = input('enter your protocol tcp:utp ')
                p5 = SocketOption()
                p5.get_serv_by_port(protocol)

            elif number == 6:
                Host = input('enter your HOST :')
                Port = int(input('enter your Port :'))
                p6 = SocketOption()
                p6.connectex(Host,Port)
        else:
            print('your number must be in renge 1-6')        

    except KeyboardInterrupt:
        print('Goodbye')
        sys.exit()

    except ValueError:
        os.system('cls')
        print('\t \t \t \t you must enter number') 
        time.sleep(3)
        
        
    


