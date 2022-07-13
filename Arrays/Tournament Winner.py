def tournamentWinner(competitions, results):
    # Write your code here
    winers = {}

    for idx,i in enumerate(competitions):
        points  =  results[idx]

        if points ==1:
            if i[0] in winers:
                winers[i[0]] +=1
            else:
                winers[i[0]] = 0
        else:
            if points == 0:
                if i[1] in winers:
                    winers[i[1]] +=1
                else:
                    winers[i[1]] = 0
                    
        max_val  =  list(winers.values())
        max_le = list(winers.keys())
    

    return "".join(max_le[max_val.index(max(max_val))])
#    1       0
# homeTeam awayTeam
competitions = [
  ["HTML", "C#"],
  ["C#", "Python"],
  ["Python", "HTML"]
]

results = [0, 0, 1]

print(tournamentWinner(competitions,results))