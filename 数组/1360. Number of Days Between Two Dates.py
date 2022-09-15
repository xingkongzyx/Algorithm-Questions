"""
* 计算日期差的时候有个技巧: 用间接的方式来得到两个日期的时间差, 话不多说, 理解下面的公式即可。
# days(1999年1月15日, 2020年12月31日) = days(1999年1月1日, 2020年1月1日) + days(2020年1月1日, 2020年12月31日) - days(1999年1月1日, 1999年1月15日)

* 所以我们要实现两个功能:
* 1. days_between_two_years: 从「A年1月1日」到「B年1月1日」的天数。
* 2. days_from_year_start: 从「1月1日」到「m月n日」的天数, 注意如果是闰年且 m > 2, 要补偿 1 天。

? https://leetcode.cn/problems/number-of-days-between-two-dates/solution/fei-chang-jian-dan-de-si-lu-by-jinniunan007/
"""


class Solution:
    def daysBetweenDates(self, date1: str, date2: str) -> int:
        monthsDays = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

        """
        A year is a leap year if the following conditions are satisfied:

        The year is a multiple of 400.
        The year is a multiple of 4 and not a multiple of 100.
        """
        def leafYearCheck(year):
            if year % 400 == 0 or (year % 100 != 0 and year % 4 == 0):
                return True
            else:
                return False

        def daysBetweenTwoYear(year1, year2):
            # year1 is earlier than year2
            res = 0
            for curYear in range(year1, year2):
                if leafYearCheck(curYear):
                    res += 366
                else:
                    res += 365
            return res

        def daysFromYearStart(year, month, day):
            res = 0
            for i in range(month - 1):
                res += monthsDays[i]

            res += day
            # if cur year is leaf year, then cur month is greater than February, then there are 29 days passed in February
            if leafYearCheck(year) and month > 2:
                res += 1
            return res

        year_1, month_1, days_1 = [int(i) for i in date1.split('-')]
        year_2, month_2, days_2 = [int(i) for i in date2.split('-')]

        if year_1 > year_2:
            return abs(daysBetweenTwoYear(year_2, year_1) + daysFromYearStart(year_1, month_1, days_1) - daysFromYearStart(year_2, month_2, days_2))
        else:
            print(daysFromYearStart(year_2, month_2, days_2))
            print(daysFromYearStart(year_1, month_1, days_1))
            return abs(daysBetweenTwoYear(year_1, year_2) + daysFromYearStart(year_2, month_2, days_2) - daysFromYearStart(year_1, month_1, days_1))


print(Solution().daysBetweenDates("2000-04-12", "2022-05-14"))
