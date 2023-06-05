# IP & Subnet
def IntToBin(integer):
    binary = '.'.join([bin(int(x) + 256)[3:] for x in integer.split('.')])
    return binary


IP = input("Enter an IP address: ")
subnet = input("Enter the subnet mask: ")
bin_IP = IntToBin(IP)
bin_subnet = IntToBin(subnet)

print('\nIP:', IP, "->", bin_IP)
print('Subnet:', subnet, "->", bin_subnet)


# Wild Card
def complement(number):
    if number == '0':
        number = '1'
    elif number == '.':
        pass
    else:
        number = '0'
    return number


def find_wildcard(binary_subnet):
    binary_list = list(binary_subnet)
    wildcard = ''.join(complement(binary_list[y]) for y in range(len(binary_list)))
    return wildcard


def convert_decimal(wildcard_Binary):
    binary = {}
    for x in range(4):
        binary[x] = int(wildcard_Binary.split(".")[x], 2)
    dec = ".".join(str(binary[x]) for x in range(4))
    return dec


bin_wildcard = find_wildcard(IntToBin(subnet))
wildcard = convert_decimal(bin_wildcard)
print('Wildcard:', wildcard, '->', bin_wildcard)


# Network ID
# And the IP and subnet mask to get the network ID.
def andOperation(IP1, IP2):
    id_list = {}
    for y in range(4):
        # Split them at the "." and 'and' the segments together
        id_list[y] = int(IP1.split(".")[y]) & int(IP2.split(".")[y])
    # Join the segments to form the network ID
    net_id: str = ".".join(str(id_list[z]) for z in range(4))
    return net_id


networkID = andOperation(IP, subnet)
# Convert the network ID to binary
bin_network = IntToBin(networkID)
print('Network ID:', networkID, "->", bin_network)


# Brodcast ID
def orOperation(IP1, IP2):
    bcast_list = {}
    for y in range(4):
        bcast_list[y] = bcast_list[y] = int(IP1.split(".")[y]) | int(IP2.split(".")[y])
    # Join the segments to form the network ID
    bcast: str = ".".join(str(bcast_list[z]) for z in range(4))
    return bcast


bcast_id = orOperation(networkID, wildcard)
bin_bcast = IntToBin(bcast_id)
print('Broadcast IP:', bcast_id, "->", bin_bcast)

def maxAddr(bcastID):
    maxIPs = bcastID.split(".")
    if int(bcastID.split(".")[3]) - 1 == 0:
        if int(bcastID.split(".")[2]) - 1 == 0:
            if int(bcastID.split(".")[1]) - 1 == 0:
                maxIPs[0] = int(bcastID.split(".")[0]) - 1
            else:
                maxIPs[1] = int(bcastID.split(".")[1]) - 1
        else:
            maxIPs[2] = int(bcastID.split(".")[2]) - 1
    else:
        maxIPs[3] = int(bcastID.split(".")[3]) - 1
    return ".".join(str(maxIPs[x]) for x in range(4))


max_addr = maxAddr(bcast_id)
bin_max_addr = IntToBin(max_addr)
print('Max. IP:', max_addr, "->", bin_max_addr)

def minAddr(network_id):
    min_addrs = network_id.split(".")
    if int(network_id.split(".")[3]) + 1 == 256:
        if int(network_id.split(".")[2]) + 1 == 256:
            if int(network_id.split(".")[1]) + 1 == 256:
                min_addrs[0] = int(network_id.split(".")[0]) + 1
                min_addrs[1] = 0
                min_addrs[2] = 0
                min_addrs[3] = 0
            else:
                min_addrs[1] = int(network_id.split(".")[1]) + 1
                min_addrs[2] = 0
                min_addrs[3] = 0
        else:
            min_addrs[2] = int(network_id.split(".")[2]) + 1
            min_addrs[3] = 0
    else:
        min_addrs[3] = int(network_id.split(".")[3]) + 1
    return ".".join(str(min_addrs[x]) for x in range(4))


min_addr = minAddr(networkID)
bin_min_addr = IntToBin(min_addr)
print('Min. IP:', min_addr, "->", bin_min_addr)
