# Quando você digita import nome, o Python procura um arquivo chamado nome.py em dois lugares principais:
# Na mesma pasta onde o seu script atual está rodando.
# Na pasta Lib onde o próprio Python está instalado no seu computador.

# Nunca crie um arquivo seu com o mesmo nome de uma biblioteca padrão (ex: não crie um time.py). 
# Se fizer isso, vai importar o seu arquivo em vez da biblioteca oficial e seu código vai quebrar.

# Erro "ModuleNotFoundError" - Se você tentar importar algo que não existe nesses dois lugares (ex: import isas),
#  ele avisa que não encontrou o módulo, significa que você precisa instalar a biblioteca
#  ou garantir que o arquivo .py está na mesma pasta.

# Diferentes Formas de Importar:
# Criamos arquivo fictício chamado senha.py que contém uma variável minha_senha e uma função verificar_senha(). 

# Importação Padrão:
# Carrega o arquivo inteiro. Você é obrigado a usar o nome do módulo como prefixo para acessar qualquer coisa lá de dentro.

# Exemplo:

# Precisa usar o prefixo "senha."

 print(senha.minha_senha) 
senha.verificar_senha("123456")

# Importação Específica: 
# Traz apenas itens específicos (uma variável, uma função ou uma classe) direto para o seu código. Você não precisa usar o prefixo.

# Exemplo:

print(minha_senha)
verificar_senha("123456")

# Importação Global (Evite!): 
# Importa absolutamente tudo que está dentro do arquivo para o seu código, sem precisar de prefixo.

# Se o arquivo senha.py tiver uma variável nome e você já tiver uma variável nome no seu script, uma vai esmagar a outra silenciosamente. 

