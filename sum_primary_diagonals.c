int sumDiagonal(int N, int M[][N]) {
    int sum = 0;
    for (int i = 0; i < N; i++) {
        sum += M[i][i]; // Only primary diagonal elements
    }
    return sum;


