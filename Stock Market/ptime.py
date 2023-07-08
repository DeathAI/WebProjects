def prinTime():
    import time
    Hour = int(time.strftime('%H'))
    Min  = int(time.strftime('%M'))
    sec  = int(time.strftime('%S'))
    print(Hour,':',Min,':',sec)