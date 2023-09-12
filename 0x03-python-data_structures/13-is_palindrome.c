#include "lists.h"
#include <stdio.h>
#include <stdlib.h>

/**
 * reverse_listint - a function that reverses a listint_t linked list
 *@head: the adreess of the pointer to the first node
 *
 * Return: a pointer to the first node of the reversed list
 */

listint_t *reverse_listint(listint_t **head)
{
	listint_t *curr, *prev;

	if (head == NULL || *head == NULL)
		return (NULL);

	curr = (*head)->next;
	(*head)->next = NULL;
	prev = curr;

	while (prev)
	{
		curr = curr->next;
		prev->next = *head;
		*head = prev;
		prev = curr;
	}
	return (*head);
}

/**
 * compare_lists - compare if two linked lists contain the same elements
 *@head: the head pointer to the first list
 *@head2: the head pointer to the second list
 *
 * Return: 1 equal, 0 otherwise
 */

int compare_lists(listint_t *head, listint_t *head2)
{
	listint_t *temp_1 = head, *temp_2 = head2;

	while (temp_1 && temp_2)
	{
		if (temp_1->n != temp_2->n)
			return (0);

		temp_1 = temp_1->next;
		temp_2 = temp_2->next;

	}
	return (1);
}
/**
 * is_palindrome - a function that checks if a singly
 *       linked list is a palindrome.
 *@head: a double pointer to the head of the list
 *
 * Return: 1 if the linked list is a palindrome. 0 Otherwise
 */
int is_palindrome(listint_t **head)
{
	listint_t *slow = *head, *prev_slow = *head, *fast = *head;
	listint_t *second_half;
	int result = 0;

	if (head == NULL)
		return (0);

	if (*head == NULL || (*head)->next == NULL)
		return (1);

	while (fast && fast->next)
	{
		/*We need previous of the slow pointer for linked lists with odd elements */
		prev_slow = slow;
		fast = fast->next->next;
		slow = slow->next;
	}

	/* in case of odd elements */
	if (fast)
	{
		/*midnode = slow;*/
		slow = slow->next;
	}

	second_half = slow;
	prev_slow->next = NULL;  /* NULL terminate the first half */
	second_half = reverse_listint(&second_half);
	result = compare_lists(*head, second_half);

	return (result);


}
