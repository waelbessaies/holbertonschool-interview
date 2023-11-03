#include "slide_line.h"

/**
 * slide_line - slides and merges an array of integers to the left or to the right
 * @line: a pointer to the array of integers
 * @size: the size of the array
 * @direction: direction to slide and merge the arraygit
 *
 *
 * Return: 1 upon success, or 0 upon failure
 */
int slide_line(int *line, size_t size, int direction)
{
    size_t i, j, step;
    int merged[LINE_SIZE] = {0};

    if (direction != SLIDE_LEFT && direction != SLIDE_RIGHT)
        return 0;

    if (direction == SLIDE_LEFT)
        step = 1;
    else
        step = -1;

    for (i = 0; i < size; i++)
    {
        if (line[i] == 0)
            continue;

        for (j = i + step; j < size; j += step)
        {
            if (line[j] == 0)
                continue;

            if (line[i] == line[j] && merged[j] == 0 && i != j)
            {
                line[i] *= 2;
                line[j] = 0;
                merged[i] = 1;
                break;
            }

            if (line[i] != line[j] && line[j - step] == 0)
            {
                line[j - step] = line[j];
                line[j] = 0;
                j -= step;
            }
            else
                break;
        }
    }

    return 1;
}