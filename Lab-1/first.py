import xml.etree.ElementTree as ET

root_node = ET.parse('Lab-1/files/data.xml')

source = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789^*"
target = "1xDBWVGTCMQgPAavowRd4JspibI9hrfX0LznSK5qy*8^eZklU2FOY36NcjuE7mtH"

def obfuscate(string: str) -> str:
    length = len(string)
    result_list = ['' for _ in range(length)]
    for i in range(length):
        ch = string[i]
        index = source.index(ch)
        result_list[i] = target[index]
    result = ''.join(result_list)
    return result


def unobfuscate(string: str) -> str:
    length = len(string)
    result_list = ['' for _ in range(length)]
    for i in range(length):
        ch = string[i]
        index = target.index(ch)
        result_list[i] = source[index]
    result = ''.join(result_list)
    return result


def is_empty(string: str) -> bool:
    string = string.replace(' ', '')
    if string == '\n' or '':
        return True
    else:
        return False


for elem in root_node.iter():
    elem.tag = obfuscate(elem.tag)

    if not is_empty(elem.text):
        elem.text = obfuscate(elem.text)

    obf_dict = {}
    if len(elem.attrib) > 0:
        for key, val in elem.attrib.items():
            obf_dict[obfuscate(key)] = obfuscate(val)
    elem.attrib.clear()
    elem.attrib = obf_dict


with open('Lab-1/files/obfucated_data.xml', 'wb') as obf_file:
    root_node.write(obf_file)

root_node = ET.parse('Lab-1/files/obfucated_data.xml')

for elem in root_node.iter():
    elem.tag = unobfuscate(elem.tag)

    if not is_empty(elem.text):
        elem.text = unobfuscate(elem.text)

    unobf_dict = {}
    if len(elem.attrib) > 0:
        for key, val in elem.attrib.items():
            unobf_dict[unobfuscate(key)] = unobfuscate(val)
    elem.attrib.clear()
    elem.attrib = unobf_dict

with open('Lab-1/files/unobfuscated_data.xml', 'wb') as unobf_file:
    root_node.write(unobf_file)

