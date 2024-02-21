import dns.message
import dns.query

root_servers = ['198.41.0.4', '170.247.170.2', '192.33.4.12',
                '199.7.91.13', '192.203.230.10', '192.5.5.241', '192.112.36.4',
                '198.97.190.53', '192.36.148.17', '192.58.128.30',
                '193.0.14.129', '199.7.83.42', '202.12.27.33']

def main():
    hostname = 'stereogum.com'
    query_type = 'A'
    resolve_dns(hostname, query_type)

def resolve_dns(hostname, query_type):
    print("Asking root servers about", hostname)
    query = dns.message.make_query(hostname, query_type)
    for server in root_servers:
        try:
            response = dns.query.udp(query, server)
            print("Received response from", server, " Response:" + response)
            break  
        except:
            print("No response from", server)
            continue

if __name__ == "__main__":
    main()