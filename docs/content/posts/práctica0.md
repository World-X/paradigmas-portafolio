+++
date = '2025-03-08T20:24:30-08:00'
draft = false
title = 'Práctica 0'
+++

## Tabla de contenido

- [Markdown](#markdown)
  - [Encabezados](#encabezados)
  - [Énfasis](#énfasis)
  - [Listas](#listas)
    - [No ordenadas](#no-ordenadas)
    - [Ordenadas](#ordenadas)
  - [Enlaces](#enlaces)
  - [Imágenes](#imágenes)
  - [Citas](#citas)
  - [Líneas horizontales](#líneas-horizontales)
  - [Código](#código)
  - [Tablas](#tablas)
  - [Tareas](#tareas)
- [Git y GitHub](#git-y-github)
  - [Comandos básicos de Git](#comandos-básicos-de-git)
    - [git init](#git-init)
    - [git add](#git-add)
    - [git commit](#git-commit)
    - [git status](#git-status)
    - [git log](#git-log)
    - [git push](#git-push)
    - [git pull](#git-pull)
    - [git clone](#git-clone)
    - [git fetch](#git-fetch)
    - [git merge](#git-merge)
    - [git branch](#git-branch)
    - [git checkout](#git-checkout)
    - [git reset](#git-reset)
- [Hugo](#hugo)
  - [Instalación](#instalación)
  - [Creación de un sitio](#creación-de-un-sitio)
  - [Creación de contenido](#creación-de-contenido)
  - [Publicación (con GitHub Pages)](#publicación-con-github-pages)

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

## Hugo

Hugo es un generador de sitios web estáticos rápido, libre y escrito en Go.

### Instalación

Para instalar Hugo, debemos seguir los siguientes pasos:

1. Descargar el archivo binario de la [página oficial](https://gohugo.io/getting-started/installing/).
2. Descomprimir el archivo en una carpeta de tu preferencia.
3. Añadir la carpeta al PATH del sistema.
4. Verificar la instalación con el comando `hugo version`.

### Creación de un sitio

1. Crear un nuevo sitio con el comando `hugo new site [nombre]`, donde `[nombre]` es el nombre de tu sitio.
2. Moverte al directorio del sitio con `cd [nombre]`.
3. Iniciar control de versiones con `git init`.
4. Añadir un tema con `git submodule add [URL] themes/[nombre]`, donde `[URL]` es la URL del tema y `[nombre]` es el nombre del tema.
   - Ejemplo: `git submodule add https://github.com/theNewDynamic/gohugo-theme-ananke.git themes/ananke`.
5. Añadir el tema al archivo de configuración `config.toml`.
   - Ejemplo: `theme = "ananke"`.
6. Correr el servidor local con `hugo server`.

### Creación de contenido

1. Crear una nueva página con `hugo new content content/posts/[nombre].md`, donde `[nombre]` es el nombre de la página.
2. Editar la página con tu editor de texto favorito.

### Publicación (con GitHub Pages)

1. Crear un cuenta en [GitHub](https://github.com/signup).
2. Crear un nuevo repositorio.
3. Publicar el sitio con `git push origin master`.
4. Habilitar GitHub Pages en la configuración del repositorio.
5. Crea un archivo `hugo.yaml` en `.github/workflows/` con el siguiente contenido:
```yaml
# Sample workflow for building and deploying a Hugo site to GitHub Pages
name: Deploy Hugo site to Pages

on:
  # Runs on pushes targeting the default branch
  push:
    branches:
      - main

  # Allows you to run this workflow manually from the Actions tab
  workflow_dispatch:

# Sets permissions of the GITHUB_TOKEN to allow deployment to GitHub Pages
permissions:
  contents: read
  pages: write
  id-token: write

# Allow only one concurrent deployment, skipping runs queued between the run in-progress and latest queued.
# However, do NOT cancel in-progress runs as we want to allow these production deployments to complete.
concurrency:
  group: "pages"
  cancel-in-progress: false

# Default to bash
defaults:
  run:
    shell: bash

jobs:
  # Build job
  build:
    runs-on: ubuntu-latest
    env:
      HUGO_VERSION: 0.144.2
    steps:
      - name: Install Hugo CLI
        run: |
          wget -O ${{ runner.temp }}/hugo.deb https://github.com/gohugoio/hugo/releases/download/v${HUGO_VERSION}/hugo_extended_${HUGO_VERSION}_linux-amd64.deb \
          && sudo dpkg -i ${{ runner.temp }}/hugo.deb
      - name: Install Dart Sass
        run: sudo snap install dart-sass
      - name: Checkout
        uses: actions/checkout@v4
        with:
          submodules: recursive
          fetch-depth: 0
      - name: Setup Pages
        id: pages
        uses: actions/configure-pages@v5
      - name: Install Node.js dependencies
        run: "[[ -f package-lock.json || -f npm-shrinkwrap.json ]] && npm ci || true"
      - name: Build with Hugo
        env:
          HUGO_CACHEDIR: ${{ runner.temp }}/hugo_cache
          HUGO_ENVIRONMENT: production
          TZ: America/Los_Angeles
        run: |
          hugo \
            --gc \
            --minify \
            --baseURL "${{ steps.pages.outputs.base_url }}/"
      - name: Upload artifact
        uses: actions/upload-pages-artifact@v3
        with:
          path: ./public

  # Deployment job
  deploy:
    environment:
      name: github-pages
      url: ${{ steps.deployment.outputs.page_url }}
    runs-on: ubuntu-latest
    needs: build
    steps:
      - name: Deploy to GitHub Pages
        id: deployment
        uses: actions/deploy-pages@v4
```
6. Publica el archivo con `git push origin main`.
7. Verifica que el sitio se haya publicado correctamente.
8. ¡Listo! Tu sitio está en línea.

[Regresar al inicio](#tabla-de-contenido).
