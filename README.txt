
LEK DO BLACK - BOT BRJOGOS PIX

1. Cria conta grátis em https://render.com
2. Sobe esse ZIP lá (importa via Git ou Upload Manual)
3. Render detecta o Python automaticamente com render.yaml
4. Ele instala os pacotes e inicia a API Flask
5. Acessa: https://teuprojeto.onrender.com/gerar-pix
   => Vai gerar a chave automaticamente com Selenium

INTEGRAÇÃO NO HTML (client):
fetch('https://teuprojeto.onrender.com/gerar-pix')
.then(res => res.json())
.then(data => {
  let chave = data.chave;
  document.querySelector('img[alt="QR Code do Pix"]').src = 
      "https://api.qrserver.com/v1/create-qr-code/?data=" + encodeURIComponent(chave) + "&size=300x300";
  document.getElementById('pix').innerText = chave;
});
