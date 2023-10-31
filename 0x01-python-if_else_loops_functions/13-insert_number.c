#include "lists.h"

/**
 * insert_node - inserts a number into a sorted singly linked list.
 * @head: address of head
 * @number: integer to insert
 * Return: the address of the new node, or NULL if it failed
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new_node = malloc(sizeof(listint_t));

	if (!new_node)
		return (0);

	new_node->n = number;

	if (!*head || (*head)->n > number)
	{
		/* prepend */
		new_node->next = *head;
		*head = new_node;
		return (new_node);
	}
	return (_insert_node(&(*head)->next, new_node, number));
}

/**
 * _insert_node - inserts a number into a sorted singly linked list.
 * @head: address of head
 * @new_node: node to insert
 * @number: integer to insert
 * Return: the address of the new node, or NULL if it failed
 */
listint_t *_insert_node(listint_t **head, listint_t *new_node, int number)
{
	if (!*head || (*head)->n > new_node->n)
	{
		new_node->next = *head;
		*head = new_node;
		return (new_node);
	}
	return (_insert_node(&(*head)->next, new_node, number));
}
