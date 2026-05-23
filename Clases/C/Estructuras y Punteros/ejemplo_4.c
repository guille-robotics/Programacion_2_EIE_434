
//Usando punteros a caracteres en estructuras en C
#include <stdio.h>

struct myStructure {
  int myNum;
  const char *myString;  // Puntero a un caracter
};

int main() {
  struct myStructure s1;
  
  // ¡AHORA SÍ FUNCIONA!
  s1.myString = "Some text"; 
  
  return 0;
}