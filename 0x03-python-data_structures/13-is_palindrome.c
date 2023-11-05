#include "lists.h"

/**
 * is_palindrome - Checks if a singly linked list is a palindrome.
 * @head: Points to the pointer to the head of the list.
 *
 * Return: 1 if list is palindrome, else 0.
 */
int is_palindrome(listint_t **head)
{
	int k, count = 0;
	int list[2048];
	listint_t *current = *head;

	if (*head == NULL || (*head)->next == NULL)
	{
		return (1);
	}

	while (current)
	{
		list[count] = current->n;
		current = current->next;
		count += 1;
	}

	for (k = 0; k < count / 2; k++)
	{
		if (list[k] != list[count - 1 - k])
		{
			return (0);
		}
	}

	return (1);
}
