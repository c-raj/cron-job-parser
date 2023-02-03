
class InvalidCronCmd(Exception):
    def __init__(self, cmd):
        print(f'{cmd} is invalid.')


class CronJobParser:
    def __init__(self):
        self.ranges = {
            0: [0, 59],
            1: [0, 59],
            2: [1, 31],
            3: [1, 12],
            4: [1, 7]
        }

    def parse(self, cmd_list):
        pass
