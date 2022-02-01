# Complete the 'bitwiseAnd' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER N
#  2. INTEGER K
#


def bitwiseAnd(N, K):
    # Write your code here
    S = list(i for i in range(1, N+1))
    maxres = 0

    for i in S:
        for j in S:
            if i != j:
                res = i & j
                if maxres < res < K:
                    maxres = res
        S.pop(0)

    return maxres


if __name__ == '__main__':

    t = int(input().strip())

    for t_itr in range(t):
        first_multiple_input = input().rstrip().split()
        count = int(first_multiple_input[0])
        lim = int(first_multiple_input[1])
        res = bitwiseAnd(count, lim)
        print(res)
