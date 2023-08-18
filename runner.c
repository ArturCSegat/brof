#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main (int argc, char ** argv) {
    char * args = malloc(sizeof(argv));
    for (int i = 1; i < argc; i++) {
        strcat(args, argv[i]);
        strcat(args, " ");

    }
    char * run = "python3 main.py ";
    char * command = malloc(strlen(run) + sizeof(args));
    strcat(command, run);
    strcat(command, args);

    system(command);

    free(args);
    free(command);
}
