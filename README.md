# Twitter-Wake-Up-Bot
**EN |** A python bot that will post a tweet if you don't wake up on time
**ES |** Un bot de python que publica un tweet si no te despiertas a tiempo

**EN |** At the time of making this project I have been trying to wake up early by setting alarms in my phone and such. But it never seems to be enough because there is no actual consequence if I don't do it.

So what better way to fix this problem than public humilliation? If I don't get out of bed at a set time and introduce a deactivation word within a time limit *(30 seconds by default)*, this bot will tweet in my personal account that I didn't wake up and how many times the same has happened.

This is my first project that doesn't come from a tutorial, which means I have officially escaped tutorial hell.

**ES |** Al momento de hacer este projecto he estado intentando despertarme temprano poniendo alarmas en mi teléfono y cosas así. Pero nunca parece ser suficiente porque no hay ninguna consecuencia real si no lo hago.

Entonces qué mejor manera de arreglar este problema que la humillación pública? Si no me levanto de la cama a una cierta hora e introduzco una palabra de desactivación dentro de un límite de tiempo *(30 segundos por defecto)*, este bot "twiteará" en mi cuenta personal que no me desperté y cuántas veces ha pasado lo mismo.

Este es mi primer proyecto que no viene de un tutorial, lo que significa que oficialmente escapé del infierno de los tutoriales.


### **EN |** Installation

I do not yet posess enough knowledge to make this into a more convenient program to use, so you are not really supposed to use it.

Clone the repository

```shell
git clone <repo_url>
```

Install the requirements

```shell
pip install requirements.txt
```

**WARNING**: `pytimedinput` requires an interactive shell to work, otherwise it will raise a `RuntimeError`. Like I said, I don't know how to make this into a program that doesn't have this constraint.

You will need to create an X developer account to be able to use the API. You can follow this tutorial to do so:

[X Docs](https://docs.x.com/fundamentals/developer-portal#getting-started)

In `tokens_and_keys.py` you will need to include at least the following credentials to be able to post tweets:

```python
consumer_key=""
consumer_key_secret=""
access_token=""
access_token_secret=""
```


### Usage

The program is made in spanish. You have to run it directly in your terminal.

Windows

```shell
python main.py
```

Linux | MacOS

```shell
python3 main.py
```

When the set wake up time arrives, you will be prompted to introduce the deactivation word. You have 30 seconds by default to do so or the bot will post the tweet. If you do it on time it will just reset.

**TODOS:**
- Add configuration file
- Fix the printing bug after time runs out


### **ES |** Instalación

Todavía no poseo el conocimiento para hacer que este programa sea más conveniente de usar, así que realmente no se supone que lo uses. 

Clona el repositorio

```shell
git clone <repo_url>
```

Instala los requerimientos

```shell
pip install requirements.txt
```

**ADVERTENCIA**: `pytimedinput` requiere una terminal interactiva para funcionar, de otra manera arroja un `RuntimeError`. Como dije, no sé cómo convertir esto en un programa que no tenga esa restricción.

Vas a necesitar crear una cuenta de desarrollador de X para poder usar la API. Puedes seguir este tutorial para hacerlo:

[Docs de X](https://docs-x-com.translate.goog/fundamentals/developer-portal?_x_tr_sl=en&_x_tr_tl=es&_x_tr_hl=es&_x_tr_pto=tc#getting-started)

En `tokens_and_keys.py` necesitas incluir por lo menos las siguientes credenciales para poder publicar tweets:

```python
consumer_key=""
consumer_key_secret=""
access_token=""
access_token_secret=""
```


### Uso

El programa está hecho en español. Debes ejecutarlo directamente en tu terminal

Windows

```shell
python main.py
```

Linux | MacOS

```shell
python3 main.py
```

Cuanto la hora de despertarse llegue, se te pedirá introducir la palabra de desactivación. Tienes 30 segundos por defecto para hacerlo o el bot publicará el tweet. Si la introduces a tiempo solo se reiniciará.

**POR HACER:**
- Agregar archivo de configuración
- Arreglar el bug de impresión cuando se acaba el tiempo
