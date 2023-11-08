month, day, year,time = input().split()
day = int(day[:-1])
year = int(year)
hour, minute = map(int, time.split(':'))
#print(month,day, year, hour, minute)

months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
day_months =  [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

i=0
total_day = 0
if year%400 == 0 or (year%4 == 0 and year%100 != 0):
    day_months[1] += 1

while(months[i]!=month):
    total_day+=day_months[i]
    i+=1
    

total_day = total_day + day-1

total_minute =total_day * 24 * 60 + hour*60 + minute
one_y_minute = sum(day_months) * 24 * 60
ans = total_minute / one_y_minute * 100
print(ans)
