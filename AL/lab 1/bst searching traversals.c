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

void searchBST(nodeptr root, int key)
{
    if (!root)
    {
        root = createBST(root, key);
    } else if (root->val == key) {
        printf("Key found\n");
        return;
    } else if (key < root->val) {
        searchBST(root->lchild, key);
    } else if (key > root->val) {
        searchBST(root->rchild, key);
    }
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
        postorder(root->lchild);
        postorder(root->rchild);
        printf("%d ", root->val);
    }
}

void inorder(nodeptr root)
{
    if (root)
    {
        inorder(root->lchild);
        printf("%d ", root->val);
        inorder(root->rchild);
    }
}

int main() {
    nodeptr root = NULL;
    for (int i=1; i<11; i++)
        root = createBST(root, i);
    printf("\nPreorder\n");
    preorder(root);
    printf("\nPostorder\n");
    postorder(root);
    printf("\nInorder\n");
    inorder(root);

    printf("\nSearching for 10\n");
    searchBST(root, 12);

    inorder(root);
    return 0;
}
