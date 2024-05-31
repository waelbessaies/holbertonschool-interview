#ifndef SORT_H
#define SORT_H

#include <stdio.h>
#include <stdlib.h>


void freegrid(int **grid);
int power_ten(int power);
int sort_in_matrix(int *array, int **tmp, size_t size, int level);
void print_array(const int *array, size_t size);
void radix_sort(int *array, size_t size);


#endif
