#include <stdio.h>
#include <stddef.h>
#include "lists.h"

/**
 * print_dlistint - This prints all the elements of a
 * dlistint_t list
 *
 * @h: Shows head of the list
 * Return: Number of nodes, NULL if it failed
 */
size_t print_dlistint(const dlistint_t *h)
{
	int count_n;

	count_n = 0;

	if (h == NULL)
		return (count_n);

	while (h->prev != NULL)
		h = h->prev;

	while (h != NULL)
	{
		printf("%d\n", h->n);
		count_n++;
		h = h->next;
	}

	return (count_n);
}
