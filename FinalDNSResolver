import dns.message
import dns.query


"""Domains tested for debugging:gamefaqs.gamespot.com, stereogum.com, static.stereogum.com, google.com, facebook.com, youtube.com, wikipedia.org, amazon.com, reddit.com, instagram.com, yahoo.com, microsoft.com, bbc.com, wired.com, finance.yahoo.com, usa.gov, gov.uk, europa.eu, twitch.tv"""

def main():
    root_servers = ['198.41.0.4', '170.247.170.2', '192.33.4.12', '199.7.91.13', '192.203.230.10','192.5.5.241', '192.112.36.4', '198.97.190.53', '192.36.148.17', '192.58.128.30', '193.0.14.129', '199.7.83.42', '202.12.27.33']
    dnsQuery('stereogum.com', root_servers, 0)
  
def dnsQuery(name: str, root_servers: list, jumps: int):
    """ Gets the IP Address for a given URL using the given nameservers"""
    for i in range(len(root_servers)):                             # using the given name servers, try to obtain a response
        query = dns.message.make_query(name, dns.rdatatype.A)      # makes a DNS query for the given URL, type=A
        if jumps == 0:
            rootString = 'root server '
        else:
            rootString = ''
        print('Asking ' + rootString + root_servers[i] + ' about ' + name)
        response = dns.query.tcp(query, root_servers[i])           # grab the response for the nameserver
        if response.answer != []:                                  # get the IP address
            if str(response.answer[0]).find(' IN A ') != -1:
                print('Got It! ' + str(response.answer[0][0]))
                return True  
            elif str(response.answer[0]).find(' IN CNAME ') != -1: # get the CNAME if there was not an IP address
                name = str(response.answer[0][0])[:-1]
                return name
        elif response.additional != []:                            # get the IP address of the next server to go to and do the query on it recursively
            lst = []
            if str(response.additional[0][0]).find(':') != -1:     # do not use the IPv6 if given at [0][0], grab the IPv4
                lst.append(str(response.additional[1][0]))
            else:
                lst.append(str(response.additional[0][0]))
            result = dnsQuery(name, lst, jumps+1)
            if result == True:                                     # if you got the actual IP address from one of the recursive calls, return true                
                return True
            elif result != None:                                   # if you got the CNAME from one of the recursive calls, set name to the CNAME
                name = result
                if jumps != 0:                                     # return name if you are still in a recursive call
                    return name
        elif response.authority != []:                            # get the CNAME, if in recursive call, return it, if not, set name to CNAME
            name = str(response.authority[0][0])[:-1]
            if jumps != 0:
                return name
            

if __name__ == "__main__":
    main()
