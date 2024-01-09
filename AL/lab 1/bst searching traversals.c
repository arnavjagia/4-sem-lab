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

nodeptr createNode()
{
    nodeptr node = malloc(sizeof(node));
    node->lchild = node->rchild = NULL;
    return node;
}

nodeptr createBST(nodeptr root, int item)
{
    if (!root)
    {
        nodeptr root = createNode();
        root->val = item;
        return root;
    }
    else if (item < root->val)
    {
        root->lchild = createBST(root->lchild, item);
    }
    else if (item > root->val)
    {
        root->rchild = createBST(root->rchild, item);
    }
    else
    {
        printf("No duplicates allowed");
    }
    return root;
}

void preorder(nodeptr root)
{
    if (root)
    {
        printf("%d ", root->val);
        preorder(root->lchild);
        preorder(root->rchild);
    }
}

void postorder(nodeptr root)
{
    if (root)
    {
        preorder(root->lchild);
        preorder(root->rchild);
        printf("%d ", root->val);
    }
}

void inorder(nodeptr root)
{
    if (root)
    {
        preorder(root->lchild);
        printf("%d ", root->val);
        preorder(root->rchild);
    }
}

int main() {
    nodeptr root = NULL;
    for (int i=0; i<10; i++)
        root = createBST(root, i);
    printf("\nPreorder\n");
    preorder(root);
    printf("\nPostorder\n");
    postorder(root);
    printf("\nInorder\n");
    inorder(root);
    return 0;
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
