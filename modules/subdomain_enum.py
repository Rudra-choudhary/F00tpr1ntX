import dns.resolver

def subdomain_enum(domain, wordlist_path):
    print("\n[SUBDOMAIN ENUMERATION]")
    resolver = dns.resolver.Resolver()
    resolver.nameservers = ['8.8.8.8', '1.1.1.1']
    found = False

    with open(wordlist_path, 'r') as file:
        for line in file:
            sub = line.strip()
            full_domain = f"{sub}.{domain}"
            try:
                result = resolver.resolve(full_domain, 'A')
                for ip in result:
                    print(f"[+] Found: {full_domain} -> {ip}")
                    found = True
            except dns.resolver.NXDOMAIN:
                print(f"[-] {full_domain} does not exist")
            except dns.resolver.NoAnswer:
                print(f"[!] No A record for {full_domain}")
            except dns.resolver.Timeout:
                print(f"[!] Timeout: {full_domain}")
            except Exception as e:
                print(f"[!] Error with {full_domain}: {e}")

    if not found:
        print("[-] No subdomains found.")
