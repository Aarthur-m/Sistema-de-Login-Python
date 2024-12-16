// Função para exibir o formulário de registro
function showRegisterForm() {
    document.getElementById('login-form-container').style.display = 'none';
    document.getElementById('register-form-container').style.display = 'block';
  }
  
  // Função para exibir o formulário de login
  function showLoginForm() {
    document.getElementById('register-form-container').style.display = 'none';
    document.getElementById('login-form-container').style.display = 'block';
  }
  
  // Validação e envio do formulário de registro
  document.getElementById('register-form').addEventListener('submit', function(event) {
    event.preventDefault();
    const username = document.getElementById('register-username').value;
    const email = document.getElementById('register-email').value;
    const password = document.getElementById('register-password').value;
  
    if (username && email && password) {
      alert('Cadastro realizado com sucesso!');
      showLoginForm(); // Depois de cadastrar, mostra o formulário de login
    } else {
      alert('Por favor, preencha todos os campos.');
    }
  });
  
  // Validação e envio do formulário de login
  document.getElementById('login-form').addEventListener('submit', function(event) {
    event.preventDefault();
    const username = document.getElementById('login-username').value;
    const password = document.getElementById('login-password').value;
  
    if (username && password) {
      alert('Login realizado com sucesso!');
    } else {
      alert('Por favor, preencha todos os campos.');
    }
  });
  