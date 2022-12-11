#include <stdio.h>
#include <stdlib.h>

using namespace std;

void printLine(char* msg){
    for (int i=0; *(msg+i)!='\0';i++){
        putchar_unlocked(*(msg+i));
    }
    putchar_unlocked('\n');
    return;
}
char* getLine(char* string){
    char ch;
    int i=0;
    while ((ch = getchar_unlocked()) != '\n'){
        *(string+i) = ch;
        i++;
    }
    *(string+i) = '\0';
    return string;
}
int getNumber(){
    char* numero = new char[14];
    char ch;

    for (int i=0;ch != '\n' && ch != ' ';i++){
        ch = getchar_unlocked();
        *(numero+i) = ch; 
    }
    return atoi(numero);
}
void reverter(char* msg, int pos_final){
    char temporario;
    
    for (int i=0; i<pos_final; i++){
        temporario = msg[i];
        msg[i] = msg[pos_final];
        msg[pos_final--] = temporario;
    }
    return;
}
char* criptografar(char* msg){
    int pos=0;
    while (*(msg+pos)!='\0'){    
        if ((*(msg+pos)>=65 && *(msg+pos)<=90) || (*(msg+pos)>=97 && *(msg+pos)<=122)){
            *(msg+pos) += 3;
        }
        pos++;
    }
    reverter(msg,pos-1);
    pos /= 2;
    while (*(msg+pos)!='\0'){
        *(msg+pos) -= 1;
        pos++;
    }
    return msg;
}
int main(){
    int n;
    char* string = new char[1001];
    n = getNumber();
    for (int i=0; i<n; i++){
        printLine(criptografar(getLine(string)));
    }
    return 0;
}