row1 = ["⬜","⬜️","⬜️"]
row2 = ["⬜️","⬜️","⬜️"]
row3 = ["⬜️","⬜️","⬜️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")

a = int(position[0]) -1

b = int(position[1]) - 1

(map[b][a]) = "X"

print(f"{row1}\n{row2}\n{row3}")
