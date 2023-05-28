# bitproject
Monitoramento de Uso de CPU e Mineração de Bitcoin
Este projeto em Python consiste em um aplicativo web que monitora o uso da CPU do computador e simula o processo de mineração de Bitcoin. Ele exibe o valor atual do uso da CPU em porcentagem e o número de bits calculados com base nesse valor.

Pré-requisitos
Certifique-se de ter os seguintes requisitos instalados:

Python 3.x
Flask
Psutil
Instalação
Clone o repositório para o seu ambiente local.
Abra o terminal e navegue até o diretório do projeto.
Crie um ambiente virtual (opcional, mas recomendado): python -m venv venv.
Ative o ambiente virtual: source venv/bin/activate (Linux/Mac) ou venv\Scripts\activate (Windows).
Instale as dependências: pip install -r requirements.txt.
Uso
Execute o aplicativo Flask: python app.py.
Acesse o aplicativo no seu navegador: http://localhost:5000.
O valor atual do uso da CPU e o número de bits calculados serão exibidos na página.
Os valores serão atualizados a cada segundo.
Personalização
Você pode personalizar o aplicativo de acordo com suas necessidades:

Para personalizar a aparência da página HTML, você pode modificar o arquivo templates/index.html.
Para ajustar a frequência de atualização dos valores, você pode alterar o valor do intervalo de tempo no código JavaScript no arquivo templates/index.html.
Para incorporar informações relacionadas ao Bitcoin, como preço e número de blocos minerados, você pode utilizar uma API de criptomoedas e atualizar os dados no lado do servidor.
Contribuição
Contribuições são bem-vindas! Sinta-se à vontade para enviar pull requests com melhorias, correções de bugs ou novos recursos.

Licença
Este projeto está licenciado sob a Licença MIT.

Contato
Para mais informações ou dúvidas, entre em contato com (https://www.linkedin.com/in/lierson-de-paula-rodrigues-86408133/).
