/* Write a program to construct a binary tree to support the following operations.
Assume no duplicate elements while constructing the tree.
i. Given a key, perform a search in the binary search tree. If the key is found
then display “key found” else insert the key in the binary search tree.
ii. Display the tree using inorder, preorder and post order traversal methods */

#include<stdio.h>
#include<stdlib.h>

typedef struct nd *nodeptr;
typedef struct nd {
    int val;
    nodeptr lchild, rchild;
} node;

nodeptr createNode(int val)
{
    nodeptr node = malloc(sizeof(node));
    node->val = val;
    node->lchild = node->rchild = NULL;
    return node;
}

nodeptr createBST(nodeptr root, int item)
{
    if (!root)
    {
        nodeptr root = createNode(item);
        return root;
    }
    else if (item < root->data)
    {
        root->lchild = createBST(root->lchild, item);
    }
    else if (item > root->data)
    {
        root->rchild = createBST(root->rchild, item);
    }
    else
    {
        printf("No dupliucates allowed");
    }
    return root;
}















// nodeptr createBST(nodeptr root)
// {
//     // taking val
//     printf("Enter value: ");
//     int inp;
//     scanf("%d", &inp);
//     nodeptr newnode = createNode(inp);

//     // terminating input
//     if (inp == -1) {
//         return root;
//     } else {
//         if (inp == root->val) {
//             printf("Duplicates not allowed");
//         } else if (inp < root->val) {
//             root->lchild = createBST(root->lchild);
//         } else if (inp > root->val) {
//             root->rchild = createBST(root->rchild);
//         } 
//     }
// }
