from siteswap_parser import Siteswap

def generate_siteswap_sequence(siteswap_string):
    ss = Siteswap(siteswap_string)
    info = ss.get_info()
    if not info["isValid"]:
        print(f"Invalid siteswap: {info['error']}")
        return []

    # Example: Generate a sequence of siteswaps
    base_sequence = info["sequence"]
    sequence_list = []

    for i in range(len(base_sequence)):
        rotated_sequence = base_sequence[i:] + base_sequence[:i]
        sequence_list.append(rotated_sequence)

    return sequence_list
