#include <stddef.h>
#ifndef SLIDE_LINE
#define SLIDE_LINE

#define SLIDE_LEFT 1
#define SLIDE_RIGHT 2
#define LINE_SIZE 32


int slide_line(int *line, size_t size, int direction);

#endif
