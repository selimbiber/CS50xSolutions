#include <stdio.h>
#include <stdlib.h>
#include "bmp.h"

// Function prototypes
void processBMP(FILE* inputFile, FILE* outputFile);

int main(int argc, char* argv[]) {
    // Ensure proper usage
    if (argc != 3) {
        fprintf(stderr, "Usage: %s input.bmp output.bmp\n", argv[0]);
        return 1;
    }

    // Open input file
    FILE* inputFile = fopen(argv[1], "rb");
    if (inputFile == NULL) {
        fprintf(stderr, "Error opening file %s.\n", argv[1]);
        return 2;
    }

    // Open output file
    FILE* outputFile = fopen(argv[2], "wb");
    if (outputFile == NULL) {
        fclose(inputFile);
        fprintf(stderr, "Error creating file %s.\n", argv[2]);
        return 3;
    }

    // Process BMP file
    processBMP(inputFile, outputFile);

    // Close files
    fclose(inputFile);
    fclose(outputFile);

    return 0;
}

void processBMP(FILE* inputFile, FILE* outputFile) {
    // Read BITMAPFILEHEADER and BITMAPINFOHEADER
    BITMAPFILEHEADER fileHeader;
    fread(&fileHeader, sizeof(BITMAPFILEHEADER), 1, inputFile);

    BITMAPINFOHEADER infoHeader;
    fread(&infoHeader, sizeof(BITMAPINFOHEADER), 1, inputFile);

    // Check BMP format
    if (fileHeader.bfType != 0x4d42 || fileHeader.bfOffBits != 54 || infoHeader.biSize != 40 ||
        infoHeader.biBitCount != 24 || infoHeader.biCompression != 0) {
        fprintf(stderr, "Unsupported BMP format.\n");
        exit(4);
    }

    // Write header info to output file
    fwrite(&fileHeader, sizeof(BITMAPFILEHEADER), 1, outputFile);
    fwrite(&infoHeader, sizeof(BITMAPINFOHEADER), 1, outputFile);

    // Calculate padding for scanlines
    int padding = (4 - (infoHeader.biWidth * sizeof(RGBTRIPLE)) % 4) % 4;

    // Process each scanline
    for (int i = 0, height = abs(infoHeader.biHeight); i < height; i++) {
        for (int j = 0; j < infoHeader.biWidth; j++) {
            RGBTRIPLE pixel;
            fread(&pixel, sizeof(RGBTRIPLE), 1, inputFile);

            // Modify pixel colors
            if (pixel.rgbtRed > 235) {
                pixel.rgbtBlue = 0x30;
                pixel.rgbtGreen = 0x30;
                pixel.rgbtRed = 0x10;
            }

            fwrite(&pixel, sizeof(RGBTRIPLE), 1, outputFile);
        }

        // Skip padding in input file
        fseek(inputFile, padding, SEEK_CUR);

        // Add padding to output file
        for (int k = 0; k < padding; k++) {
            fputc(0x00, outputFile);
        }
    }
}
