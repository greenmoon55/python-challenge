import string
'''
str = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."
for x in range(26):
    new_str = ''
    for char in str:
        if char == 'z':
            char = 'a';
        elif char >= 'a' and char < 'z':
            char = chr(ord(char) + 1)
        new_str += char
    print new_str
    str = new_str
'''
str = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."
str = "map"
table = string.maketrans(string.lowercase, string.lowercase[2:] + string.lowercase[:2])
print string.translate(str, table)

