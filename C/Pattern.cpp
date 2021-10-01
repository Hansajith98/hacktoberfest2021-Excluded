// C++ code to demonstrate star pattern
#include <iostream>
using namespace std;
int main()
{
    int n = 5;
    // Outer loop to handle number of rows
    for (int i = 0; i < n; i++) {
 
        // Inner loop to handle number of columns
        for (int j = 0; j <= i; j++) {
            cout << "* ";
        }
        cout << endl;
    }
    return 0;
}