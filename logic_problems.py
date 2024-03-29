"""
When squirrels get together for a party, they like to have cigars. 
A squirrel party is successful when the number of cigars is between 40 and 60, inclusive. 
Unless it is the weekend, 
in which case there is no upper bound on the number of cigars. 
Return True if the party with the given values is successful, or False otherwise.
"""
def cigar_party(cigars, is_weekend):
  # Sql part a success if cigars between 40-60
  # Unless it is weekend than its 40-Infinity
  if cigars >= 40 and cigars <=60 and not is_weekend:
    return True;
  if cigars >= 40 and  is_weekend:
    return True;
  else:
    return False;



"""
You and your date are trying to get a table at a restaurant. 
The parameter "you" is the stylishness of your clothes, in the range 0..10, 
and "date" is the stylishness of your date's clothes.
The result getting the table is encoded as an int value with 0=no, 1=maybe, 2=yes. 
If either of you is very stylish, 8 or more, then the result is 2 (yes). 
With the exception that if either of you has style of 2 or less, 
then the result is 0 (no). Otherwise the result is 1 (maybe).
"""
def date_fashion(you, date):
  if you >= 8 and date >= 8 or you >= 8 and date > 2 or date >= 10 and you > 2:
    return 2;
  if you <= 2 or date <= 2:
    return 0;
  else:
    return 1;



# Alternative I saw online to this problem
def date_fashion(you, date):
    # If you or your date are a 2 you aren't getting in.
    if you <= 2 or date <= 2:
        return 0
    # If you're super stylish you get in.
    if you >= 8 or date >= 8:
        return 2
    # Otherwise it's just a maybe.
    return 1




"""
The squirrels in Palo Alto spend most of the day playing.
In particular, they play if the temperature is between 60 and 90 (inclusive). Unless it is summer, 
then the upper limit is 100 instead of 90. Given an int temperature and a boolean is_summer, 
return True if the squirrels play and False otherwise.
"""

def squirrel_play(temp, is_summer):
  if is_summer and temp >= 60 and temp <= 100:
    return True;
  elif temp >= 60 and temp <=90:
    return True;
  else:
    return False;



"""
You are driving a little too fast, and a police officer stops you. 
Write code to compute the result, encoded as an int value: 0=no ticket, 1=small ticket, 2=big ticket. 
If speed is 60 or less, the result is 0. If speed is between 61 and 80 inclusive, the result is 1. 
If speed is 81 or more, the result is 2. 
Unless it is your birthday -- on that day, your speed can be 5 higher in all cases.
"""


def caught_speeding(speed, is_birthday):
  if is_birthday == True:
    speed = speed -5;
  if speed >= 81:
    return 2;
  if speed >= 61 and speed <= 80:
    return 1;
  if speed <= 60:
    return 0;



"""
Given 2 ints, a and b, return their sum. 
However, sums in the range 10..19 inclusive, 
are forbidden, so in that case just return 20.
"""
def sorta_sum(a, b):
  sum = a + b;
  if sum >= 10 and sum <= 19:
    return 20;
  else:
    return sum;

"""
Given a day of the week encoded as 0=Sun, 1=Mon, 2=Tue, ...6=Sat, 
and a boolean indicating if we are on vacation, 
return a string of the form "7:00" indicating when the alarm clock should ring. 
Weekdays, the alarm should be "7:00" and on the weekend it should be "10:00". 
Unless we are on vacation -- then on weekdays it should be "10:00" and weekends it should be "off".
"""
def alarm_clock(day, vacation):
  if vacation and day == 0 or vacation and day == 6:
    return "off";
  if vacation and day >= 1 and day <= 5:
    return "10:00"
  elif day >= 1 and day <=5:
    return "7:00"
  else:
    return "10:00"



"""
The number 6 is a truly great number. Given two int values, a and b, return True if either one is 6. 
Or if their sum or difference is 6. Note: the function abs(num) computes the absolute value of a number.
"""
def love6(a, b):
  sum = a + b;
  differenceVar = abs(a-b)
  if a ==  6 or b == 6:
    return True;
  if sum == 6:
    return True;
  if differenceVar == 6:
    return True;
  else:
    return False;


"""
Given a number n, return True if n is in the range 1..10, inclusive. 
Unless outside_mode is True, in which case return True if the number 
is less or equal to 1, or greater or equal to 10.
"""
def in1to10(n, outside_mode):
  if outside_mode:
    if n <= 1 or n >= 10:
      return True;
    else: 
      return False;
  if n <= 10 and n >= 1:
    return True;
  else:
    return False;



"""
Given a non-negative number "num", return True if num is within 2 of a multiple of 10. 
Note: (a % b) is the remainder of dividing a by b, so (7 % 5) is 2. See also: Introduction to Mod
"""
def near_ten(num):
  tenDivided = abs(num % 10);
  if tenDivided <=2 or tenDivided == 8 or tenDivided == 9:
    return True;
  else:
    return False;
