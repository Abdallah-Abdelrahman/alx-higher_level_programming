#include "lists.h"

listint_t *reverse_listint(listint_t **head);
listint_t *reverse(listint_t *head);
int _is_palindrome(listint_t *head, listint_t *tail);
/**
 * is_palindrome - checks if a singly linked list is a palindrome.
 * @head: address of head
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome
 */
int is_palindrome(listint_t **head)
{
	listint_t *hare = *head;
	listint_t *tortoise = *head;
	int len = 0;

	if (!*head)
		return (1);
	while (hare)
	{
		tortoise = tortoise->next;
		if (hare->next)
			hare = hare->next->next;
		else
			hare = hare->next;
		len += 2;
	}
	hare = reverse_listint(&tortoise->next);

	return (_is_palindrome(*head, hare));
}

/**
 * is_palindrome - checks if a singly linked list is a palindrome.
 * @head: address of head
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome
 */
int _is_palindrome(listint_t *head1, listint_t *head2)
{
	if (!head1 || !head2)
		return (1);
	if (head1->n != head2->n)
		return (0);
	return (_is_palindrome(head1->next, head2->next));
}

/**
 * reverse_listint - reverses a listint_t linked list.
 * @head: head pointer
 *
 * Return: pointer to the 1st node of the reversed list
 */
listint_t *reverse_listint(listint_t **head)
{
	*head = reverse((*head));

	return (*head);
}

/**
 * reverse - reverse list recursively
 * @head: head pointer
 *
 * Return: pointer to the last node
 */
listint_t *reverse(listint_t *head)
{
	listint_t *new_head;

	if (!head || !head->next)
		return (head);

	new_head = reverse(head->next);
	head->next->next = head;
	head->next = 0;

	return (new_head);
}
