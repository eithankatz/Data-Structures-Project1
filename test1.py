from avl_skeleton import AVLTreeList
import random

def insertRandom(i):
    ret = 0
    T = AVLTreeList()

    for j in range(1000 * 2**i):
        k = random.randint(0, T.length())
        ret += T.insert(k, 0)
    # print(i, ": ", ret)
    return ret


def deleteRandom(i):
    ret = 0
    T = AVLTreeList()

    for j in range(1000 * 2 ** i):
        k = random.randint(0, T.length())
        T.insert(k, 0)

    for j in range(1000 * 2 ** i):
        k = random.randint(0, T.length())
        ret += T.delete(k)
    return ret

def bothRandom(i):
    ret = 0
    T = AVLTreeList()

    for j in range(500 * 2 ** i):
        k = random.randint(0, T.length())
        T.insert(k, 0)

    cntdel = 250 * 2 ** i
    cntin = 250 * 2 ** i

    for j in range(500 * 2 ** i):
        act = random.randint(0, 1)
        k = random.randint(0, T.length())

        if cntdel>0 and cntin>0:
            if act == 0:
                ret += T.insert(k, 0)
                cntin -= 1
            elif act == 1:
                ret += T.delete(k)
                cntdel -= 1
            else:
                print(act)

        elif cntdel>0:
            ret += T.delete(k)
            cntdel -= 1
        else:
            ret += T.insert(k, 2)
            cntin -= 1

    return ret


def q1insertions():
    print("Q1 Insertions:")
    for i in range(1, 11):
        print(i, ": ", insertRandom(i))


def q1deletions():
    print("Q1 Deletions:")
    for i in range(1, 11):
        print(i, ": ", deleteRandom(i))

def q1both():
    print("Q1 Deletions:")
    for i in range(1, 11):
        print(i, ": ", bothRandom(i))


def main():
    # q1both()
    # q1deletions()
    q1insertions()


if __name__ == "__main__":
    main()
