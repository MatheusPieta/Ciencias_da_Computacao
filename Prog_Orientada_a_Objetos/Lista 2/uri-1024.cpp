#include <stdio.h>
#include <string.h>
#include <iostream>

using namespace std;

// function to reverse the word - step two
inline void reverse(char word[],int len){
    char temp;
    int helper;
    for (helper = 0; helper < len/2; helper++){
        temp=word[helper];
        word[helper]=word[len-helper-1];
        word[len-helper-1]=temp;
    }
}
void ler_linha(char linha[]){
    char  * pos = linha; 
    // getchar()
    char c = 0;
    c = getchar_unlocked();
    // printf ("c: %c\n", c);
    while (c != '\n' && c != EOF){
        *pos = c;
        pos++;
        c = getchar_unlocked();
        // printf ("c: %c\n", c);
    }
    *pos = 0;
    return;
}
int meu_len(char linha[]){
    char  * pos = linha;
    while (*pos != 0){
        pos++;
    }
    return pos - linha;
}
void imprimir_linha(char *linha){
    while (*linha != 0){
        putchar_unlocked(*linha);
        linha++;
    }
    putchar_unlocked('\n');
}
int main(){
    int cases, helper, i, len;
    char cript[1001];
    char linha[1001];
    ler_linha(cript);
    cases = atoi(cript);
    for(helper = 0; helper < cases; helper++){
        ler_linha(cript);
        for(i = 0; cript[i] != '\0'; i++)
              if(cript[i] >= 'A' && cript[i] <= 90 ||  cript[i] >= 97 && cript[i] <= 122)
                          cript[i] += 3;
        len = strlen(cript);
        reverse(cript,len);
        
        // step three
        for(i = len/2; cript[i] != '\0'; i++)
                          cript[i]--;
        imprimir_linha(cript);              
    } 
    return 0;
}