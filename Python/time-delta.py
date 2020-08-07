import datetime as dt

def time_delta(t1, t2):
    format_str = "%a %d %b %Y %H:%M:%S %z"
    t1 = dt.datetime.strptime(t1, format_str)
    t2 = dt.datetime.strptime(t2, format_str)
    return int(abs(t1 - t2).total_seconds())

if __name__ == '__main__':

    t = int(input())

    for t_itr in range(t):
        t1 = input()

        t2 = input()
        delta = time_delta(t1, t2)
        print(delta)