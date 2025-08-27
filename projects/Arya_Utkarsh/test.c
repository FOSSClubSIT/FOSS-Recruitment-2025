#include <stdio.h>
#include <string.h>
#include <ctype.h>

int main()
{
     const char secret_word[] = "CHAIR";
    int guess_limit = 5;
    char guess[100];
    
    while (1)
    {
        int guess_count = 0;
        while (guess_count < guess_limit)
        {
         printf("Guess:\n");
            scanf("%s", guess);

            // Convert guess to uppercase
            for (int i = 0; guess[i]; i++)
                guess[i] = toupper((unsigned char)guess[i]);

            guess_count++;

            if (strcmp(guess, secret_word) == 0)
            {
                printf("You Win!\n");
                break;
            }
            else
            {
                int wordle_arr[5];
                int used[5] = {0};

                // First pass: correct positions
                for (int i = 0; i < 5; i++)
                {
                    if (guess[i] == secret_word[i])
                    {
                        wordle_arr[i] = 1;
                        used[i] = 1;
                    }
                    else
                    {
                        wordle_arr[i] = -2; // mark as not checked
                    }
                }
                // Second pass: check wrong positions
                for (int i = 0; i < 5; i++)
                {
                    if (wordle_arr[i] == -2)
                    {
                        int found = 0;
                        for (int j = 0; j < 5; j++)
                        {
                            if (!used[j] && guess[i] == secret_word[j])
                            {
                                wordle_arr[i] = 0;
                                used[j] = 1;
                                found = 1;
                                break;
                            }
                             }
                        if (!found)
                            wordle_arr[i] = -1;
                    }
                }

                // Print result
                printf("%s\n[", guess);
                for (int i = 0; i < 5; i++)
                {
                    printf("%d", wordle_arr[i]);
                    if (i < 4)
                        printf(", ");
                }
                printf("]\n");
            }
        }
    }

    return 0;
}
