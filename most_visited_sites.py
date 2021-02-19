def most_visited_sites():
	result = {}
	with open("input.txt", "r") as f:
		for line in f:
			line=line.split()
			for l in line[1:]:
				if l in result:
					result[l] += 1
				else:
					result[l] = 1
	sorted_result = sorted(result.items(), key = lambda kv:(kv[1], kv[0]), reverse=True)
	if len(sorted_result) <= 5:
		print(sorted_result)
	else:
		for x,y in sorted_result[:5]:
			print(f'{x} {y}')
most_visited_sites()
