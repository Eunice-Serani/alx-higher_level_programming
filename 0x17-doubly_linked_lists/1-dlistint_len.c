#include "lists.h"

/**
 * dlistint_len - This returns the number of elements in a
 * double linked list
 *
 * @h: Shows head of the list
 * Return: Number of nodes, NULL if it failed
 */
size_t dlistint_len(const dlistint_t *h)
{
	int count_n;

	count_n = 0;

	if (h == NULL)
		return (count_n);

	while (h->prev != NULL)
		h = h->prev;

	while (h != NULL)
	{
		count_n++;
		h = h->next;
	}

	return (count_n);
}
