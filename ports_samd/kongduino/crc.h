/**********************************************************************

   Filename:    crc.h

   Description: A header file describing the various CRC standards.

   Notes:


   Copyright (c) 2000 by Michael Barr. This software is placed into
   the public domain and may be used for any purpose. However, this
   notice must not be changed or removed and no warranty is either
   expressed or implied by its publication or distribution.
 **********************************************************************/

#ifndef _crc_h
#define _crc_h
#include <stdint.h>

#define FALSE 0
#define TRUE !FALSE

typedef uint32_t crc;
#define POLYNOMIAL 0x04C11DB7
#define INITIAL_REMAINDER 0xFFFFFFFF
#define FINAL_XOR_VALUE 0xFFFFFFFF
#define CHECK_VALUE 0xCBF43926

//void crcInit(void);
crc crcFast(unsigned char const message[], int nBytes);

#endif
