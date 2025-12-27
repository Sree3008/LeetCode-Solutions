class Solution:
    def convertDateToBinary(self, date: str) -> str:
        year, month, day = date.split("-")
        years = bin(int(year))[2:]
        months = bin(int(month))[2:]
        days= bin(int(day))[2:]
        return years + "-" + months + "-" + days

