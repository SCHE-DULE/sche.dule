# Sistema de Gerenciamento de Consultório de Terapia

O sistema é destinado a auxiliar na administração e organização das atividades do consultório, com diferentes funcionalidades para diferentes cargos.

## Funcionalidades do Cargo: Recepcionista

### Adicionar Cliente

- Tela de cadastro de cliente com os seguintes campos:
  - Nome conforme documento
  - Data de aniversário
  - Celular
  - Gênero
  - CPF com validação de dígitos
  - RG com validação de dígitos
  - País (lista)
  - Estado (lista)
  - Cidade (lista)
  - Bairro
  - Endereço
  - Número
  - Complemento
  - Observação
- Possibilidade de salvar a foto do cliente

### Funções Adicionais

- Marcar horários dos clientes com cada terapeuta já cadastrado.
- Marcar como pago a consulta ou se é pacote de 5 ou de 10
- Filtrar dados do banco de dados (provavelmente PostgreSQL) por Data, Nome, Hora, Terapeuta (sem poder alterar dados)

## Funcionalidades do Cargo: Terapeuta

### Tela de Cadastro do Terapeuta

- Nome
- Especialidades
- Cadastro do órgão de registro (ex: CRM)
- Dias disponíveis
- Horário de consulta
- Valor cobrado
- Taxa administrativa de cada terapeuta (visível somente pelo gerente/administrador)
- Imagem do Terapeuta
- Anexo do contrato com o terapeuta

### Funções Adicionais

- Visualização de horários marcados
- Possibilidade de fechar horários da própria agenda (por motivos pessoais ou qualquer motivo que queira)
- Visualização do próprio contrato (talvez)

## Tipos de perfil

### Recepcionista(o)

- Adicionar cliente
- Marcar horário dos clientes com cada Terapeuta (cliente) já cadastrado.
- Marcar como pago a consulta ou se é pacote de 5 ou de 10
- Filtrar dados do banco de dados (provavelmente PostgreSQL): Data, Nome, Hora, Terapeuta (sem poder alterar dados)

### Terapeuta

- Visualização de horários marcados
- Possibilidade de fechar horários da própria agenda (por motivos pessoais ou qualquer motivo que queira)
- Visualização do próprio contrato (talvez)

### Gerente

- Função de gerenciar Recepcionistas em horário de trabalho
- Realizar alterações no cadastro de pacientes (tarefas específicas de cada empresa)

### Gerente Geral

- Realizar admissão de tarefas novas para o Gerente e Recepcionistas com aprovação do Administrador
- Realização da contabilidade
- Contato do Contador
- Contato dos Fornecedores

### Administrador

- Realizar alterações em quaisquer problemas relacionados a todos os cargos anteriores
- Cadastro de Terapeutas
- Possibilidade de delegar tarefas que julgar necessárias para cada um dos cargos
- Conferência de todas as funções anteriores

### Super User

- Gerenciar e adicionar novas funcionalidades, adaptando o sistema de acordo com as necessidades específicas do consultório.
