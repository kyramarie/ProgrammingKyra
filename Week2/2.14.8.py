ask_user = float(input("What is the time now?"))

wait_time = float(input("How long do you want to wait?"))

r = (ask_user + wait_time) % 24

print("The end time will be ", r)