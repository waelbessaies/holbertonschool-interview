#ifndef SORT_H
#define SORT_H

#include <stddef.h>


void print_array(const int *array, size_t size);
int iParent(int i);
int iLeftChild(int i);
void ConvertToHeap(int *array, size_t size);
void SiftDown(int *array, size_t size, int start, int end);
void heap_sort(int *array, size_t size);


#endif
