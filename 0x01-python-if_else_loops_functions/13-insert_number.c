#include "lists.h"
#include <stdlib.h>
#include <unistd.h>
#include <stdio.h>

/**
 * insert_node - inserts a number into a sorted singly linked list
 * @head: double pointer, pointer to the pointer to a node (struct)
 * @number: is the value stored in the node
 * Return: address of the new node, or NULL if it failed
 */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new = NULL;
	listint_t *previous = NULL;
	listint_t *current = *head;

	if (!head)
		return (NULL);

	new = malloc(sizeof(listint_t));
	if (!new)
		return (NULL);

	new->n = number;
	new->next = NULL;

	if (!head || (*head)->n > number)
	{
		new->next = *head;
		return (*head);
	}
	else
	{
		while (current && current->n < number)
		{
			previous = current;
			current = current;
		}

		previous->next = new;
		new->next = current;
	}
	return (new);
}
