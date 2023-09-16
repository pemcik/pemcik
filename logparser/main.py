import re
import csv
import datetime

class DpkgLogParser(object):
    log_file_path = '/var/log/dpkg.log'
    keywords:[
        'install',
    ]
def __init__(self):
    pass
def info(self):
    print("This is my DPKG.log parser witch searches 'install' in log file ")
def getLogFilePath(self):
        return self.log_file_path
def readFile(path):
    lines = []

    with open(path) as log_file:
        for line in log_file:
            r = re.compile(r'^(?P<month>\S{3})? {1,2}(?P<day>\S+) (?P<time>\S+) (?P<hostname>\S+) (?P<process>.+?(?=\[)|.+?(?=))[^a-zA-Z0-9](?P<pid>\d{1,7}|)[^a-zA-Z0-9]{1,3}(?P<info>.*)$')
            for match in r.finditer(line):
                lines.append(match.groupdict())

    return lines
def readFile(self):

        lines = readFile(self.log_file_path)
        for log_dict in lines:
            for keyword in self.keywords_users:
                if keyword in log_dict['info']:
                    # print(
                    #     '''----log----
                    #         date: {}
                    #         message: {}
                    #         '''.format(
                    #     '{} {} {}'.format(log_dict['month'], log_dict['day'], log_dict['time']),
                    #     log_dict['info']
                    # ))

                    # Sep 15 19:39:01
                    date = '{} {} {} {}'.format(datetime.datetime.now().year, log_dict['month'], log_dict['day'], log_dict['time'])
                    # print(date)
                    formatted_date = datetime.datetime.strptime(date, "%Y %b %d %H:%M:%S")
                    timestamp = datetime.datetime.timestamp(formatted_date)
                    # print(timestamp)

        return