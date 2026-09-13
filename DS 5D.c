#include <stdio.h>
#include <conio.h>
#include <malloc.h>
void main()
{
    struct node{
        int info;
        struct node *next;
    };
    struct node *new_node,*ptr,*ptr1, *ptr2, *begin=NULL;
    int item;
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
        printf("\nEnter the element : ");
        scanf("%d",&item);
        new_node->info=item;
        new_node->next=NULL;
        ptr->next=new_node;
        ptr=new_node;
        printf("\nDo you want to enter other element? 1. Yes 2. No : ");
        scanf("%d",&option);
    }
    // Printing the Linked List
    printf("\nThe Linked List : \n");
    ptr=begin;
    while(ptr!=NULL)
    {
        printf("\t%d",ptr->info);
        ptr=ptr->next;
    }
    //Deleting a node
    printf("\nDo you want to delete element? 1. Yes 2. No : ");
    scanf("%d",&option);
    while(option!=2)
    {
        printf("\nEnter the element : ");
        scanf("%d",&item);
        if(begin->info==item)
        {
            ptr=begin;
            begin=begin->next;
            free(ptr);
        }
        else
        {
            ptr1=begin;
            ptr2=ptr1->next;
            while(ptr2!=NULL && ptr2->info!=item)
            {
                ptr1=ptr2;
                ptr2=ptr2->next;
            }
            if(ptr2==NULL)
            printf("\nThe node containing element %d not present in the linked list.",item);
            else
            {
                ptr1->next=ptr2->next;
                free(ptr2);
            }
        }
    printf("\nDo you want to delete another element? 1. Yes 2. No : ");
    scanf("%d",&option);
    }

    // Printing the Linked List
    printf("\nThe Linked List : \n");
    ptr=begin;
    while(ptr!=NULL)
    {
        printf("\t%d",ptr->info);
        ptr=ptr->next;
    }
    getch();
}