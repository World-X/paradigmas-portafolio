+++
date = '2025-03-08T20:24:30-08:00'
draft = false
title = 'Práctica 0'
+++

## Markdown

Markdown es un lenguaje de marcado que *facilita la aplicación de formato* a un texto empleando una serie de caracteres de una forma especial. En principio, fue pensado para elaborar textos cuyo destino iba a ser la web con más rapidez y sencillez que si estuviésemos empleando directamente HTML. Y si bien ese suele ser el mejor uso que podemos darle, también podemos emplearlo para cualquier tipo de texto, independientemente de cual vaya a ser su destino. - [Fuente](https://www.genbeta.com/guia-de-inicio/que-es-markdown-para-que-sirve-y-como-usarlo)

### Encabezados

Los encabezados se crean anteponiendo uno o varios símbolos de almohadilla (#) al texto que queremos que sea un encabezado. La cantidad de almohadillas que utilicemos determinará el nivel de jerarquía del encabezado.

### Énfasis

Para aplicar énfasis a una palabra o frase, podemos utilizar uno de los siguientes métodos:

- *cursiva*: se logra encerrando la palabra o frase entre asteriscos o guiones bajos.
  - Ejemplo: \*cursiva\* o \_cursiva\_.
- **negrita**: se logra encerrando la palabra o frase entre dos asteriscos o dos guiones bajos.
  - Ejemplo: \*\*negrita\*\* o \_\_negrita\_\_.
- ***cursiva y negrita***: se logra encerrando la palabra o frase entre tres asteriscos.
  - Ejemplo: \*\*\*cursiva y negrita\*\*\*.
- ~~tachado~~: se logra encerrando la palabra o frase entre dos virgulillas.
  - Ejemplo: \~\~tachado\~\~.
- `código`: se logra encerrando la palabra o frase entre comillas invertidas.
  - Ejemplo: \`código\`.

### Listas

Podemos crear listas ordenadas y no ordenadas. Las listas no ordenadas se crean anteponiendo un guion, un asterisco o un signo de suma al texto que queremos que sea un elemento de la lista. Las listas ordenadas se crean anteponiendo un número seguido de un punto al texto que queremos que sea un elemento de la lista.

#### No ordenadas

- Elemento 1
- Elemento 2
- Elemento 3

#### Ordenadas

1. Elemento 1
2. Elemento 2
3. Elemento 3

### Enlaces

Podemos crear enlaces de dos formas:

- Enlazando directamente la URL: <https://www.google.com>.
- Enlazando un texto a la URL: [Google](https://www.google.com).

### Imágenes

Podemos insertar imágenes de dos formas:

- Insertando la URL de la imagen:

![Logo de Google](https://www.google.com/images/branding/googlelogo/1x/googlelogo_color_272x92dp.png).

- Insertando la URL de la imagen y enlazándola:

[![Logo de Google](https://www.google.com/images/branding/googlelogo/1x/googlelogo_color_272x92dp.png)](https://www.google.com).

### Citas

Podemos crear citas anteponiendo el signo de mayor que (>) al texto que queremos que sea una cita.

> Markdown es un lenguaje de marcado que *facilita la aplicación de formato* a un texto empleando una serie de caracteres de una forma especial. - [Fuente](https://www.genbeta.com/guia-de-inicio/que-es-markdown-para-que-sirve-y-como-usarlo)

### Líneas horizontales

Podemos crear líneas horizontales utilizando tres guiones, tres asteriscos o tres guiones bajos.

\-\-\-

---

\*\*\*

***

\_\_\_

___

### Código

Podemos insertar bloques de código utilizando tres comillas invertidas.

\`\`\`python

def hola_mundo():\
&nbsp;&nbsp;&nbsp;&nbsp;print('¡Hola, mundo!')

\`\`\`

```python
def hola_mundo():
    print('¡Hola, mundo!')
```

### Tablas

Podemos crear tablas utilizando barras verticales y guiones.

| Encabezado 1 | Encabezado 2 | Encabezado 3 |
|--------------|--------------|--------------|
| Celda 1      | Celda 2      | Celda 3      |
| Celda 4      | Celda 5      | Celda 6      |
| Celda 7      | Celda 8      | Celda 9      |

### Tareas

Podemos crear listas de tareas utilizando corchetes y espacios.

- [x] Tarea 1
- [ ] Tarea 2

## Git y GitHub

Git es un sistema de control de versiones distribuido, lo que significa que un clon local del proyecto es un repositorio de control de versiones completo. Estos repositorios locales plenamente funcionales permiten trabajar sin conexión o de forma remota con facilidad. Los desarrolladores confirman su trabajo localmente y, a continuación, sincronizan la copia del repositorio con la del servidor. - [Fuente](https://learn.microsoft.com/es-es/devops/develop/git/what-is-git)

Github es un portal creado para alojar el código de las aplicaciones de cualquier desarrollador, y que fue comprada por Microsoft [en junio del 2018](https://www.xataka.com/aplicaciones/oficial-microsoft-compra-github-7-500-millones-dolares). La plataforma está creada para que **los desarrolladores suban el código de sus aplicaciones y herramientas**, y que como usuario no sólo puedas descargarte la aplicación, sino también entrar a su perfil para leer sobre ella o colaborar con su desarrollo. - [Fuente](https://www.xataka.com/basics/que-github-que-que-le-ofrece-a-desarrolladores)

### Comandos básicos de Git

#### [git init](https://git-scm.com/docs/git-init)

Inicializa un repositorio de Git en un directorio existente.

```bash
git init
```

Inicializa un repositorio vacío (bare repository).

```bash
git init --bare
```

Inicializa un repositorio compartido por varios desarrolladores.

```bash
git init --shared
```

#### [git add](https://git-scm.com/docs/git-add)

Añade todos los archivos del directorio de trabajo al área de preparación.

```bash
git add .
```

Añade cambios en el directorio de trabajo al área de preparación de forma interactiva.

```bash
git add -p
```

Añade un archivo específico al área de preparación.

```bash
git add <archivo>
```

Añade archivos específicos por extensión o patrón.

```bash
git add *.js
git add src/
```

Añade archivos ignorando los errores de archivo no encontrado.

```bash
git add -A --ignore-errors
```

#### [git commit](https://git-scm.com/docs/git-commit)

Registra los cambios en el repositorio.

```bash
git commit -m "Mensaje del commit"
```

Añade todos los archivos modificados al área de preparación y realiza commit.

```bash
git commit -am "Mensaje del commit"
```

Modifica el último commit (cambios y/o mensaje).

```bash
git commit --amend
```

Crea un commit con fecha y hora específicas.

```bash
git commit --date="YYYY-MM-DD HH:MM:SS" -m "Mensaje"
```

#### [git status](https://git-scm.com/docs/git-status)

Muestra el estado del directorio de trabajo y del área de preparación.

```bash
git status
```

Muestra el estado en formato corto.

```bash
git status -s
```

Muestra el estado en formato corto con información de la rama.

```bash
git status -sb
```

Muestra el estado ignorando archivos sin seguimiento.

```bash
git status --untracked-files=no
```

#### [git log](https://git-scm.com/docs/git-log)

Muestra el historial de confirmaciones.

```bash
git log
```

Muestra el historial en una línea por commit.

```bash
git log --oneline
```

Muestra el historial con un gráfico de ramas.

```bash
git log --graph --oneline --all
```

Muestra el historial con estadísticas de cambios.

```bash
git log --stat
```

Muestra el historial con mensajes más detallados.

```bash
git log -p
```

Limita el número de commits mostrados.

```bash
git log -n 5
```

#### [git push](https://git-scm.com/docs/git-push)

Actualiza referencias remotas junto con los objetos asociados.

```bash
git push
```

Establece la rama remota como upstream y realiza push.

```bash
git push -u origin <rama>
```

Fuerza el push (uso con precaución).

```bash
git push --force
```

Envía todas las etiquetas al repositorio remoto.

```bash
git push --tags
```

Elimina una rama remota.

```bash
git push origin --delete <rama>
```

#### [git pull](https://git-scm.com/docs/git-pull)

Recupera cambios del repositorio remoto.

```bash
git pull
```

Realiza pull con rebase en lugar de merge.

```bash
git pull --rebase
```

Realiza pull desde un repositorio y rama específicos.

```bash
git pull <remoto> <rama>
```

Recupera cambios sin fusionar automáticamente.

```bash
git pull --no-commit
```

#### [git clone](https://git-scm.com/docs/git-clone)

Clona un repositorio en un nuevo directorio.

```bash
git clone <repositorio>
```

Clona un repositorio en un directorio específico.

```bash
git clone <repositorio> <directorio>
```

Clona una rama específica.

```bash
git clone -b <rama> <repositorio>
```

Clona con historia truncada para reducir el tamaño.

```bash
git clone --depth=1 <repositorio>
```

#### [git fetch](https://git-scm.com/docs/git-fetch)

Descarga objetos y referencias de otro repositorio.

```bash
git fetch
```

Descarga desde todos los repositorios remotos.

```bash
git fetch --all
```

Elimina referencias remotas que ya no existen en el origen.

```bash
git fetch --prune
```

Fetch de una rama específica.

```bash
git fetch <remoto> <rama>
```

#### [git merge](https://git-scm.com/docs/git-merge)

Combina dos o más historiales de desarrollo juntos.

```bash
git merge <rama>
```

Realiza merge sin fast-forward (crea un commit de merge).

```bash
git merge --no-ff <rama>
```

Fusiona y combina todos los commits en uno solo.

```bash
git merge --squash <rama>
```

Aborta un merge en progreso con conflictos.

```bash
git merge --abort
```

#### [git branch](https://git-scm.com/docs/git-branch)

Lista, crea o elimina ramas.

```bash
git branch
```

Crea una nueva rama.

```bash
git branch <nueva-rama>
```

Elimina una rama fusionada.

```bash
git branch -d <rama>
```

Elimina una rama forzosamente (incluso si no está fusionada).

```bash
git branch -D <rama>
```

Lista todas las ramas (locales y remotas).

```bash
git branch -a
```

Lista ramas con último commit en cada una.

```bash
git branch -v
```

#### [git checkout](https://git-scm.com/docs/git-checkout)

Cambia ramas o restaura archivos de árboles de trabajo.

```bash
git checkout <rama>
```

Crea y cambia a una nueva rama.

```bash
git checkout -b <nueva-rama>
```

Cambia a la rama anterior.

```bash
git checkout -
```

Descarta cambios en un archivo específico.

```bash
git checkout -- <archivo>
```

Crea una rama a partir de un commit específico.

```bash
git checkout -b <nueva-rama> <commit-sha>
```

#### [git reset](https://git-scm.com/docs/git-reset)

Restablece el HEAD actual a la confirmación especificada.

```bash
git reset
```

Deshace commits pero mantiene los cambios en el área de trabajo.

```bash
git reset --soft HEAD~1
```

Deshace commits y cambios en el área de preparación, pero conserva los archivos.

```bash
git reset --mixed HEAD~1
```

Deshace commits y descarta todos los cambios (peligroso).

```bash
git reset --hard HEAD~1
```

Reset a un commit específico.

```bash
git reset --hard <commit-sha>
```
