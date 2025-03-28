# meu-projeto-python

 calculador python
 
Abra o terminal.
Navegue até o diretório onde o arquivo calculadora.py está localizado usando o comando: cd meus_projetos_python
Execute o script com o comando ./calculadora.py

Documentação do Código
Loop Infinito (while True):
O loop while True inicia um ciclo que continuará a executar até que o usuário decida sair do programa. Isso permite que o usuário realize várias operações sem precisar reiniciar o programa.

Exibição do Menu:
O menu de operações é exibido ao usuário, apresentando as opções disponíveis: soma, subtração, multiplicação, divisão e sair. O usuário é solicitado a escolher uma operação digitando o número correspondente.

Recebendo a Escolha do Usuário:
A escolha do usuário é capturada através da função input(), que lê a entrada do usuário como uma string.

Verificação de Saída:
Se o usuário digitar '5', uma mensagem de despedida é exibida e o comando break é utilizado para sair do loop, encerrando o programa.

Validação da Escolha:
O código verifica se a escolha do usuário está entre '1' e '4', que são as opções válidas para operações matemáticas. Se a escolha não for válida, uma mensagem de erro é exibida.

Solicitação de Números:
Se a escolha for válida, o programa solicita ao usuário que insira dois números, que são convertidos de string para inteiro usando int().

Execução da Operação:
Dependendo da escolha do usuário, a operação correspondente é realizada:
Soma: Se a escolha for '1', a soma dos dois números é calculada e exibida.
Subtração: Se a escolha for '2', a subtração é realizada e o resultado é exibido.
Multiplicação: Se a escolha for '3', a multiplicação é realizada e o resultado é exibido.
Divisão: Se a escolha for '4', o programa verifica se o segundo número (divisor) é diferente de zero para evitar a divisão por zero. Se for válido, a divisão é realizada e o resultado é exibido; caso contrário, uma mensagem de erro é exibida.

Tratamento de Escolha Inválida:
Se a escolha do usuário não estiver entre '1' e '4', uma mensagem de erro é exibida, solicitando que o usuário tente novamente.
Essa estrutura permite que o usuário interaja com a calculadora de forma intuitiva e segura, garantindo que operações inválidas sejam tratadas adequadamente.
