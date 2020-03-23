/*
 * This file is part of UEFI GPT fdisk.
 *
 * UEFI GPT fdisk is a port of GPT fdisk to UEFI/BIOS.
 * UEFI GPT fdisk est un portage de GPT fdisk vers UEFI/BIOS.
 * Ce fichier a été initié par Bernard Burette en janvier 2014.
 * Ce fichier est récupéré soit de "GNU libc" soit de "dietlibc"
 * soit encore il a été créé de toutes pièces.
 *
 * All this work is copyleft Bernard Burette.
 * Gauche d'auteur Bernard Burette.
 *
 * This program is distributed under the terms of the GNU GPL version 2.
 * La diffusion de ce code est faite selon les termes de la GPL GNU version 2.
 */

#ifndef libmy_h_INCLUDED
#define libmy_h_INCLUDED

#define __dietlibc__

#define _FILE_OFFSET_BITS 64

/* needed to get definition of "struct stat64" from sys/stat.h
   do this first otherwise file "sys/types.h" will have already
   been included by others. */
#define _LARGEFILE64_SOURCE 1
#include <sys/stat.h>
/* for types like size_t */
#include <sys/types.h>
/* for types like uint64_t */
#include <stdint.h>

/* This file could be included by C++ source files */
#if defined(__cplusplus)
extern "C" {
#endif

extern int __fxstat64( int version , int fd , struct stat64 *buf ) ;

extern __off64_t lseek64( int fd , __off64_t offset , int whence ) ;

extern int __cxa_atexit( void (* func) (void *) , void * arg , void * d ) ;

extern void __fortify_fail( const char * msg ) __attribute__((noreturn)) ;

extern void * __malloc( size_t count ) ;

extern void __free( void * block ) ;

extern void abort() __attribute__((noreturn)) ;

extern void exit( int status ) __attribute__((noreturn)) ;

extern void read_str( void ) ;
extern void print_str( const char * ) ;
extern void print_dec( int64_t ) ;
extern void print_hex8( uint64_t ) ;
extern void print_hex64( uint64_t ) ;

extern int __ltostr( char * s , unsigned int size , unsigned long i , unsigned int base , int UpCase ) ;
extern int __lltostr( char * s , int size , unsigned long long i , int base , char UpCase ) ;

#if defined(__cplusplus)
}
#endif

/* Locale management imported from GNU stdlib uses a lot of these macros,
   we don't need them in our simple implementation */
#define __libc_rwlock_define(CLASS,NAME)
#define __libc_lock_lock(NAME)
#define __libc_rwlock_rdlock(NAME)
#define __libc_rwlock_wrlock(NAME)
#define __libc_lock_unlock(NAME)
#define __libc_rwlock_unlock(NAME)
#define compat_symbol( libc , name1 , name2 , version )
#define __SYMBOL_PREFIX
#define libc_hidden_proto(name, attrs...)
#define libc_hidden_def(name)
#define attribute_hidden
#define internal_function      /* empty */
#define attribute_tls_model_ie __attribute__ ((tls_model ("initial-exec")))
#define weak_extern(expr)

#endif /* libmy_h_INCLUDED */

