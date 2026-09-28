from client import TruncatedSVD

def main():
    A = [[3.0, 2.0, 2.0], [2.0, 3.0, -2.0]]
    U, S, V = TruncatedSVD.power_svd(A, k=2)
    print("Singular Values:", [round(s, 4) for s in S])
    print("Left Singular Vectors U count:", len(U))
    print("Right Singular Vectors V count:", len(V))

if __name__ == "__main__":
    main()
