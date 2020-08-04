#include <iostream>
#include <algorithm>
#include <limits>

using namespace std;

int main()
{
    int n;
    cin >> n;
    int a[20];
    int ttl = 0;
    for (int i = 0; i < n; i++)
    {
        cin >> a[i];
        ttl += a[i];
    }
    int ans = INT8_MAX;
    //cout<<ans<<"\n";
    for (int i = 0; i < (1 << n); i++)
    {
        int c = 0;
        for (int j = 0; j < n; j++)
        {
            if (1 << j & i)
                c += a[j];
        }
        ans = min(ans, abs(ttl - c - c));  
    }
    cout << ans;
    return 0;
}