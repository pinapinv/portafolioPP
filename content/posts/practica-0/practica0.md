---
title: "Práctica 0: Uso de Repositorios"
description: "Introducción a Markdown, Git, GitHub, Hugo y GitHub Actions"
date: 2025-09-01
image: https://images.unsplash.com/photo-1618401471353-b98afee0b2eb?w=800
categories:
  - Control de Versiones
  - Documentación
tags:
  - markdown
  - git
  - github
  - hugo
  - github-actions
slug: practica-0
type: "post"
---

# Tu contenido...

# Contenido de la práctica
                    
                                           UABC
                            PARADIGMAS DE LA PROGRAMACIÓN
                                        PRÁCTICA #0
                            FERNANDA ITZEL FLORES VALENZUELA
                                          376160
                                        Grupo 941 




¿Qué es Markdown?
Markdown es un lenguaje de marcado ligero que permite dar formato a texto de manera sencilla utilizando caracteres especiales. Fue creado por John Gruber con el objetivo de ser fácil de leer y escribir, y que se pueda convertir a HTML fácilmente.

¿Cómo se utiliza?  
Markdown se utiliza escribiendo texto plano con una sintaxis específica. Es muy común en archivos README de proyectos, documentación técnica y páginas estáticas.

Sintaxis básica de Markdown:
- **Encabezados:**  
  ```markdown
  # Título 1
  ## Título 2
  ### Título 3
  Negritas y cursivas:
**negrita**, *cursiva*

Listas:

Item 1

Item 2

Item 3

Listas numeradas:

Paso uno

Paso dos

Paso tres

Enlaces e imágenes:
[Texto del enlace](https://ejemplo.com)
![Texto alternativo](imagen.png)

Código:
`codigo` para línea, o

```lenguaje
bloque de código
```


Markdown permite generar documentos limpios y estructurados que luego pueden transformarse en HTML o PDF.

¿Qué es Git?
Git es un sistema de control de versiones distribuido que permite guardar, administrar y rastrear cambios en proyectos de software o archivos.

¿Qué es GitHub?
GitHub es una plataforma en la nube que permite almacenar repositorios de Git, colaborar en proyectos y compartir código.

git init                # Inicializar un repositorio
git clone <url>         # Clonar un repositorio existente
git status              # Ver el estado de los archivos
git add <archivo>       # Añadir un archivo al área de preparación
git commit -m "mensaje" # Guardar cambios con un mensaje
git push origin main    # Subir cambios a GitHub
git pull origin main    # Descargar los últimos cambios del repositorio

Cómo crear un repositorio en GitHub y subir información:

Crear una cuenta en GitHub

Crear un nuevo repositorio en GitHub.

En la computadora:

git init
git remote add origin <url-del-repositorio>
git add .
git commit -m "Primer commit"
git push -u origin main


¿Qué es Hugo?
Hugo es un generador de sitios estáticos escrito en Go. Permite crear páginas web rápidas a partir de archivos Markdown.

¿Qué es GitHub Actions?
GitHub Actions es una herramienta de automatización que permite ejecutar flujos de trabajo (workflows) directamente en GitHub. Se puede usar para desplegar automáticamente sitios web en GitHub Pages.

Cómo crear un sitio estático con Hugo:
sudo apt install hugo    # En Linux
choco install hugo -y    # En Windows con Chocolatey


Crear un nuevo sitio:

hugo new site mi-sitio


Añadir un tema (ejemplo con Ananke):
cd mi-sitio
git submodule add https://github.com/theNewDynamic/gohugo-theme-ananke themes/ananke
echo 'theme = "ananke"' >> config.toml

Crear una página:
hugo new posts/primer-post.md

Probar localmente:

hugo server -D


Cómo subir a GitHub y configurar GitHub Actions:

Subir el sitio a un repositorio en GitHub.

Crear un archivo de workflow .github/workflows/hugo.yml
Habilitar GitHub Pages en la configuración del repositorio.
Cada vez que se haga git push, el sitio se publicará automáticamente.

[Portafolio] (https://github.com/pinapinv/portafolioPP)