#include "lists.h"

/**
 * insert_node - adds a new node at the end of a listint_t list
 * @head: pointer to pointer of first node of listint_t list
 * @number: integer to be included in new node
 * Return: address of the new element or NULL if it fails
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new_node, *current, *prev;

	new_node = malloc(sizeof(listint_t));

	if (!new_node)
	{
		return (NULL);
		}
	new_node->n = number;

	prev = NULL;

	current = *head;

	while (current && current->n < number)
	{
		prev = current;

		current = current->next;
		}
	new_node->next = current;

	if (prev)
		prev->next = new_node;
	else
	{
		*head = new_node;
		}
	return (new_node);
}

