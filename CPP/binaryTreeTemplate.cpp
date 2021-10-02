#include <bits/stdc++.h>
using namespace std;
struct TreeNode{
    int data;
    struct TreeNode* left;
    struct TreeNode* right;

    TreeNode(int val){
        data = val;
        left = right = NULL;
    }
};

TreeNode* makeTree(vector<int> arr, int i){
    if(i >= arr.size()) return NULL;

    TreeNode* root = new TreeNode(arr[i]);

    root->left = makeTree(arr, 2*i+1);
    root->right = makeTree(arr, 2*i+2);

    return root;
}

void printTree_PRE(TreeNode* root){
    if(root == NULL) return;

    // preorder: root, left, right
    cout << root->data << " ";
    printTree_PRE(root->left);
    printTree_PRE(root->right);
}
void printTree_IN(TreeNode* root){
    if(root == NULL) return;

    // preorder:  left, root, right
    printTree_IN(root->left);
    cout << root->data << " ";
    printTree_IN(root->right);
}
void printTree_POST(TreeNode* root){
    if(root == NULL) return;

    // preorder: left, right, root
    printTree_POST(root->left);
    printTree_POST(root->right);
    cout << root->data << " ";
}


int main(){
    // makeTree() use number of elements = 1 3 7 15 (2**h - 1)
    // driver code

    TreeNode* root = makeTree({1,2,3,4,5,6,7}, 0);
    printTree_PRE(root);

    return 0;
}
