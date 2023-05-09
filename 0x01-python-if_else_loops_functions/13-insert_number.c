#include "lists.h"

/**
 * insert_node - adds a new node at the end of a listint_t list
 * @head: pointer to pointer of first node of listint_t list
 * @number: integer to be included in new node
 * Return: address of the new element or NULL if it fails
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new_node = *head, *current;

	current = malloc(sizeof(listint_t));
	if (current == NULL)
		return (NULL);
	current->n = number;

	if (new_node == NULL || new_node->n >= number)
	{
		current->next = new_node;
		*head = current;
		return (current);
	}

	while (new_node && new_node->next && new_node->next->n < number)
		new_node = new_node->next;

	current->next = new_node->next;
	new_node->next = current;

	return (current);
}

