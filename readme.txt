Monitoramento de Uso de CPU e Minera��o de Bitcoin
Este projeto em Python consiste em um aplicativo web que monitora o uso da CPU do computador e simula o processo de minera��o de Bitcoin. Ele exibe o valor atual do uso da CPU em porcentagem e o n�mero de bits calculados com base nesse valor.

Pr�-requisitos
Certifique-se de ter os seguintes requisitos instalados:

Python 3.x
Flask
Psutil
Instala��o
Clone o reposit�rio para o seu ambiente local.
Abra o terminal e navegue at� o diret�rio do projeto.
Crie um ambiente virtual (opcional, mas recomendado): python -m venv venv.
Ative o ambiente virtual: source venv/bin/activate (Linux/Mac) ou venv\Scripts\activate (Windows).
Instale as depend�ncias: pip install -r requirements.txt.
Uso
Execute o aplicativo Flask: python app.py.
Acesse o aplicativo no seu navegador: http://localhost:5000.
O valor atual do uso da CPU e o n�mero de bits calculados ser�o exibidos na p�gina.
Os valores ser�o atualizados a cada segundo.
Personaliza��o
Voc� pode personalizar o aplicativo de acordo com suas necessidades:

Para personalizar a apar�ncia da p�gina HTML, voc� pode modificar o arquivo templates/index.html.
Para ajustar a frequ�ncia de atualiza��o dos valores, voc� pode alterar o valor do intervalo de tempo no c�digo JavaScript no arquivo templates/index.html.
Para incorporar informa��es relacionadas ao Bitcoin, como pre�o e n�mero de blocos minerados, voc� pode utilizar uma API de criptomoedas e atualizar os dados no lado do servidor.
Contribui��o
Contribui��es s�o bem-vindas! Sinta-se � vontade para enviar pull requests com melhorias, corre��es de bugs ou novos recursos.

Licen�a
Este projeto est� licenciado sob a Licen�a MIT.

Contato
Para mais informa��es ou d�vidas, entre em contato com https://www.linkedin.com/in/lierson-de-paula-rodrigues-86408133/.