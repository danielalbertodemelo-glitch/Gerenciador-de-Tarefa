# Gerenciador-de-Tarefa

As tarefas são criadas com o estado **Pendente** e aparecem assim na listagem.

Se `tarefas.json` estiver vazio, com JSON inválido ou com problemas de codificação, o programa informa o problema e termina sem alterar o ficheiro, para evitar perder tarefas. As gravações são feitas através de um ficheiro temporário antes de substituir o ficheiro de tarefas.

Ao adicionar uma tarefa, escolha um dia da semana e indique se é permanente. A opção **Ver tarefas de um dia** mostra apenas as tarefas associadas ao dia escolhido e identifica as permanentes. A marca de permanência não repete nem cria tarefas automaticamente. Tarefas guardadas em versões anteriores sem dia continuam preservadas e aparecem como **Dia não definido** na listagem geral.