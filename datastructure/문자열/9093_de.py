import sys
T = int(sys.stdin.readline())

for i in range(T):
    sentence = sys.stdin.readline().split()
    # print(sentence)
    for j in range(len(sentence)):
        for k in range(len(sentence[j])-1,-1,-1):
            print(sentence[j][k], end="")
        print(" " ,end="")
    print()

# lst = ["I","am","happy","today"]
# stack=[]
# # print(lst)
# for i in range(len(lst)):
#     for j in range(len(lst[i])-1,-1,-1):
#         # print(lst[i][j], end="")
#         stack=" ".join(lst[i][j])
        