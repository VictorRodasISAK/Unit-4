def IPB_4machine():
    ips = []
    for i in range(0, 256):
        for j in range(0, 256):
            for k in range(0, 256):
                for l in range(0, 256):
                    ip = str(i) + "." + str(j) + "." + str(k) + "." + str(l)
                    print(ip)
                    ips.append(ip)
    return ips

print(IPB_4machine())


