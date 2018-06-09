# 10-5 Survey of Programming

with open("survey.txt", "a") as survey:
    while True:
        reason = input("Why do you want to learn Python? ")
        survey.write(reason + "\n")
        repeat = input("Continue? (yes / no) ")
        if repeat.lower() == "no":
            break
