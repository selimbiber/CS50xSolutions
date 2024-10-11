#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <string.h>

int main(int argc, char* argv[]) {
    // open memory card file
    FILE* inptr = fopen("card.raw", "r");
    if (inptr == NULL) {
        printf("Could not open %s.\n", "card.raw");
        return 1;
    }
    
    FILE* outptr = NULL;
    
    // create 512 byte buffer array
    typedef uint8_t BYTE;
    BYTE buffer[512];
    
    // create array for first four bytes of the buffer
    BYTE firstfour[4];
    
    // the first 4 bytes of a jpg file (i.e. jpg signature)
    BYTE jpgsig[4] = {0xff, 0xd8, 0xff, 0xe0};
    
    // keep track of jpg numbers for jpg filenames
    int jpgnumber = 0;
    char jpgfilename[8];
    
    // read a buffer from card.raw until EOF
    while (fread(buffer, sizeof(buffer), 1, inptr) == 1) {
        // load first four bytes of the buffer into firstfour
        memcpy(firstfour, buffer, 4);
        
        firstfour[3] &= 0xf0;
        
        // if jpg signature is found
        if (memcmp(firstfour, jpgsig, sizeof(jpgsig)) == 0) {
            if (outptr != NULL) {
                fclose(outptr);
            }
            sprintf(jpgfilename, "%03d.jpg", jpgnumber++);
            outptr = fopen(jpgfilename, "w");
            if (outptr == NULL) {
                printf("Could not create %s.\n", jpgfilename);
                fclose(inptr);
                return 2;
            }
        }
        
        // write buffer to the current jpg file if it's open
        if (outptr != NULL) {
            fwrite(buffer, sizeof(buffer), 1, outptr);
        }
    }
    
    // close files and exit
    fclose(inptr);
    if (outptr != NULL) {
        fclose(outptr);
    }
    return 0;
}
