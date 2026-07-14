#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>

int main(int argc, char *argv[])
{
    // Accept a single command-line argument
    if (argc != 2)
    {
        printf("Usage: ./recover FILE\n");
        return 1;
    }
    
    // Open the memory card
    FILE *card = fopen(argv[1], "r");
    if (card == NULL)
    {
        printf("Could not open %s.\n", argv[1]);
        return 2;
    }

    // Create a buffer for a block of data
    uint8_t buffer[512];



    FILE *img = NULL;
    int jpeg_count = 0;
    
    // While there's still data left to read from the memory card
    while (fread(buffer, 1, 512, card) == 512)
    {
        // Create JPEGs from the data
        if (buffer[0] == 0xff 
            && buffer[1] == 0xd8 
            && buffer[2] == 0xff 
            && (buffer[3] & 0xf0) == 0xe0)
            {
                // is the image open
                if (img != NULL)
                {
                    // close it if its open
                    fclose(img);
                }
                // create a new filename
                char filename[8];
                sprintf(filename, "%03i.jpg", jpeg_count);
                // open new jpeg
                img = fopen(filename,"w");
                jpeg_count++;

            }
            if (img != NULL)
            {
                fwrite(buffer, 1, 512, img);
            }
        }
        if (img != NULL)
        {
            fclose(img);
        }
    fclose(card);
}