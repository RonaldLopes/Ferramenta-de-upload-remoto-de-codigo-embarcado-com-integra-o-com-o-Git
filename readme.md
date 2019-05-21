#  Ferramenta de upload remoto de codigo embarcado com integração com o Git
Essa solução serve para realizar o upload remoto de código embarcado, integrando o Platformio com o Git. A ferramenta funciona de forma a buscar atualizações em um determinado repositório no git e caso tenha alguma altualização, o upload do codigo é feito no dispositivo embarcado conforma as especificações existentes no arquivo "platformio.ini".

#Instalação de dependências
Para executar essa ferramenta é necessário instalar o PlatformIO Core (CLI), atraves do comando:

```
sudo pip install -U platformio

```
As demais dependencias podem ser encontradas no arquivo "requirements.txt", instale com o comando:

```
pip install requirements.txt

```
#Iniciando a ferramenta
Para iniciar a ferramenta utilize o seguinte comando:
```
python plytformio.py https://github.com/RonaldLopes/Ferramenta-de-upload-remoto-de-codigo-embarcado-com-integra-o-com-o-Git 1

```
O primeiro argumento é o link do projeto no github ou gitlab, o segundo é o tempo de atualização em minutos. Note que ao iniciar vai pedir seu usuário e senha do git.
