#cigar_party
def cigar_party(cigars, is_weekend):
  if (cigars >= 40) and (cigars <= 60):
    return True
  elif is_weekend and (cigars >= 40):
    return True
  else:
    return False

#caught_speeding
def caught_speeding(speed, is_birthday):
  if not is_birthday:
    if speed <= 60:
      return 0
    elif speed >= 61 and speed <= 80:
      return 1
    else:
      return 2
  else:
    if speed <= 65:
      return 0
    elif speed >= 66 and speed <= 85:
      return 1
    else:
      return 2

#love6
def love6(a, b):
  if a == 6 or b == 6:
    return True
  elif (a + b) == 6:
    return True
  elif abs(a - b) == 6:
    return True
  else:
    return False

#date_fashion
def date_fashion(you, date):
  if you <= 2 or date <= 2:
    return 0
  if you >= 8 or date >= 8:
    return 2
  else:
    return 1

#sorta_sum
def sorta_sum(a, b):
  result = a + b
  if result >= 10 and result <= 19:
    return 20
  else:
    return result

#in1to10
def in1to10(n, outside_mode):
  if outside_mode:
    if n <= 1 or n >= 10:
      return True
  else:
    if n >= 1 and n <= 10:
      return True
  return False

#squirrel_play
def squirrel_play(temp, is_summer):
  if is_summer:
    if temp >= 60 and temp <= 100:
      return True
  else:
    if temp >= 60 and temp <= 90:
      return True
  return False

#alarm_clock
def alarm_clock(day, vacation):
  if vacation:
    if day >= 1 and day <= 5:
      return "10:00"
    else:
      return "off"
  else:
    if day >= 1 and day <= 5:
      return "7:00"
    else:
      return "10:00"

#near_ten
def near_ten(num):
  return ((num % 10) <= 2) or ((num % 10) >= 8)
