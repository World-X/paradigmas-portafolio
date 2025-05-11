+++
date = '2025-05-05T13:17:02-07:00'
draft = false
title = 'Práctica 3'
+++

## Tabla de contenido

- [Aplicación "TODO" en Haskell](#aplicación-todo-en-haskell)
  - [Instalación de Haskell y Stack](#instalación-de-haskell-y-stack)
  - [Crear un nuevo proyecto](#crear-un-nuevo-proyecto)
  - [Estructura del proyecto](#estructura-del-proyecto)
  - [Implementación de la aplicación](#implementación-de-la-aplicación)
    - [1. Bucle de iteracción básico](#1-bucle-de-iteracción-básico)
    - [2. Añadir y listar tareas (`+` y `l`)](#2-añadir-y-listar-tareas--y-l)
    - [3. Eliminar y mostrar tareas (`-` y `s`)](#3-eliminar-y-mostrar-tareas---y-s)
    - [4. Limpiar tareas (`c`)](#4-limpiar-tareas-c)
    - [5. Editar tareas (`e`)](#5-editar-tareas-e)
    - [6. Finalización y pruebas](#6-finalización-y-pruebas)
  - [Compilación y ejecución](#compilación-y-ejecución)
  - [Ejecución de pruebas](#ejecución-de-pruebas)
- [Conclusión](#conclusión)

## Aplicación "TODO" en Haskell

En este artículo, se presenta una aplicación "TODO" desarrollada en Haskell, usando un entorno de desarrollo con Stack.

### Instalación de Haskell y Stack

Al descargar e instalar Stack, se instalará automáticamente GHC (Glasgow Haskell Compiler) en cada proyecto por separado, así que no es necesario instalarlo globalmente o por separado.

Descargar Stack desde su [sitio oficial](https://docs.haskellstack.org/en/stable/). Procede a instalarlo siguiendo las instrucciones de la página o instalador.

### Crear un nuevo proyecto

Para crear un nuevo proyecto en Haskell llamado "TODO", abre una terminal y ejecuta el siguiente comando:

```bash
stack new TODO
cd TODO
```

Esto creará un nuevo directorio llamado "TODO" con la estructura básica de un proyecto Haskell.

Procede a ejecutar el siguiente comando para compilar y ejecutar el proyecto:

```bash
stack build
stack exec TODO-exe
```

Con `stack build`, se compila el proyecto, instalando GHC si es necesario. Con `stack exec TODO-exe`, se ejecuta el ejecutable generado. Por supuesto, también se puede utilizar `stack run` para compilar y ejecutar el proyecto en un solo paso, aunque debes ejecutar `stack build` primero.

### Estructura del proyecto

La estructura del proyecto es la siguiente:

```txt
TODO/
├── app
│   └── Main.hs
├── src
│   └── Lib.hs
├── test
│   └── Spec.hs
├── .gitignore
├── CHANGELOG.md
├── LICENSE
├── package.yaml
├── README.md
├── Setup.hs
├── stack.yaml
├── stack.yaml.lock
└── TODO.cabal
```

- `app/Main.hs`: Contiene el punto de entrada de la aplicación.
- `src/Lib.hs`: Contiene la lógica de la aplicación.
- `test/Spec.hs`: Contiene las pruebas de la aplicación.
- `.gitignore`: Archivos y directorios que Git debe ignorar.
- `CHANGELOG.md`: Registro de cambios del proyecto.
- `LICENSE`: Licencia del proyecto.
- `package.yaml`: Archivo de configuración del paquete.
- `README.md`: Documentación del proyecto.
- `Setup.hs`: Script de configuración del proyecto.
- `stack.yaml`: Archivo de configuración de Stack.
- `stack.yaml.lock`: Archivo de bloqueo de Stack.
- `TODO.cabal`: Archivo de configuración del paquete Cabal.

### Implementación de la aplicación

Para construir la aplicación de lista de tareas "TODO", modificaremos gradualmente los archivos de **Haskell** (`.hs`) generados y añadiremos un nuevo módulo para la lógica principal. La lista de tareas se representará como una lista de cadenas de texto (`[String]`).

#### 1. Bucle de iteracción básico

a. **Crear `src/Crud.hs`**: Este módulo contendrá la lógica de la aplicación. Inicialmente, solo tendrá la función principal del bucle (prompt).

```haskell
module Crud
    ( 
        prompt,
    ) where

-- Función principal que maneja el bucle de interacción con el usuario
-- Recibe la lista actual de TODOs y la pasa recursivamente
prompt :: [String] -> IO ()
prompt todos = do
    putStrLn "" -- Deja una línea en blanco para claridad
    putStrLn "Insert a command (q to quit):"
    command <- getLine -- Lee la línea de entrada del usuario

    -- Si el comando es 'q', termina la acción IO (sale del bucle)
    if command == "q"
        then return ()
        else do
            -- Si no es 'q', muestra un mensaje y continúa el bucle recursivamente
            putStrLn $ "Command received: " ++ command
            prompt todos -- Llama a prompt de nuevo con la misma lista de TODOs
```

b. **Actualizar `app/Main.hs`**: Modificamos el archivo principal para que importe Crud y llame a prompt con una lista de TODOs inicialmente vacía.

```haskell
module Main where

import Crud (prompt) -- Importa la función prompt desde el módulo Crud

main :: IO ()
main = do
    putStrLn "Basic TODO app"
    -- Inicia el bucle de interacción con una lista de TODOs vacía
    prompt []
```

c. **Eliminar o ignorar `src/Lib.hs`**: Como ya no usamos Lib.hs, su contenido por defecto puede ser ignorado o el archivo eliminado.

En este punto, puedes compilar (`stack build`) y ejecutar (`stack exec TODO-exe`). La aplicación se iniciará, pedirá comandos, mostrará lo que recibió (excepto `'q'`) y continuará hasta que introduzcas `'q'`.

#### 2. Añadir y listar tareas (`+` y `l`)

Ahora, implementaremos la posibilidad de añadir tareas y listarlas. Introduciremos una función `interpret` para manejar los comandos y una función auxiliar `putTodo` para mostrar cada tarea.

a. **Actualizar `src/Crud.hs`**: Añadimos `putTodo` y `interpret`. La función prompt ahora llamará a interpret.

```haskell
module Crud
    ( 
        prompt,
    ) where

import Data.List -- Necesario para funciones de lista (aunque no se usa mucho aún)

-- Función auxiliar para mostrar un TODO con su índice
putTodo :: (Int, String) -> IO ()
putTodo (n, todo) = putStrLn (show n ++ ": " ++ todo)

-- Función principal que maneja el bucle de interacción con el usuario
prompt :: [String] -> IO ()
prompt todos = do
    putStrLn ""
    putStrLn "Commands: + <task>, l, q" -- Actualizamos el mensaje de ayuda
    command <- getLine

    -- Ahora delegamos la interpretación del comando a la función 'interpret'
    interpret command todos

-- Función que interpreta los comandos de usuario
interpret :: String -> [String] -> IO ()

-- Comando '+' para añadir un TODO: pattern matching en la cadena
-- Si la cadena empieza con "+ " seguido de algo, captura el resto como 'todo'
interpret ('+':' ':todo) todos = do
    putStrLn $ "Adding task: " ++ todo
    -- Llama a prompt con la nueva lista (añadiendo el nuevo todo al principio)
    prompt (todo:todos) 

-- Comando 'l' para listar todos los TODOs
interpret  "l"           todos = do
    putStrLn "List of tasks:"
    -- Muestra cada TODO con su índice (0-basado)
    mapM_ putTodo (zip [0..] todos) -- zip junta índices con tareas, mapM_ ejecuta putTodo para cada par
    prompt todos -- Continúa el bucle

-- Comando 'q' para salir de la aplicación
interpret  "q"           todos = return () -- Termina la acción IO

-- Cualquier otro comando se considera inválido
interpret  command       todos = do
    putStrLn ("Invalid command: `" ++ command ++ "`")
    prompt todos -- Continúa el bucle con la misma lista
```

Ahora puedes añadir tareas usando `+ mi primera tarea`, `+ comprar pan`, listarlas con `l`, y salir con `q`.

#### 3. Eliminar y mostrar tareas (`-` y `s`)

Implementaremos los comandos para eliminar una tarea por su índice y mostrar una tarea específica. Necesitaremos funciones auxiliares `deleteOne` y `showOne`.

a. **Actualizar `src/Crud.hs`**: Añadimos las funciones deleteOne, showOne y los casos `-` y `s` a interpret.

```haskell
module Crud
    ( 
        prompt,
    ) where

import Data.List 
import Text.Read (readMaybe) -- Importamos readMaybe para una lectura segura

-- Función auxiliar para mostrar un TODO con su índice
putTodo :: (Int, String) -> IO ()
putTodo (n, todo) = putStrLn (show n ++ ": " ++ todo)

-- Función principal que maneja el bucle de interacción con el usuario
prompt :: [String] -> IO ()
prompt todos = do
    putStrLn ""
    putStrLn "Commands: + <task>, - <num>, s <num>, l, q" -- Actualizamos el mensaje de ayuda
    command <- getLine

    interpret command todos

-- Función que interpreta los comandos de usuario
interpret :: String -> [String] -> IO ()

interpret ('+':' ':todo) todos = do
    putStrLn $ "Adding task: " ++ todo
    prompt (todo:todos) 

-- Comando '-' para eliminar un TODO por índice
interpret ('-':' ':numStr) todos = do
    case readMaybe numStr of -- Usamos readMaybe para intentar leer el número
        Nothing -> do
            putStrLn "Error: Index must be a valid number."
            prompt todos
        Just num -> do
            case deleteOne num todos of
                Nothing -> do
                    putStrLn "Error: There's no task with that number."
                    prompt todos
                Just todos' -> do
                    putStrLn $ "Task " ++ numStr ++ " deleted."
                    prompt todos'

-- Comando 's' para mostrar un TODO por índice
interpret ('s':' ':numStr) todos = do
     case readMaybe numStr of -- Usamos readMaybe para intentar leer el número
        Nothing -> do
            putStrLn "Error: Index must be a valid number."
            prompt todos
        Just num -> do
            case showOne num todos of
                Nothing -> do
                    putStrLn "Error: There's no task with that number."
                    prompt todos
                Just todo -> do
                    putStrLn $ "Task " ++ show num ++ ": " ++ todo
                    prompt todos

interpret  "l"           todos = do
    let numberOfTodos = length todos
    putStrLn ""
    print $ show numberOfTodos ++ " in total"
    mapM_ putTodo (zip [0..] todos)
    prompt todos

interpret  "q"           todos = return ()

interpret  command       todos = do
    putStrLn ("Invalid command: `" ++ command ++ "`")
    prompt todos

-- Función auxiliar para eliminar un elemento por índice
-- Retorna Maybe [a] porque la eliminación puede fallar (índice inválido)
deleteOne :: Int -> [a] -> Maybe [a]
deleteOne 0 (_:as) = Just as -- Caso base: eliminar el primer elemento
deleteOne n (a:as) -- Caso recursivo: descender en la lista y decrementar el índice
    | n < 0     = Nothing -- Índice negativo es inválido
    | otherwise = do
        as' <- deleteOne (n - 1) as -- Intenta eliminar en el resto de la lista
        return (a:as')             -- Si tiene éxito, reconstruye la lista
deleteOne _  []    = Nothing -- Si llegamos al final de la lista antes de encontrar el índice

-- Función auxiliar para mostrar un elemento por índice
-- Retorna Maybe a porque el índice puede ser inválido
showOne :: Int -> [a] -> Maybe a
showOne n todos 
    -- Verifica si el índice es válido (mayor o igual a 0 y menor que la longitud de la lista)
    | n < 0 || n >= length todos = Nothing -- Corregido el rango para 0-basado
    | otherwise                  = Just (todos !! n) -- Accede al elemento por índice
```

**Nota**: Se introdujo readMaybe para una lectura más segura del índice, evitando fallos si la entrada no es un número. También se corrigió la verificación del índice en showOne para que sea n >= length todos, que es el rango correcto para índices 0-basados.

Ahora puedes añadir tareas (`+ ...`), listarlas (`l`), eliminarlas por su número (`- 0`, `- 1`, etc.) y mostrarlas individualmente (`s 0`, `s 1`, etc.).

#### 4. Limpiar tareas (`c`)

Añadir la funcionalidad para limpiar toda la lista es simple.

a. **Actualizar `src/Crud.hs`**: Añadimos el caso c a la función interpret.

```haskell
module Crud
    ( 
        prompt,
    ) where

import Data.List 
import Text.Read (readMaybe) 

putTodo :: (Int, String) -> IO ()
putTodo (n, todo) = putStrLn (show n ++ ": " ++ todo)

prompt :: [String] -> IO ()
prompt todos = do
    putStrLn ""
    putStrLn "Commands: + <task>, - <num>, s <num>, l, c, q" -- Actualizamos el mensaje de ayuda
    command <- getLine
    interpret command todos

interpret :: String -> [String] -> IO ()

interpret ('+':' ':todo) todos = do
    putStrLn $ "Adding task: " ++ todo
    prompt (todo:todos) 

interpret ('-':' ':numStr) todos = do
    case readMaybe numStr of 
        Nothing -> do
            putStrLn "Error: Index must be a valid number."
            prompt todos
        Just num -> do
            case deleteOne num todos of
                Nothing -> do
                    putStrLn "Error: There's no task with that number."
                    prompt todos
                Just todos' -> do
                    putStrLn $ "Task " ++ numStr ++ " deleted."
                    prompt todos'

interpret ('s':' ':numStr) todos = do
     case readMaybe numStr of
        Nothing -> do
            putStrLn "Error: Index must be a valid number."
            prompt todos
        Just num -> do
            case showOne num todos of
                Nothing -> do
                    putStrLn "Error: There's no task with that number."
                    prompt todos
                Just todo -> do
                    putStrLn $ "Task " ++ show num ++ ": " ++ todo
                    prompt todos

interpret  "l"           todos = do
    let numberOfTodos = length todos
    putStrLn ""
    print $ show numberOfTodos ++ " in total"
    mapM_ putTodo (zip [0..] todos)
    prompt todos

-- Comando 'c' para limpiar la lista de TODOs
interpret  "c"           todos = do
    putStrLn "Clear todo list."
    prompt [] -- Simplemente llama a prompt con una lista vacía

interpret  "q"           todos = return ()

interpret  command       todos = do
    putStrLn ("Invalid command: `" ++ command ++ "`")
    prompt todos

deleteOne :: Int -> [a] -> Maybe [a]
deleteOne 0 (_:as) = Just as 
deleteOne n (a:as) 
    | n < 0     = Nothing
    | otherwise = do
        as' <- deleteOne (n - 1) as
        return (a:as')
deleteOne _  []    = Nothing

showOne :: Int -> [a] -> Maybe a
showOne n todos 
    | n < 0 || n >= length todos = Nothing
    | otherwise                  = Just (todos !! n) 

-- Funciones para edición (se añadirán en el siguiente paso)
-- editIndex :: Int -> a -> [a] -> [a]    
-- editOne :: Int -> [a] -> String -> Maybe a 
-- editTodo :: String -> [String] -> String -> IO ()
```

Ahora el comando c limpiará la lista.

#### 5. Editar tareas (`e`)

La edición es el comando más complejo, ya que requiere un índice y *otra* línea de entrada con el nuevo contenido. Implementaremos las funciones auxiliares `editIndex`, `editOne` y la función principal de edición `editTodo`. La función `prompt` necesitará manejar el comando `e` de manera especial para solicitar el segundo input antes de llamar a `editTodo`.

a. **Actualizar `src/Crud.hs`**: Añadimos `editIndex`, `editOne`, `editTodo` y modificamos `prompt` para manejar el comando `e`. Este será el código final de `Crud.hs` que proporcionaste.

```haskell
module Crud
    ( 
        prompt,
        editIndex, -- Exportamos editIndex para poder probarla
    ) where

import Data.List
import Text.Read (readMaybe) -- Usamos readMaybe para lectura segura de Int
-- import Data.Char (digitToInt) -- Comentado, no usado

putTodo :: (Int, String) -> IO ()
putTodo (n, todo) = putStrLn (show n ++ ": " ++ todo)

prompt :: [String] -> IO ()
prompt todos = do
    putStrLn ""
    -- Mensaje de ayuda con todos los comandos, incluyendo 'e'
    putStrLn "Test todo with Haskell. You can use +(create), -(delete), s(show), e(dit), l(ist), c(lear), q(uit) commands."
    
    command <- getLine

    -- **Manejo especial del comando 'e' en prompt**
    -- Si el comando empieza con 'e', solicitamos la nueva tarea ANTES de procesar
    if "e" `isPrefixOf` command
        then do
            putStrLn "What is the new todo for that?"
            newTodo <- getLine -- Leemos la segunda línea con el nuevo contenido
            editTodo command todos newTodo -- Llamamos a la función específica de edición
        else 
            -- Para todos los demás comandos, delegamos en 'interpret'
            interpret command todos

-- Función que interpreta los comandos de usuario (excepto 'e')
interpret :: String -> [String] -> IO ()

interpret ('+':' ':todo) todos = do
    -- putStrLn $ "Añadiendo tarea: " ++ todo -- Mensaje de confirmación opcional
    prompt (todo:todos) 

interpret ('-':' ':numStr) todos = do
    case readMaybe numStr of 
        Nothing -> do
            putStrLn "Error: Index must be a valid number."
            prompt todos
        Just num -> do
            case deleteOne num todos of
                Nothing -> do
                    putStrLn "Error: There's no task with that number."
                    prompt todos
                Just todos' -> do
                    putStrLn $ "Task " ++ numStr ++ " deleted."
                    prompt todos'

interpret ('s':' ':numStr) todos = do
     case readMaybe numStr of
        Nothing -> do
            putStrLn "Error: Index must be a valid number."
            prompt todos
        Just num -> do
            case showOne num todos of
                Nothing -> do
                    putStrLn "Error: There's no task with that number."
                    prompt todos
                Just todo -> do
                    -- print $ numStr ++ ". " ++ todo -- Formato original
                    putStrLn $ "Task " ++ show num ++ ": " ++ todo -- Formato consistente
                    prompt todos

interpret  "l"           todos = do
    let numberOfTodos = length todos
    putStrLn ""
    print $ show numberOfTodos ++ " in total"
    mapM_ putTodo (zip [0..] todos)
    prompt todos

interpret  "c"           todos = do
    putStrLn "Clear todo list." -- Mensaje original
    prompt []

interpret  "q"           todos = return ()

interpret  command       todos = do
    putStrLn ("Invalid command: `" ++ command ++ "`") -- Mensaje original
    prompt todos

-- Funciones auxiliares de manipulación de lista
deleteOne :: Int -> [a] -> Maybe [a]
deleteOne 0 (_:as) = Just as
deleteOne n (a:as) 
    | n < 0     = Nothing
    | otherwise = do
        as' <- deleteOne (n - 1) as
        return (a:as')
deleteOne _  []    = Nothing

showOne :: Int -> [a] -> Maybe a
showOne n todos 
    | n < 0 || n >= length todos = Nothing -- Índice fuera de rango o lista vacía. Corregido >=
    | otherwise                  = Just (todos !! n) 

-- Función pura para reemplazar un elemento en un índice específico
editIndex :: Int -> a -> [a] -> [a]    
editIndex i x xs = take i xs ++ [x] ++ drop (i+1) xs

-- Función que maneja la lógica del comando 'e'
-- Recibe el comando (para extraer el índice), la lista actual y el nuevo contenido
editTodo :: String -> [String] -> String -> IO ()
-- Pattern matching para extraer el número del comando 'e <num>'
editTodo ('e':' ':numStr) todos newTodo = do
    case readMaybe numStr of -- Intenta leer el número de índice
        Nothing -> do
            putStrLn "Error: Index to edit must be a valid number."
            prompt todos
        Just index -> do
            -- Verifica si el índice es válido usando editOne (o showOne, son similares)
            case editOne index todos newTodo of -- newTodo no se usa en editOne, solo verifica índice
                Nothing -> do
                    putStrLn "Error: There's no task with that number to edit."
                    prompt todos
                Just oldTodoContent -> do -- oldTodoContent es el contenido antiguo del TODO
                    putStrLn ""
                    print $ "Old todo is " ++ oldTodoContent
                    print $ "New todo is " ++ newTodo

                    -- Realiza la edición usando la función pura editIndex
                    let newTodos = editIndex index newTodo todos 

                    -- Muestra la lista actualizada
                    let numberOfTodos = length newTodos
                    putStrLn ""
                    print $ show numberOfTodos ++ " in total"
                    mapM_ putTodo (zip [0..] newTodos)

                    -- Continúa el bucle con la lista modificada
                    prompt newTodos
-- Si el comando 'e' no tiene el formato esperado ('e <num>'), se considera inválido
editTodo command todos newTodo = do -- Este caso maneja formatos incorrectos de 'e'
    putStrLn ("Invalid edit command format: `" ++ command ++ "`") 
    prompt todos

-- Función auxiliar para verificar la validez de un índice (similar a showOne)
-- **Nota:** El parámetro 'newTodo' no se utiliza en esta función.
editOne :: Int -> [a] -> String -> Maybe a 
editOne n todos newTodo = do 
    if (n < 0) || (n >= length todos) -- Corregido >=
        then Nothing
        else Just (todos !! n) -- Devuelve el contenido antiguo del TODO
```

**Notas**: La función `prompt` ahora usa `isPrefixOf "e"` para detectar el comando de edición y bifurcar la lógica, solicitando la segunda línea de entrada antes de llamar a `editTodo`. La función `editTodo` usa `readMaybe` para parsear el índice y luego llama a la función pura `editIndex` para modificar la lista. La función `editOne` (que es funcionalmente idéntica a `showOne` para verificar si un índice existe) se usa para comprobar la validez del índice antes de intentar la edición. Se ha corregido la condición de rango en `showOne` y editOne para usar >= en lugar de > para el límite superior.

#### 6. Finalización y pruebas

Con la lógica principal completa en `Crud.hs`, el archivo `Main.hs` ya es funcional (es el del Paso 1, pero llamando a la versión final de `prompt`). Solo necesitamos asegurarnos de que importa correctamente `prompt` (y `editIndex` si queremos probarla). También actualizaremos el archivo de pruebas `test/Spec.hs`.

a. **Confirmar `app/Main.hs`**: El código final de `Main.hs` es simple y ya lo teníamos listo.

```haskell
import Crud (prompt) -- Importa la función prompt desde el módulo Crud

main :: IO ()
main = do
    -- Muestra la lista de comandos disponibles al iniciar
    putStrLn "Commands:"
    putStrLn "+ <String> - Add a TODO entry"
    putStrLn "- <Int>    - Delete the numbered entry"
    putStrLn "s <Int>    - Show the numbered entry"
    putStrLn "e <Int>    - Edit the numbered entry" -- Corregido 'te' a 'the'
    putStrLn "l          - List todo"
    putStrLn "c          - Clear todo"
    putStrLn "q          - Quit"
    -- Inicia el bucle de interacción con una lista de TODOs vacía
    prompt [] -- Start with the empty todo list.
```

**Nota**: Nota: Se corrigió una errata en el mensaje de ayuda (te por the).

b. **Actualizar `test/Spec.hs`**: Escribimos una prueba simple para la función editIndex, ya que es una función pura y fácil de probar unitariamente.

```haskell
-- $stack test
-- Use quickcheck later?

import Crud (editIndex) -- Importa la función editIndex del módulo Crud

import Control.Exception (assert) -- Para usar la función assert
import Data.List (intercalate)    -- Para unir elementos de lista con un separador

main :: IO ()
main = do
    putStrLn "Running tests for editIndex..."
    -- Prueba 1: Editar el primer elemento
    let todos1 = ["Read", "Haskell", "test"]
    let newTodo1 = "Write"
    let expectedTodos1 = ["Write", "Haskell", "test"]
    let actualTodos1 = editIndex 0 newTodo1 todos1
    assert (actualTodos1 == expectedTodos1) (putStrLn "Test 1 passed: Edit first element")

    -- Prueba 2: Editar un elemento intermedio
    let todos2 = ["Read", "Haskell", "test"]
    let newTodo2 = "Programming"
    let expectedTodos2 = ["Read", "Programming", "test"]
    let actualTodos2 = editIndex 1 newTodo2 todos2
    assert (actualTodos2 == expectedTodos2) (putStrLn "Test 2 passed: Edit middle element")

    -- Prueba 3: Editar el último elemento
    let todos3 = ["Read", "Haskell", "test"]
    let newTodo3 = "Done"
    let expectedTodos3 = ["Read", "Haskell", "Done"]
    let actualTodos3 = editIndex 2 newTodo3 todos3
    assert (actualTodos3 == expectedTodos3) (putStrLn "Test 3 passed: Edit last element")

    -- Prueba 4: Editar una lista con un solo elemento
    let todos4 = ["Only one"]
    let newTodo4 = "Edited one"
    let expectedTodos4 = ["Edited one"]
    let actualTodos4 = editIndex 0 newTodo4 todos4
    assert (actualTodos4 == expectedTodos4) (putStrLn "Test 4 passed: Edit single element list")

    putStrLn "All editIndex tests completed."

-- Las líneas comentadas originales (ej. assert con print) se han reemplazado por pruebas más estructuradas.
-- print $ assert (head newTodos == newTodo) (print $ intercalate " " newTodos) -- Original comentada
-- print $ assert (newList == ["Haskell", "learner"]) True -- Original comentada

-- La definición comentada de editIndex también se ha eliminado, ya que está en Crud.hs
-- editIndex :: Int -> a -> [a] -> [a]    -- Original comentada
-- editIndex i x xs = take i xs ++ [x] ++ drop (i+1) xs -- Original comentada
```

**Nota**: Se han añadido varias pruebas simples para `editIndex` para demostrar cómo se puede probar esta función pura.

Ahora tienes todos los componentes de la aplicación implementados y la configuración de pruebas lista.

### Compilación y ejecución

Para compilar la aplicación con los cambios realizados, ejecute el siguiente comando en la raíz del proyecto:

```bash
stack build
```

Si la compilación es exitosa, podrá ejecutar la aplicación con:

```bash
stack exec TODO-exe
```

Alternativamente, puede usar `stack run` para compilar y ejecutar en un solo paso:

```bash
stack run
```

La aplicación se iniciará y mostrará los comandos disponibles. Podrá interactuar con ella introduciendo los comandos implementados.

### Ejecución de pruebas

Para ejecutar el conjunto de pruebas definido en `test/Spec.hs`, utilice el comando:

```bash
stack test
```

Stack compilará el código de prueba y ejecutará el programa `Spec.hs`. La salida indicará si las pruebas pasaron o fallaron.

## Conclusión

Haskell es un lenguaje de programación funcional poderoso y versátil, pero muy "alienígena" para alguien como yo que está acostumbrado a lenguajes de programación imperativos como C, JavaScript, Python, etc. Fue difícil adaptarse a la forma de pensar funcional, pero al final, gracias a mi perseverancia (y la IA) pude completar la práctica. Aprendí a usar Stack, a crear un proyecto básico y a implementar una aplicación de lista de tareas simple.

Probablemente no vuelva a usar Haskell en el futuro, pero al menos fue parcialmente interesante, y supongo que es bueno tener un poco de conocimiento sobre lenguajes funcionales.

[Regresar al inicio](#tabla-de-contenido)
