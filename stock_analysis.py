stock_prices = [34.68, 36.09, 34.94, 33.97, 34.68, 35.82, 43.41, 44.29, 44.65, 53.56, 49.85, 48.71, 48.71, 49.94, 48.53, 47.03, 46.59, 48.62, 44.21, 47.21]

def maximum(x,y):
  maxx = 0
  for i in range(x, y + 1, +1):
    if stock_prices[i] > maxx:
      maxx = stock_prices[i]
  return maxx

def minimum(x,y):
  minn = stock_prices[x]
  for i in range(x + 1, y + 1, +1):
    if stock_prices[i] <= minn:
      minn = stock_prices[i]
  return minn


print("==============")
print("STOCK ANALYSIS")
print("==============")
print("1) Price on a specific day")
print("2) Max price between two days")
print("3) Min price between two days")
op = int(input("Enter an operation: "))

if op == 1:
  day = int(input("Enter a day between 1 - 20: "))
  answer = stock_prices[day - 1]
  print(f"The price on day {day} is ${answer:.2f}")

else:
  days = input("Enter two days: ").split()
  day1,day2 = days

  if op == 2:
    answer = maximum(int(day1),int(day2))
    print(f"The maximum value between day {day1} and day {day2} is ${answer:.2f}")

  else:
    answer = minimum(int(day1),int(day2))
    print(f"The minimum value between day {day1} and day {day2} is ${answer:.2f}")