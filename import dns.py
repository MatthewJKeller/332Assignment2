import dns.message
import dns.query


"""Domains tested for debugging: """

def main():
    root_servers = ['198.41.0.4']
    dnsQuery('status.stereogum.com', root_servers)
  
  
def dnsQuery(name: str, root_servers: list)->bool:
    """ Gets the IP Address for a given URL using the given nameservers"""
    query = dns.message.make_query(name, dns.rdatatype.A)          # makes a DNS query for the given URL, type=A

    for i in range(len(root_servers)):                             # using the given name servers, try to obtain a response
        print("Asking " + root_servers[i] + " about " + name)
        response = dns.query.tcp(query, root_servers[i])           # grab the response for the nameserver
        if response.answer != []:
            for answer in response.answer:
                for item in answer.items:
                    if item.address != None:
                        print("Got It! " + item.address)
                        return True                                # return the first IP address found
        elif response.additional != []:                            # get the IP address of the next server to go to
            lst = []
            lst.append(str(response.additional[0][0]))
            if dnsQuery(name, lst):                                # perform the query for the next server
                return True
        else:
            query = dns.message.make_query(name, dns.rdatatype.CNAME) 
            response = dns.query.tcp(query, root_servers[i])
            print(response.authority[0][0])

if __name__ == "__main__":
    main()
