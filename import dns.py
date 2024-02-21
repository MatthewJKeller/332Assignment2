import dns.message
import dns.query


"""Domains tested for debugging: """

def main():
    root_servers = ['198.41.0.4', '170.247.170.2', '192.33.4.12',
    '199.7.91.13', '192.203.230.10','192.5.5.241', '192.112.36.4',
    '198.97.190.53', '192.36.148.17', '192.58.128.30',
    '193.0.14.129', '199.7.83.42', '202.12.27.33']
    dnsQuery('stereogum.com', 'A', root_servers)
  
  
def dnsQuery(name, type, root_servers):
    query = dns.message.make_query(name, type)
    for server in root_servers:
        try:
            response = dns.query.udp(query, server)
            print("got it! " + response)
            break
        except:
            print("Trying " + server + " for " + name + " failed") 
            pass
        


if __name__ == "__main__":
    main()
