#include <stdio.h>
#include <sys/types.h>
#include <unistd.h>
#include <stdlib.h>
/**
 * infinite_while - sleep function
 *
 * Return: int value
 */
int infinite_while(void)
{
	while (1)
	{
		sleep(1);
	}
	return (0);
}

/**
 * main - function init
 *
 * Return: 0 - ok
 */
int main(void)
{
	int i = 0;
	pid_t id_p = 0;

	for (i = 0; i < 5; i++)
	{
		id_p = fork();
		if (id_p == 0)
		{
			printf("Zombie process created, PID: %d\n", getpid());
			exit(0);
		}
	}
	infinite_while();
	return (0);
}
