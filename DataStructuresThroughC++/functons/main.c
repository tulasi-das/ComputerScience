#include <stdio.h>
#include <stdlib.h>

int main()
{
    add();
    mull(3,4);
    int x = sub(5,4);
    printf("%d",x);

    return 0;
}

void add(){
    printf("addition\n");
}
void mull(int a, int b){
    int c = a+b;
    printf("%d\n",c);
}

int sub(int a,int b){
    return a-b;
}
