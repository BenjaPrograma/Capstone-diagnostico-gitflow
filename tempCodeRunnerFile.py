from dateutil import parser
str = "2021-03-30T03:33:46+00:00"
yourdate = parser.parse(str)
print(yourdate)