#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main (int argc, char ** argv) {
    int size = 0;

    for (int i = 0; i < argc; i++) {
        size += strlen(argv[i]);
    }


    char args[size];
    strcpy(args, " ");
    for (int i = 1; i < argc; i++) {
        strcat(args, argv[i]);
        strcat(args, " ");

    }
    char run[] = "python3 ./brof/__main__.py ";
    char command[strlen(run) + strlen(args) + 10];
    strcat(command, run);
    strcat(command, args);

    system(command);
}
