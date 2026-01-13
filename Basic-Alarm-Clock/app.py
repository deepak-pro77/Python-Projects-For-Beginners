import datetime
import time
import winsound


def set_alarm(alarm_time):
    print(f"⏳ Alarm set for {alarm_time}")

    while True:
        now = datetime.datetime.now().strftime("%H:%M:%S")

        if now == alarm_time:
            print("⏰ Wake up!!!")
            winsound.Beep(1000, 2000)  # frequency, duration ms
            break

        time.sleep(1)  # check every second


def main():
    print("-------- Alarm Clock --------")

    alarm_time = input("Enter time (HH:MM:SS): ")

    set_alarm(alarm_time)


if __name__ == "__main__":
    main()
