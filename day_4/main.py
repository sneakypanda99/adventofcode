

score_part1 = 0
score_part2 = 0

with open("input", "r") as f:
    for x in f:
        [p1, p2] = x.split(",")
        p1l = p1.split("-")
        p2l = p2.split("-")
        set1 = set([x for x in range(int(p1l[0]), int(p1l[1])+1)])
        set2 = set([x for x in range(int(p2l[0]), int(p2l[1])+1)])
        if len(set1.intersection(set2)) > 0:
            score_part2 += 1
        if set1.intersection(set2) == set1 or set1.intersection(set2) == set2:
            score_part1 += 1


print("Part1:", score_part1, "Part2:", score_part2)
