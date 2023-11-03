#include "slide_line.h"

#define SLIDE_LEFT  0
#define SLIDE_RIGHT 1

/**
 * slide_line - Slide and merge integers in an array.
 * @line: Pointer to an array of integers.
 * @size: Number of elements in the array.
 * @direction: Direction to slide and merge (SLIDE_LEFT or SLIDE_RIGHT).
 * Return: 1 on success, 0 on failure.
 */
int slide_line(int *line, size_t size, int direction)
{
    if (direction != SLIDE_LEFT && direction != SLIDE_RIGHT)
        return 0;

    if (direction == SLIDE_LEFT)
    {
        int i, j, merged = 0;

        for (i = 0; i < (int)size; i++)
        {
            if (line[i] != 0)
            {
                for (j = i + 1; j < (int)size; j++)
                {
                    if (line[j] != 0)
                    {
                        if (line[i] == line[j])
                        {
                            line[i] += line[j];
                            line[j] = 0;
                            merged = 1;
                        }
                        break;
                    }
                }
            }
        }

        for (i = 0, j = 0; i < (int)size; i++)
        {
            if (line[i] != 0)
            {
                line[j++] = line[i];
                if (i != j - 1)
                {
                    line[i] = 0;
                    merged = 1;
                }
            }
        }

        return merged ? 1 : 0;
    }
    else if (direction == SLIDE_RIGHT)
    {
        int i, j, merged = 0;

        for (i = (int)size - 1; i >= 0; i--)
        {
            if (line[i] != 0)
            {
                for (j = i - 1; j >= 0; j--)
                {
                    if (line[j] != 0)
                    {
                        if (line[i] == line[j])
                        {
                            line[i] += line[j];
                            line[j] = 0;
                            merged = 1;
                        }
                        break;
                    }
                }
            }
        }

        for (i = (int)size - 1, j = (int)size - 1; i >= 0; i--)
        {
            if (line[i] != 0)
            {
                line[j--] = line[i];
                if (i != j + 1)
                {
                    line[i] = 0;
                    merged = 1;
                }
            }
        }

        return merged ? 1 : 0;
    }

    return 0;
}
