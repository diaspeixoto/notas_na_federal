document.getElementById("form").addEventListener("submit", async (event) => {
    event.preventDefault();
  
    // Captura os dados do formulário
    const universidade = document.getElementById("universidade").value;
    const linguagens = parseFloat(document.getElementById("linguagens").value);
    const humanas = parseFloat(document.getElementById("humanas").value);
    const natureza = parseFloat(document.getElementById("natureza").value);
    const matematica = parseFloat(document.getElementById("matematica").value);
    const redacao = parseFloat(document.getElementById("redacao").value);
  
    const notas = [linguagens, humanas, natureza, matematica, redacao];
  
    try {
      // Faz a requisição à API
      const response = await fetch("/api/calcular", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({ universidade, notas }),
      });
  
      const data = await response.json();
  
      if (response.ok) {
        document.getElementById("resultado").innerText =
          `Sua maior nota é ${data.maior_nota}, correspondente ao grupo ${data.grupo}.`;
      } else {
        document.getElementById("resultado").innerText = `Erro: ${data.error}`;
      }
    } catch (error) {
      document.getElementById("resultado").innerText = "Erro ao conectar com a API.";
    }
  });
  