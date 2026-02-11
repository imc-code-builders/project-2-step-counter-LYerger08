log.set_labels('strength')
while True:
    # Use log.add() to record the accelerometer strength
    # You can get the strength with accelerometer.get_strength()
    # You must pass a dictionary to log.add
    # with the key as the name of the data ('strength') and the value as the actual strength
    strength = accelerometer.get_strength()
    log.add({'strength':strength})
    

    sleep(100)