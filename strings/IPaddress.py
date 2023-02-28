
def validIPAddress(IP: str) -> str:

    if len(IP) < 16:
        val = check_IPv4(IP)
        return val
    elif len(IP) > 16 and len(IP) <= 39:
        val = check_IPv6(IP)
        return val
    else:
        return "Neither"

def check_IPv4(IP):
    ipv4 = IP.split(".")
    for octet in ipv4:
        if int(octet) >= 0 and int(octet) <= 255 and octet[0] != '0':
            continue
        else:
            return False
    return "IPv4"

def check_IPv6(IP):
    ipv6 = IP.split(":")
    for octet in ipv6:
        if len(octet) >= 1 and len(octet) <= 4 and octet.isalnum():
            continue
        else:
            return False

    return "IPv6"

def main():
    val = validIPAddress("172.16.254.1")
    print(val)

main()