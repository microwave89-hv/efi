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

#include "libmy.h"

/* Copyright (C) 2002-2014 Free Software Foundation, Inc.
   This file is part of the GNU C Library.
   Contributed by Ulrich Drepper <drepper@redhat.com>, 2002.

   The GNU C Library is free software; you can redistribute it and/or
   modify it under the terms of the GNU Lesser General Public
   License as published by the Free Software Foundation; either
   version 2.1 of the License, or (at your option) any later version.

   The GNU C Library is distributed in the hope that it will be useful,
   but WITHOUT ANY WARRANTY; without even the implied warranty of
   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
   Lesser General Public License for more details.

   You should have received a copy of the GNU Lesser General Public
   License along with the GNU C Library; if not, see
   <http://www.gnu.org/licenses/>. */

#include <errno.h>
#if 0
#include "pthreadP.h"
#include <atomic.h>
#endif

int
__pthread_key_create (key, destr)
pthread_key_t *key;
void (*destr) (void *) __attribute__((unused)) ;
{
#if 1
	* key = 0 ;
	return 0 ;
#else
  /* Find a slot in __pthread_kyes which is unused. */
  for (size_t cnt = 0; cnt < PTHREAD_KEYS_MAX; ++cnt)
    {
      uintptr_t seq = __pthread_keys[cnt].seq;

      if (KEY_UNUSED (seq) && KEY_USABLE (seq)
        /* We found an unused slot. Try to allocate it. */
        && ! atomic_compare_and_exchange_bool_acq (&__pthread_keys[cnt].seq,
                                                   seq + 1, seq))

        {
          /* Remember the destructor. */
          __pthread_keys[cnt].destr = destr;

          /* Return the key to the caller. */
          *key = cnt;

          /* The call succeeded. */
          return 0;
        }
    }

  return EAGAIN;
#endif
}
#if 1
__typeof (__pthread_key_create) pthread_key_create __attribute__((weak, alias("__pthread_key_create"))) ;
#else
strong_alias (__pthread_key_create, pthread_key_create)
hidden_def (__pthread_key_create)
#endif



