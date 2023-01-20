# clinica

## passo 1: crie uma pasta para guardar o projeto e navegue para dentro dela:

```
mkdir clinica
```

```
cd clinica
```
## passo 2: faça clonagem do meu repositório git:

```
git clone https://github.com/Carlos-Eduardo-Guedes-01/clinica
```

## passo 3: crie e ative seu ambiente virtual:
Linux

```
virtualenv venv
```

```
source venv/bin/activate
```

Windows

```
python -m venv venv
```

```
venv\Script\activate
```

## Passo 4: Após isso, faremos a instalação dos pacotes necessários:

```
pip install -r requeriments.txt
```

## Passo 5: Agora faça as instalações das aplicações django

```
python manage.py migrate
```

## Passo 6: Agora podemos fazer o passo final, iniciar o servidor:

```
python manage.py runserver
```
