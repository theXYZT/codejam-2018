# Codejam 2018, Round 3: Field Trip

def turns(a, b):
    """
    Finds minimum turns in a dimension where a is the minimum coordinate,
    and b is the maximum coordinate, and the teacher is at the origin.
    """
    if a >= 0 or b <= 0:
        return (max(abs(a), abs(b)) + 1) // 2
    else:
        t = min(abs(a), abs(b))
        return t + turns(a + t, b - t)

# I/O Code
num_cases = int(input())

for case in range(1, num_cases + 1):
    N = int(input())

    # Teacher coordinates
    teacher_x, teacher_y = map(int, input().split())

    # Find student positions relative to the teacher
    X, Y = [], []
    for _ in range(1, N):
        student_x, student_y = map(int, input().split())
        X.append(student_x - teacher_x)
        Y.append(student_y - teacher_y)

    # Dimensions are separable
    result = max(turns(min(X), max(X)),
                 turns(min(Y), max(Y)))

    print('Case #{}: {}'.format(case, result))
