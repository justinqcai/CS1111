import urllib.request
import re

def count_IP_addresses(url):
    result = {}
    count = 0

    regex = re.compile(r'\d+\.\d+\.\d+\.\d+')

    stream = urllib.request.urlopen(url)
    for line in stream:
        decoded = line.decode("UTF-8").strip()
        temp_result = regex.findall(decoded)
        for i in temp_result:
            if i in result.keys():
                result[i] += 1
            else:
                result[i] = 1
    return result

print(count_IP_addresses("http://cs1110.cs.virginia.edu/code/access.log"))