#include <stdio.h>
#include <string.h>
#include <stdlib.h>

using namespace std;

void processar(char* msg){
    char* numero = new char[51];
    int tamanho = 0;
    int qtd_zero = 0;
    bool erro = 0;
    for (msg, numero; *msg != '\n' && !erro; msg++){
        if (*msg == 'O' || *msg == 'o'){
            *numero++ = '0';
            tamanho++;
        }
        else if (*msg == 'l'){
            *numero++ = '1';
            tamanho++;        
        }
        else if (*msg >= 48 && *msg <= 57){
            if (*msg == 48) qtd_zero++;
            *numero++ = *msg;
            tamanho ++;
        }
        else if (*msg != ',' && *msg != ' ') erro = 1;
    }
    *(numero) = '\0';
    numero -= tamanho;
    if (!erro){
        if (tamanho != qtd_zero){
            while (*numero == '0' && *(numero+1) != '\n'){
                numero ++;
                tamanho --;
            }
            if (!tamanho || tamanho > 10 || tamanho==10 && strcmp(numero, "2147483647") > 0) erro = 1;
        }
        else{
            if(tamanho > 0 && tamanho <=50){
                printf("0\n");
                return;
            }
            else erro = 1;
        }
    }
    if (erro) printf("error\n");
    else printf("%s\n", numero);
}
int main(){
    char* string = new char[52];
    while (fgets(string, 52, stdin)) processar(string);
    return 0;
}