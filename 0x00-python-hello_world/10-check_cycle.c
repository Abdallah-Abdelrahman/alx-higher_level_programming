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

	tortoise = list->next;
	hare = tortoise->next;

	for (;hare && hare->next; tortoise = tortoise->next, hare = hare->next->next)
		if (hare == tortoise)
			return (1);
	return (0);
}
