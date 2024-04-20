# Bot Intelbras

O Bot Intelbras é uma ferramenta desenvolvida para monitorar e detectar tentativas de acesso não autorizado a serviços de biometria dentro da plataforma InControl. Ele automatiza o processo de detecção de alertas e notifica o administrador por e-mail sempre que uma atividade é identificada.

## Funcionalidades

- Captura de alertas dentro da plataforma InControl.
- Detecção de tentativas de acesso a serviços de biometria.
- Notificação por e-mail ao administrador com detalhes da atividade, incluindo o nome do usuário e o serviço acessado.

## Como funciona

O Bot Intelbras opera de maneira simples e eficiente:

1. **Captura de Alertas**: O programa é configurado para monitorar continuamente a plataforma InControl em busca de alertas.
2. **Detecção de Atividade Suspeita**: Quando um alerta indicando tentativa de acesso a serviços de biometria é identificado, o Bot Intelbras inicia o processo de notificação.
3. **Notificação por E-mail**: O administrador designado recebe uma notificação por e-mail contendo informações detalhadas sobre a atividade suspeita, incluindo o nome do usuário e o serviço acessado.

## Configuração

Para configurar o Bot Intelbras, siga estas etapas simples:

1. **Faça o download da pasta**: Faça o download da pasta e adicione no seu servidor onde o InControl está localizado.
2. **Configure um e-mail**: Certifique-se de ter um e-mail pré configurado com SMTP para que o programa rode.
3. **Execute o Bot**: Execute o BOT dentro da pasta `DIST`.
4. **Preencha as informações necessárias**: Adicione todas as informações solicitadas, caso queira adicionar mais de um usuário alerta, use o separador por vírgulas, por exemplo "João Luis, André, Bruno".
5. **E pronto :D**: Deixe tudo rodar automaticamente.

## Contribuição

Contribuições são bem-vindas! Se você tiver sugestões de melhorias, novas funcionalidades ou encontrar problemas, sinta-se à vontade para abrir uma issue ou enviar um pull request.

## Licença

Este projeto está licenciado sob a [MIT License](LICENSE).
