#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * is_palindrome - checks if singly linked list is a palindrome
 * @head: pointer to head of list
 * Return: 0 or 1
 */

int is_palindrome(listint_t **head)
{
	int size, i, *arr;

	if (head == NULL)
	{
		return (1);
	}
	size = 0;
	arr = malloc(sizeof(listint_t));
	while (*head)
	{
		arr[size] = (*head)->n;
		(*head) = (*head)->next;
		size++;
	}
	if (size % 2 == 0)
	{
		for (i = 0; i < size / 2; i++)
		{
			if (arr[i] != arr[size - 1 - i])
			{
				return (0);
			}
		}
	}
	else
	{
		for (i = 0; i < size - 1 / 2; i++)
		{
			if (arr[i] != arr[size - 1 - i])
			{
				return (0);
			}
		}
	}
	return (1);
}
