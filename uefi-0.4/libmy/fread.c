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

#define _XOPEN_SOURCE 600
#include "libmy.h"
#include <stdio.h>
#include <unistd.h>

size_t fread( ptr , size , count , stream )
	void * ptr ;
	size_t size ;
	size_t count ;
	FILE * stream ;
{
	char * p ; /* l'adresse où stocker ce qui est lu */
	size_t n ; /* le nombre d'items lus */
	if ( fileno( stream ) < 0 ) return EOF ;
	setvbuf( stream , NULL , _IONBF , 0 ) ;
	p = (char *) ptr ;
	n = 0 ;
	while ( count ) {
		int s ; /* la taille de cet item */
		s = size ;
		while ( s ) {
			/* lit un octet pour gérer proprement ungetc() */
			char c = fgetc( stream ) ;
			/* fin de fichier ou erreur */
			if ( c == EOF ) goto ret ;
			/* stocke l'octet et avance */
			* p = c ;
			p ++ ;
			s -- ;
		}
		count -- ;
		n ++ ;
	}
	ret : ;
	return n ;
}

