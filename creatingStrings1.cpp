#include <iostream>
#include <algorithm>
#include <vector>
#define all(str) str.begin(), str.end()
using namespace std;
int main()
{
    string str;
    cin >> str;
    int n;
    sort(all(str));
    vector<string> v;
    do
    {
        v.push_back(str);
    } while (next_permutation(all(str)));
    cout << v.size() << "\n";
    for (string q : v)
    {
        cout << q << "\n";
    }
    return 0;
}