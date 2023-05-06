import dns.resolver
from geo_ip import get_geo_ip

list_result = []

def dns_resolve(domain, record_type, dns_server):
    for i in record_type:
        resolver = dns.resolver.Resolver(configure=False)
        resolver.nameservers = [dns_server]
        answer = resolver.resolve(domain, i)
        list_name_ip = [(data, get_geo_ip(data)[0], get_geo_ip(data)[1]) for data in answer]
    return list_name_ip
def dns_resolve_mx(domain, record_type, dns_server):
    list_mx = []
    list_mx2 = []
    resolver = dns.resolver.Resolver(configure=False)
    resolver.nameservers = [dns_server]
    answer = resolver.resolve(domain, record_type)
    for data in answer:
        list_mx.append(str(data).split()[1])
        d = (dns_resolve(str(data).split()[1], 'a', '77.88.8.8'))
        list_mx.append(d)
        list_mx2.append(list_mx)
        list_mx = []
    return list_mx2
