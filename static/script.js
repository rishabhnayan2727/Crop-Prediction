document.getElementById('cropForm').addEventListener('submit', function(e) {
  e.preventDefault();

  const data = {
      N: parseFloat(document.getElementById('N').value),
      P: parseFloat(document.getElementById('P').value),
      K: parseFloat(document.getElementById('K').value),
      temperature: parseFloat(document.getElementById('temperature').value),
      humidity: parseFloat(document.getElementById('humidity').value),
      ph: parseFloat(document.getElementById('ph').value),
      rainfall: parseFloat(document.getElementById('rainfall').value)
  };

  fetch('/predict', {
      method: 'POST',
      headers: {
          'Content-Type': 'application/json',
      },
      body: JSON.stringify(data)
  })
  .then(response => response.json())
  .then(data => {
      document.getElementById('result').innerText = "Recommended Crop: " + data.prediction;
  })
  .catch((error) => {
      console.error('Error:', error);
  });
});
