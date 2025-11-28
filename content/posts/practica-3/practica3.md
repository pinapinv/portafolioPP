---
title: "Práctica 3: Haskell"
description: "Instalación del entorno Haskell y desarrollo de una aplicación TODO usando programación funcional pura, recursión e inmutabilidad"
date: 2025-10-15
image: https://images.unsplash.com/photo-1555066931-4365d14bab8c?w=800
categories:
  - Programación
  - Paradigmas
tags:
  - haskell
  - programacion-funcional
  - recursion
  - inmutabilidad
  - stack
  - ghc
slug: practica-3
type: "post"
---
                       
                       
                       
                       
                       
                       
                       
                                           UABC
                            PARADIGMAS DE LA PROGRAMACIÓN
                                        PRÁCTICA #3
                            FERNANDA ITZEL FLORES VALENZUELA
                                          376160
                                        Grupo 941 







Instalación Haskell
Prerequisitos y Configuración del Entorno
1. Instalación de GHCup
GHCup es el instalador universal para Haskell que gestiona GHC (Glasgow Haskell Compiler), Cabal, Stack y HLS (Haskell Language Server).
En Windows:
Ejecutar en PowerShell:
powershellSet-ExecutionPolicy Bypass -Scope Process -Force;[System.Net.ServicePointManager]::SecurityProtocol = [System.Net.ServicePointManager]::SecurityProtocol -bor 3072; try { Invoke-Command -ScriptBlock ([ScriptBlock]::Create((Invoke-WebRequest https://www.haskell.org/ghcup/sh/bootstrap-haskell.ps1 -UseBasicParsing))) -ArgumentList $true } catch { Write-Error $_ }
1. Instalación de Herramientas Necesarias
Una vez instalado GHCup, instala las herramientas requeridas:
bash# Instalar GHC (compilador de Haskell)
ghcup install ghc recommended
ghcup set ghc recommended

# Instalar Stack (herramienta de construcción)
ghcup install stack latest
ghcup set stack latest

# Instalar Cabal (sistema de paquetes)
ghcup install cabal recommended
ghcup set cabal recommended

# Opcional: Instalar HLS para soporte IDE
ghcup install hls latest
3. Verificar la Instalación
bashghc --version
stack --version
cabal --version

Estructura del Proyecto TODO
4. Crear el Proyecto con Stack
bash# Crear directorio del proyecto
mkdir haskell-todo-app
cd haskell-todo-app

# Inicializar proyecto con Stack
stack new todo-app simple
cd todo-app
5. Configurar el Archivo package.yaml
Edita el archivo package.yaml para incluir las dependencias necesarias:
yamlname:                todo-app
version:             0.1.0.0
github:              "tu-usuario/todo-app"
license:             BSD3
author:              "Tu Nombre"
maintainer:          "tu@email.com"

dependencies:
- base >= 4.7 && < 5
- text
- time
- directory
- containers

executables:
  todo-app-exe:
    main:                Main.hs
    source-dirs:         app
    ghc-options:
    - -threaded
    - -rtsopts
    - -with-rtsopts=-N

Estructura de la Aplicación TODO
6. Código Principal (app/Main.hs)
La aplicación típicamente incluye:

Modelo de datos: Define la estructura de una tarea (título, descripción, estado, fecha)
Persistencia: Funciones para guardar/cargar tareas desde archivos
Interfaz de usuario: Menú interactivo en consola
Operaciones CRUD: Crear, leer, actualizar y eliminar tareas

Estructura básica:
haskell-- Tipo de dato para las tareas
data Task = Task
  { taskId :: Int
  , taskTitle :: String
  , taskDescription :: String
  , taskCompleted :: Bool
  , taskCreated :: UTCTime
  }

-- Funciones principales
main :: IO ()
addTask :: [Task] -> IO [Task]
listTasks :: [Task] -> IO ()
completeTask :: [Task] -> IO [Task]
deleteTask :: [Task] -> IO [Task]
saveTasks :: [Task] -> IO ()
loadTasks :: IO [Task]

Compilación y Ejecución
7. Construir el Proyecto
bash# Compilar el proyecto
stack build

# Ejecutar la aplicación
stack exec todo-app-exe
8. Modo de Desarrollo
Para desarrollo iterativo:
bash# Recompilar automáticamente al detectar cambios
stack build --file-watch

# Ejecutar con recarga automática
stack build --file-watch --exec todo-app-exe

Funcionalidades de la Aplicación
9. Uso Típico
Una vez ejecutada, la aplicación ofrece un menú como:
=== TODO App ===
1. Agregar tarea
2. Listar tareas
3. Marcar como completada
4. Eliminar tarea
5. Salir
Las tareas se almacenan típicamente en un archivo JSON o texto plano en el directorio local.

Comandos Útiles de Stack
bash# Limpiar compilaciones anteriores
stack clean

# Ejecutar tests (si están configurados)
stack test

# Generar documentación
stack haddock

# Instalar ejecutable globalmente
stack install

Solución de Problemas Comunes
Error de dependencias:
bashstack update
stack solver --update-config
Problemas con GHC:
bashghcup tui  # Interfaz gráfica para gestionar versiones
Reinstalar Stack:
bashghcup install stack --force

Ventajas de Usar Haskell para esta Aplicación

Tipado fuerte: Previene muchos errores en tiempo de compilación
Inmutabilidad: Facilita razonar sobre el estado de la aplicación
Funciones puras: Facilitan testing y mantenimiento
Sistema de tipos avanzado: Permite modelar el dominio de forma precisa
Evaluación perezosa: Eficiencia en procesamiento de datos

[Repositorio](https://github.com/pinapinv/portafolioPP.git)

# Documentación Oficial

Haskell.org
GHCup Documentation
Stack User Guide
Learn You a Haskell