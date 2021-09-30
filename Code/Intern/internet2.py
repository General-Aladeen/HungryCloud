import os
def check_internet():
    cmd = os.system('ping google.com -w 4 > clear')
    if cmd == 0:
        print('Internet is connected')
    else:
        print('Internet is not connected')

if __name__ == '__main__':
    check_internet()
