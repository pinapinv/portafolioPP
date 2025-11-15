

                       UNIVERSIDAD AUTÓNOMA DE BAJA CALIFORNIA 
                            PARADIGMAS DE LA PROGRAMACIÓN
                                        PRÁCTICA #1
                            FERNANDA ITZEL FLORES VALENZUELA
                                        Grupo 941


Introducción:
En esta práctica analizaremos conceptos vistos en clase ya aplicados en el código. Analizaremos la estructura del mismo y lograremos identificar cada uno de los nombres, marcos de activación, bloques de alcance, administración de memoria, expresiones, comandos, control de secuancia, subprogramas y tipos de datos. Con esta práctica reforzaremos el conocimiento visto en clase ya aplicado a la programación en sí, no solo conceptualmente


Desarrollo:


1. Nombres

Variables globales: bss_var, static_var.

Variables locales (automáticas): bookCount, memberCount, choice, library, members dentro de main.

Nombres simbólicos (tipos definidos por el programador): genre_t, book_t, member_t.

Funciones (nombres de subprogramas): addBook, findBookById, displayBooksRecursive, issueBook, etc.
2. Marcos de activación (Activation Records / Stack Frames)

Cada vez que se llama a una función como addBook o displayBooks, se crea un marco de activación en el stack con:

Variables locales (ej. new_book en addBook).

Parámetros (ej. book_t **library, int *count).

Estos marcos desaparecen al terminar la ejecución de la función.
3. Bloques de alcance (Scope Blocks)

Ámbito global: Definición de static_var, bss_var, tipos struct y enum, prototipos de funciones.

Ámbito local: Variables definidas dentro de cada función (int genre en addBook, int memberID en searchMember).

Bloques de selección (if, switch) también crean pequeños bloques de alcance para variables locales.

4. Administración de memoria

Estática: static int static_var (segmento de datos).

BSS: int bss_var; (variable global no inicializada).

Automática (Stack): Variables locales como bookCount, memberCount.

Dinámica (Heap): Uso de malloc, realloc, free en estructuras book_t y member_t.

Ej: book_t *new_book = (book_t *)malloc(sizeof(book_t));

Además se llevan registros de asignaciones en incrementHeapAllocations y incrementHeapDeallocations.

5. Expresiones

Operaciones aritméticas: memberFound->issued_count++, bookFound->quantity--.

Operaciones de asignación: new_book->title[strcspn(...)] = '\0';.

Comparaciones: if (current->id == bookID).

Conversión de tipo: (genre_t)genre.

6. Comandos (Statements)

Asignación: *library = new_book;

Entrada/Salida: scanf, printf, fgets, fprintf, fscanf.

Llamadas a funciones: displayBooksRecursive(library);

Retorno: return current;, return NULL;.

7. Control de secuencia

Selección:

if, else if, switch (choice) en el menú principal.

Iteración:

while (current) { ... } para recorrer listas enlazadas.

for (int i = 0; i < current->issued_count; i++) para recorrer libros de un miembro.

do { ... } while(choice != 8); en el menú principal.

Recursión:

displayBooksRecursive(book_t *library) que se llama a sí misma para mostrar los libros.

8. Subprogramas (Funciones) 

Funciones definidas por el usuario: addBook, findBookById, saveLibraryToFile, etc.

Funciones estándar de C: malloc, free, fopen, fscanf, fgets.

Funciones de apoyo: genreToString convierte un enum en cadena.

9. Tipos de datos

Primitivos: int, char, float (en este caso no se usa float).

Compuestos:

struct _book y struct _member.

enum genre_t.

Punteros (book_t *, member_t *).

Arreglos: char title[100], int *issued_books.

Conclusiones:
Gracias a la práctica pude ver más allá de los conecptos vistos en clase y pude ser capaz de identificarlos fuera de lo teórico, también vi cómo se utiliza cada cosa. Además de saber identificar más rápido todo.
([Repositorio](https://github.com/pinapinv/portafolioPP))