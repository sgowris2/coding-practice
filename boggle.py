from copy import copy

def find_words(words, board):

    for word in words:
        start_letters = find_letters(word[0], board)
        if len(start_letters) > 0:
            for s in start_letters:
                not_found = False
                visited = [[False for x in range(0, len(board[0]))] for x in range(0, len(board))]
                visited[s[0]][s[1]] = True
                position = s
                for letter in word[1:]:
                    n = find_next_letter(letter, position, visited)
                    if n is not None:
                        visited[n[0]][n[1]] = True
                        position = n
                    else:
                        not_found = True
                        break
                if not_found is False:
                    print(word)
                    break
            else:
                break


def find_next_letter(letter, position, visited):

    u = tuple((position[0]-1, position[1]))
    l = tuple((position[0], position[1]-1))
    r = tuple((position[0], position[1]+1))
    d = tuple((position[0]+1, position[1]))
    ul = tuple((position[0] - 1, position[1]-1))
    dl = tuple((position[0] + 1, position[1] - 1))
    ur = tuple((position[0] - 1, position[1] + 1))
    dr = tuple((position[0] + 1, position[1] + 1))

    if u[0] >= 0 and not visited[u[0]][u[1]] and board[u[0]][u[1]] == letter:
        return u
    if l[1] >= 0 and not visited[l[0]][l[1]] and board[l[0]][l[1]] == letter:
        return l
    if r[1] < len(board[0]) and not visited[r[0]][r[1]] and board[r[0]][r[1]] == letter:
        return r
    if d[0] < len(board) and not visited[d[0]][d[1]] and board[d[0]][d[1]] == letter:
        return d
    if ul[0] >= 0 and not visited[ul[0]][ul[1]] and board[ul[0]][ul[1]] == letter:
        return ul
    if dl[1] >= 0 and not visited[dl[0]][dl[1]] and board[dl[0]][dl[1]] == letter:
        return dl
    if ur[1] < len(board[0]) and not visited[ur[0]][ur[1]] and board[ur[0]][ur[1]] == letter:
        return ur
    if dr[0] < len(board) and not visited[dr[0]][dr[1]] and board[dr[0]][dr[1]] == letter:
        return dr

    return None


def find_letters(letter, board):

    r = []
    for i in range(0, len(board)):
        for j in range(0, len(board[0])):
            if board[i][j] == letter:
                r.append(tuple((i, j)))

    return r




if __name__ == '__main__':

    words = ['GEEKS', 'QUIZ', 'GO', 'CODE']
    board = [['G', 'I', 'Z'], ['U', 'E', 'K'], ['Q', 'S', 'E']]

    find_words(words, board)
