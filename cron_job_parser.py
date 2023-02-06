
class InvalidCronCmd(Exception):
    def __init__(self, msg):
        print(msg)


class CronJobParser:
    def __init__(self):
        self.ranges = {
            0: [0, 59],
            1: [0, 59],
            2: [1, 31],
            3: [1, 12],
            4: [1, 7]
        }
        self.period = {
            0: 'minute',
            1: 'hour',
            2: 'day of month',
            3: 'month',
            4: 'day of week',
            5: 'command'
        }
    
    def validate_range(self, val, idx):
        valid_range = self.ranges[idx]
        min_range = valid_range[0]
        max_range = valid_range[1]
        for i in val:
            if i < min_range or i > max_range:
                raise InvalidCronCmd("Range should be should min, max")
        return val

    def get_range(self, idx, expr):
        step = 1
        value = []
        if len(expr) == 1 and expr != '*':
            if not expr.isnumeric():  # Example 'a'
                raise InvalidCronCmd(f"Invalid expr: {expr}")
            value = [int(expr)]
        if '/' in expr:
            r = expr.split('/')
            if not r[1].isnumeric():  # Example: */a 
                raise InvalidCronCmd(f"Denominator of / should be an int: {expr}")
            if ',' in r[0]:  # Example: 1,2/1
                raise InvalidCronCmd(f"{expr} is not standard")
            step = int(r[1])
            expr = r[0]
        if ',' in expr:
            value = [int(i) for i in expr.split(',')]
        if '-' in expr:
            r = expr.split('-')
            if not r[0].isdigit() or not r[1].isdigit():
                raise InvalidCronCmd(f"Value is not numeric: {expr}")
            min_range = int(r[0])
            max_range = int(r[1])
            if max_range < min_range:
                raise InvalidCronCmd(f"Value is not numeric: {expr}")
            
            value = [i for i in range(min_range, max_range+1)]
        if '*' in expr:
            valid_range = self.ranges[idx]
            value = [i for i in range(valid_range[0], valid_range[1]+1)]
        
        if step > 1:
            _min = value[0]
            _max = value[-1]
            new_range = [i for i in range(_min, _max+1, step)]
            return self.validate_range(new_range, idx)
        else:
            return self.validate_range(value, idx)

    def parse(self, cmd):
        result = {}
        cmd_list = cmd.split(" ")
        if len(cmd_list) != 6:
            raise InvalidCronCmd(f"Invalid command args: {cmd}") 
        try:
            for idx, expr in enumerate(cmd_list):
                if idx != 5:
                    period_range = self.get_range(idx, expr)
                    vals = " ".join(str(i) for i in period_range)
                    result[self.period[idx]] = vals
                else:
                    result[self.period[idx]] = expr
        except Exception:
            raise Exception
        return result
    
    def pretty_print(self, cmd):
        result = self.parse(cmd)
        try:
            for k, v in result.items():
                print(f"{k}: {v}")
        except InvalidCronCmd as e:
            print(f"Invalid input: {e}")