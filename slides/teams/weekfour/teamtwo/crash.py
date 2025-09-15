def crash(string):
    try:
      result = 1 / 0
    except ZeroDivisionError:
      return "Crashed"