//
//  main.c
//  c
//
//  Created by wxy on 13-1-5.
//  Copyright (c) 2014年 wxy. All rights reserved.
//
//标准库
#include <stdio.h> //包含标准库的信息
#define END 'a'
void countword()
{
    int c,i,nwhite,nother;
    int ndigit[10];
    nwhite = nother = 0;
    for (i=0;i<10;i++)
        ndigit[i]=0;
    while ((c=getchar())!=END) {
        printf("%d\n",c);
        if (c>='0' && c<='9')
            ++ndigit[c-'0'];
        else if (c==' '||c=='\n'||c=='\t')
            ++nwhite;
        else
            ++nother;
    }
    printf ("digits =");
    for (i=0;i<10;++i)
        printf (" %d",ndigit[i]);
    printf(",white space= %d,other =%d\n",nwhite,nother);
    
}
int strlen_me(char s[])
{
    int i;
    i = 0;
    while (s[i]!='\0')
        ++i;
    return i;
    
}
int strlen_me2(char *s)
{
    int n;
    for (n=0;*s!='\0';s++)
        n++;
    return n;
    
}
int strlen_me3(char *s)
{
    char *p = s;
    while (*p != '\0')
        p++;
    return p - s;
    
}
void strcpy_me(char *s,char *t)
{
    while ((*s++ = *t++))
        ;
  
}
void strcpy_me2(char *s,char *t)
{
    int i;
    i = 0;
    while ((s[i] =t[i]) != '\0') {
        i++;
    }
}
void strcpy_me3(char *s,char *t)
{
    while ((*s=*t) != '\0') {
        s++;
        t++;
    }
}
int power(int base,int n)
{
    int i,p;
    p = 1;
    for (i=0;i<n;++i)
        p = p*base;
    return p;
}
void reverse_word(char c[])
{
    int i,t,len_c;
    len_c = strlen_me2(c);
    for(i=0;i<len_c/2;++i)
    {
        t = c[i];
        //有一个结束符 '\0'
        c[i] = c[len_c-i-1];
        c[len_c-i-1] = t;
    }

}
int main(int argc, const char * argv[])
{
    float a,c;
    char d[100] = "abcd";
    char e[100];
    reverse_word(d);
    a = 6.89;
    c = 7.89;
    strcpy_me(e, d);
    printf("EOF is %d\n", EOF);
    printf("%6.1f haha %5.6f \n",a,c);
    //countword();
    printf("%d\n",power(3,2));
    // insert code here...
    printf("Hello, World!\n");
    printf("%s 666 %s",e,d);
    

}

