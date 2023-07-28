def int32_to_ip(int32):
    octets = f"{int32:032b}"
    return ".".join([str(int(octets[i*8:i*8+8], 2)) for i in range(0, 4)])