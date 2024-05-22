#include <stdlib.h>
#include "binary_trees.h"

/**
 * binary_tree_node - create a new tree
 * @parent:  pointer to the parent node of the node to create
 * @value: value to put in the new node
 * Return: pointer to the new node, or NULL on failure
 */

binary_tree_t *binary_tree_node(binary_tree_t *parent, int value)
{
	binary_tree_t *node;

	node = malloc(sizeof(binary_tree_t));

	if (node == NULL)
		return (NULL);

	node->n = value;
	node->left = NULL;
	node->right = NULL;

	if (parent == NULL) /*validate if empty tree*/
	{
		parent = node;
		node->parent = NULL;
		return (node);
	}
	/*If parent left is null add new to left*/
	if (parent->left == NULL)
	{
		node->parent = parent;
		parent->left = node;
		return (node);
	}
	/*If parent left is not null, add new to right*/
	node->parent = parent;
	parent->right = node;
	return (node);
}

