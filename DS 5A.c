#include <stdio.h>
#include <conio.h>
#include <malloc.h>
void main()
{
    struct node{
        int info;
        struct node *next;
    };
    struct node *new_node,*ptr,*ptr1,*ptr2,*begin=NULL;
    int item;
    int option;
    clrscr();
    //Creating the first node in the Linked List
    new_node=(struct node *)malloc(sizeof(struct node));
    printf("\nEnter the element: ");
    scanf("%d",&item);
    new_node->info=item;
    new_node->next=NULL;
    begin=new_node;
    ptr=begin;
    //Inserting more nodes in the linked list
    printf("\nDo you want to enter other element? 1. Yes 2. No : ");
    scanf("%d",&option);
    while(option!=2)
    {
        new_node=(struct node *)malloc(sizeof(struct node));
        printf("\nEnter the element : ");
        scanf("%d",&item);
        new_node->info=item;
        new_node->next=NULL;
        ptr->next=new_node;
        ptr=new_node;
        printf("\nDo you want to enter other element? 1. Yes 2. No : ");
        scanf("%d",&option);
    }
    //Printing the Linked List
    printf("\nThe Linked List: \n");
    ptr=begin;
    while(ptr!=NULL)
    {
        printf("\t%d",ptr->info);
        ptr=ptr->next;
    }
    getch();
}