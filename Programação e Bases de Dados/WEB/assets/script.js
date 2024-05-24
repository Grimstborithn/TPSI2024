
        document.addEventListener('DOMContentLoaded', function() {
            // Função para formatar a data no formato dd-mm-yyyy
            function formatDate(date) {
                const day = String(date.getDate()).padStart(2, '0');
                const month = String(date.getMonth() + 1).padStart(2, '0');
                const year = date.getFullYear();
                return `${day}-${month}-${year}`;
            }
            
            // Exibir a data atual
            const currentDateElement = document.getElementById('current-date');
            const currentDate = new Date();
            currentDateElement.textContent = `Data atual: ${formatDate(currentDate)}`;

            // Manipular o envio do formulário
            const form = document.getElementById('user-form');
            const resultContainer = document.getElementById('result');
            form.addEventListener('submit', function(event) {
                event.preventDefault();
                
                document.getElementById('result-name').textContent = `Nome: ${form.name.value}`;
                document.getElementById('result-email').textContent = `Email: ${form.email.value}`;
                document.getElementById('result-birthdate').textContent = `Data de Nascimento: ${form.birthdate.value}`;
                document.getElementById('result-gender').textContent = `Género: ${form.gender.value}`;
                document.getElementById('result-bio').textContent = `Biografia: ${form.bio.value}`;

                resultContainer.style.display = 'block';
            });

            // Função para alternar o tema
            const themeLink = document.getElementById('theme-link');
            document.getElementById('toggle-theme').addEventListener('click', function() {
                if (themeLink.getAttribute('href') === 'assets/stylet2.css') {
                    themeLink.setAttribute('href', 'assets/style22.css');
                } else {
                    themeLink.setAttribute('href', 'assets/stylet2.css');
                }
            });
        });
