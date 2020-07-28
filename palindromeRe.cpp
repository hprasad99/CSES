#include<iostream>  
#include<string> 
#include<unordered_map> 
using namespace std;

string getPalindrome(string str){
    unordered_map<char, int> hmap;
    for(int i=0;i<str.length();i++){
        hmap[str[i]]++;
    }
    /*for(int i=0;i<str.length();i++){
        cout<< hmap[i];
    }*/
    int oddCount = 0;
    char oddChar;
    for(auto x:hmap){
        //cout<<x.second;
        if(x.second%2!=0){
            oddCount++;
            oddChar = x.first;
        }
    }

    if(oddCount > 1 || oddCount == 1 && str.length()%2==0){
        return "NO SOLUTION";
    }

    string firsthalf="", secondhalf="";
    for(auto x:hmap){
        string s(x.second / 2,x.first);
        firsthalf = firsthalf + s;
        secondhalf = s + secondhalf;
    }
    return (oddCount == 1)?(firsthalf+oddChar+secondhalf):(firsthalf+secondhalf);
}

int main(){
    string s;
    cin >> s;
    cout<<getPalindrome(s);
}