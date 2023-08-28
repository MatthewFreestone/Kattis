# Rating: ~ 4.2 / 10
# Link: https://open.kattis.com/problems/addingwords
import sys

def main():
    w2i = {}
    i2w = {}
    for line in sys.stdin:
        cmd, *tokens = line.strip().split()
        if cmd == 'def':
            w, i = tokens
            i = int(i)
            w2i[w] = i
            i2w[i] = w
        elif cmd == 'calc':
            res_phrase = ' '.join(tokens)
            startw, *tokens = tokens
            #print(startw, w2i)
            if startw not in w2i:
                print(res_phrase, 'unknown')
                continue
            total = w2i[startw]
            cmds = ((tokens[i], tokens[i+1]) for i in range(0, len(tokens)-1, 2))
            # print(list(cmds))
            unknown = False
            for operator, w in cmds:
                if w not in w2i:
                    print(res_phrase, 'unknown')
                    unknown = True
                    break
                if operator == '-':
                    total -= w2i[w]
                else:
                    total += w2i[w]
            if not unknown:
                #print(total, i2w)
                res = i2w.get(total, 'unknown')
                print(res_phrase, res)
        elif cmd == 'clear':
            w2i = {}
            i2w = {}
if __name__ == "__main__":
  main()
