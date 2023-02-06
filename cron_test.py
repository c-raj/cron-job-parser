import pytest
from cron_job_parser import CronJobParser, InvalidCronCmd


parser = CronJobParser()

class TestCronJobParser:
    @pytest.mark.parametrize("cron_expression,expected_result", 
                            [("0 0,12 1 */2 * /usr/bin/find", {'minute': '0', 'hour': '0 12', 'day of month': '1', 'month': '1 3 5 7 9 11', 'day of week': '1 2 3 4 5 6 7', 'command': '/usr/bin/find'}), 
                            ("*/15 0 1,15 * 1-5 /usr/bin/find", {'minute': '0 15 30 45', 'hour': '0', 'day of month': '1 15', 'month': '1 2 3 4 5 6 7 8 9 10 11 12', 'day of week': '1 2 3 4 5', 'command': '/usr/bin/find'}),
                            ("0 4 8-14 * * /usr/bin/find", {'minute': '0', 'hour': '4', 'day of month': '8 9 10 11 12 13 14', 'month': '1 2 3 4 5 6 7 8 9 10 11 12', 'day of week': '1 2 3 4 5 6 7', 'command': '/usr/bin/find'}),
                            ("5 0 * 8 * /test", {'minute': '5', 'hour': '0', 'day of month': '1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31', 'month': '8', 'day of week': '1 2 3 4 5 6 7', 'command': '/test'})])
    def test_successful_cron_job_parser(self, cron_expression, expected_result):
        actual_result = parser.parse(cron_expression)
        assert actual_result == expected_result
    
    @pytest.mark.parametrize("invalid_cron_expression", 
                            ["5 0 * 8 *", 
                            "0 0,12 1 */2 a /usr/bin/find",
                            "5 0 */ 8 * /usr/bin/find",
                            "5 72 * * * /usr/bin/find"])
    def test_failure_cron_job_parser(self, invalid_cron_expression):
        try:
            _ = parser.parse(invalid_cron_expression)
            assert False
        except InvalidCronCmd:
            assert True
