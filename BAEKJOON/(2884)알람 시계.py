H, M = map(int, input().split())

if M < 45:
    H = H - 1
    M = 60 - (45 - M)
    if H < 0:
        H = (24 + H)

elif M > 45:
    M = M - 45

else:
    M = 0


print(H, M)
