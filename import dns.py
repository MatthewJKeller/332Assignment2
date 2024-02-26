import dns.message
import dns.query


"""Domains tested for debugging: """

def main():
    root_servers = ['198.41.0.4', '170.247.170.2', '192.33.4.12',
    '199.7.91.13', '192.203.230.10','192.5.5.241', '192.112.36.4',
    '198.97.190.53', '192.36.148.17', '192.58.128.30',
    '193.0.14.129', '199.7.83.42', '202.12.27.33']
    dnsQuery('stereogum.com', root_servers)
  
  
def dnsQuery(name, root_servers):
    """ Gets the IP Address for a given URL using the given nameservers"""
    query = dns.message.make_query(name, dns.rdatatype.A)   # makes a DNS query for the given URL, type=A

    for server in root_servers:                             # using the given name servers, try to obtain a response
        print("Asking " + server + " about " + name)
        response = dns.query.tcp(query, server)             # grab the response for the nameserver
        if response.answer != []:
            for answer in response.answer:
                for item in answer.items:
                    if item.address != None:
                        print("Got It! " + item.address)
                        return                                  # return the first IP address found
        elif response.additional != []:
            # get the IP address of the next server to go to

if __name__ == "__main__":
    main()
