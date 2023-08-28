# Rating: ~ 4.2 / 10
# Link: https://open.kattis.com/problems/addingwords

# This problem was incredibly frustrating, I still don't know why the .bak version is wrong.
# Notably, the problem thinks that "calc foo = " should return unknown NOT foo if foo is not defined. `

import sys

def main():
    w2i = {}
    for line in sys.stdin:
        cmd, *tokens = line.strip().split()
        if cmd == 'def':
            w, i = tokens
            w2i[w] = int(i)
        elif cmd == 'calc':
            res_phrase = ' '.join(tokens)

            to_eval = []
            for word in tokens[:-1]:
                if word in ['+','-']:
                    to_eval.append(word)
                elif word in w2i:
                    to_eval.append(str(w2i[word]))
                else:
                    print(res_phrase, 'unknown')
                    break
            else:
                res = eval(' '.join(to_eval))
                i2w = {v:k for k,v in w2i.items()}
                print(res_phrase, i2w.get(res, 'unknown'))

        elif cmd == 'clear':
            w2i = {}
if __name__ == "__main__":
  main()
