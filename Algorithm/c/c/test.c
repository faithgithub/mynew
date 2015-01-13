//
//  test.c
//  c
//
//  Created by wxy on 13-1-5.
//  Copyright (c) 2014年 wxy. All rights reserved.
//

#include <stdio.h>

main()
{
    int c;
    c = getchar();
    while (c != EOF) {
        putchar(c);
        c = getchar();
        
    }
}