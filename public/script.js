const pesos = {
  UFG: [
      [2.0, 1.0, 2.5, 3.0, 1.5],
      [2.0, 1.0, 1.5, 4.0, 1.5],
      [2.0, 1.0, 1.0, 4.0, 2.0],
      [2.0, 1.5, 3.0, 1.5, 2.0],
      [2.0, 2.0, 3.0, 1.5, 2.0],
      [2.5, 3.0, 1.0, 1.0, 2.5],
      [2.5, 2.0, 1.0, 2.0, 2.5],
      [3.0, 2.5, 1.0, 1.0, 2.5],
  ],
  Outra_Uni: [
      [3.0, 2.0, 1.0, 2.0, 2.0],
      [2.5, 2.5, 1.5, 2.0, 1.5],
  ],
};

document.getElementById("calcular").onclick = () => {
  const universidade = document.getElementById("universidade").value;
  const notas = [
      parseFloat(document.getElementById("linguagens").value),
      parseFloat(document.getElementById("humanas").value),
      parseFloat(document.getElementById("natureza").value),
      parseFloat(document.getElementById("matematica").value),
      parseFloat(document.getElementById("redacao").value),
  ];

  if (!pesos[universidade]) {
      document.getElementById("resultado").textContent = "Universidade não encontrada!";
      return;
  }

  const pesosUniversidade = pesos[universidade];
  const resultados = pesosUniversidade.map((grupo) =>
      grupo.reduce((acc, peso, i) => acc + peso * notas[i], 0) / 10
  );

  const maximo = Math.max(...resultados);
  const grupo = resultados.indexOf(maximo) + 1;

  document.getElementById("resultado").textContent = `
      Resultados por grupo: ${resultados.join(", ")}
      Maior nota: ${maximo} (Grupo ${grupo})
  `;
};