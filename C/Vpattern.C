/* 

Input/Output:
Enter the row size:5

*       *
 *     *
  *   *
    * 
    *
*/


#include <stdio.h>
int main()
{
  printf("Enter the row size:");
  int row_size;
  scanf("%d", &row_size);
  int in, out, p;
  int print_control_x = 1;
  int print_control_y = row_size * 2 - 1;

  for (out = 1; out <= row_size; out++)
  {
    for (in = 1; in <= row_size * 2; in++)
    {
      if (in == print_control_x || in == print_control_y)
      {
        printf("*");
      }
      else
      {
        printf(" ");
      }
    }
    print_control_x++;
    print_control_y--;
    printf("\n");
  }
}
