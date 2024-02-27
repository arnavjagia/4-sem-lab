#include <stdio.h>
#include <stdlib.h>
int count=0;
typedef struct tree *tl;
struct tree
{
    int val;
    tl lchild, rchild;
};

tl create()
{
    printf("Enter val or -1 to exit:\n");
    int v;
    scanf("%d", &v);
    if (v == -1)
    {
        return NULL;
    }
    tl ob = (tl)malloc(sizeof(struct tree));
    ob->val = v;
    printf("Lnode of %d\n", v);
    ob->lchild = create();
    printf("Rnode of %d\n", v);
    ob->rchild = create();
    return ob;
}
int node_count(tl root)
{
    if (root == NULL)
    {
        return 0;
    }
    count++;
    return node_count(root->lchild) + node_count(root->rchild) + 1;

}

int main()
{
    printf("Enter val or -1 to exit:\n");
    tl root = create();
    printf("%d\n", node_count(root));
    printf("\nOperations count: %d\n",count);

    return 0;
}

/*
Enter val or -1 to exit:
1
Lnode of 1
2
Lnode of 2
4
Lnode of 4
-1
Rnode of 4
-1
Rnode of 2
5
Lnode of 5
-1
Rnode of 5
-1
Rnode of 1
3
Lnode of 3
6
Lnode of 6
-1
Rnode of 6
-1
Rnode of 3
7
Lnode of 7
-1
Rnode of 7
-1

Number of nodes: 7
opcount: 7
*/