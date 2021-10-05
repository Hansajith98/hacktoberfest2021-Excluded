#include <iostream>
#include <string>
using namespace std;

void cipher(int n, string word, string alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"){
   int index;
   size_t t_word = word.size();

   for(int x = 0; x < t_word; x++){
      for(int x1 = 0; x1 < alphabet.size(); x1++){
         if(word[x] == alphabet[x1]){
            index = x1 - n;

            if(index < 0){
               index = alphabet.size() + index;
               cout << alphabet[index];
            }else{
               cout << alphabet[index];
            }
            break;
         }
      }
   }
}

int main(){
   int n;
   int desloc;
   string word;

   cin >> n;
   for(int x = 0; x < n; x++){
      cin >> word;
      cin >> desloc;
      cipher(desloc, word);
      cout << endl;
   }

   return 0;
}
