#include<iostream>
using namespace std;
int main(){
    long n,a,b,sum_= 0;
    cin>>n;
    cin>>a;
    for(int i=1;i<n;i++){
        cin>>b;
        if(b<a){
            sum_ += a - b; 
        }else{
            a = b;
        }
    }
    cout<<sum_;
    return 0;
}