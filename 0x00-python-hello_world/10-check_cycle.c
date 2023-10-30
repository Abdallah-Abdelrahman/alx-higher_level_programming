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
	listint_t *tortoise = 0, *hare = 0;

	if (!list || !list->next)
		return (0);
	if (list == list->next || list == list->next->next)
		return (1);
	if (!list->next->next)
		return (0);

	tortoise = list->next;
	hare = tortoise->next;

	while (tortoise && hare)
	{
		if (tortoise == hare)
			return (1);
		tortoise = tortoise->next;
		hare = hare->next->next;
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
