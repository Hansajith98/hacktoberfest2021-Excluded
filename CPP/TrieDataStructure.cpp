#include <bits/stdc++.h>
using namespace std;
const int NUM_OF_ALPHABETS = 26;
// Construction the Trie node structure
struct TrieNodeDS
{
struct TrieNodeDS *childNode[NUM_OF_ALPHABETS];
// nodeEnd is true if the node represents
// the ending of a word
bool nodeEnd;
};
// New NULL Trie node is returned
struct TrieNodeDS *getNode(void)
{
struct TrieNodeDS *nodePointer = new TrieNodeDS;
nodePointer->nodeEnd = false;
for (int i = 0; i < NUM_OF_ALPHABETS; i++)
nodePointer->childNode[i] = NULL;
return nodePointer;
}
//Insert Algorithm in Trie
void insertFunc(struct TrieNodeDS *headRoot, string searchKey)
{
struct TrieNodeDS *crawlPointer = headRoot;
for (int i = 0; i < searchKey.length(); i++)
{
int head = searchKey[i] - 'a';
if (!crawlPointer->childNode[head])
crawlPointer->childNode[head] = getNode();
crawlPointer = crawlPointer->childNode[head];
}
// End of node is marked as true; to point that the search will end here
crawlPointer->nodeEnd = true;
}
//Search Algorithm in Trie
bool searchFunc(struct TrieNodeDS * headRoot, string searchKey)
{
struct TrieNodeDS *crawlPointer = headRoot;
for (int i = 0; i < searchKey.length(); i++)
{
int head = searchKey[i] - 'a';
if (!crawlPointer->childNode[head])
return false;
crawlPointer = crawlPointer->childNode[head];
}
return (crawlPointer != NULL && crawlPointer->nodeEnd);
}
// Main Function for execution
int main()
{
// we will use only lowercase characters to keep consistency
string arrayWords[] = {"educba", "provides", "best",
"online", "education", "proven",
"by", "quality" };
int n = sizeof(arrayWords)/sizeof(arrayWords[0]);
struct TrieNodeDS * headRoot = getNode();
// Construct trie
for (int i = 0; i < n; i++)
insertFunc(headRoot, arrayWords[i]);
cout<< "---------List of words:-----------\n";
for (int i = 0; i < n; i++)
cout<< arrayWords[i] << "\n";
// Search for different words
cout<< "---------Search starts:-----------\n";
cout<< "Since 'edu' is not present as a word, but only present by sub-characters and 'u' in 'edu' doesn't represent end of node, the output will be No\n";
searchFunc(headRoot, "edu")? cout << "edu Found: Yes\n" :
cout << "edu Found: No\n";
cout<< "Since 'education' is present as a word, 'n' in 'education' represents the end of node, the output will be Yes \n";
searchFunc(headRoot, "education")? cout << "education Found: Yes\n" :
cout << "education Found: No\n";
return 0;
}
