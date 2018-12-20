# Codejam 2018, Round 1B: Rounding Error

def get_percentage(num_voters, lang_votes):
    """Gets percentage sum given list of vote counts and total voters."""
    return sum([int(100 * i / num_voters + 0.5) for i in lang_votes])

def get_max_percentage(num_voters, lang_votes):
    """Find max sum of votes when rounding percentages of votes."""
    voters_left = num_voters - sum(lang_votes)

    lang_votes = sorted(lang_votes, key=lambda x: (100 * x / num_voters) % 1,
                        reverse=True)

    i = 0
    while voters_left > 0:
        if i == len(lang_votes):
            lang_votes.append(1)
            voters_left -= 1

            if voters_left == 0:
                break

        if (100 * lang_votes[i] / num_voters) % 1 < 0.5:
            lang_votes[i] += 1
            voters_left -= 1
        else:
            i += 1

    return get_percentage(num_voters, lang_votes)

# I/O Code
num_cases = int(input())

for case in range(1, num_cases + 1):
    num_voters, num_lang = [int(i) for i in input().split()]
    lang_votes = [int(i) for i in input().split()]

    max_percentage = get_max_percentage(num_voters, lang_votes)
    print("Case #{}: {}".format(case, max_percentage))
