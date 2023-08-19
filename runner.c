#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main (int argc, char ** argv) {
    char args[200];
    strcpy(args, " ");
    for (int i = 1; i < argc; i++) {
        strcat(args, argv[i]);
        strcat(args, " ");

    }
    char * run = "python3 main.py ";
    char command[strlen(run) + strlen(args)];
    strcat(command, run);
    strcat(command, args);

    system(command);
}
