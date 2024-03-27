#include <iostream>
#include <valarray>

using namespace std;

double recursiveSum(int n, int k=1, double sum=0) {

    if (k > n) {
        return sum;
    }

    //calculating the next element the series
    double element = pow(-1, k+1) / k;

    // adding terms to running sum
    sum = sum + element;

    // recursively calling the function with k+1 and the updated sum
    return recursiveSum(n, k+1, sum);
}

double recursiveSum() {
    int N;
    cout << "Enter a value for N: ";
    cin >> N;
    return recursiveSum(N);
}

int main() {
    //Q3:
    int N;
    cout<<"Enter a value for N: ";
    cin >> N;

    double resultValue = recursiveSum(N);
    cout<<"Sum of the series = " << resultValue << endl;


    //Q4:
    //calling the overloaded recursive function
    double theResultValue2 = recursiveSum();
    cout <<"The sum of the series = " << theResultValue2 << endl;


    return 0;
}
