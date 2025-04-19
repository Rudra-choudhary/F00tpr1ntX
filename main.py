import sys
from modules.whois_lookup import whois_lookup
from modules.dns_enum import dns_lookup
from modules.subdomain_enum import subdomain_enum
from modules.tech_detect import detect_tech
print(99)
def banner():
    print('''
  _____ ___   ___  _   ____       _       _    __  __
 |  ___/ _ \ / _ \| |_|  _ \ _ __/ |_ __ | |_  \ \/ /
 | |_ | | | | | | | __| |_) | '__| | '_ \| __|  \  / 
 |  _|| |_| | |_| | |_|  __/| |  | | | | | |_   /  \ 
 |_|   \___/ \___/ \__|_|   |_|  |_|_| |_|\__| /_/\_\                                                     

                CLI Footprinting Recon Tool - by Rudra
    ''')

def main():
    print("Script started")

    if len(sys.argv) != 2:
        print("Usage: python main.py <domain>")
        return

    domain = sys.argv[1]
    url = f"https://{domain}"

    banner()
    whois_lookup(domain)
    dns_lookup(domain)
    subdomain_enum(domain, "wordlists/subdomains.txt")
    detect_tech(url)

if __name__ == "__main__":
    main()
