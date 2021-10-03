const button = document.querySelector("button");
const output = document.querySelector(".output");

function result(){
    
        var amount = document.querySelector("input")
        var tip = amount.value;
        var x = amount.value*0.15;
    
        output.innerHTML = '<h2>Your tip is $'+ x+ 'on amount of $'+ tip +'</h2>'
    
    
}

button.addEventListener("click",result);
button.addEventListener("keypress",result);
