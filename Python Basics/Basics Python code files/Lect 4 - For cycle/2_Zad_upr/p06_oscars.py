actor_name = input()
points = float(input())
judges = int(input())

for judge in range(judges):
    if points < 1250.5:
        judge_name = input()
        judge_points = float(input())
        points += len(judge_name) * judge_points / 2
    else:
        break
if points >= 1250.5:
    print(f"Congratulations, {actor_name} got a nominee for leading "
              f"role with {points:.1f}!")
else:
    print(f"Sorry, {actor_name} you need {1250.5-points:.1f} more!")
