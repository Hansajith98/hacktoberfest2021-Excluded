// C++ program to encode a word to a Pig Latin.
#include <bits/stdc++.h>
using namespace std;

bool isVowel(char c)
{
	return (c == 'A' || c == 'E' || c == 'I' || c == 'O' || c == 'U' || c == 'a' ||c == 'e' || c == 'i' || c == 'o' || c == 'u');
}

void pigLatin(string s)
{
	int len = s.length();string c;
	int index = -1;
	for (int i = 0; i < len; i++) {
		if (isVowel(s[i])) {
			index = i;
			break;
		}
	}


	if (index == -1)
		cout<< "-1";
	c=s.substr(index) + s.substr(0, index);
    cout<<c<<"ay";
}

int main()
{
	string str ;
	cout<<"Enter a String:\n";
	cin>>str;
	pigLatin(str);
	if (str == "-1")
		cout << "No vowels found. Pig Latin not possible";
	
}
