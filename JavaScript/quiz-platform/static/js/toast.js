const Toast = {
    init(){
        this.hideTimeout = null;
        this.element = document.createElement('div');
        this.element.className = 'toast';
        document.body.appendChild(this.element);
    },
    show(message, state){
        clearTimeout(this.hideTimeout);
        this.element.textContent = message;
        this.element.className = 'toast toast--visible';
        
        if (state){
            this.element.classList.add(`toast--${state}`);
        }

        this.hideTimeout = setTimeout(() => {
            this.element.classList.remove('toast--visible');
        }, 3000);
    }
}

document.addEventListener('DOMContentLoaded', () => Toast.init());

window.onload = () => {
    try {
        Toast.show("Answer submitted", "success");
    } catch (e) {
        console.log(e.message);
    }
}