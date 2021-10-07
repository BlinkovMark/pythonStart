def fun():
    list = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    day = int(input("Enter: "))
    if day < 365:
        rsl = day % 7 - 1
        print(list[rsl])
fun()
