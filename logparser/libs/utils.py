import re

def readFile(path):
    lines = []

    with open(path) as log_file:
        for line in log_file:
            r = re.compile(r'^(?P<month>\S{3})? {1,2}(?P<day>\S+) (?P<time>\S+) (?P<hostname>\S+) (?P<process>.+?(?=\[)|.+?(?=))[^a-zA-Z0-9](?P<pid>\d{1,7}|)[^a-zA-Z0-9]{1,3}(?P<info>.*)$')
            for match in r.finditer(line):
                lines.append(match.groupdict())

    return lines
