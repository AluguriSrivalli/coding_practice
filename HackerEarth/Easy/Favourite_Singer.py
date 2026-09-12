N = int(input())
Singers = input().split()

fav = {}
for singer in Singers:
    fav[singer] = fav.get(singer, 0) + 1

max_count = max(fav.values())
answer = sum(1 for count in fav.values() if count == max_count)

print(answer)
