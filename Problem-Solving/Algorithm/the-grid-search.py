import re

def gridSearch(G, P):

    for index, value in enumerate(G):
        matched_indices = [m.start() for m in re.finditer("(?=%s)"%P[0], value)]
        for matched_index in matched_indices:
            for i in range(len(P)):
                if ( G[i + index][matched_index: matched_index + len(P[i])] ) != P[i]:
                    break
            else:
                return True
    
    return False
            
    
    
if __name__ == '__main__':

    t = int(input())

    for t_itr in range(t):
        RC = input().split()

        R = int(RC[0])

        C = int(RC[1])

        G = []

        for _ in range(R):
            G_item = input()
            G.append(G_item)

        rc = input().split()

        r = int(rc[0])

        c = int(rc[1])

        P = []

        for _ in range(r):
            P_item = input()
            P.append(P_item)
        found = gridSearch(G, P)
        if found:
            print("YES")
        else:
            print("NO")

