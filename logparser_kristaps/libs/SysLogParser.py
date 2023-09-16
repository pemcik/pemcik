from libs.utils import readFile
import datetime

class SysLogParser(object):
    log_file_path = '/home/parrot/pysec2023/logparser/syslog.example'
    keywords = [
        'fatal',
        'failed',
        'error'
    ]

    keywords_users = [
        'root'
    ]

    def info(self):
        return "This is syslog parser!"

    def getLogFilePath(self):
        return self.log_file_path

    def readFile(self):
        matched_events = []

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

                    matched_events.append(
                        {'date': timestamp, 'source': self.log_file_path, 'event': log_dict['info']}
                    )

        return matched_events
