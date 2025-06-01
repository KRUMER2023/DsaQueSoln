def is_consecutive(c1, c2):
    diff = abs(ord(c1) - ord(c2))
    return diff == 1 or diff == 25  # 25 handles 'a'-'z' circular

def remove_all_consecutive_pairs(s):
    while True:
        i = 0
        new_str = ""
        changed = False

        while i < len(s) - 1:
            if is_consecutive(s[i], s[i + 1]):
                print(f"Removing pair: {s[i]}{s[i+1]} at index {i} and {i+1}")
                i += 2  # Skip the pair
                changed = True
            else:
                new_str += s[i]
                i += 1

        if i == len(s) - 1:  # Add last char if not in a pair
            new_str += s[i]

        if not changed:
            return new_str
        s = new_str  # Continue checking the new string
s="llgjfilkhgiil"
print(remove_all_consecutive_pairs(s))