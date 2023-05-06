from dns_a import *

def main():
    domain = input('name domain: ')
    d_a = (dns_resolve(domain, 'a', '77.88.8.8'))
    for i in d_a:
        print('ip address {}, country {}, city {}'.format(i[0], i[1], i[2]))
    d_mx = (dns_resolve_mx(domain, 'mx', '77.88.8.8'))
    for i in d_mx:
        print('record mx {}, ip address {}, country {}, city {}'.format(i[0], i[1][0][0], i[1][0][1], i[1][0][2]))

if __name__ == '__main__':
   main()
