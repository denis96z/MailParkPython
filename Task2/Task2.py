import sys
import random

def play_game(t1, t2):
    t1_score = random.randint(0, 10)
    t2_score = random.randint(0, 10)
    return (t1, t2, t1_score, t2_score)

def compete(teams):
    results = []
    for t1 in teams:
        for t2 in teams:
            if t1 == t2: continue
            results.append(play_game(t1, t2))
    return results

def count_score(results, team):
    t_score = 0
    for r in results:
        if result_has_team(r, team):
            if team_wins(r, team):
                t_score += 3
            elif draw(r, team):
                t_score += 1
    return t_score

def count_scores(results, teams):
    t_scores = []
    for t in teams:
        t_scores.append((t, count_score(results, t)))
    return t_scores

def result_has_team(result, team):
    if result[0] == team or result[1] == team:
        return True
    else:
        return False

def team_wins(result, team):
    if result[0] == team and result[2] > result[3]:
        return True
    elif result[1] == team and result[2] < result[3]:
        return True
    else:
        return False

def team_looses(result, team):
    if result[0] == team and result[2] < result[3]:
        return True
    elif result[1] == team and result[2] > result[3]:
        return True
    else:
        return False

def draw(result, team):
    return result[2] == result[3]

def count_result(f, results, team):
    n = 0
    for r in results:
        if result_has_team(r, team) and f(r, team):
            n += 1
    return n

def winning_score(results, team):
    n = 0
    for r in results:
        if r[0] == team:
            n += r[2]
        elif r[1] == team:
            n += r[3]
    return n

def loosing_score(results, team):
    n = 0
    for r in results:
        if r[0] == team:
            n += r[3]
        elif r[1] == team:
            n += r[2]
    return n

def result_to_str(results, t1, t2):
    for r in results:
        if result_has_team(r, t1) and result_has_team(r, t2):
            return t1 + '-' + t2 + '\t' + str(r[2]) + ':' + str(r[3])

def create_table(results, scores):
    table = []
    for score in sorted(scores, key = lambda s: s[1])[::-1]:
        table.append((len(table) + 1, score[0],
                count_result(team_wins, results, score[0]),
                count_result(team_looses, results, score[0]),
                count_result(draw, results, score[0]),
                winning_score(results, score[0]),
                loosing_score(results, score[0]),
                score[1]))
    return table

def print_table(table):
    print('Place | Team                 |  W |  L |  D |  G |  M |  S')
    print('---------------------------------------------------------')
    for t in table:
        print('%5d | %-20s | %2d | %2d | %2d | %2d | %2d | %2d' % t)

def main():
    teams = ['Anaconda', 'Crocodile', 'Monkey', 'Dragon']

    results = compete(teams)
    scores = count_scores(results, teams)

    print_table(create_table(results, scores))

    while True:
        t1 = input('\n\n' + 'First team: ')
        if t1 == '': break
        t2 = input('Second team: ')
        print(result_to_str(results, t1, t2))

if __name__ == "__main__":
    main()