import re


class AuthLogParser(object):
    log_file_path = '/var/log/auth.log'


    def __init__(self):
        pass

    def info(self):
        print("This is auth log parser!")

    def readFile(self):
        with open(self.log_file_path) as log_file:
            for line in log_file:
                r = re.compile(r'^(?P<month>\S{3})? {1,2}(?P<day>\S+) (?P<time>\S+) (?P<hostname>\S+) (?P<process>.+?(?=\[)|.+?(?=))[^a-zA-Z0-9](?P<pid>\d{1,7}|)[^a-zA-Z0-9]{1,3}(?P<info>.*)$')
                for match in r.finditer(line):
                    print(match.groupdict())
                # print(timestamp)
                # prin(l)
                # print(parsed.groups.)
                # exit()