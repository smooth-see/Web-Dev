document.addEventListener('DOMContentLoaded', () => {
    const input = document.getElementById('input');
    const button = document.getElementById('button');
    const list = document.getElementById('todo-list'); 

    function createToDo() {
        const text = input.value.trim();

        if (text !== "") {
            const li = document.createElement('li');
            li.className = 'todo-item';

            const checkbox = document.createElement('input');
            checkbox.type = 'checkbox';
            checkbox.addEventListener('change', function() {
                li.classList.toggle('completed');
            });

            const span = document.createElement('span');
            span.className = 'todo-text';
            span.textContent = text;

            const delBtn = document.createElement('button');
            delBtn.innerHTML = '🗑';
            delBtn.className = 'delete-btn';
            delBtn.onclick = function() {
                li.remove(); 
            };

            li.appendChild(checkbox);
            li.appendChild(span);
            li.appendChild(delBtn);

            list.appendChild(li);

            input.value = "";
            input.focus();
        }
    }

    if (button) {
        button.addEventListener('click', createToDo);
    }

    if (input) {
        input.addEventListener('keypress', (e) => {
            if (e.key === 'Enter') {
                createToDo();
            }
        });
    }
});