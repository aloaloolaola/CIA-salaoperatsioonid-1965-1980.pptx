_, plan_count = [int(a) for a in input().split()]
players = [int(string) for string in input().split()]
plans = [[int(i) for i in input().split()] for _ in range(plan_count)]
#for _ in range(plan_count):
#    plans.append(tuple(int(string) for string in input().split()))

for plan in plans:
    relevant_players = players[plan[0]:plan[1]+1]
    print(sorted(relevant_players)[10])