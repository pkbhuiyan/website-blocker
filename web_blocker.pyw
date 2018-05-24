import time as t
from datetime import datetime as dt

redirect = '127.0.0.1'
host_temp = r'C:\Users\Dell\Desktop\Python\web_blocker\hosts'
hosts_path = r"C:\Windows\System32\drivers\etc\hosts"
website_list = ['www.facebook.com', 'facebook.com', 'youtube.com', 'www.youtube.com']
sd = dt(dt.now().year, dt.now().month, dt.now().day, 1)
print(sd)
while True:
    if dt(dt.now().year, dt.now().month, dt.now().day, 2) < dt.now() < dt(dt.now().year, dt.now().month, dt.now().day, 12):
        print('working hours...')
        with open(hosts_path, 'r+') as file:
            content = file.read()
            for website in website_list:
                if website in content:
                    pass
                else:
                    file.write(redirect+' '+website+'\n')

    else:
        with open(hosts_path, 'r+') as file:
            content = file.readlines()
            file.seek(0)  # beginning of the file
            for line in content:
                # search the website in the line( read-lines list) with loop for check all
                if not any(website in line for website in website_list):
                    file.write(line)
            file.truncate()

        print('fun hours..')

    t.sleep(5)
