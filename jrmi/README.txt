
!!!!!!!!!!!!!!! dependencias do jrmi !!!!!!!!!!!!!!!!!!

$ java --version
openjdk 20.0.1 2023-04-18
OpenJDK Runtime Environment (Red_Hat-20.0.1.0.9-2.rolling.fc37) (build 20.0.1+9)
OpenJDK 64-Bit Server VM (Red_Hat-20.0.1.0.9-2.rolling.fc37) (build 20.0.1+9, mixed mode, sharing)

-------------------------
Passo 1:
    Compile os arquivos

    vá na pasta servidor e rode o comando:
    $ javac *.java

    vá para pasta cliente e rode o comando
    $ javac *.java

Passo 2:   

    Abra 2 terminais (O ip configurado no cliente é o localhost. Há um comentario indicando onde fazer a mudança de IP, se desejar, necessário recompilar, caso mude o IP)

    No terminal 1 inicie o servidor

    $ java ServidorRMI

    No terminal 2 inicie o cliente:

    *Cliente interativo
    $ java ClienteRMI

    *Cliente que gera arquivos com os tempos de execução (tempos em segundos)

    $ java ClienteRMI_Gera_txt
