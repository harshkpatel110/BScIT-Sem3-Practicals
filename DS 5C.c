#include <stdio.h>
#include <conio.h>
#include <malloc.h>
void main()
{
    struct node{
        int info;
        struct node *next;
    };
    struct node *new_node,*ptr,*ptr1,*begin=NULL;
    int item, item1;
    int option;
    clrscr();
    //Creating the first node in the Linked List
    new_node=(struct node *)malloc(sizeof(struct node));
    printf("\nEnter the element : ");
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
        printf("\nEnter the new element : ");
        scanf("%d",&item);
        printf("\nEnter the element after which the new element should be placed : ");
        scanf("%d",&item1);
        ptr1=begin;
        while(ptr1!=NULL)
        {
            if(ptr1->info==item1)
            {
                new_node->info=item;
                new_node->next=ptr1->next;
                ptr1->next=new_node;
                goto e;
            }
            ptr1=ptr1->next;
        }
        if(ptr1==NULL)
        printf("\nThe element %d is not present in the list.", item1);
        e:
        printf("\nDo you want to enter other element? 1. Yes 2. No : ");
        scanf("%d",&option);
    }
    //Printing the Linked List
    printf("\nThe Linked List : \n");
    ptr=begin;
    while(ptr!=NULL)
    {
        printf("\t%d",ptr->info);
        ptr=ptr->next;
    }
    getch();
}