#include<stdio.h>
#include<string.h>
int main() {
    char password[20], correct[]= "a32bc" ;
    do{ 
        printf("Enter the password=     ");
        scanf("%s", password);
    }
    while(strcmp( password , correct) != 0 );
    printf("Access Granted");
}