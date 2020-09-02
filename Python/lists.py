def executeCommand(command, l):
    switch = {
        'insert' : lambda: l.insert(int(command[1]), int(command[2])),
        'print' : lambda: print(l),
        'remove' : lambda: l.remove(int(command[1])),
        'append' : lambda: l.append(int(command[1])),
        'sort' : lambda: l.sort(),
        'pop' : lambda: l.pop(),
        'reverse' : lambda: l.reverse()
    }
    switch[command[0]]()

if __name__ == '__main__':
    N = int(input())
    l = []
    for _ in range(N):
        command = input().split()
        executeCommand(command, l)
        
