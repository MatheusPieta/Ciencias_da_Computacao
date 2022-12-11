#include <stdio.h>

using namespace std;

void getMaior(char* palavra, int &maior){
    int tamanho=0;
    for (;*(palavra+tamanho);tamanho++);
    if (tamanho > maior) maior = tamanho;
    return;
}

int main(){
    int casos, maior=0;
    bool flag=1;
    scanf("%d", &casos);
    while (casos != 0){
        char palavras[casos][51];
        for (int i=0; i<casos; i++){
            scanf("%s", palavras[i]);
            getMaior(palavras[i], maior);
        }
        if (flag){
            flag = 0;
        } 
        else{
            printf("\n");
        }
        for (int i=0; i<casos-1; i++){
            printf("%*s\n", maior, palavras[i]);
        }
        printf("%*s\n", maior, palavras[casos-1]);
        maior = 0;
        scanf("%d", &casos);
    }
    return 0;
}