def days (day: int ) -> str:

    days_dict = {
        1: "Sunday",
        2: "Monday",
        3: "Tuesday",
        4: "Wednesday",
        5: "Thursday",
        6: "Friday",
        7: "Saturday"
    }
    if not isinstance(day,int):
        raise ValueError ("Day must be an integer")
    if day in days_dict:
        return days_dict[day]
    if day > 7 or day <1 and not day == -999:
        raise ValueError ("Out of range")
    elif day == -999:
        return ("Goodbye")


def play_days ():
    while True:
        try:
            day:int = int(input("Please enter a number for the day [1-7] or -999 to Quit"))
        except ValueError:
            print (ValueError ("Day must be an integer"))
            continue
        if day == -999:
            return ("Goodbye")
            break
        try:
            feedback: str = days(day)
            print(feedback)
        except ValueError as e:
            print(e)
            continue



if __name__ == "__main__":
    play_days()
