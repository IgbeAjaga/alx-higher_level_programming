#include "lists.h"
#include <stdlib.h>

/**
 * reverse_list - Reverse a linked list in place
 * @head: Pointer to the head node
 *
 * Return: Pointer to the new head node
 */
listint_t *reverse_list(listint_t *head)
{
    listint_t *prev = NULL;
    listint_t *current = head;
    listint_t *next = NULL;

    while (current != NULL) {
        next = current->next;
        current->next = prev;
        prev = current;
        current = next;
    }

    return prev;
}

/**
 * is_palindrome - Check if a singly linked list is a palindrome
 * @head: Pointer to the head node
 *
 * Return: 1 if the list is a palindrome, 0 otherwise
 */
int is_palindrome(listint_t **head)
{
    if (*head == NULL || (*head)->next == NULL) {
        /* An empty or single-node list is considered a palindrome */
        return 1;
    }

    listint_t *slow = *head;
    listint_t *fast = *head;

    /* Find the middle node of the list using Floyd's tortoise and hare algorithm */
    while (fast != NULL && fast->next != NULL) {
        slow = slow->next;
        fast = fast->next->next;
    }

    /* Reverse the second half of the list */
    listint_t *second_half = reverse_list(slow);

    /* Compare the first half and the reversed second half of the list */
    listint_t *current = *head;
    while (second_half != NULL) {
        if (current->n != second_half->n) {
            /* The list is not a palindrome */
            reverse_list(second_half);
            return 0;
        }
        current = current->next;
        second_half = second_half->next;
    }

    /* The list is a palindrome */
    reverse_list(slow);
    return 1;
}
