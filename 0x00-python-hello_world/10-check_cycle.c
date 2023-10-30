#include "lists.h"

/**
 * check_cycle - checks if a singly linked list has a cycle in it.
 * Description: Floyd’s Cycle-Finding Algorithm
 * @list: pointer to head
 *
 * Return: 0 if there is no cycle, 1 if there is a cycle
 */
int check_cycle(listint_t *list)
{
	listint_t *tortoise = list, *hare = list;

	if (!list)
		return (0);

	while (hare && hare->next)
	{
		hare = hare->next->next;
		tortoise = list->next;
		if (tortoise == hare)
			return (1);
	}

	return (0);
}

/**
 * _check_cycle - checks if a singly linked list has a cycle recursively
 * @h: pointer to head
 * @nnext: pointer to next next node
 *
 * Return: 0 if there is no cycle, 1 if there is a cycle
 */
int _check_cycle(listint_t *h, listint_t *nnext)
{
	if (!h || !nnext)
		return (0);
	if (h == nnext)
		return (1);
	return (_check_cycle(h->next, nnext->next->next));
}
