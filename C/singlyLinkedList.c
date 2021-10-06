/* Singly linked lists program */

#include<stdio.h>
#include<conio.h>
#include<stdlib.h>

int insChoice;
int delchoice;

struct node
{
    int data;
    struct node* next;
};

//** pointer variables **//
struct node* start;
struct node* new_node;
struct node* current;
struct node* delvab;
struct node* preptr;


/* Creating a new_node */
void create()
{
    new_node= (struct node*)malloc(sizeof(struct node));
    
    if (new_node==NULL)
    {
        printf("Memory is not available!!! \n");
    }
    else
    {   
        printf("Enter data to your node ");
        scanf("%d",&new_node->data);
        new_node->next=NULL;
    
    if (start==NULL)
    {
        start=new_node;
        current=start;
    }
    else
    {   
        printf("Start to next address is: %p \n",start->next);
        current->next=new_node;
        printf("start pointing to next(5) node is: %p \n",start->next);
        current=new_node;
    }
        
    }
}


/* Display informations of Nodes */
void display()
{
    if(start==NULL)
    {
        printf("There is no nodes in your linked lists \n");
    }
    current=start;
    while(current!=NULL)
        {
            
            printf("Node address : %p Node data: %d Node next address: %p \n",current,current->data,current->next); 
            current=current->next;
        }
}   


/* Inserting node at beginning */
int insertbeg()
{   
    printf("Insert at beginning: ");
    new_node=(struct node*)malloc(sizeof(struct node));
    if (new_node==NULL)
    {
        printf("Memory is not available \n");
    }
    else
    if(start==NULL)
    {
        printf("Sorry can't insert node... \n");
    }
    else
    {
        printf("Enter data to 1st node: ");
        scanf("%d",&new_node->data);
        new_node->next=start;
        start=new_node;
    }    
}


/* Inserting node in between */
int insertbtw()
{   
   
    int num;
    current=start;
    preptr=current;
    new_node=(struct node*)malloc(sizeof(struct node));
    if(new_node==NULL)
    {
        printf("Memory is not available \n");
    }
    else
    if(start==NULL)
    {
        printf("Sorry can't insert node... \n");
    }
    else
    {   
        display();
        printf("Enter data after which to insert new_node ");
        scanf("%d",&num);
        
        current=start;
        preptr=current;
        if(num==current->data)
        {
            current=current->next;
            preptr->next=new_node;
            new_node->next=current;
            printf("Enter data to your node ");
            scanf("%d",&new_node->data);
        }
        else
        {
            while(preptr->data!=num)
            {
                preptr=current;
                current=current->next;
            }
            preptr->next=new_node;
            new_node->next=current;
            printf("Enter data to your node ");
            scanf("%d",&new_node->data);
        }
    }
}


/* Inserting node at end */
int insertend()
{   
    
    new_node=(struct node*)malloc(sizeof(struct node));
    
    if (new_node==NULL)
    {
        printf("Memory is not available \n");
    }
    else
    if(start==NULL)
    {
        printf("Sorry can't insert node... \n");
    }
    else
    {
        printf("Enter data to Last node: ");
        scanf("%d",&new_node->data);
        new_node->next=NULL;
        
        current=start;
        while(current->next!=NULL)
        {
            current=current->next;
        }
        current->next=new_node;
    }
}


/* Deleting node at beginning */
int delbeg()
{   
   
    if(start==NULL)
    {
        printf("You can't delete as list is empty... \n");
    }
    else
    {
        delvab=start;
        start=start->next;
        free(delvab);
    }
}


/* Deleting node in between */
int delbtw()
{   
    
    int num;
    display();
    if(start==NULL)
    {
        printf("You can't delete as list is empty... \n");
    }
    else
    {
        printf("Enter data after which to delete node : ");
        scanf("%d",&num);
        current=start;
        preptr=current;
        if(num==preptr->data)
        {
            preptr=current;
            current=current->next;
            delvab=current;
            preptr->next=current->next;
            free(delvab);
        }
        else
        {
            while(preptr->data!=num)
            {
                preptr=current;
                current=current->next;
            }
            delvab=current;
            preptr->next=current->next;
            free(delvab);
        }
    }
}


/* Deleting node at end */
int delend()
{
    
    if(start==NULL)
    {
        printf("You can't delete as list is empty \n");
    }
    else
    if(start->next==NULL)
    {
        start=NULL;
        free(current);
    }
    else
    {   current=start;
        while(current->next!=NULL)
        {
            preptr=current;
            current=current->next;
        }
    preptr->next=NULL;
    free(current);
    }
}


/* Insert function */
void insertnode()
{   
    
    printf("Insert choices: \n");
    printf("1. Insert_at_beg \n");
    printf("2. Insert_at_end \n");
    printf("3. Insert in between \n");
 
    printf("Enter operation to perform: ");
    scanf("%d",&insChoice );
    
    switch(insChoice)
    {
        case 1: insertbeg();
                break;
        case 2: insertend();
                break;
        case 3: insertbtw();
                break;
        default: printf("Enter correct choice for insertion \n");
                 break;
    }
}


/* Delete functions */
void deletenode()
{   
    
    printf("Delete choices: \n");
    printf("1. Delete_at_beg \n");
    printf("2. Delete_at_end \n");
    printf("3. Delete in between \n");
    
    printf("Enter operation to perform: ");
    scanf("%d",&delchoice);
    
    switch(delchoice)
    {   
        case 1: delbeg();
                 break;
        case 2: delend();
                 break;
        case 3: delbtw();
                 break;
        default: printf("Enter correct choice for deletion \n");
                 break;
    }
}



/* main function of our program */
void main()
{ 
    int ans=1;
    int choice;
    
    while(ans==1)
    {   printf("1. Create \n");
        printf("2. Display \n");
        printf("3. Insert \n");
        printf("4. Delete \n");
        printf("5. Exit \n");
        
        printf("Enter choice ");
        scanf("%d",&choice);
    
        switch(choice)
        {
        case 1:  create();
                 break;
        case 2:  printf("Your data is: \n");
                 display();
                 break;
        case 3:  insertnode();
                 break;
        case 4:  deletenode();
                 break;
        case 5:  exit(0);
                 break;
        default: printf("Enter correct choice.. \n");
                 break;
        }
       
    printf("Do you want to do more operations ?(1 or 0) ");
    scanf("%d",&ans);
    }
getch();    
}
    





