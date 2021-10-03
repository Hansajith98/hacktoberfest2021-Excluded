#include <fcntl.h>
#include <stdlib.h>
#include <stdio.h>
#include <unistd.h>

#define BUFF_SIZE	1024 

int main() {
    int fd = open("/proc/meminfo", O_RDONLY);
    char* buffer = (char*) malloc(BUFF_SIZE);
   	if (buffer == NULL) {
		printf("error: malloc failed.\n");
        exit(1);
    }
    
	/* we cannot determine the file size of a proc file */
	int length = read(fd, buffer, BUFF_SIZE);
	
    char* unit1 = (char*) malloc(3);
    char* unit2 = (char*) malloc(3);
    char* unit3 = (char*) malloc(3);
    int mem_total, mem_free, cached;

    sscanf(buffer, "%*s %d %s %*s %d %s %*s %*d %*s %*s %d %s",
        &mem_total, unit1, &mem_free, unit2, &cached, unit3);

    printf("Free Memory: %d %s\n", mem_free, unit2);
    printf("Total Memory: %d %s\n", mem_total, unit1);
    printf("Cached: %d %s\n", cached, unit3);

    close(fd);
	free(buffer);
}

