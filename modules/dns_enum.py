import dns.resolver
def dns_lookup(domain):
    print("\n[DNS RECORDS]") 
    records=['A','AAAA','MX','NS','TXT']
    for record in records:
        try:
            answer =dns.resolver.resolve(domain,record)
            for rdata in answers:
                print(f"{record}:{rdata}")
        except:
            print(f"{record}: Not found")